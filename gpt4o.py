import openai
from dotenv import load_dotenv
import json

def call_gpt(problem):
    load_dotenv()
    client = openai

    messages = [
            {"role": "system", "content": "You are a smart decision maker."},
            {"role": "user", "content": problem}
    ]

    response = client.chat.completions.create(
                model='gpt-4o-2024-08-06',
                messages=messages,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "identifier",
                        "strict": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "choose_statement": {"type": "boolean"},
                                "reasoning": {"type": "string"}
                                },
                            "required": ["choose_statement", "reasoning"],
                            "additionalProperties": False
                        }
                    }
                }
            )
    
    
    choose_statement = json.loads(response.choices[0].message.content).get("choose_statement", None)
    reasoning = json.loads(response.choices[0].message.content).get("reasoning", None)

    return choose_statement, reasoning