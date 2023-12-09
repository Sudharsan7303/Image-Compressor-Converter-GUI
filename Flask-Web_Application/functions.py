from PIL import Image
import os

def Convert(image):
    image=Image.open(image)
    image_format = image.format
    rgb_im=image.convert('RGB')


    if image_format=='JPEG':
        image_format='png'
    else:
        image_format='jpeg'
    
    rgb_im.save('tmp/'+f'converted_image.{image_format}',format=image_format.upper())
    path=f'tmp/converted_image.{image_format}'
    return path
    

def Compress(image,qual):
    qual=int(qual)

    image=Image.open(image)
    format = image.format
    if format=='JPEG':
        format='JPEG'
        
        a=2
        if qual==75:
            q=96
        elif qual==50:
            q=92
        else:
            q=75
        
    elif format=='PNG':
        format='PNG'
        q=85
        if qual==75:
            a=2.5
        elif qual==50:
            a=3
        else:
            a=5

    width, height = image.size
    new_size = round(width/a), round(height/a)
    resized_image = image.resize(new_size)
    
    resized_image.save('tmp/'+f'compressed_image.{format.lower()}',format=format.upper(), optimize=True, quality=q)
    path=f'tmp/compressed_image.{format.lower()}'
    return path