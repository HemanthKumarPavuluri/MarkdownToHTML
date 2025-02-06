from textnode import TextNode, TextType
from htmlnode import LeafNode
import re

def text_node_to_html_node(text_node):

    if not isinstance(text_node, TextNode):
        raise TypeError("Expected at TextNode instance")
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK type TextNode must have a url")
        return LeafNode("a",text_node.text,{"href": text_node.url})
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("IMAGE type TextNode must have a url")
        return LeafNode("img", "",{"src":text_node.url, "alt": text_node.text})
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    raise ValueError(f"Unsupported TextType: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only process nodes that are of TEXT type
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        # If the delimiter is not found, keep the original node
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        is_inside = False  # Track whether we are inside a delimited section
        for part in parts:
            if part == "":
                continue  # Ignore empty splits
            
            if is_inside:
                new_nodes.append(TextNode(part, text_type))  # Apply the given text type
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))  # Keep as plain text
            
            is_inside = not is_inside  # Flip state after each section

    return new_nodes

""" 
takes raw markdown text and returns a list of tuples. 
Each tuple should contain the alt text and the URL of any markdown images.
"""
def extract_markdown_images(text):
    x = re.findall("!\[(.*?)\]\((https?://[^\)]+)\)", text)
    return x

def extract_markdown_links(text):
    x = re.findall("\[(.*?)\]\((https?://[^\)]+)\)", text)
    return x










