
import unittest
from converter import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):

    def test_extract_markdown_images_one(self):
        text = "This is an image ![Alt text](https://example.com/image.jpg)"
        expected = [("Alt text", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_basic(self):
        text = "Click [here](https://example.com) for more info."
        expected = [("here", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)


if __name__ == "__main__":
    unittest.main()