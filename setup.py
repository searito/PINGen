from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("pinGenerator.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "<Pin Generator>",
    options = options,
    version = "1.0",
    description = "<Generador De Pins Para Acceso Wifi>",
    executables = executables
)