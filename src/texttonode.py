import textnode as tn
import textnode_inline as ti

def text_to_textnodes(input_text: str)->list[tn.TextNode]:
  text_nodes = [tn.TextNode(content=input_text, type=tn.TextType.TEXT)]
  text_nodes.extend(ti.split_nodes_delimiter(text_nodes,"**",tn.TextType.BOLD))
  text_nodes.extend(ti.split_nodes_delimiter(text_nodes,"_",tn.TextType.ITALIC))
  text_nodes.extend(ti.split_nodes_delimiter(text_nodes,"`",tn.TextType.CODE))
  text_nodes.extend(ti.split_nodes_image(text_nodes))
  text_nodes.extend(ti.split_nodes_link(text_nodes))
  return text_nodes


