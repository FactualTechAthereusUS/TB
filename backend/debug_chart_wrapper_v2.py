
import json
import re

class OutputEngine:
    def _wrap_bare_json_chart(self, text: str) -> str:
        """
        Detects if the text contains bare JSON chart objects OR generic json blocks, 
        and ensures they are wrapped in ```json-chart blocks.
        """
        try:
            # Case 1: Convert generic ```json blocks to ```json-chart if they contain chart data
            def replace_json_tag(match):
                content = match.group(1)
                if '"type"' in content and '"series"' in content:
                    return f"```json-chart\n{content}\n```"
                return match.group(0)
            
            text = re.sub(r"```json\s*(\{.*?\})\s*```", replace_json_tag, text, flags=re.DOTALL)

            # Case 2: Wrap bare JSON objects
            indices = [i for i, char in enumerate(text) if char == '{']
            
            valid_charts = []
            
            for start in indices:
                snippet = text[start:]
                # Fast fail
                if '"type"' not in snippet or '"series"' not in snippet:
                    continue
                
                # Find matching brace
                balance = 0
                end = -1
                for k, char in enumerate(snippet):
                    if char == '{':
                        balance += 1
                    elif char == '}':
                        balance -= 1
                        if balance == 0:
                            end = start + k + 1
                            break
                
                if end != -1:
                    candidate = text[start:end]
                    # Check if it's already wrapped
                    pre_context = text[max(0, start-20):start]
                    if "```json-chart" in pre_context or "```json" in pre_context:
                        continue

                    try:
                        json.loads(candidate)
                        valid_charts.append((start, end, candidate))
                    except json.JSONDecodeError as e:
                        print(f"JSON Decode Error at {start}: {e}")
                        continue
            
            # Sort by start index descending
            valid_charts.sort(key=lambda x: x[0], reverse=True)
            
            result_text = text
            last_wrap_start = float('inf')
            
            for start, end, candidate in valid_charts:
                if end > last_wrap_start:
                    continue
                
                fenced = f"\n```json-chart\n{candidate}\n```\n"
                last_wrap_start = start
                result_text = result_text[:start] + fenced + result_text[end:]
            
            return result_text
            
        except Exception as e:
            print(f"Error: {e}")
            return text

# Test Data from Screenshot (Approximate)
test_text = """
Revenue Comparison: Ford vs. Tesla
Here's a comparison of total revenues for Ford and Tesla over the past three fiscal years.
Results Snapshot
Company 2024 Revenue ($ billion) 2023 Revenue ($ billion) 2022 Revenue ($ billion)
Ford 184.99 176.19 158.06
Tesla 97.69 96.77 81.46

Sources
{
  "type": "bar",
  "title": "Annual Revenue Comparison: Ford vs. Tesla",
  "labels": ["2024", "2023", "2022"],
  "series": [
    {"name": "Ford Revenue", "data": [184.99, 176.19, 158.06], "unit": "B"},
    {"name": "Tesla Revenue", "data": [97.69, 96.77, 81.46], "unit": "B"}
  ],
  "yAxisLabel": "Revenue ($ Billion)"
}
Sources
10-K, Page N/A
"""

engine = OutputEngine()
wrapped = engine._wrap_bare_json_chart(test_text)

print("--- Original ---")
print(test_text)
print("\n--- Wrapped ---")
print(wrapped)

if "```json-chart" in wrapped:
    print("\n✅ SUCCESS: Chart wrapped")
else:
    print("\n❌ FAILURE: Chart NOT wrapped")
