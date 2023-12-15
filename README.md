# MomentOCR
Perform live OCR on the text/images on your screen. Currently tested on Linux/Windows

## Framework
- Utilizes tesseract as OCR engine with pytesseract
- Overlay GUI made using tkinter
- Screen is captured using pyscreenshot
- Results are pasted into clipboard using pyperclip

## Usage
- Install required modules using:
```
pip install -r requirements.txt
```

- Make sure tesseract is installed on your system. Refer to the tesseract wiki for installation instructions.
> [!IMPORTANT]  
> If you are using windows make sure to change the path of tesseract executable in the code
> ```py
> pytesseract.pytesseract.tesseract_cmd =r'<PATH>'
> ```

> [!TIP]
> Compile the code using pyinstaller for a portable version
