

import re
from textnode import TextType, TextNode, split_nodes_delimiter
from htmlnode import HTMLNode

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_images(old_node.text)
        if links == None:
            new_nodes.append(old_node)
        else:
            text_to_process = old_node.text
            for link in links:
                alt_text = link[0]
                img_url = link[1]
                pieces = text_to_process.split(f"![{alt_text}]({img_url})", 1)
                text_to_process = pieces[1]
                if pieces[0] != "":
                    new_nodes.append(TextNode(pieces[0], TextType.TEXT))
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))
            if text_to_process != "":
                new_nodes.append(TextNode(text_to_process, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if links == None:
            new_nodes.append(old_node)
        else:
            text_to_process = old_node.text
            for link in links:
                alt_text = link[0]
                url = link[1]
                pieces = text_to_process.split(f"[{alt_text}]({url})", 1)
                text_to_process = pieces[1]
                if pieces[0] != "":
                    new_nodes.append(TextNode(pieces[0], TextType.TEXT))
                    new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            if text_to_process != "":
                new_nodes.append(TextNode(text_to_process, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    raw = []
    raw.append(TextNode(text, TextType.TEXT))
    raw = split_nodes_delimiter(raw, "**", TextType.BOLD)
    raw = split_nodes_delimiter(raw, "*", TextType.ITALIC)
    raw = split_nodes_delimiter(raw, "`", TextType.CODE)
    raw.extend(split_nodes_image(raw))
    raw.extend(split_nodes_link(raw))
    return raw