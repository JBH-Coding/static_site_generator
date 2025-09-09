import unittest
import htmlnode as hn


class TestHTMLNode(unittest.TestCase):
    def test_nodeeq(self):
        node=hn.HTMLNode(tag="p", value="Random text")
        node2=hn.HTMLNode(tag="p", value="Random text")
        self.assertEqual(node, node2)

    def test_propseq(self):
        node=hn.HTMLNode(tag="p", value="Random text", props={"alt":"Alt Text", "number":"Two"})
        node2=hn.HTMLNode(tag="p", value="Random text", props={"alt":"Alt Text", "number":"Two"})
        self.assertEqual(node, node2)

    def test_propsneq(self):
        node = hn.HTMLNode(
            tag="p",
            value="Random text",
            props={"alt": "Alt Text", "number": "Two"})
        node2=hn.HTMLNode(
            tag="p", 
            value="Random text", 
            props={"alt":"Alt Text", "number":"Three"})
        self.assertNotEqual(node, node2)

