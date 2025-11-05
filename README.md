A PyTest-based framework for UI and backend testing.

## 🎯 Project Overview  
This project provides a test automation framework built on [PyTest](https://pytest.org) for both UI and backend testing. It’s designed to help testers and developers quickly write, organise and run automated tests in a consistent and scalable way.

## 🔍 Features  
- Unified test framework supporting **UI** and **backend** test cases  
- Use of PyTest fixtures, marking and parametrisation for flexibility  
- Easily extensible: add new test modules, configure dependencies and environments  
- Modular test organisation: separate folders for UI tests, API/backend tests  
- Integration with CI/CD workflows (see the `.github/workflows` folder)  
- Requirements file (`requirements.txt`) to install dependencies easily

### Prerequisites  
- Python 3.x installed  
- Optional: virtual environment tool (`venv`, `virtualenv`, etc.)  
- Browser driver (for UI tests) if needed — e.g., ChromeDriver for Chrome-based UI automation  

### Installation  
```bash
git clone https://github.com/frincubogdan20/Pytest_framework.git
cd Pytest_framework
python3 -m venv venv                      # (optional but recommended)
source venv/bin/activate                  # Linux/Mac
venv\\Scripts\\activate                     # Windows
pip install --upgrade pip
pip install -r requirements.txt
