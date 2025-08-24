import yaml
import re

def process_title(name):
    return name.replace('-', ' ').replace('_', ' ').title()

def get_frontmatter_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if content.startswith('---'):
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                return yaml.safe_load(match.group(1)).get('title')
    except:
        pass
    return None

def safe_process_nav_item(nav_item):
    try:
        if hasattr(nav_item, 'file') and nav_item.file:
            frontmatter_title = get_frontmatter_title(nav_item.file.abs_src_path)
            nav_item.title = frontmatter_title or process_title(nav_item.title or '')
        elif hasattr(nav_item, 'title') and nav_item.title:
            nav_item.title = process_title(nav_item.title)
        
        if hasattr(nav_item, 'children'):
            for child in nav_item.children:
                safe_process_nav_item(child)
    except:
        pass

def on_nav(nav, config, files):
    if nav:
        for nav_item in nav:
            safe_process_nav_item(nav_item)
