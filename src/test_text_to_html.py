import unittest
import leafnode as ln
import parentnode as pn
import textnode as tn
import texttohtml as t2h

class TestSimpleParent(unittest.TestCase):
    def test_text(self):
        node = tn.TextNode("This is a text node", tn.TextType.TEXT)
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = tn.TextNode("This is a bold node", tn.TextType.BOLD)
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = tn.TextNode("This is an italic node", tn.TextType.ITALIC)
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = tn.TextNode("This is a code node", tn.TextType.CODE)
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = tn.TextNode("This is a link node", tn.TextType.LINK, "http://www.google.com")
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props['href'],"http://www.google.com")

    def test_img(self):
        node = tn.TextNode("This is an image node", tn.TextType.IMAGE, "http://www.bogus.net/cat.png")
        html_node = t2h.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props['src'], "http://www.bogus.net/cat.png")
        self.assertEqual(html_node.props['alt'],"This is an image node")
