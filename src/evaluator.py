import json
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent / "data" / "evaluations.json"

CRITERIA = [
    "accuracy",
    "relevance",
    "clarity",
    "instruction_following",
]


def load_evaluations():
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def calculate_total_score(scores):
    return sum(scores[criterion] for criterion in CRITERIA)


def evaluate_response_pair(evaluation):
    score_a = calculate_total_score(
        evaluation["scores"]["response_a"]
    )
    score_b = calculate_total_score(
        evaluation["scores"]["response_b"]
    )

    if score_a > score_b:
        winner = "A"
    elif score_b > score_a:
        winner = "B"
    else:
        winner = "TIE"

    return {
        "id": evaluation["id"],
        "score_a": score_a,
        "score_b": score_b,
        "winner": winner,
        "expected_winner": evaluation["preferred_response"],
        "matches_expected": winner == evaluation["preferred_response"],
    }


def evaluate_all(evaluations):
    return [
        evaluate_response_pair(evaluation)
        for evaluation in evaluations
    ]


if __name__ == "__main__":
    evaluations = load_evaluations()
    results = evaluate_all(evaluations)

    for result in results:
        print(
            f"{result['id']}: "
            f"A={result['score_a']} | "
            f"B={result['score_b']} | "
            f"Winner={result['winner']} | "
            f"Expected={result['expected_winner']} | "
            f"Match={result['matches_expected']}"
        )
