# GenAI-Course

## Installation Guide

This project uses Python and a virtual environment to isolate dependencies.

### 1. Install Python

- Install Python 3.11 or later from https://www.python.org/downloads/windows
- During installation, enable:
  - `Add Python to PATH`
  - `pip`
  - `venv`

### 2. Create a virtual environment

Open PowerShell in the project root:

```powershell
cd D:\Ayush_Files\Users\kumar\GenAI-Course
py -m venv .venv
```

### 3. Activate the virtual environment

In PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

In CMD:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

Once the environment is active:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Verify installation

Run a Python check:

```powershell
python --version
python -c "import langchain, openai, numpy, pandas, torch"
```

### 6. Project layout

- `chains/` - example chain scripts
- `Models/` - model definitions
- `parser/` - parser utilities
- `prompt/` - prompt examples
- `structured_data/` - structured data examples

### Notes

- `venv` is a standard Python module and does not require `pip install venv`.
- If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

That’s all you need to get started with this repository.