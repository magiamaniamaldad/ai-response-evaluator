# 🤖 AI Response Evaluator

A Python-based framework for evaluating and comparing AI-generated responses using structured quality rubrics, automated scoring, and A/B preference validation.

The project simulates a practical AI evaluation workflow in which multiple model responses are assessed across predefined criteria and compared to determine the strongest output.

## 🔎 What It Evaluates

Each response is scored across four quality dimensions:

- **Accuracy** — Is the response factually and logically correct?
- **Relevance** — Does it directly address the user's request?
- **Clarity** — Is the response understandable and well structured?
- **Instruction Following** — Does it satisfy the requirements of the prompt?

The evaluator calculates an aggregate score for each response and determines whether **Response A**, **Response B**, or a **tie** is the resulting preference.

## ⚖️ A/B Response Comparison

Evaluation samples are stored as structured JSON data containing:

- A user prompt
- Response A
- Response B
- Individual rubric scores
- An expected preferred response

The Python evaluation engine calculates both total scores and verifies whether the computed winner matches the expected preference.

## 🛠️ Tech Stack

- Python 3.12
- JSON
- Pytest
- GitHub Actions

## 📁 Project Structure

```text
ai-response-evaluator/
├── .github/
│   └── workflows/
│       └── ai-evaluator-tests.yml
├── data/
│   └── evaluations.json
├── src/
│   ├── __init__.py
│   └── evaluator.py
├── tests/
│   └── test_evaluator.py
├── .gitignore
└── README.md
```

## ⚙️ How It Works

The evaluation pipeline follows four main steps:

1. Load structured evaluation samples from JSON.
2. Calculate scores across the evaluation criteria.
3. Compare Response A and Response B.
4. Validate the calculated winner against the expected preference.

Example result:

```text
eval_001: A=20 | B=13 | Winner=A | Expected=A | Match=True
```

## 🧪 Automated Testing

The project includes automated tests covering:

- Rubric score calculation
- Response A winning a comparison
- Tie handling
- Expected preference validation
- Evaluation of multiple response pairs

Run the test suite with:

```bash
pytest -v
```

## 🔄 Continuous Integration

GitHub Actions automatically executes the test suite on pushes and pull requests to the `main` branch.

The CI workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs Pytest
4. Configures the project import path
5. Runs the automated evaluator tests

This ensures changes to the evaluation logic are continuously validated.

## 🎯 Project Purpose

This project demonstrates practical skills relevant to **AI quality evaluation and model output assessment**, including structured rubric design, A/B comparison, data validation, Python automation, automated testing, and continuous integration.

All evaluation examples in this repository are synthetic and were created specifically for demonstration purposes.
