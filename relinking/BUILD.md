# Building and Relinking

## Requirements
1. Python version: 3.12.10
2. Git
3. The dependencies listed in requirements.txt

## Instructions
### (1) Source Code

To obtain the corresponding application source code, go to the repository linked below and find the corresponding to the release version being rebuilt.

https://github.com/Noga-Levy/FieldMouse

Extract the supplied pynput source archive from `third_party/pynput_source.zip`, which corresponds to the version of pynput used in the release.

### (2) Dependency Installation

After creating a Python virtual environment, install the required dependencies via

```pip install -r requirements.txt```

#### (Optional) Pynput Modification

Users who wish to modify pynput may edit the supplied source code. To do this, ensure that the modified version remains compatible with the application, and install the modified pynput such that the application uses that version, rather than an unmodified copy obtained from PyPI. Users can do this via the command below:

```python -m pip install -e ./path/to/modified-pynput```

To verify which version of pynput Python is using, run the following command:

```python -c "import pynput; print(pynput.__file__)"```

If it's using the modified pynput, the resulting path should point to the modified pynput installation. Make sure that the modified pynput, should the user be using one, replaces the one installed from `requirements.txt`.

### (3) Application Building

With all the dependencies and source code installed, build the application by running the command below.

`python -m PyInstaller --onefile --clean main.py`

## Additional Information

The application source code is provided under the terms specified in the project's `LICENSE.md` file.

pynput is separately licensed under the GNU Lesser General Public License, version 3. Its corresponding source code and applicable license texts are provided with this release.

Users are permitted to modify pynput and rebuild the application with their modified version, subject to the applicable licenses.

For additional information, see `NOTICE.md` and the license texts in `licenses/`. For pynput's source code, see `third_party/pynput_source.zip`.