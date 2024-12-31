# Photo Collage Generator for "2024" Pattern

## Description
This Python script generates a high-resolution photo collage in a user-defined pattern, such as the "2024" shape. It ensures proper orientation, cropping, and resizing of images while preventing duplicates in the collage.

## Features
- **Customizable Grid:** Define your own pattern matrix for the collage.
- **High Resolution:** Supports adjustable output sizes.
- **EXIF Orientation Support:** Corrects photo orientation.
- **Unique Photos:** Ensures no duplicate photos in the output.
- **Flexible Input Formats:** Supports `.heic`, `.jpeg`, `.jpg`, and `.png` formats.

## Requirements
- Python 3.x
- Pillow (`pip install pillow`)
- Pillow-Heif (`pip install pillow-heif`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/photo-collage-generator.git
   cd photo-collage-generator
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your photos in a folder (e.g., `2024car`).
2. Define the pattern matrix for the collage. For example:
   ```python
   pattern = [
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
       [1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
       [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
       [1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
       [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
   ]
   ```
3. Adjust the output resolution by modifying the `image_size` parameter.
4. Run the script:
   ```bash
   python photo_collage_generator.py
   ```

## Example
The following example creates a collage for the year "2024":
```python
photo_directory = "./2024car"
output_file = "2024_collage.jpg"
image_size = (3400, 1800)  # High-resolution output
pattern = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
create_collage(output_file, photos, image_size=image_size, pattern_matrix=pattern)
```

## Output
The output will be a high-resolution image (`2024_collage.jpg`) containing the photos arranged in the specified "2024" pattern.

## License
This project is licensed under the MIT License.

