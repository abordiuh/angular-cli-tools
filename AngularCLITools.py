#!/usr/bin/env python3
"""
Simple Angular CLI Toolset by Artem Bordiuh
"""
import os
import regex
import glob
import click


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class ErrorCodes:
    OK = 0
    NOT_AN_ANGULAR_PROJECT = 1


ANGULAR_APP_PATH = 'src/app'


def find_string_in_folder(pattern, folderpath, is_regex=False):
    for filepath in glob.iglob(folderpath, recursive=True):
        with open(filepath) as currentFile:
            text = currentFile.read()

            if not is_regex:
                if pattern in text:
                    print(Color.RED + Color.BOLD + filepath + Color.END)
                    print('true')

            else:
                found = regex.search(pattern, text, regex.MULTILINE | regex.DOTALL)
                if found:
                    print(Color.RED + Color.BOLD + filepath + Color.END + ': ')
                    print(found.group())


def check_if_angular_project(project_path):
    if os.path.exists(os.path.join(project_path, ANGULAR_APP_PATH)):
        return True
    return False


def find_routes_in_project(project_path):
    if not check_if_angular_project(project_path):
        return ErrorCodes.NOT_AN_ANGULAR_PROJECT

    find_string_in_folder('const(.*)Routes(.*)($|.)*(];)', os.path.join(project_path, ANGULAR_APP_PATH, '**/*.ts'),
                          True)
    return ErrorCodes.OK


@click.group()
def cli():
    click.echo('Simple Angular CLI Toolset by Artem Bordiuh')


@click.command('routes')
@click.option('--project', default='', help='Path to project')
def find_routes(project):
    click.echo(Color.GREEN + Color.BOLD + 'Looking for routes of the Angular project: ' + project + Color.END)
    error = find_routes_in_project(project)
    if error == ErrorCodes.NOT_AN_ANGULAR_PROJECT:
        click.echo(Color.RED + 'Not an angular project or --project not specified' + Color.END)


cli.add_command(find_routes)


if __name__ == '__main__':
    cli()


