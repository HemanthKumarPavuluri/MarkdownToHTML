

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}


    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in a subclass.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

# LeafNode child class of HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        if self.tag in ["img", "br", "hr", "input", "meta", "link"]:
            return f'<{self.tag}{self.props_to_html()}>'
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if not children or not isinstance(children, list):
            raise ValueError("ParentNode must have a list of child nodes.")
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        child_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
        
        






