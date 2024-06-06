#!/usr/bin/env python3

import os
import shutil
import argparse
import json
import subprocess

CONFIG_FILE = os.path.expanduser("~/.file_organizer_config.json")
SHELL_RC_FILE = os.path.expanduser("~/.zshrc")  # Change this if you use a different shell, e.g., "~/.bashrc"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def organize_directory(directory):
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            target_dir = os.path.join(directory, file_extension)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved: {filename} to {target_dir}")

def add_shortcut(name, shortcut_command):
    config = load_config()
    config['shortcuts'][name] = shortcut_command
    save_config(config)
    add_shortcut_to_shell(name, shortcut_command)
    print(f"Shortcut added: {name} -> {shortcut_command}")

def add_shortcut_to_shell(name, shortcut_command):
    with open(SHELL_RC_FILE, 'a') as file:
        file.write(f"alias {name}='{shortcut_command}'\n")
    source_shell_config()

def remove_shortcut(name):
    config = load_config()
    if name in config['shortcuts']:
        del config['shortcuts'][name]
        save_config(config)
        remove_shortcut_from_shell(name)
        print(f"Shortcut removed: {name}")
    else:
        print(f"No shortcut found for: {name}")

def remove_shortcut_from_shell(name):
    if os.path.exists(SHELL_RC_FILE):
        with open(SHELL_RC_FILE, 'r') as file:
            lines = file.readlines()
        with open(SHELL_RC_FILE, 'w') as file:
            for line in lines:
                if not line.strip().startswith(f"alias {name}="):
                    file.write(line)
        source_shell_config()

def list_shortcuts():
    config = load_config()
    for name, command in config.get('shortcuts', {}).items():
        print(f"{name}: {command}")

def execute_shortcut(name):
    config = load_config()
    command = config['shortcuts'].get(name)
    if command:
        subprocess.run(command, shell=True)
    else:
        print(f"No shortcut found for: {name}")

def source_shell_config():
    # Create a small script to source the shell configuration
    source_script = os.path.expanduser("~/.source_shell_config.sh")
    with open(source_script, 'w') as file:
        file.write(f"#!/bin/sh\n")
        file.write(f"exec $SHELL -c 'source {SHELL_RC_FILE}'\n")
    subprocess.run(["/bin/sh", source_script])
    os.remove(source_script)

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory and manage command shortcuts")
    subparsers = parser.add_subparsers(dest='command')

    organize_parser = subparsers.add_parser('organize', help="Organize files in a directory by their file extension")
    organize_parser.add_argument("directory", help="The directory to organize")

    add_parser = subparsers.add_parser('add', help="Add a new command shortcut")
    add_parser.add_argument("name", help="The name of the shortcut")
    add_parser.add_argument("shortcut_command", help="The command to shortcut")

    remove_parser = subparsers.add_parser('remove', help="Remove an existing command shortcut")
    remove_parser.add_argument("name", help="The name of the shortcut to remove")

    subparsers.add_parser('list', help="List all command shortcuts")

    exec_parser = subparsers.add_parser('exec', help="Execute a command shortcut")
    exec_parser.add_argument("name", help="The name of the shortcut to execute")

    args = parser.parse_args()

    if args.command == 'organize':
        organize_directory(args.directory)
    elif args.command == 'add':
        add_shortcut(args.name, args.shortcut_command)
    elif args.command == 'remove':
        remove_shortcut(args.name)
    elif args.command == 'list':
        list_shortcuts()
    elif args.command == 'exec':
        execute_shortcut(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    config = load_config()
    if 'shortcuts' not in config:
        config['shortcuts'] = {}
        save_config(config)
    main()
