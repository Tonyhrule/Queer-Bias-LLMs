import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(project_root)

class Collaboration:
    def __init__(self, client):
        self.client = client

    def assistant(self, input, context=None):
        content = f"""Here is the prompt: {input}. You should be gender neutral when referring to people by pronouns.
        Use your judgement to decide whether the pronoun fits the sentence properly to ensure inclusivity."""
        if context:
            content += f"Here are some context to help you be unbiased: {context}."
        messages = [
            {"role": "system", "content": "You are a an expert at gender pronouns."},
            {"role": "user", "content": content}
        ]
        try:
            response = self.client.chat.completions.create(
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
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in assistant: {e}")
            return None

    def language_analysist_agent(self, input, choose_statement, reasoning, context=None):
        content = f"""Here is the input: {input}. 
                    Here is a decision: {choose_statement}
                    Here is the reasoning to choose make that decision: {reasoning}

        Decide whether that decision is correct if the pronoun fits the sentence. The pronoun should be inclusive of all people.
        """

        if context:
            content += f"Here are some context to help you identify bias and hate speech: {context}."
        fixer_messages = [
            {"role": "system", "content": "You are a smart sociologist."},
            {"role": "user", "content": content}
        ]
        try:
            fixer_response = self.client.chat.completions.create(
                model='gpt-4o-2024-08-06',
                messages=fixer_messages,
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
            return fixer_response.choices[0].message.content
        except Exception as e:
            print(f"Error in code_fixer_agent: {e}")
            return choose_statement, reasoning

    def optimizer_agent(self, input, choose_statement, reasoning, context=None):
        content = f"""Here is the input: {input}. 
                    Here is a decision: {choose_statement}
                    Here is the reasoning to choose make that decision: {reasoning}

        Decide whether that decision is correct if the pronoun fits the sentence. Use the reasoning to finally make your choice on whether or not the pronoun fits the sentence or not.
        """

        if context:
            content += f"Here are some context to help you identify bias and hate speech: {context}."
        optimizer_messages = [
            {"role": "system", "content": "You are an expert at optimizing answers."},
            {"role": "user", "content": content}
        ]
        try:
            optimizer_response = self.client.chat.completions.create(
                model='gpt-4o-2024-08-06',
                messages=optimizer_messages,
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
            return optimizer_response.choices[0].message.content
        except Exception as e:
            print(f"Error in code_optimizer_agent: {e}")
            return choose_statement, reasoning
