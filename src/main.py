#!/opt/homebrew/bin/python3

from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import subprocess

def file_copy():
    result = subprocess.run(["ls", "-la", "../static/"], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["ls", "-la", "../public"], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["rm", "-rf", "../public/"], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["cp", "-r", "../static/", "../public/"], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["ls", "-la", "../public"], capture_output=True, text=True)
    print(result.stdout)

def extract_title(markdown):
    lines = markdown.splitlines()
    if lines[0].startswith("#", 0, 1):
        temp = lines[0].strip("#")
        return temp.strip()
    else:
        raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file at from_path and store the contents in a variable.
    result = subprocess.run(["ls", from_path], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if line.endswith(".md"):
            with open(f"{from_path}/{line}") as file:
                markdown_raw = file.read()
    print(markdown_raw)


def main():
    generate_page("../content", "", "")
    return

main()