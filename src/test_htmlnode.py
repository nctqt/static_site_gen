#!/opt/homebrew/bin/python3

import unittest

from htmlnode import HTMLNode

props_dict = {"href":"https://www.google.com"}
test_node = HTMLNode("a", "value text", None, None)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "value text", None, None)
        node2 = HTMLNode("p", "value text", None, None)
        self.assertEqual(node, node2)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "value text", None, props_dict)
        node2 = HTMLNode("a", "value text", None, props_dict)
        self.assertEqual(node, node2)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "value text", None, None)
        node2 = HTMLNode("a", "value text", None, None)
        self.assertNotEqual(node, node2)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "value text", [test_node], props_dict)
        node2 = HTMLNode("a", "value text", [test_node], props_dict)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()