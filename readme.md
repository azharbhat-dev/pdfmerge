# 📄 PDF Resizer and Merger Web App

A lightweight web application built with Flask for resizing and merging multiple PDF files. The app ensures all pages in the merged output are uniformly resized to fit standard A4 dimensions while maintaining the original content's aspect ratio.

## ✨ Features

- **📤 Upload Multiple PDFs**: Easily upload multiple PDF files through the browser.
- **📏 Uniform Page Sizing**: All pages are resized to standard A4 dimensions (595x842 points).
- **🔗 PDF Merging**: Combines all uploaded files into a single, resized PDF.
- **⬇️ Download Output**: Download the processed PDF directly after merging.

## 🤔 Why This App?

Merging PDFs often results in mismatched page sizes, making them difficult to view or print uniformly. This app addresses this issue by resizing each page to a standard size, ensuring consistency in the final output.

## 🚀 Getting Started

### Prerequisites

To run the app, you'll need:
- **Python 3.7+**
- **pip** (Python package manager)

### 🛠 Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/pdf-resizer-merger.git](https://github.com/azharbhat-dev/pdfmerge.git)
   cd pdfmerge
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Required packages include:
   - Flask
   - PyMuPDF (`fitz`)

3. Create the uploads folder:
   ```bash
   mkdir uploads
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5001/
   ```

## 🖱️ Usage

1. Open the web app in your browser.
2. Upload one or more PDF files via the file selection form.
3. Click **Upload and Merge** to process the PDFs.
4. Download the resized and merged PDF file.

## 🗂️ Project Structure

```
pdf-resizer-merger/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML template for the web app
├── uploads/              # Folder for uploaded and processed files
```

## 🔧 Key Functions

### Resizing and Merging PDFs

The core functionality is handled by the `resize_and_merge_pdfs` function in `app.py`. This function:
- Resizes all pages to A4 dimensions while preserving their aspect ratio.
- Merges the resized pages into a single PDF.

## 🛠️ Customization

- **Target Page Size**: Modify the `target_size` parameter in `resize_and_merge_pdfs` to use custom dimensions.
- **Port Number**: Change the port in `app.run(debug=True, port=5001)` to host on a different port.

## 🤝 Contribution

Contributions and feedback are welcome! Feel free to:
- Fork this repository
- Submit issues
- Propose new features via pull requests

## 📄 License

This project is licensed under the MIT License. Use it freely for personal or commercial projects.

---

**Happy PDF Resizing and Merging! 🎉**
