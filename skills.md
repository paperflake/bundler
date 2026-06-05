# AI Agent Skill: ProjectToBash Bundler

## Description
You have access to a local CLI tool called `ProjectToBash` (`project2bash.py`). This tool packages an entire directory, including its folder structure and text-based source code, into a single, self-extracting bash script (`.sh`). It automatically ignores binary files and heavy directories (like `node_modules` or `.git`).

## When to use this tool
Trigger this tool when the human user asks you to:
- "Export" or "Bundle" the current project.
- Create a deliverable, boilerplate, or template.
- Share the codebase so they can run it on another machine.
- Consolidate multiple files you just generated into a single file for easy download.

## How to use this tool
Execute the tool via the command line using Python. 

### Basic Command
```bash
python project2bash.py <target_directory> -o <output_filename.sh>

Advanced Commands

    Include environment variables: (Only do this if explicitly asked by the user, as it may leak secrets)
    Bash

    python project2bash.py <target_directory> -o <output_filename.sh> --include-env

    Ignore specific directories:
    Bash

    python project2bash.py <target_directory> -o <output_filename.sh> -i <folder1> <folder2>

Post-Execution Instructions for the AI

    Do not attempt to read the generated .sh file. It is a deployment artifact and will consume too much of your context window.

    Confirm success to the user. Tell the user the name of the file that was generated.

    Provide extraction instructions. Instruct the user to run the following command on their target machine to unpack the project:
    Bash

    bash <output_filename.sh>
