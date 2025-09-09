import htmlnode as hn

class LeafNode(hn.HTMLNode):
    def __init__(
        self, tag: str, value: str, props: dict[str, str] | None = None
    ) -> "LeafNode":
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value set.")
        if not self.tag:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
