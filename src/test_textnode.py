#!/opt/homebrew/bin/python3

import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.ITALIC)
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

def test_split_nodes_delimiter():
    # Test 1: Basic split with code
    node = TextNode("hello `code` world", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert len(nodes) == 3
    assert nodes[0].text == "hello "
    assert nodes[0].text_type == TextType.TEXT
    assert nodes[1].text == "code"
    assert nodes[1].text_type == TextType.CODE
    assert nodes[2].text == " world"
    assert nodes[2].text_type == TextType.TEXT

    # Test 2: Node that's already bold should be unchanged
    node = TextNode("already bold", TextType.BOLD)
    nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    assert len(nodes) == 1
    assert nodes[0].text == "already bold"
    assert nodes[0].text_type == TextType.BOLD

    # Test 3: Missing delimiter should raise exception
    node = TextNode("missing delimiter `", TextType.TEXT)
    try:
        split_nodes_delimiter([node], "`", TextType.CODE)
        assert False, "Expected exception"
    except Exception:
        assert True



if __name__ == "__main__":
    unittest.main()