

class HTMLNode():
  def __init__(self, 
               tag: str | None = None, 
               value: str | None = None, 
               children: list['HTMLNode'] | None = None,
               props: dict[str,str] | None = None,
  )->'HTMLNode':
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def __eq__(self, other:'HTMLNode')->bool:
    return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    return ''.join([f' {key}="{value}"' for key, value in self.props])

  def __repr__(self):
    repr = f'{type(self).__name__} : {hex(id(self))}'
    repr += f'tag: {self.tag}\n{self.value}\n'
    repr += '\n'.join([f'\t{key}={value}' for key, value in self.props])
    children = ','.join([f'{hex(node.id())}' for node in self.children])
    repr += f'Children: [{children}]'