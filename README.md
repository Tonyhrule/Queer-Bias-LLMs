# Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach

This repository is an official implementation of Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach.

- To read more about this project, please visit our paper on [arXiv](https://arxiv.org/abs/2411.07656).

## Project Overview

Large Language Models (LLMs) often perpetuate biases in pronoun usage, leading to misrepresentation or exclusion of queer individuals through inappropriate usage of traditionally gendered pronouns like "he" and "she." This project addresses the specific issue of biased pronoun usage in LLM outputs, particularly when inclusive language is essential to represent all identities accurately.

To address this issue, we introduce a collaborative agent pipeline designed to detect and mitigate these biases by analyzing and optimizing pronoun usage for inclusivity. Our multi-agent framework includes specialized agents for both identifying biased language and applying corrective measures to enhance inclusivity.

We evaluated our approach using the Tango dataset, a benchmark focused on gender pronoun usage. Results show that our method achieves a 32.6 percentage point improvement over GPT-4 in correctly disagreeing with inappropriate traditionally gendered pronouns (χ² = 38.57, p < 0.0001). These findings demonstrate the potential of agent-driven frameworks to enhance fairness and inclusivity in AI-generated content, highlighting their efficacy in reducing biases and advancing socially responsible AI.

## Project Structure

Here’s a breakdown of the main files in this repository:

- **agent_workflow.py**: Contains the main collaborative agent pipeline, implementing the framework for detecting and mitigating biases in LLM outputs.
- **gpt4o.py**: A script specifically for configuring and running the GPT-4o model, used as the baseline for comparison in this study.
- **requirements.txt**: Lists the Python dependencies needed to run this project.
- **testing_data.csv**: The Tango Dataset used for testing.
- **testing_return.py**: Script for all the defined functions that is called in testing.
- **testing_tango.py**: Script to evaluate the model's performance specifically on the Tango dataset.

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

## Citation

If you find this project helpful for your research, please cite our work:
```
@misc{huang2024mitigatingbiasqueerrepresentation,
      title={Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach}, 
      author={Tianyi Huang and Arya Somasundaram},
      year={2024},
      eprint={2411.07656},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.07656}, 
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
