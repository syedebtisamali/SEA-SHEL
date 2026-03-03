# SEA Shell

SEA Shell (Simple Executable Assistant Shell) is a lightweight Python-based interface that combines natural language processing with a command-line environment. It uses the Cohere API to translate plain-English queries into functional shell commands.

## Features

* **Natural Language to CLI**: Ask for a command (e.g., "how do I list all hidden files") and get a direct answer.
* **Direct Execution**: Use the `~` prefix to execute commands directly from the SEA Shell interface.
* **Persistent Context**: Remembers previous queries within the session for better conversational flow.

## Getting Started

### Prerequisites

* Python 3.x
* A Cohere API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/sea-shell.git](https://github.com/yourusername/sea-shell.git)
    cd sea-shell
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

3.  **Configure your API Key:**
    Open `SEA Shell.py` and replace `"YOUR_API_KEY"` with your actual Cohere API key:
    ```python
    def response(user_input, api_key="your-key-here"):
    ```

### Usage

Run the script to start the shell:
```bash
python "SEA Shell.py"
Commands

Ask for help: Type naturally.

Input: << how do I check my disk space?

Output: >> Use df -h

Execute a command: Prefix your command with ~.

Input: << ~ls -la

Output: (Lists all files in current directory)

Exit: Type exit or quit.

Security Note
The ~ prefix uses subprocess.run(shell=True). Please be cautious when executing commands, as this allows for full system access through the script.

License
MIT
