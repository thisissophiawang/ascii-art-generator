import cv2
import gradio as gr
import numpy as np

# Using more ASCII characters to represent grayscale levels from darkest to lightest
ascii_chars = ['M', 'N', 'B', 'F', '@', '#', 'S', '&', '%', '$', '*', '!', ';', ':', ',', '.', ' ']

# Map the pixel intensity to corresponding ASCII characters
def pixel_to_ascii(pixel_value):
    return ascii_chars[int(pixel_value / 256 * len(ascii_chars))]

# Resize the image and maintain aspect ratio with width scaling
def resize_image(image, max_width=150, max_height=60):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    height, width = image.shape[:2]
    
    # Apply a width scaling factor to better match ASCII characters' aspect ratio
    aspect_ratio = width / height
    width_scale_factor = 2  # Scaling factor to account for character aspect ratio
    
    # Adjust width by scaling factor
    new_width = int(min(max_width, width) * width_scale_factor)
    new_height = min(max_height, height)
    
    # Calculate new dimensions while maintaining aspect ratio
    if aspect_ratio > 1:  # Wider images
        new_width = min(new_width, max_width)
        new_height = int(new_width / (aspect_ratio * width_scale_factor))
    else:  # Taller images
        new_height = min(new_height, max_height)
        new_width = int(new_height * aspect_ratio * width_scale_factor)
    
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Convert the image to grayscale
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Enhance the contrast of the grayscale image
def apply_contrast_enhancement(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

# Optional: Apply edge detection if selected
def apply_edge_detection(image):
    edges = cv2.Canny(image, 100, 200)
    return edges

# Generate ASCII art while maintaining aspect ratio and adding optional edge detection
def generate_ascii_art(image, max_width=150, max_height=60, edge_detection=False):
    # Apply edge detection if enabled
    if edge_detection:
        image = apply_edge_detection(image)
    
    height, width = image.shape[:2]
    ascii_art = []
    
    # Convert each pixel to an ASCII character
    for y in range(height):
        line = ''
        for x in range(width):
            line += pixel_to_ascii(image[y, x])
        ascii_art.append(line)
    
    # Add horizontal padding to center the ASCII art
    max_line_length = max(len(line) for line in ascii_art)
    ascii_art = [line.center(max_width) for line in ascii_art]
    
    # Add vertical padding to center the ASCII art
    vertical_padding = max(0, max_height - len(ascii_art))
    top_padding = vertical_padding // 2
    bottom_padding = vertical_padding - top_padding
    
    ascii_art = ([' ' * max_width] * top_padding) + ascii_art + ([' ' * max_width] * bottom_padding)
    
    return '\n'.join(ascii_art)

# Main function to generate ASCII art
def image_to_ascii(image, edge_detection=False):
    resized_image = resize_image(image)
    grayscale_image = convert_to_grayscale(resized_image)
    enhanced_image = apply_contrast_enhancement(grayscale_image)
    ascii_art = generate_ascii_art(enhanced_image, edge_detection=edge_detection)
    
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)
    
    return ascii_art, "ascii_art.txt"

# Gradio UI
def ascii_art_interface(image, edge_detection):
    ascii_output, text_file = image_to_ascii(image, edge_detection=edge_detection)
    return ascii_output, text_file

# Custom CSS for styling
custom_css = """
    .ascii-art-output {
        font-family: monospace;
        font-size: 7px;
        line-height: 1;  /* Adjust line height */
        white-space: pre;
        overflow: hidden;
        padding: 10px;
        border: 1px solid #ccc;
        background-color: #f8f8f8;
    }
    .container {
        max-width: 100% !important;
        padding: 0 !important;
    }
"""

# Build Gradio interface
demo = gr.Blocks(css=custom_css)

with demo:
    gr.Markdown("# Image to ASCII Art Converter")
    gr.Markdown("Upload an image and convert it into ASCII art. You can also download the result as a .txt file.")
    
    with gr.Row():
        input_image = gr.Image(label="Upload Image", type="pil")
    
    with gr.Row():
        edge_detection_checkbox = gr.Checkbox(label="Enable Edge Detection", value=False)
    
    with gr.Row():
        submit_btn = gr.Button("Convert to ASCII")
    
    # Increase ASCII output box size
    with gr.Row():
        ascii_output = gr.Textbox(label="ASCII Art", lines=60, max_lines=60, elem_classes=["ascii-art-output"])
    
    with gr.Row():
        file_output = gr.File(label="Download ASCII Art File")
    
    submit_btn.click(
        fn=ascii_art_interface,
        inputs=[input_image, edge_detection_checkbox],
        outputs=[ascii_output, file_output]
    )

if __name__ == "__main__":
    demo.launch(share=True)
