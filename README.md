### Hexlet tests and linter status:
[![Actions Status](https://github.com/makaralina/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/makaralina/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1f531e934429de2a1a63/maintainability)](https://codeclimate.com/github/makaralina/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1f531e934429de2a1a63/test_coverage)](https://codeclimate.com/github/makaralina/python-project-50/test_coverage)
[![Python CI](https://github.com/makaralina/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/makaralina/python-project-50/actions/workflows/main.yml)

### **DIFFERENCE CALCULATOR**
---
#### This is a CLI program to get differences between two *JSON* or *YAML* files in the following formats:
- stylish;
- plain;
- json.

### **Installation Requirements:**
---
- python 3.10+
- poetry

### **Installation:**
---
`pip install git+https://github.com/makaralina/python-project-50.git`

Next, follow these steps:
- ```make install```
- ```make build```
- ```make package-reinstall```



###  Commands:
---
```gendiff <file_path1> <file_path2> --format <format>```

- *```<file_path1>```* — path to first file;
- *```<file_path2>```* — path to second file;
- *```<format>```* — stylish/plain/json format.

Display help on using the program — ```gendiff -h```.

### **Usage examples:**
---


#### **Diffs between two flat .json files:**
   [![asciicast](https://asciinema.org/a/pAAV7T3ozOVRyfD1K1LfeFNXG.svg)](https://asciinema.org/a/pAAV7T3ozOVRyfD1K1LfeFNXG)

#### **Diffs between two flat .yml files:**
   [![asciicast](https://asciinema.org/a/NmbPA25nfhvDST8Q5SSjWoRRe.svg)](https://asciinema.org/a/NmbPA25nfhvDST8Q5SSjWoRRe)

#### **Diffs between two .json or .yaml files with a nested structure:**
   
   - #### Stylish output format:
   [![asciicast](https://asciinema.org/a/k8Tr0y9pqEdbsgedAsemr5VMi.svg)](https://asciinema.org/a/k8Tr0y9pqEdbsgedAsemr5VMi)

   - #### Plain output format:
   [![asciicast](https://asciinema.org/a/NbWR53aqcOI9vbDlbzn8Tb9sh.svg)](https://asciinema.org/a/NbWR53aqcOI9vbDlbzn8Tb9sh)

   - #### JSON output format:
   [![asciicast](https://asciinema.org/a/8sNsK1huLstCMEWTfYMrHX4dO.svg)](https://asciinema.org/a/8sNsK1huLstCMEWTfYMrHX4dO)
