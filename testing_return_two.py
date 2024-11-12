import sys
import os
import json
import openai
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(project_root)

from agent_workflow import Collaboration

load_dotenv()

def fixed_openai_call(func, *args, **kwargs):
    try:
        """
        for arg in args:
            print(f'Arg: {arg}')
            """
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error in OpenAI call: {e}")
        return None

def run_baseline(agent_workflow, input):
    initial_response = fixed_openai_call(agent_workflow.assistant, input)
    choose_statement = json.loads(initial_response)['choose_statement']
    reasoning = json.loads(initial_response)['reasoning']
    mid_response = fixed_openai_call(agent_workflow.language_analysist_agent, input, choose_statement, reasoning)
    choose_statement = json.loads(mid_response)['choose_statement']
    reasoning = json.loads(mid_response)['reasoning']
    return choose_statement, reasoning

def evaluate_two_performance(input):
    client = openai
    agent_workflow = Collaboration(client=client)

    baseline_code = run_baseline(agent_workflow, input)
    results = baseline_code

    return results

