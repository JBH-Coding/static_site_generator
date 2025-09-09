import unittest
import leafnode as ln


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = ln.LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_header(self):
        node = ln.LeafNode("h2", "Header 2 Text")
        self.assertEqual(node.to_html(), "<h2>Header 2 Text</h2>")

    def test_leaf_to_html_main(self):
        node = ln.LeafNode("main", "This represents the main portion of the page.")
        self.assertEqual(
            node.to_html(), "<main>This represents the main portion of the page.</main>"
        )
