import asyncio
import sys
from database import SessionLocal
from models.document import DocumentChunk
from services.vector_service import vector_service
from sqlalchemy import text
from services.ingest_service import ingest_service
from services.gemini_service import gemini_service

async def ingest_debug():
    print("\n=== INGESTION DEBUG ===")
    ticker = "TSLA"
    
    # 1. URL
    print(f"Finding 10-K URL for {ticker}...")
    url = await ingest_service._get_latest_10k_url(ticker)
    print(f"URL: {url}")
    
    if not url:
        return

    # 2. Download
    print("Downloading text...")
    html = await ingest_service._download_text(url)
    print(f"HTML Length: {len(html) if html else 0}")
    
    if not html:
        return

    # 3. Clean
    print("Cleaning HTML...")
    text = ingest_service._clean_html(html)
    print(f"Cleaned Text Length: {len(text)}")
    print(f"Sample Text: {text[:200]}...")

    # 4. Chunk
    print("Chunking...")
    chunks = ingest_service._chunk_text(text)
    print(f"Generated {len(chunks)} chunks")
    
    # 5. Embed (Test one chunk)
    if chunks:
        print("Testing embedding on first chunk...")
        emb = await gemini_service.embed_content(chunks[0])
        print(f"Embedding length: {len(emb)}")
        if not emb:
            print("ERROR: Embedding failed!")
        else:
            print("SUCCESS: Embedding generated!")

async def debug():
    # await ingest_debug()
    
    print("\n=== DATABASE DIAGNOSTICS ===")
    db = SessionLocal()
    try:
        # 1. Check Extension
        print("Checking pgvector extension...")
        res = db.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector'")).fetchone()
        if res:
            print("✅ pgvector extension is enabled.")
        else:
            print("❌ pgvector extension is MISSING!")
            # Try to enable it
            try:
                db.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
                db.commit()
                print("✅ Enabled pgvector extension.")
            except Exception as e:
                print(f"❌ Failed to enable extension: {e}")

        # 2. Check Table
        print("\nChecking document_chunks table...")
        res = db.execute(text("SELECT to_regclass('public.document_chunks')")).fetchone()
        if res and res[0]:
            print("✅ Table 'document_chunks' exists.")
        else:
            print("❌ Table 'document_chunks' DOES NOT EXIST!")
            # Try to create it
            from database import engine, Base
            Base.metadata.create_all(bind=engine)
            print("✅ Created tables.")

        # 3. Try Insert
        print("\nAttempting dummy insert...")
        try:
            import uuid
            dummy = DocumentChunk(
                ticker="TEST",
                content="Test content",
                embedding=[0.1] * 768,
                source="DEBUG",
                chunk_index=0
            )
            db.add(dummy)
            db.commit()
            print("✅ Dummy insert successful!")
            
            # Clean up
            db.delete(dummy)
            db.commit()
            print("✅ Dummy cleanup successful!")
            
        except Exception as e:
            print(f"❌ Insert failed: {e}")
            db.rollback()

    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(debug())
