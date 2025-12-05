
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
                    except json.JSONDecodeError:
                        continue
            
            # Sort by start index descending
            valid_charts.sort(key=lambda x: x[0], reverse=True)
            
            result_text = text
            last_wrap_start = float('inf')
            
            for start, end, candidate in valid_charts:
                # Ensure no overlap
                if end > last_wrap_start:
                    continue
                
                fenced = f"\n```json-chart\n{candidate}\n```\n"
                
                last_wrap_start = start
                result_text = result_text[:start] + fenced + result_text[end:]
            
            return result_text
            
        except Exception as e:
            print(f"Error: {e}")
            return text

# Test Data from Screenshot
test_text = """
PepsiCo's direct-store-delivery network are expected to show most distribution benefits in early 2026.
Sources [Source: 1. Celsius Holdings Reports Third Quarter 2025 Financial Results, 2025-11-06]
{
  "type": "bar",
  "title": "Celsius Holdings Annual Revenue (2022-2025 TTM)",
  "labels": ["2022", "2023", "2024", "2025 TTM"],
  "series": [
    {
      "name": "Revenue",
      "data": [653.6, 1318.0, 1360.0, 2130.0],
      "unit": "million"
    }
  ],
  "yAxis": {
    "title": "Revenue (Millions USD)"
  }
}
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
