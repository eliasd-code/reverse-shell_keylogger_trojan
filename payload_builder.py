import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["logging","getpass"], 
    "excludes": ["pynput.keyboard"],
    "includes": ["Key","Listener"] 
}


setup(name="EXE",
      version="1.0",
      description="",
      executables = [Executable("payload.py")])
