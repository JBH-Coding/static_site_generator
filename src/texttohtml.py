import textnode as tn
import htmlnode as hn
import leafnode as ln

def text_node_to_html_node(text_node: tn.TextNode)->hn.HTMLNode:
  if text_node.text_type == tn.TextType.TEXT:
    return ln.LeafNode(tag=None, value=text_node.text)
  if text_node.text_type == tn.TextType.BOLD:
    return ln.LeafNode(tag="b", value=text_node.text)
  if text_node.text_type == tn.TextType.ITALIC:
    return ln.LeafNode(tag="i", value=text_node.text)
  if text_node.text_type == tn.TextType.CODE:
    return ln.LeafNode(tag="code", value=text_node.text)
  if text_node.text_type == tn.TextType.LINK:
    return ln.LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
  if text_node.text_type == tn.TextType.IMAGE:
    return ln.LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
  raise ValueError(f"Unknown text type: {text_node.text_type}")
