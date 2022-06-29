import json
import openai

openai.api_key = "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"
response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

from api import GPT, Example, set_openai_key
gpt = GPT(engine="davinci",
          temperature=1.0,
          max_tokens=120)



output = gpt.submit_request('At the darkest forest,')

print(output.choices[0]['text'])