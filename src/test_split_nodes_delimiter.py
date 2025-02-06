import unittest
from textnode import TextNode, TextType
from converter import split_nodes_delimiter

class TestplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        node = TextNode("Just normal text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, [node])
    
    def test_single_delimiter_section(self):
        node = TextNode("this is *italic* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])

    def test_multiple_delimiter_sections(self):
        node = TextNode("This is *italic* and this is *bold*.", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("bold", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ])

    def text_code_block(self):
        node = TextNode("Use `print('Hello')` in Python", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Use ", TextType.TEXT),
            TextNode("print('Hello')", TextType.CODE),
            TextNode(" in Python", TextType.TEXT),
        ])

    def test_multiple_delimiters(self):
        node = TextNode("This is *italic* and `code` inside.", TextType.TEXT)
        italic_result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        final_result = split_nodes_delimiter(italic_result, "`", TextType.CODE)

        self.assertEqual(final_result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inside.", TextType.TEXT),
        ])

    def test_edge_case_empty_text(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, [node])
    
if __name__ == "__main__":
    unittest.main()










