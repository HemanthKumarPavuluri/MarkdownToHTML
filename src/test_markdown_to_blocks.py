

import unittest
from converter import markdown_to_blocks

class TestMarkdownToBlock(unittest.TestCase):

    def test_single_block(self):
        text = "# this is a heading"
        block = markdown_to_blocks(text)
        result = ["# this is a heading"]
        self.assertEqual(block, result)

    def test_multiple_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        block = markdown_to_blocks(markdown)
        result = ["# This is a heading",
                   "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(block, result)
    

    def test_empty_input(self):
        markdown = ""
        block = markdown_to_blocks(markdown)
        result = []
        self.assertEqual(block, result)
    
    def test_only_whitespace(self):
        markdown = "   \n   \n"
        block = markdown_to_blocks(markdown)
        result = []
        self.assertEqual(block, result)
    
    def test_multiple_blank_lines(self):
        markdown = """# Heading


This is a paragraph.


* List item 1

* List item 2

"""
        block = markdown_to_blocks(markdown)
        result = [
            "# Heading",
            "This is a paragraph.",
            "* List item 1",
            "* List item 2"
        ]
        self.assertEqual(block, result)

    def test_extra_spaces_and_newlines(self):
        markdown = """   # Heading    

   This is a paragraph.   

   * List item 1   
   * List item 2   

   """
        block = markdown_to_blocks(markdown)
        result = [
            "# Heading",
            "This is a paragraph.",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(block, result)


if __name__ == '__main__':
    unittest.main()