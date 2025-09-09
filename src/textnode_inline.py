import textnode as tn
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type)->list[tn.TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
          new_nodes.append(node)
        else:
          fragments = node.text.split(delimiter)
          if len(fragments) % 2 == 0:
            raise ValueError(
              f"Mismatched or empty delimiter {delimiter} in input {node.text}"
            )
          else:  # Odd indices are the delimited text
            for index, fragment in enumerate(fragments):
                    if index % 2 == 0:  # Plain text
                        new_nodes.append(tn.TextNode(fragment, tn.TextType.TEXT))
                    else:
                        new_nodes.append(tn.TextNode(fragment, text_type))
    return new_nodes

def extract_markdown_images(text: str)->list[(str,str)]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches 

def extract_markdown_links(text: str)->list[(str,str)]:
    matches = re.findall(r"[^!]\[(.*?)\]\((.*?)\)",text)
    return matches

def to_md_link(link: tuple[str,str])->str:
    return f"[{link[0]}]({link[1]})"

def split_urls_from_text(input_text: str, 
                         type: tn.TextType, 
                         links = list[tuple[str,str]], 
                         prefix: str = "")->list[tn.TextNode]:
    split_nodes = []
    remaining_text = input_text
    for link in links:
      fragments = remaining_text.split(prefix+to_md_link(link), maxsplit=2)
      split_nodes.append(tn.TextNode(fragments[0], tn.TextType.TEXT))
      split_nodes.append(tn.TextNode(content=link[0], type=type, url=link[1]))
      remaining_text = fragments[1]
    if len(remaining_text) > 0:
      split_nodes.append(tn.TextNode(remaining_text, tn.TextType.TEXT))
    return split_nodes

def split_nodes_image(old_nodes: list[tn.TextNode]) -> list[tn.TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(
                split_urls_from_text(
                    node.text,
                    tn.TextType.IMAGE,
                    extract_markdown_images(node.text),
                    prefix="!"
                )
            )
    return new_nodes

def split_nodes_link(old_nodes: list[tn.TextNode]) -> list[tn.TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(
                split_urls_from_text(
                    node.text,
                    tn.TextType.LINK,
                    extract_markdown_links(node.text),
                    prefix=""
                )
            )
    return new_nodes
