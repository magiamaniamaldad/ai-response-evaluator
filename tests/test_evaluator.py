from src.evaluator import (
    calculate_total_score,
    evaluate_response_pair,
    evaluate_all,
)


def test_calculate_total_score():
    scores = {
        "accuracy": 5,
        "relevance": 4,
        "clarity": 3,
        "instruction_following": 5,
    }

    assert calculate_total_score(scores) == 17


def test_response_a_wins():
    evaluation = {
        "id": "test_001",
        "scores": {
            "response_a": {
                "accuracy": 5,
                "relevance": 5,
                "clarity": 5,
                "instruction_following": 5,
            },
            "response_b": {
                "accuracy": 3,
                "relevance": 3,
                "clarity": 3,
                "instruction_following": 3,
            },
        },
        "preferred_response": "A",
    }

    result = evaluate_response_pair(evaluation)

    assert result["winner"] == "A"
    assert result["matches_expected"] is True


def test_tie():
    evaluation = {
        "id": "test_002",
        "scores": {
            "response_a": {
                "accuracy": 4,
                "relevance": 4,
                "clarity": 4,
                "instruction_following": 4,
            },
            "response_b": {
                "accuracy": 4,
                "relevance": 4,
                "clarity": 4,
                "instruction_following": 4,
            },
        },
        "preferred_response": "A",
    }

    result = evaluate_response_pair(evaluation)

    assert result["winner"] == "TIE"
    assert result["matches_expected"] is False


def test_evaluate_all():
    evaluations = [
        {
            "id": "test_003",
            "scores": {
                "response_a": {
                    "accuracy": 5,
                    "relevance": 5,
                    "clarity": 5,
                    "instruction_following": 5,
                },
                "response_b": {
                    "accuracy": 2,
                    "relevance": 2,
                    "clarity": 2,
                    "instruction_following": 2,
                },
            },
            "preferred_response": "A",
        }
    ]

    results = evaluate_all(evaluations)

    assert len(results) == 1
    assert results[0]["winner"] == "A"
