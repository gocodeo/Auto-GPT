# Date: 2023-5-20
# Author: Generated by GoCodeo.


import json

import pytest

from autogpt.commands.improve_code import improve_code


@pytest.fixture
def mock_call_ai_function(mocker):
    return mocker.patch("autogpt.commands.improve_code.call_ai_function")


class TestImproveCode:
    def test_positive_improve_code(self, mock_call_ai_function):
        mock_call_ai_function.return_value = "Improved code"
        suggestions = ["Use better variable names", "Optimize loops"]
        code = "def example():\n    x = 5\n    for i in range(x):\n        print(i)"
        expected_result = "Improved code"
        result = improve_code(suggestions, code)
        assert result == expected_result
        mock_call_ai_function.assert_called_once_with(
            "def generate_improved_code(suggestions: list[str], code: str) -> str:",
            [json.dumps(suggestions), code],
            "Improves the provided code based on the suggestions provided, making no other changes.",
        )

    def test_negative_improve_code(self, mock_call_ai_function):
        mock_call_ai_function.return_value = "Original code"
        suggestions = []
        code = "def example():\n    x = 5\n    for i in range(x):\n        print(i)"
        expected_result = "Original code"

        result = improve_code(suggestions, code)
        assert result == expected_result
        mock_call_ai_function.assert_called_once_with(
            "def generate_improved_code(suggestions: list[str], code: str) -> str:",
            [json.dumps(suggestions), code],
            "Improves the provided code based on the suggestions provided, making no other changes.",
        )

    def test_error_improve_code(self, mock_call_ai_function):
        mock_call_ai_function.side_effect = Exception("Error occurred")
        suggestions = ["Use better variable names", "Optimize loops"]
        code = "def example():\n    x = 5\n    for i in range(x):\n        print(i)"

        with pytest.raises(Exception) as context:
            improve_code(suggestions, code)
            assert str(context.exception) == "Error occurred"
            mock_call_ai_function.assert_called_once_with(
                "def generate_improved_code(suggestions: list[str], code: str) -> str:",
                [json.dumps(suggestions), code],
                "Improves the provided code based on the suggestions provided, making no other changes.",
            )

    def test_edge_improve_code(self, mock_call_ai_function):
        mock_call_ai_function.return_value = "Improved code"
        suggestions = ["Use better variable names"]
        code = "def example():\n    pass"
        expected_result = "Improved code"

        result = improve_code(suggestions, code)
        assert result == expected_result
        mock_call_ai_function.assert_called_once_with(
            "def generate_improved_code(suggestions: list[str], code: str) -> str:",
            [json.dumps(suggestions), code],
            "Improves the provided code based on the suggestions provided, making no other changes.",
        )
