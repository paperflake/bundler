#!/usr/bin/env python3
"""
ProjectToBash - Bundles a directory into a single, executable shell script.
Perfect for sharing context with AI agents or distributing boilerplate projects.
"""

import os
import argparse
from pathlib import Path

# Default directories to ignore
DEFAULT_IGNORE_DIRS = {
    '.git', 'node_modules', '__pycache__', 'venv', '.venv', 
    'dist', 'build', '.idea', '.vscode'
}

def is_text_file(filepath: Path) -> bool:
    """Checks if a file is plain text by attempting to read it in UTF-8 format."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(1024)  # Read only the beginning to save memory
        return True
    except UnicodeDecodeError:
        return False

def generate_bundle(source_dir: str, output_file: str, extra_ignores: list):
    source_path = Path(source_dir).resolve()
    out_path = Path(output_file).resolve()
    
    ignore_dirs = DEFAULT_IGNORE_DIRS.copy()
    if extra_ignores:
        ignore_dirs.update(extra_ignores)

    dirs_to_create = set()
    file_contents = []

    print(f"📦 Bundling directory: {source_path}")

    # 1. Traverse the directory tree
    for root, dirs, files in os.walk(source_path):
        # Filter out ignored directories on the fly
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            filepath = Path(root) / file
            
            # Ignore the generated script itself and this tool
            if filepath == out_path or file == Path(__file__).name:
                continue
            
            # Ensure it's a text file
            if not is_text_file(filepath):
                continue
            
            rel_path = filepath.relative_to(source_path).as_posix()
            parent_dir = filepath.parent.relative_to(source_path).as_posix()
            
            if parent_dir != ".":
                dirs_to_create.add(parent_dir)
                
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                file_contents.append((rel_path, content))
            except Exception as e:
                print(f"⚠️ Skipping {rel_path} (read error: {e})")

    # 2. Write the output file (Bash script)
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write("#!/bin/bash\n")
        out.write("# ==========================================\n")
        out.write(f"# ProjectToBash - Generated bundle\n")
        out.write("# Run this script to extract the project\n")
        out.write("# ==========================================\n\n")
        
        # Directory creation
        if dirs_to_create:
            out.write("echo '📁 Creating directory structure...'\n")
            sorted_dirs = sorted(list(dirs_to_create))
            for d in sorted_dirs:
                out.write(f'mkdir -p "{d}"\n')
            out.write("\n")

        # File creation
        out.write("echo '📝 Writing files...'\n\n")
        for rel_path, content in file_contents:
            out.write(f"echo '  -> {rel_path}'\n")
            # Use cat << 'EOF' (single quotes prevent bash variable evaluation inside the code)
            out.write(f"cat << 'EOF' > \"{rel_path}\"\n")
            out.write(content)
            if not content.endswith('\n'):
                out.write('\n')
            out.write("EOF\n\n")
            
        out.write("echo '✅ Done! Project has been extracted.'\n")

    print(f"✨ Done! Bundled {len(file_contents)} files into script: {out_path.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bundles a project directory into a single executable Bash script.")
    
    parser.add_argument(
        "directory", 
        nargs="?", 
        default=".", 
        help="Directory to bundle (default: current directory '.')"
    )
    
    parser
