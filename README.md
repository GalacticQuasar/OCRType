# OCR Typing Application
By Akash Ravandhu

### Functionality:
This app allows the user to take any clear image screenshot containing text and simulate humanlike typing. The image is processed through an OCR (Optical Character Recognition) algorithm in PyTesseract.

> Note: If you intend to run this application as a python script, you must install PyTesseract on your device, which you may do through [this link](https://github.com/UB-Mannheim/tesseract/releases).

### Instructions:
Keep in mind that the escape key is `ESC`.
1. Run the script (instructions will be available in the console)
2. Take a screenshot with `WIN` + `SHIFT` + `S` or copy any image containing text to your clipboard.
3. Click enter in the console (this will prompt the app to take the image that is currently copied to your clipboard and process it into a string of text through OCR).
4. Press `CTRL` when you are ready to start typing. The typing speed is set to be around 200 WPM.

### Packages:
- PyTesseract (for OCR)
- Keyboard (for key listeners and simulating input)
- PIL (for Image object)
