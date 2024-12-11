Windows environment setup
```
python -m venv .venv
.venv\Scripts\activate.bat 
pip install uv
pip install -r .\requirements.txt

fastapi dev main.py
```