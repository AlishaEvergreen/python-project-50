### Hexlet tests and linter status:
[![Actions Status](https://github.com/makaralina/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/makaralina/python-project-50/actions)
[![Python CI](https://github.com/makaralina/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/makaralina/python-project-50/actions/workflows/main.yml)

---

### 🔸**Project Overview**

**Difference Calculator** is a CLI tool that allows users to compare two configuration files (*JSON* or *YAML*) and output their differences in various formats:
- stylish (default);
- plain;
- json.

---

### 🔸**Requirements**

- python 3.10+
- poetry

---

### 🔸**Installation**

`pip install git+https://github.com/makaralina/python-project-50.git`

After installation, run these commands to set up the project:
- ```make install```
- ```make build```
- ```make package-reinstall```

---

### 🔸**Usage**

To use the tool from the command line, run the following command:
```gendiff <file_path1> <file_path2> --format <format>```
Arguments:
- *```<file_path1>```* — path to first file;
- *```<file_path2>```* — path to second file;
- *```<format>```* — stylish/plain/json format.

For help with available commands and options, run: ```gendiff -h```.

---

### 🔸**Usage Examples**

#### **Comparing two flat .json files:**

   [![asciicast](https://asciinema.org/a/pAAV7T3ozOVRyfD1K1LfeFNXG.svg)](https://asciinema.org/a/pAAV7T3ozOVRyfD1K1LfeFNXG)

#### **Comparing two flat .yml files:**

   [![asciicast](https://asciinema.org/a/NmbPA25nfhvDST8Q5SSjWoRRe.svg)](https://asciinema.org/a/NmbPA25nfhvDST8Q5SSjWoRRe)

#### **Comparing two .json or .yaml files with a nested structure:**
   
   - #### Stylish Output Format:
   [![asciicast](https://asciinema.org/a/k8Tr0y9pqEdbsgedAsemr5VMi.svg)](https://asciinema.org/a/k8Tr0y9pqEdbsgedAsemr5VMi)

   - #### Plain Output Format:
   [![asciicast](https://asciinema.org/a/NbWR53aqcOI9vbDlbzn8Tb9sh.svg)](https://asciinema.org/a/NbWR53aqcOI9vbDlbzn8Tb9sh)

   - #### JSON Output Format:
   [![asciicast](https://asciinema.org/a/8sNsK1huLstCMEWTfYMrHX4dO.svg)](https://asciinema.org/a/8sNsK1huLstCMEWTfYMrHX4dO)

---

### ❤️ **Acknowledgements**

#### Thanks for stopping by, buddy! If you find this tool helpful, don't forget to give it a ⭐ on GitHub!
