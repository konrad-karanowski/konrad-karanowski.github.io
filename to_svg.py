import cv2
import numpy as np
import svgwrite
import os
import sys

def convert_image_to_svg(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply edge detection
    edges = cv2.Canny(image, 100, 200)

    # Get contours from edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Prepare output SVG file path
    base_name = os.path.splitext(image_path)[0]  # Get the file name without extension
    output_path = f"{base_name}.svg"  # Create SVG file path

    # Create an SVG drawing
    dwg = svgwrite.Drawing(output_path, profile='tiny')

    for contour in contours:
        points = [(point[0][0], point[0][1]) for point in contour]
        dwg.add(dwg.polyline(points, stroke=svgwrite.rgb(0, 0, 0), fill='none'))

    # Save the SVG file
    dwg.save()

    print(f"SVG file saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_to_svg.py <image_file>")
        sys.exit(1)

    image_file = sys.argv[1]
    convert_image_to_svg(image_file)
