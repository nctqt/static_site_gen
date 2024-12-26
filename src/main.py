#!/opt/homebrew/bin/python3

from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import subprocess

def rec_file_copy():
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

def main():
    rec_file_copy("source", "dest")
    return

main()