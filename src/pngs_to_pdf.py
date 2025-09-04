from PIL import Image
import os
from loguru import logger
import typer

app = typer.Typer(help="Merge PNG screenshots into a single PDF.")


def pngs_to_pdf(input_folder: str, output_path: str, output_filename_pdf: str):
    """
    Merge all PNG images from a given folder into a single PDF file.

    The PNG files are collected from the input folder, sorted
    alphabetically by filename, and combined into a single PDF.
    The resulting PDF is saved in the specified output path with
    the given filename.

    Args:
        input_folder (str): Path to the folder containing PNG files.
        output_path (str): Path to the folder where the PDF will be saved.
        output_filename_pdf (str): Name of the output PDF file (e.g., "screenshots.pdf").
    """
    logger.info(f"Collecting PNG files from: {input_folder}")
    os.makedirs(output_path, exist_ok=True)
    logger.debug(f"Ensured output directory exists: {output_path}")

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".png")]
    files.sort()

    if not files:
        logger.warning("No PNG files found in the folder.")
        return

    logger.info(f"Found {len(files)} PNG files to merge.")

    images = []
    for file in files:
        img_path = os.path.join(input_folder, file)
        logger.debug(f"Opening image: {img_path}")
        img = Image.open(img_path).convert("RGB")
        images.append(img)

    first_image, *other_images = images

    output_pdf = os.path.join(output_path, output_filename_pdf)
    first_image.save(output_pdf, save_all=True, append_images=other_images)
    logger.success(f"PDF created successfully: {output_pdf}")


@app.command()
def main(
    input: str = typer.Option(..., help="Path to the folder containing PNG files."),
    output: str = typer.Option(
        ..., help="Path to the folder where the PDF will be saved."
    ),
    name: str = typer.Option(
        "screenshots_default_name.pdf",
        help="Output PDF filename (default: screenshots_default_name.pdf).",
    ),
):
    """
    _summary_

    Args:
    input (str, optional): _description_. Defaults to typer.Option(..., help="Path to the folder containing PNG files.").
    output (str, optional): _description_. Defaults to typer.Option(..., help="Path to the folder where the PDF will be saved.").
    name (_type_, optional): _description_. Defaults to typer.Option("screenshots_default_name.pdf", help="Output PDF filename (default: screenshots_default_name.pdf).").
    """
    logger.info("Starting PNG to PDF conversion...")
    pngs_to_pdf(input, output, name)
    logger.info("Process finished.")


if __name__ == "__main__":
    app()
