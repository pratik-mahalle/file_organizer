
# File Organizer and Command Shortcuts CLI

This is a command-line tool for Linux that organizes files in a directory by their file extensions and manages command shortcuts. It can help keep your directories tidy and allow you to define, save, and execute command shortcuts easily.

## Features

- **Organize files by extension:** Automatically move files into subdirectories based on their file extensions.
- **Manage command shortcuts:** Add, remove, list, and execute command shortcuts to save time and effort.
- **Persistent shortcuts:** Shortcuts are added directly to your shell configuration file, making them available in new shell sessions.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/file_organizer.git
   cd file_organizer

    Make the script executable:

    shell

    chmod +x organizer.py

  Usage
  Organize Files

   Organize files in a specified directory by their file extensions.

   shell

    ./organizer.py organize /path/to/your/directory

   Manage Command Shortcuts
   Add a Shortcut

Add a new command shortcut.

shell

    ./organizer.py add <name> <shortcut_command>

Example:

shell

    ./organizer.py add k 'kubectl'

Remove a Shortcut

Remove an existing command shortcut.

shell

    ./organizer.py remove <name>

Example:

shell

    ./organizer.py remove k

List Shortcuts

List all saved command shortcuts.

shell

    ./organizer.py list

Execute a Shortcut

Execute a command shortcut.

shell

     ./organizer.py exec <name>

Example:

shell

    ./organizer.py exec k

Persistent Shortcuts

After adding a shortcut, the shell configuration is automatically sourced. If you face any issues, manually source your shell configuration:

shell

    source ~/.bashrc  # Or ~/.zshrc if you use Zsh


Configuration

Command shortcuts are stored in a JSON configuration file located at ~/.file_organizer_config.json. This file is created and managed automatically by the script.

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

Contact

For any questions or suggestions, please open an issue on GitHub or contact me at [mahallepratik683@gmail.com].

