from PIL import Image, ImageSequence
import json

def crop_trans(img):
    alpha = img.getchannel('A')
    bbox = alpha.getbbox()
    if bbox: return img.crop(bbox)
    return img

def gen_fireballs(gif_name, output_dir):
    with Image.open(gif_name) as img, open('infomation.txt', 'w') as info:
        fireballs = []
        for idx, frame in enumerate(ImageSequence.Iterator(img)):
            frame = frame.transpose(method=Image.FLIP_TOP_BOTTOM)
            bmp = frame.convert("RGBA")
            cropped_bmp = crop_trans(bmp)
            output = f"{output_dir}/fireball{idx}.bmp"
            fireballs.append(output)
            cropped_bmp.save(output, 'BMP')
        info.write(json.dumps({'fireballs':fireballs}))

gen_fireballs('images/fireball.gif', './images')
