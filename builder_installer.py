import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["zipfile", "os","getpass"], 
    "excludes": ["swinlnk.swinlnk"],
    "includes": ["SWinLnk"] 
}


setup(name="EXE",
      version="1.0",
      description="",
      executables = [Executable("installer.py")])
