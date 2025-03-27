# Python Project LINEARCKTS_THOMAS
Problems from the textbook: Analysis and Design of Linear Circuits, 6th edition by Thomas, Rosa.

# ENKI2 Laptop
## Generate Virtual Env

```
C:\SourceCode\GitHub\electronix\linearckts_thomas>py -0p
 -V:3.12 *        C:\TechRoot\py\3.12.0\python.exe

C:\SourceCode\GitHub\electronix\linearckts_thomas> py -3.12 -m venv .venvPy3-12-0  <======
```
In VSCode, if a dialog pops-up asking

`We noticed a new environment has been created.  Do you
want to select if for the workspace folder?`

Click `No`.

## Activate the 3.12.0 Environment and Dump Help
See specific config_*.ini file for details on how to run.

```
C:\SourceCode\GitHub\electronix\linearckts_thomas> pyactivate_3-12-0.bat  <======

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\linearckts_thomas> python --version  <======
Python 3.12.0

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\linearckts_thomas> pip --version  <======
pip 23.2.1 from C:\SourceCode\GitHub\electronix\linearckts_thomas\.venvPy3-12-0\Lib\site-packages\pip (python 3.12)

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\linearckts_thomas> pip freeze  <======

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\linearckts_thomas> cd run

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\linearckts_thomas\run> microelx.py  <====== dump help

```

## VSCode Setup

If this `~` in source code as below complaining about

`Bad indentation. Found 1 spaces, expected 4Pylint(W0311:bad-indentation)`:

```
def main() -> int:
~   <<<<<=============================
	"""
	Entry point for script.
```

### FIX
Ensure file .pylintrc tabs set correctly:

```
String used as indentation unit. This is usually "    " (4 spaces) or "\t" (1 tab).
indent-string='\t'
```

## Installations

```
numpy, matplotlib
```
