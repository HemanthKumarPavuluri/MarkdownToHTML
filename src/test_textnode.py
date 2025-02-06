import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def text_noteq(self):
        node = TextNode("abc", TextType.CODE, None)
        node2 = TextNode("bcd", TextType.CODE, "pornhub.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()