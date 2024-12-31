import os
from PIL import Image, ImageDraw, ExifTags
import pillow_heif  # 支持 .heic 格式
import random

def correct_orientation(image):
    """
    Correct the orientation of an image using its EXIF data.

    Args:
        image (PIL.Image.Image): The image to correct.

    Returns:
        PIL.Image.Image: The corrected image.
    """
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            orientation = exif.get(orientation)
            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # No EXIF data, or EXIF data doesn't contain orientation info
        pass
    return image

def create_collage(output_path, photo_paths, image_size=(2000, 2000), pattern_matrix=None):
    """
    Create a photo collage with a specified pattern matrix.

    Args:
        output_path (str): Path to save the output image.
        photo_paths (list): List of paths to the photos to include in the collage.
        image_size (tuple): Size (width, height) of the output image.
        pattern_matrix (list): A 2D list specifying the photo arrangement pattern.
    """
    # Ensure no duplicate photos are used
    if len(photo_paths) < sum(sum(row) for row in pattern_matrix):
        raise ValueError("Not enough unique photos to fill the collage")

    # Create blank canvas
    collage = Image.new('RGB', image_size, 'white')

    # Determine grid size from the pattern matrix
    rows = len(pattern_matrix)
    cols = len(pattern_matrix[0]) if rows > 0 else 0

    cell_size = min(image_size[0] // cols, image_size[1] // rows)

    # Shuffle photos to randomize placement
    photo_pool = photo_paths.copy()
    random.shuffle(photo_pool)

    photo_index = 0

    # Loop through the pattern matrix and fill the cells
    for row in range(rows):
        for col in range(cols):
            if pattern_matrix[row][col] == 1:
                photo_path = photo_pool[photo_index]
                if photo_path.lower().endswith(".heic"):
                    heif_file = pillow_heif.read_heif(photo_path)
                    photo = Image.frombytes(
                        heif_file.mode, heif_file.size, heif_file.data
                    )
                else:
                    photo = Image.open(photo_path)

                # Correct the orientation using EXIF data
                photo = correct_orientation(photo)

                # Crop the image to make it square
                side_length = min(photo.width, photo.height)
                left = (photo.width - side_length) // 2
                top = (photo.height - side_length) // 2
                photo = photo.crop((left, top, left + side_length, top + side_length))

                # Resize to cell size
                photo = photo.resize((cell_size, cell_size), Image.Resampling.LANCZOS)
                collage.paste(photo, (col * cell_size, row * cell_size))
                photo_index += 1

    # Save the final collage
    collage.save(output_path, quality=95)

# Example usage
photo_directory = "./Yourphotos_Path"  # 修改为当前文件夹下的子文件夹路径
output_file = "2024_collage.jpg"

# 获取所有图片文件的路径
photos = [
    os.path.join(photo_directory, file)
    for file in os.listdir(photo_directory)
    if file.lower().endswith((".heic", ".jpeg", ".jpg", ".png"))
]

# 使用指定的 17x9 模式矩阵
pattern = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
create_collage(output_file, photos, image_size=(3400, 1800), pattern_matrix=pattern)

print(f"Collage saved to {output_file}")
