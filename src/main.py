#!/opt/homebrew/bin/python3

from textnode import TextType, TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():

    test = TextNode("hello", TextType.IMAGE, "http://www.google.com")
    print(test.__repr__())

    node = HTMLNode("a", "value text", None, {"href": "https://www.google.com"})
    print(node.__repr__())

    node2 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
        ]
    )
    print(node2.to_html())



    

    return

main()