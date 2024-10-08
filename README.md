# Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach

This repository is an official implementation of [Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach](link).

## Project Overview

Large Language Models (LLMs) have transformed natural language processing but often perpetuate societal biases, especially those affecting the LGBTQIA+ community. These biases can lead to misrepresentation and marginalization, reinforcing discrimination in AI-generated content. This project introduces a collaborative agent pipeline designed to detect and mitigate biases in LLM outputs, focusing specifically on pronoun inclusivity to accurately represent all gender identities.

We present a multi-agent framework that utilizes specialized agents to sequentially analyze, critique, and optimize language outputs for enhanced inclusivity. By addressing the nuanced challenges of LGBTQIA+ representation, this work aims to advance the development of socially responsible AI that respects and reflects the diversity of human identities.

Evaluations using the Tango dataset—a benchmark focused on gender pronoun usage—demonstrate that this approach improves inclusive pronoun classification by 11.2 percentage points over the baseline GPT-4 model, achieving statistical significance (χ² = 78.52, p < 0.001).

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Set Up Instructions

Create a .env file in the root of your repository. Generate openai and paste your key in the .env file.
"key" serves as a placeholder for your API keys.
```setup
OPENAI_API_KEY = key
```

## Evaluation

To evaluate the model's performance on the TANGO dataset (testing_data.csv), run
```
python testing_tango.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
