import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')


    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Hello World, children=[], props={})")

    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=[], props={})")

    def test_to_html_with_tag(self):
        node = LeafNode("p", "iam a paragraph")
        self.assertEqual(node.to_html(), "<p>iam a paragraph</p>")
    
    def test_to_html_with_attributes(self):
        node = LeafNode('a', 'click here', {"href":"https://google.com/"})
        self.assertEqual(node.to_html(), '<a href="https://google.com/">click here</a>')

    def teat_leaf_node_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)


if __name__ == "__main__":
    unittest.main()














