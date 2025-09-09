import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestURLDifference(unittest.TestCase):
    def test_url_neq(self):
        node = TextNode("This is a url node", TextType.LINK, url="http://www.yahoo.com")
        node2 = TextNode("This is a url node", TextType.LINK, url = "http://www.google.com")
        self.assertNotEqual(node, node2)

class TestURLSame(unittest.TestCase):
    def test_url_eq(self):
        node = TextNode("Another url node", TextType.LINK, url="http://www.yahoo.com")
        node2 = TextNode("Another url node", TextType.LINK, url="http://www.yahoo.com")
        self.assertEqual(node, node2)

class TestLinkHasURL(unittest.TestCase):
    def test_linke_has_url(self):
        node = TextNode("A final url node", TextType.LINK, url="http://www.yahoo.com")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertNotEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
