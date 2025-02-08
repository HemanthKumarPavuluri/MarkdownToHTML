

import unittest
from converter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitImageAndLink(unittest.TestCase):

    def test_split_nodes_image_single(self):
        node = TextNode("Check this ![image](https://example.com/image.png)", TextType.TEXT)
        expected = [
            TextNode("Check this ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("No images here", TextType.TEXT)
        expected = [TextNode("No images here", TextType.TEXT)]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_image_multiple(self):
        """ Test extracting multiple images from text """
        node = TextNode("First ![img1](https://img1.com) and second ![img2](https://img2.com)", TextType.TEXT)
        expected = [
            TextNode("First ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "https://img1.com"),
            TextNode(" and second ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "https://img2.com"),
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_single(self):
        """ Test extracting a single markdown link """
        node = TextNode("Visit [Google](https://google.com)", TextType.TEXT)
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)
    
    def test_split_nodes_link_multiple(self):
        """ Test extracting multiple markdown links """
        node = TextNode("[GitHub](https://github.com) and [YouTube](https://youtube.com)", TextType.TEXT)
        expected = [
            TextNode("GitHub", TextType.LINK, "https://github.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("YouTube", TextType.LINK, "https://youtube.com"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_link_and_image(self):
        """ Test mixed markdown with images and links """
        node = TextNode("Here is ![an image](https://example.com) and a [link](https://example.com)", TextType.TEXT)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("an image", TextType.IMAGE, "https://example.com"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(split_nodes_link(split_nodes_image([node])), expected)

if __name__ == '__main__':
    unittest.main()
