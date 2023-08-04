from PIL import Image
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
scale_factor = float(sys.argv[3])

def resize_image(input_file, output_file, scale_factor=0.5):
    with Image.open(input_file) as img:
        # 获取原始图片的尺寸
        original_width, original_height = img.size
        
        # 计算新的尺寸
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        # 缩放图片
        resized_img = img.resize((new_width, new_height))
        
        # 保存缩放后的图片
        resized_img.save(output_file)

# 使用上面定义的函数
resize_image(input_file, output_file,scale_factor)

