from bdb import BdbQuit
from pathlib import Path
import shutil

import click

from .form import AuthorForm


@click.command()
@click.argument('form_directory')
@click.option('--verbose', '-v', is_flag=True, help='Report on each form')
@click.option('--pdb', 'with_debugger', is_flag=True, help='Drop into python debugger if an error occurs.')
def screen_forms(form_directory, verbose, with_debugger):
    try:
        _screen_forms(form_directory, verbose)
    except (BdbQuit, KeyboardInterrupt):
        # If the user halts execution, quit.
        raise
    except:
        # Otherwise, the program errored. Drop into the debugger if
        # the user wants to.  Otherwise reraise the exception and exit.
        if with_debugger:
            import pdb
            import traceback
            traceback.print_exc()
            pdb.post_mortem()
        else:
            raise


def _screen_forms(form_directory, verbose):
    p = Path(form_directory)

    clean_dir = p / 'clean'
    clean_dir.mkdir()

    dirty_dir = p / 'dirty'
    dirty_dir.mkdir()

    for form in p.iterdir():
        if form.suffix == '.pdf':
            a = AuthorForm(form)
            if is_valid_form(a):
                shutil.move(form, clean_dir / form.name)
                if verbose:
                    print(f"{form.name} validated, moving to {str(clean_dir)}")
            else:
                shutil.move(form, dirty_dir / form.name)
                if verbose:
                    print(f"{form.name} not validated, moving to {str(dirty_dir)}")


def is_valid_form(a):
    """Put your screening logic here."""
    return True
