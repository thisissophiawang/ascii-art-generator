
# ASCII Art Generator

This project converts images into ASCII art using OpenCV and Gradio for the user interface. The application supports grayscale conversion, contrast enhancement, and optional edge detection for more detailed output. It is built using Python and deployed on Hugging Face Spaces.

## Features

- Upload an image to convert it to ASCII art.
- Optional edge detection for highlighting details.
- Adjustable contrast for better clarity in ASCII art.
- Real-time image-to-ASCII conversion using a Gradio interface.

## Requirements

Before running the project, ensure you have the following Python packages installed:

```bash
gradio==4.44.0
opencv-python==4.10.0.84
numpy==1.26.4
pydub==0.25.1

## Usage

Upload an image file.
Choose whether to enable edge detection for better detail.
Click "Convert to ASCII" to generate the ASCII art.
Download the result as a .txt file if desired.

