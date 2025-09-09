import unittest
import leafnode as ln
import parentnode as pn

class TestSimpleParent(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = ln.LeafNode("span", "child")
        parent_node = pn.ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>")


class TestMultiParent(unittest.TestCase):
    def test_to_html_with_grandchildren(self):
        grandchild_node = ln.LeafNode("b", "grandchild")
        child_node = pn.ParentNode("span", [grandchild_node])
        parent_node = pn.ParentNode("div", [child_node])
        self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>")


class TestMultiChild(unittest.TestCase):
    def test_to_html_multiple_children(self):
        child_node = ln.LeafNode("span","child")
        child_node2 = ln.LeafNode("div","child2")
        sub_parent_node = pn.ParentNode("h2",[child_node, child_node2])
        child_node3 = ln.LeafNode("p","child3")
        parent_node = pn.ParentNode("h1",[sub_parent_node,child_node3])
        self.assertEqual(parent_node.to_html(),
                      "<h1><h2><span>child</span><div>child2</div></h2><p>child3</p></h1>",
      )
