# Personal Tools 🛠️

A collection of lightweight Python utilities for automating everyday file-management tasks, including PDF compression, HTML-to-PDF conversion, and merging HTML files from ZIP archives or directories.

These scripts are designed for personal use and can be adapted to suit different local workflows.

## 📂 Project Structure

```text
Personal-Tools/
├── compress.py    # Compress PDF files by re-rendering pages
├── output.py      # Convert an HTML file into a PDF
├── share.py       # Merge HTML files extracted from ZIP archives
├── share1.py      # Merge HTML files from a directory
└── README.md      # Project documentation
```

## ✨ Features

### 1. PDF Compression — `compress.py`

Reduces PDF file size by rendering each page at 150 DPI, converting the rendered page to JPEG, and rebuilding the PDF.

**How it works:**
- Opens the source PDF using PyMuPDF.
- Renders each page at 150 DPI.
- Converts each rendered page to JPEG.
- Reconstructs the PDF and applies PDF cleanup and compression options.
- Saves the resulting PDF to the configured output path.

**Dependency:** `PyMuPDF`

### 2. HTML to PDF — `output.py`

Converts a local HTML file into an A4-sized PDF using Playwright and Chromium.

**Features:**
- Opens a local HTML document in Chromium.
- Applies print media styles.
- Generates an A4 PDF with 10 mm margins.
- Preserves background graphics in the PDF output.

**Dependency:** `Playwright` and its Chromium browser.

### 3. Merge HTML Files from ZIP Archives — `share.py`

Combines HTML documents contained in ZIP archives into one HTML output file.

**Features:**
- Finds ZIP files in the configured input directory.
- Sorts archives by dates extracted from filenames matching the `YYYYMMDD` suffix pattern.
- Extracts HTML content directly from each archive without unpacking the entire archive to disk.
- Adds HTML comments identifying each source member.
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

## ⚙️ Requirements

- Python 3
- PyMuPDF for PDF compression
- Playwright and Chromium for HTML-to-PDF conversion

The HTML merging scripts require no third-party Python packages.

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

### 3. Configure file paths

The scripts currently use absolute file paths defined inside each Python file. Before running a script, edit its `input_file`, `input_folder`, and `output_file` variables as applicable to match your local files and directories.

For example, in `compress.py`:

```python
input_pdf = "/path/to/input.pdf"
output_pdf = "/path/to/compressed.pdf"
```

Use paths that exist on your machine, and ensure the output directory is writable.

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

These scripts use the file paths configured in their source code; they do not currently accept command-line arguments.

## ⚠️ Important Notes

- **PDF compression:** Pages are rasterized into JPEG images. The resulting PDF may lose selectable text, searchable text, vector graphics, and some original document properties. Image quality may also be reduced.
- **HTML merging:** Concatenating HTML documents does not guarantee a single valid, self-contained HTML page. Documents with their own `<html>`, `<head>`, or `<body>` elements, relative asset paths, or conflicting styles may need additional processing.
- **Output files:** `share.py` and `share1.py` use the same configured output path by default. Change that path if you want to preserve separate outputs.
- **File paths:** The original scripts contain machine-specific paths. Update them before running on another computer.
- **Data safety:** Keep backups of original files before performing conversions or compression.

## 🧰 Future Improvements

Potential enhancements include:

- Accept input and output paths through command-line arguments.
- Add error handling for missing files and invalid input formats.
- Add configurable PDF resolution and image quality.
- Generate valid merged HTML documents with appropriate document structure.
- Add a `requirements.txt` file for easier dependency management.

## 📄 License

No license has been specified yet. Add a license file if you intend to define how others may use, modify, and distribute this project.
