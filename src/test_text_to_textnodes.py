import unittest
from textnode import TextNode, TextType
from converter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_just_text(self):
        text = "I am Batman"
        nodes = text_to_textnodes(text)
        result = [TextNode("I am Batman", TextType.TEXT)]
        self.assertEqual(nodes, result)

    def test_text_with_code(self):
        text = "I am `programming code` Batman"
        nodes = text_to_textnodes(text)
        result = [
            TextNode("I am ", TextType.TEXT),
            TextNode("programming code", TextType.CODE),
            TextNode(" Batman", TextType.TEXT)
            ]
        self.assertEqual(nodes, result)


    def test_text_with_everything(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        result = [
            TextNode("This is ",TextType.TEXT),
            TextNode("text", TextType.ITALIC, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
if __name__=='__main__':
    unittest.main()


