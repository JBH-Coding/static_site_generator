import htmlnode as hn


class ParentNode(hn.HTMLNode):
    def __init__(
        self, tag: str, children: list['hn.HTMLNode'], props: dict[str, str] | None = None
    ) -> "ParentNode":
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A ParentNode must have a valid tag.")
        if not self.children:
            raise ValueError("A ParentNode requires one or more children.")
        return f"<{self.tag}>" + "".join([child.to_html() for child in self.children]) + f"</{self.tag}>"
