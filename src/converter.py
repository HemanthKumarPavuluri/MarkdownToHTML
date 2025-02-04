from testnode import TextNode, TextType
from htmlnode import LeafNode


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
    













