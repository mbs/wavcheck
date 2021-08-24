from cx_Freeze import setup, Executable

setup(
        name = "wavcheck",
        version = "0.1",
        description = "WAV file checker 0.1",
        executables = [Executable("wavcheck.py")])

