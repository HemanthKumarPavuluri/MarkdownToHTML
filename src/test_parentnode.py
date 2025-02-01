import unittest
from htmlnode import *

class Test_ParentNode(unittest.TestCase):

    def test_parentnode_with_children(self):
        node = ParentNode("p", 
                          [LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode('i', "italic text"),
                            LeafNode(None, "Normal text")],
                        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")










