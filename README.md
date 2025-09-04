# screenshots-to-pdf

A simple Python CLI tool to merge PNG screenshots into a single high-quality PDF file.  
The images are automatically sorted by filename to preserve the correct order.

## Features
- Merge all `.png` images from a folder into a single PDF.
- Sorts images alphabetically by filename.
- Default PDF name if not specified: `screenshots_default_name.pdf`.
- Lightweight and easy to use with a CLI interface powered by **Typer**.
- Logs progress and status using **Loguru**.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the terminal:
```bash
python src/pngs_to_pdf.py --input <input_folder> --output <output_folder> [--name <output_pdf_name>]
```

### Parameters
- --input : Path to the folder containing PNG files (required).
- --output : Path to the folder where the PDF will be saved (required).
- --name : Name of the output PDF (optional, default: screenshots_default_name.pdf).

### Examples
1. Using default PDF name:
```bash
python src/pngs_to_pdf.py \
    --input ./input_folder \
    --output ./output_folder
```
```

2. Using a custom PDF name:
```bash
python src/pngs_to_pdf.py \
    --input ./input_folder \
    --output ./output_folder \
    --name combined_screenshots.pdf
```
