
# ASCII Art Generator

This project converts images into ASCII art using OpenCV and Gradio for the user interface. The application supports grayscale conversion, contrast enhancement, and optional edge detection for more detailed output. It is built using Python and deployed on Hugging Face Spaces.

## Features

- Upload an image to convert it to ASCII art.
- Optional edge detection for highlighting details.
- Adjustable contrast for better clarity in ASCII art.
- Real-time image-to-ASCII conversion using a Gradio interface.

## Usage

Upload an image file.
Choose whether to enable edge detection for better detail.
Click "Convert to ASCII" to generate the ASCII art.
Download the result as a .txt file if desired.

## Steps for Processing ASCII Art

1. **Image Conversion and Grayscale:**
   - The process begins by resizing the input image and converting it to grayscale using OpenCV’s `cv2.cvtColor`. 
   - This reduces the image to different shades of gray, simplifying it for ASCII art generation. 
   - A width scaling factor is applied to adjust for the aspect ratio difference between images and ASCII characters, ensuring that the final ASCII output fits properly within the Gradio interface.

2. **Contrast Enhancement:**
   - After the grayscale conversion, Contrast Limited Adaptive Histogram Equalization (CLAHE) is applied to improve the local contrast of the image.
   - This enhancement ensures that important features stand out, which helps in creating clearer ASCII art. 
   - The clip limit is set to 2.0 to prevent over-amplification of noise in the image.

3. **ASCII Character Mapping:**
   - The pixel intensities of the grayscale image are mapped to a predefined set of ASCII characters:
     ```python
     ascii_chars = ['M', 'N', 'B', 'F', '@', '#', 'S', '&', '%', '$', '*', '!', ';', ':', ',', '.', ' ']
     ```
   - Each character represents a different intensity level, with darker characters for high-intensity pixels and lighter characters for low-intensity pixels.
   - The pixel intensity is scaled to match the number of available ASCII characters.

4. **Edge Detection (Optional):**
   - You can choose to apply edge detection using the Canny Edge Detection algorithm (`cv2.Canny`). 
   - This option emphasizes the outlines and edges of objects in the image, helping to produce more detailed and defined ASCII art.

5. **Generating ASCII Art:**
   - The image is processed row by row, mapping each pixel’s intensity to an ASCII character. 
   - The generated ASCII characters are then arranged into rows, forming the final output image.
   - The final result can be downloaded as a `.txt` file or viewed directly within the Gradio interface.

## Performance Metric:

1. **SSIM (Structural Similarity Index):**
   - This metric calculates the structural similarity between the original image and the generated ASCII art, producing a score between -1 and 1.
   - Higher SSIM scores indicate greater similarity between the images, with the metric considering luminance, contrast, and structure.

2. **Visual Evaluation:**
   - The quality of the ASCII art is also assessed visually, where factors like clarity, balance, and readability are considered.
   - A score from 1 to 10 can be assigned based on how well the image retains its recognizability and aesthetics in ASCII form.
  
## Requirements

Before running the project, ensure you have the following Python packages installed:

bash
gradio==4.44.0
opencv-python==4.10.0.84
numpy==1.26.4
pydub==0.25.1
