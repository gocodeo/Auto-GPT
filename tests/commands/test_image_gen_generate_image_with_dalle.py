# Date: 2023-5-13
# Author: Generated by GoCodeo.


import unittest
from unittest.mock import patch, MagicMock
from base64 import b64encode
from io import BytesIO
from autogpt.commands.image_gen import generate_image_with_dalle

patch_func1 = 'autogpt.commands.image_gen.openai.Image.create'
patch_func2 = 'autogpt.commands.image_gen.logger.info'

class TestGenerateImageWithDalle(unittest.TestCase):

    @patch(patch_func1)
    @patch(patch_func2)
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_generate_image_with_dalle_positive(self, mock_open, mock_logger_info, mock_openai_create):
        # Positive test case
        prompt = "Test prompt"
        filename = "test_image.png"
        size = 512

        mock_response = MagicMock()
        mock_response.configure_mock(**{
            "data": [{"b64_json": b64encode(b"test_image_data").decode("utf-8")}]
        })
        mock_openai_create.return_value = mock_response

        result = generate_image_with_dalle(prompt, filename, size)

        self.assertEqual(result, f"Saved to disk:{filename}")
        mock_open.assert_called_once_with(filename, mode="wb")
        mock_open().write.assert_called_once_with(b"test_image_data")
        mock_logger_info.assert_called()

    @patch(patch_func1)
    @patch(patch_func2)
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_generate_image_with_dalle_unsupported_size(self, mock_open, mock_logger_info, mock_openai_create):
        # Edge test case
        prompt = "Test prompt"
        filename = "test_image.png"
        size = 600

        mock_response = MagicMock()
        mock_response.configure_mock(**{
            "data": [{"b64_json": b64encode(b"test_image_data").decode("utf-8")}]
        })
        mock_openai_create.return_value = mock_response

        result = generate_image_with_dalle(prompt, filename, size)

        self.assertEqual(result, f"Saved to disk:{filename}")
        mock_open.assert_called_once_with(filename, mode="wb")
        mock_open().write.assert_called_once_with(b"test_image_data")
        mock_logger_info.assert_called()

if __name__ == "__main__":
    unittest.main()
