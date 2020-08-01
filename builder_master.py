import sys
from cx_Freeze import setup, Executable

build_exe_options = {           # wichtig!
    "packages": ["keylogger"],  # die "import modul" module
    "excludes": ["threading"],    # die "from modul" module
    "includes": ["Thread"]    # die "nach dem from modul import" module
}

setup(name="EXE",       # name
      version="1.0",    #datei version
      description="",   # beschreibung
      executables = [Executable("master.py")]) # die datei die zu bauen ist
