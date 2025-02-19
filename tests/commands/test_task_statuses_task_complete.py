# Date: 2023-5-13
# Author: Generated by GoCodeo.


import unittest
from unittest.mock import patch
from typing import NoReturn
from autogpt.commands.task_statuses import task_complete
patch_func1 = "autogpt.logs.logger.info"
patch_func2 = "builtins.quit"

class TestTaskComplete(unittest.TestCase):

    @patch(patch_func1)
    @patch(patch_func2)
    def test_task_complete_positive(self, mock_quit, mock_logger_info):
        # Positive test
        reason = "Test shutdown"
        task_complete(reason)
        mock_logger_info.assert_called_once_with(title="Shutting down...\n", message=reason)
        mock_quit.assert_called_once()

    @patch(patch_func1)
    @patch(patch_func2)
    def test_task_complete_empty_reason(self, mock_quit, mock_logger_info):
        # Edge test
        reason = ""
        task_complete(reason)
        mock_logger_info.assert_called_once_with(title="Shutting down...\n", message=reason)
        mock_quit.assert_called_once()

    @patch(patch_func1)
    @patch(patch_func2)
    def test_task_complete_whitespace_reason(self, mock_quit, mock_logger_info):
        # Edge test
        reason = "   "
        task_complete(reason)
        mock_logger_info.assert_called_once_with(title="Shutting down...\n", message=reason)
        mock_quit.assert_called_once()

    @patch(patch_func1)
    @patch(patch_func2)
    def test_task_complete_special_characters(self, mock_quit, mock_logger_info):
        # Positive test
        reason = "!@#$%^&*()"
        task_complete(reason)
        mock_logger_info.assert_called_once_with(title="Shutting down...\n", message=reason)
        mock_quit.assert_called_once()

    @patch(patch_func1)
    @patch(patch_func2)
    def test_task_complete_long_reason(self, mock_quit, mock_logger_info):
        # Edge test
        reason = "A" * 1000
        task_complete(reason)
        mock_logger_info.assert_called_once_with(title="Shutting down...\n", message=reason)
        mock_quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()