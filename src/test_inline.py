import unittest
import textnode as tn
import textnode_inline as ti


class TestInlineItalics(unittest.TestCase):
    def test_italics(self):
        node0 = tn.TextNode("This node has **bold text** included.", tn.TextType.TEXT)
        node1 = tn.TextNode("This node has _inline italics_ included.", tn.TextType.TEXT)
        node2 = tn.TextNode("This node has `code blocks` included.", tn.TextType.TEXT)
        node_list = [node0, node1, node2]
        nodes = ti.split_nodes_delimiter(node_list, "_", tn.TextType.ITALIC)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[2].text_type, tn.TextType.ITALIC)
        self.assertEqual(nodes[1].text, "This node has ")
        self.assertEqual(nodes[3].text, " included.")


class TestInlineBold(unittest.TestCase):
    def test_bold(self):
        node0 = tn.TextNode("This node has **bold text** included.", tn.TextType.TEXT)
        node1 = tn.TextNode(
            "This node has _inline italics_ included.", tn.TextType.TEXT
        )
        node2 = tn.TextNode("This node has `code blocks` included.", tn.TextType.TEXT)
        node_list = [node0, node1, node2]
        nodes = ti.split_nodes_delimiter(node_list, "**", tn.TextType.BOLD)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[1].text_type, tn.TextType.BOLD)
        self.assertEqual(nodes[0].text, "This node has ")
        self.assertEqual(nodes[2].text, " included.")


class TestInlineCode(unittest.TestCase):
    def test_code(self):
        node0 = tn.TextNode("This node has **bold text** included.", tn.TextType.TEXT)
        node1 = tn.TextNode(
            "This node has _inline italics_ included.", tn.TextType.TEXT
        )
        node2 = tn.TextNode("This node has `code blocks` included.", tn.TextType.TEXT)
        node_list = [node0, node1, node2]
        nodes = ti.split_nodes_delimiter(node_list, "`", tn.TextType.CODE)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[3].text_type, tn.TextType.CODE)
        self.assertEqual(nodes[2].text, "This node has ")
        self.assertEqual(nodes[4].text, " included.")

class TestInLineImages(unittest.TestCase):
    def test_extract_markdown_images(self):
      matches = ti.extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
      )
      self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestInLineLink(unittest.TestCase):
    def test_extract_markdown_link(self):
        matches = ti.extract_markdown_links(
            "This is text with a [link](http://www.google.com)"
        )
        self.assertListEqual([("link", "http://www.google.com")], matches)

class TestInLineLinkImage(unittest.TestCase):
    def test_extract_markdown_image_from_both(self):
        matches = ti.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)\n"
            + "This is text with a [link](http://www.google.com)\n"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestInLineLinkImage(unittest.TestCase):
    def test_extract_markdown_link_from_both(self):
        matches = ti.extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)\n"
            + "This is text with a [link](http://www.google.com)\n"
        )
        self.assertListEqual([("link", "http://www.google.com")], matches)


class TestSplitInlineImage(unittest.TestCase):
    def test_split_images(self):
        node = tn.TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        tn.TextType.TEXT
        )
        new_nodes = ti.split_nodes_image([node])
        self.assertListEqual(
            [
                tn.TextNode("This is text with an ", tn.TextType.TEXT),
                tn.TextNode(
                    "image", tn.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
                tn.TextNode(" and another ", tn.TextType.TEXT),
                tn.TextNode(
                    "second image", tn.TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class TestSplitInlineLink(unittest.TestCase):
    def test_split_images(self):
        node = tn.TextNode(
            "This is text with a [link](http://www.google.com) and another [second link](http://www.amazon.com)",
            tn.TextType.TEXT,
        )
        new_nodes = ti.split_nodes_link([node])
        self.assertListEqual(
            [
                tn.TextNode("This is text with a ", tn.TextType.TEXT),
                tn.TextNode(
                    "link", tn.TextType.LINK, "http://www.google.com"
                ),
                tn.TextNode(" and another ", tn.TextType.TEXT),
                tn.TextNode(
                    "second link", tn.TextType.LINK, "http://www.amazon.com"
                ),
            ],
            new_nodes,
        )


class TestSplitInlineImageBetweenLinks(unittest.TestCase):
    def test_split_images(self):
        node = tn.TextNode(
            "This is text with a [link](http://www.google.com) then an ![image](https://i.imgur.com/zjjcJKZ.png) followed by another [second link](http://www.amazon.com) and then more text",
            tn.TextType.TEXT,
        )
        new_nodes = ti.split_nodes_link([node])
        self.assertListEqual(
            [
                tn.TextNode("This is text with a ", tn.TextType.TEXT),
                tn.TextNode("link", tn.TextType.LINK, "http://www.google.com"),
                tn.TextNode(
                    " then an ![image](https://i.imgur.com/zjjcJKZ.png) followed by another ",
                    tn.TextType.TEXT,
                ),
                tn.TextNode("second link", tn.TextType.LINK, "http://www.amazon.com"),
                tn.TextNode(" and then more text", tn.TextType.TEXT, ),
            ],
            new_nodes,
        )


class TestSplitAll(unittest.TestCase):
    def test_split_images(self):
        node = tn.TextNode(
            "This is text with a [link](http://www.google.com) then an ![image](https://i.imgur.com/zjjcJKZ.png) followed by another [second link](http://www.amazon.com) and then more text",
            tn.TextType.TEXT,
        )
        new_nodes = ti.split_nodes_link([node])
        full_nodes = ti.split_nodes_image(new_nodes)
        self.assertListEqual(
            [
                tn.TextNode("This is text with a ", tn.TextType.TEXT),
                tn.TextNode("link", tn.TextType.LINK, "http://www.google.com"),
                tn.TextNode(" then an ", tn.TextType.TEXT,),
                tn.TextNode("image", tn.TextType.IMAGE, url="https://i.imgur.com/zjjcJKZ.png",),
                tn.TextNode(" followed by another ", tn.TextType.TEXT,),
                tn.TextNode("second link", tn.TextType.LINK, "http://www.amazon.com"),
                tn.TextNode(" and then more text",tn.TextType.TEXT,),
            ],
            full_nodes,
        )


if __name__ == "__main__":
    unittest.main()
