import os
from PIL import Image

def convert_jfif_to_jpg(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.jfif'):
            img_path = os.path.join(source_folder, filename)
            img = Image.open(img_path)
            new_path = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.jpg')
            img.save(new_path)
            print(f"Converted {img_path} to {new_path}")

source_folder = 'D:\download'  #jfif文件所在路径
destination_folder = 'D:\download' #jpg文件所在路径
convert_jfif_to_jpg(source_folder, destination_folder)
#确保安装了 Pillow 库（pip install Pillow）