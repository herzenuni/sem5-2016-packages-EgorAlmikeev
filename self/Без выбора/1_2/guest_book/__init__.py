import inspect
import os
import sys

def get_script_dir(follow_symlinks=True):
    """
    https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory/22881871#22881871
    """
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

sys.path.append(get_script_dir())

from guest_book_classes import JSONReadWritter
from guest_book_classes import GuestBook
from guest_book_classes import Guest
