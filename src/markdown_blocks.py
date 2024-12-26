from htmlnode import ParentNode
from processing import text_to_textnodes
from textnode import text_node_to_html_node
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = []
    for block in blocks:
        temp = block.strip()
        if temp != "":
            stripped.append(temp)
    return stripped

def block_to_block_type(md_string):
    if re.search(r"^#{1,6} ", md_string):
        return "heading"
    elif re.search(r"^\`{3}[\S\s]+\`{3}$", md_string):
        return "code"
    elif re.search(r"^>", md_string):
        lines = md_string.splitlines()
        for line in lines:
            if not re.search(r"^>", line):
                return "paragraph"
        return "quote"
    elif re.search(r"^[*-] ", md_string):
        lines = md_string.splitlines()
        for line in lines:
            if not re.search(r"^[*-] ", line):
                return "paragraph"
        return "unordered_list"
    elif re.search(r"^(\d+)\.", md_string):
        lines = md_string.splitlines()
        temp = re.findall(r"^(\d+)\.", md_string)
        index = int(temp[0])
        if index != 1:
            return "paragraph"
        for line in lines:
            if not re.search(r"^(\d+)\.", line):
                return "paragraph"
            if int(re.findall(r"^(\d+)\.", line)[0]) != (index):
                return "paragraph"
            index += 1
        return "ordered_list"
    else:
        return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)