import re
from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode instance")
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK type TextNode must have a url")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("IMAGE type TextNode must have a url")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    raise ValueError(f"Unsupported TextType: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        if len(parts) == 1:
            new_nodes.append(node)
            continue

        is_inside = False
        for part in parts:
            if part == "":
                continue
            
            if is_inside:
                new_nodes.append(TextNode(part, text_type))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
            
            is_inside = not is_inside

    return new_nodes


def extract_markdown_images(text):
    """ Extracts markdown images and returns a list of (alt_text, url) tuples. """
    return re.findall(r"!\[(.*?)\]\((https?://[^\)]+)\)", text)

def extract_markdown_links(text):
    """ Extracts markdown links and returns a list of (link_text, url) tuples. """
    return re.findall(r"\[(.*?)\]\((https?://[^\)]+)\)", text)

def split_nodes_image(old_nodes):
    """ Splits text nodes into text and image nodes. """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        image_matches = extract_markdown_images(text)
        index = 0

        for alt_text, img_url in image_matches:
            match_text = f"![{alt_text}]({img_url})"
            match_start = text.find(match_text)

            if match_start == -1:
                continue

            before_text = text[index:match_start]
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))
            index = match_start + len(match_text)

        if index < len(text):
            new_nodes.append(TextNode(text[index:], TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    """ Splits text nodes into text and link nodes. """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        link_matches = extract_markdown_links(text)
        index = 0

        for link_text, link_url in link_matches:
            match_text = f"[{link_text}]({link_url})"
            match_start = text.find(match_text)

            if match_start == -1:
                continue

            before_text = text[index:match_start]
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            index = match_start + len(match_text)

        if index < len(text):
            new_nodes.append(TextNode(text[index:], TextType.TEXT))

    return new_nodes





def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(text_node)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes

text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

nodes = text_to_textnodes(text)
for node in nodes:
    print(node)

    










