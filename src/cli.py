from loguru import logger
import typer
from pngs_to_pdf import pngs_to_pdf

app = typer.Typer(help="Merge PNG screenshots into a single PDF.")


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
