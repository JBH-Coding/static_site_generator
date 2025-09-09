import unittest
import leafnode as ln
import parentnode as pn
import textnode as tn
import texttonode as t2n

class TestSimpleParent(unittest.TestCase):
    def test_boot_required(self):
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        calc_nodes = t2n.text_to_textnodes(test_text)
        self.assertListEqual = (
            [
                tn.TextNode("This is ", tn.TextType.TEXT),
                tn.TextNode("text", tn.TextType.BOLD),
                tn.TextNode(" with an ", tn.TextType.TEXT),
                tn.TextNode("italic", tn.TextType.ITALIC),
                tn.TextNode(" word and a ", tn.TextType.TEXT),
                tn.TextNode("code block", tn.TextType.CODE),
                tn.TextNode(" and an ", tn.TextType.TEXT),
                tn.TextNode(
                    "obi wan image",
                    tn.TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                tn.TextNode(" and a ", tn.TextType.TEXT),
                tn.TextNode("link", tn.TextType.LINK, "https://boot.dev"),
            ],
            calc_nodes,
        )

    def test_mine(self):
        test_text = "This is _italic_ with a **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and another `block of code`."
        calc_nodes = t2n.text_to_textnodes(test_text)
        self.assertListEqual = (
            [
                tn.TextNode("This is ", tn.TextType.TEXT),
                tn.TextNode("italic", tn.TextType.ITALIC),
                tn.TextNode(" with a ", tn.TextType.TEXT),
                tn.TextNode("bold", tn.TextType.BOLD),
                tn.TextNode(" word and a ", tn.TextType.TEXT),
                tn.TextNode("code block", tn.TextType.CODE),
                tn.TextNode(" and an ", tn.TextType.TEXT),
                tn.TextNode(
                    "obi wan image",
                    tn.TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                tn.TextNode(" and a ", tn.TextType.TEXT),
                tn.TextNode("link", tn.TextType.LINK, "https://boot.dev"),
                tn.TextNode(" and another ", tn.TextType.TEXT),
                tn.TextNode("block of code", tn.TextType.CODE),
                tn.TextNode(".", tn.TextType.TEXT)
            ],
            calc_nodes,
        )
