# ProjectToBash 📦

A lightweight Python CLI tool that bundles an entire project directory into a single, executable `bash` script. 

Instead of dealing with `.zip` files, extraction tools, or binary data when sharing code (especially with LLMs and AI Agents), `ProjectToBash` creates a self-extracting plain-text shell script. Running the generated script instantly rebuilds the folder structure and text files anywhere.

## Why?
- **AI Context & Agent Skills:** Paste a single script to ChatGPT/Claude/Gemini to give them your entire project structure, or equip an AI agent with this script as a "tool" so it can package and deliver full boilerplates to you in one file.
- **Easy Distribution:** Distribute Docker setups, microservices, or configs via a single copy-pasteable script.
- **Safe Extraction:** Automatically detects and skips binary files (images, compiled code, etc.). It also uses a collision-proof `EOF` marker, ensuring the resulting bash script never breaks from encoding errors or internal bash variables.

## Requirements
- Python 3.x
- A bash environment to run the output (Native on Linux/macOS. On Windows, use Git Bash or WSL).

## Usage

Run the script in any directory:

```bash
# Bundle the current directory into 'bundle.sh'
python project2bash.py

# Bundle a specific folder into a custom script file
python project2bash.py ./my_project -o deploy_project.sh

# Add extra folders to ignore (e.g., 'data' and 'assets')
python project2bash.py -i data assets

# Include .env files (ignored by default to prevent leaking secrets)
python project2bash.py --include-env

How to extract

To reconstruct the project on the target machine, simply run the generated script:
Bash

bash bundle.sh
# Or make it executable: chmod +x bundle.sh && ./bundle.sh

Defaults

By default, the tool ignores common heavy directories to keep the bundle clean:
.git, node_modules, __pycache__, venv, .venv, dist, build, .idea, .vscode.

It also ignores hidden .env files automatically unless the --include-env flag is explicitly passed.
