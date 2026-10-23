# Personal Tools 🛠️

A collection of lightweight Python utilities for automating everyday file-management tasks, including PDF compression, HTML-to-PDF conversion, merging HTML files, and combining multiple PDF documents.

These scripts are designed for personal use and can be adapted to suit different local workflows.

## 📂 Project Structure

```text
Personal-Tools-/
├── compress.py    # Compress PDF files by re-rendering pages
├── output.py      # Convert an HTML file into a PDF
├── share.py       # Merge HTML files from ZIP archives
├── share1.py      # Merge HTML files from a directory
├── merge.py       # Merge multiple PDF files into one
└── README.md      # Project documentation
```

## ✨ Features

### 1. PDF Compression — `compress.py`

Reduces PDF file size by rendering each page at 150 DPI, converting the rendered page to JPEG, and rebuilding the PDF.

**How it works:**
- Opens the source PDF using PyMuPDF.
- Renders each page at 150 DPI.
- Converts the rendered page to JPEG.
- Reconstructs the PDF and applies cleanup and compression options.
- Saves the resulting PDF to the configured output path.

**Dependency:** `PyMuPDF`

### 2. HTML to PDF — `output.py`

Converts a local HTML file into an A4-sized PDF using Playwright and Chromium.

**Features:**
- Opens a local HTML document in Chromium.
- Applies print media styles.
- Generates an A4 PDF with 10 mm margins.
- Preserves background graphics in the PDF output.

**Dependencies:** `Playwright` and Chromium.

### 3. Merge HTML Files from ZIP Archives — `share.py`

Combines HTML documents contained in ZIP archives into a single HTML output file.

**Features:**
- Finds ZIP files in the configured input directory.
- Sorts archives by dates extracted from filenames matching the `YYYYMMDD` suffix pattern.
- Reads HTML content directly from ZIP archives without extracting the entire archive to disk.
- Adds HTML comments identifying each source file.
- Writes the combined content to a single HTML file.

**Dependencies:** Python standard library (`os`, `zipfile`, and `re`).

### 4. Merge HTML Files from a Directory — `share1.py`

Combines `.html` and `.htm` files from a directory into a single HTML file.

**Features:**
- Identifies HTML files in the configured directory.
- Sorts filenames naturally, so numbered files such as `2.html` appear before `10.html`.
- Adds an HTML comment identifying each source file.
- Writes the merged content to a single output file.

**Dependencies:** Python standard library (`os` and `re`).

### 5. Merge PDF Files — `merge.py`

Combines multiple PDF files from a specified directory into one PDF document.

**Features:**
- Automatically identifies PDF files in the configured input folder.
- Sorts filenames naturally, so `1.pdf`, `2.pdf`, and `10.pdf` are processed in the correct order.
- Excludes the output file, `merged.pdf`, from the input list.
- Displays the processing order before merging.
- Combines the PDFs into a single output file named `merged.pdf`.

**Dependency:** `PyPDF2`

## ⚙️ Requirements

- Python 3
- PyMuPDF for PDF compression
- Playwright and Chromium for HTML-to-PDF conversion
- PyPDF2 for PDF merging

The HTML-merging scripts use Python's standard library and require no additional third-party packages.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aarnav2425/Personal-Tools-.git
cd Personal-Tools-
```

### 2. Install dependencies

For PDF compression:

```bash
python3 -m pip install pymupdf
```

For HTML-to-PDF conversion:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
```

For PDF merging:

```bash
python3 -m pip install PyPDF2
```

### 3. Configure file paths

The scripts currently use absolute file paths defined inside their Python files.

Before running a script, edit the relevant input and output paths to match your local files and directories.

For example, in `compress.py`:

```python
input_pdf = "/path/to/input.pdf"
output_pdf = "/path/to/compressed.pdf"
```

In `merge.py`, update the input folder:

```python
input_folder = Path("/path/to/pdf/folder")
```

Ensure the input files exist and the output directory is writable.

## ▶️ Usage

Run the desired script from your terminal.

**Compress a PDF:**

```bash
python3 compress.py
```

**Convert HTML to PDF:**

```bash
python3 output.py
```

**Merge HTML files inside ZIP archives:**

```bash
python3 share.py
```

**Merge HTML files from a directory:**

```bash
python3 share1.py
```

**Merge multiple PDF files:**

```bash
python3 merge.py
```

These scripts use the file paths configured in their source code and do not currently accept command-line arguments.

## ⚠️ Important Notes

- **PDF compression:** Pages are rasterized into JPEG images. The resulting PDF may lose selectable and searchable text, vector graphics, and some original document properties. Image quality may also decrease.
- **HTML merging:** Concatenating complete HTML documents does not guarantee a single valid HTML page. Documents with their own `<html>`, `<head>`, or `<body>` elements, relative asset paths, or conflicting styles may require additional processing.
- **Output files:** `share.py` and `share1.py` use the same output filename by default. Change the output path if you want to preserve separate results.
- **PDF merging:** `merge.py` writes the combined document to `merged.pdf` in the configured input directory. Ensure that the source PDFs are the intended files and that the output can be written.
- **File paths:** Update machine-specific paths before running the scripts on another computer.
- **Data safety:** Keep backups of important source files before performing file-processing operations.

## 🧰 Future Improvements

Potential enhancements include:

- Accept input and output paths through command-line arguments.
- Add error handling for missing files and invalid input formats.
- Make PDF resolution and image quality configurable.
- Generate valid merged HTML documents with appropriate document structure.
- Add a `requirements.txt` file for easier dependency management.

## 📄 License

No license has been specified yet. Add a license file if you intend to define how others may use, modify, and distribute this project.
