# 💰 Employee Salary Calculator App

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A modern, aesthetically designed desktop application built with Python and Tkinter to calculate employee Net Salary based on Basic Pay. This project was developed as part of the AI Project curriculum at **NIELIT Ropar**.

---

## 📋 Features

* **User-Friendly Interface:** Clean, modern GUI with a "Card" layout and aesthetic color palette (Teal & White).
* **Automated Calculations:** Instantly computes:
    * **HRA** (House Rent Allowance): 20%
    * **DA** (Dearness Allowance): 10%
    * **PF** (Provident Fund): 12%
    * **Tax**: 5%
* **Error Handling:** Validates numeric input to prevent crashes.
* **Standalone Executable:** Can be compiled into a `.exe` for easy distribution.

---

## ⚙️ Logic & Formulas

The application uses the following logic to determine the Net Salary:

1.  **Gross Salary** = `Basic Salary` + `HRA (20%)` + `DA (10%)`
2.  **Deductions** = `PF (12%)` + `Tax (5%)`
3.  **Net Salary** = `Gross Salary` - `Deductions`

---

## 🚀 Installation & Usage

### Prerequisites
* Python 3.x installed on your system.

### Running the Source Code
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Anshita-sharma27/Ai-project.git](https://github.com/Anshita-sharma27/Ai-project.git)
    cd Ai-project
    ```
2.  Run the application:
    ```bash
    python salary_app.py
    ```

### Building the Executable (.exe)
To convert this Python script into a standalone Windows application:

1.  Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2.  Run the build command (ensure you have your `logo.ico` ready):
    ```bash
    pyinstaller --noconsole --onefile --icon=logo.ico salary_app.py
    ```
3.  The output file will be located in the `dist/` folder.

---

## 📸 Screenshots

<img width="487" height="717" alt="image" src="https://github.com/user-attachments/assets/98800377-d996-44f0-817c-07f4a5a494ac" />


---

## 👤 Author & Copyright

**Developed by:** Anshita Sharma  
**Institution:** NIELIT Ropar  
**Copyright:** © Anshita @ 2026  

---

*For any inquiries or contributions, please open an issue in the repository.*
