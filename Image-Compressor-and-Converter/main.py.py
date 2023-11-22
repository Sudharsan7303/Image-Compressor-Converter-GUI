import os
import PySimpleGUI as sg
from PIL import Image
import os

def compress(image,output,qual,format):  
    try:
        if format=='jpg':
            format='JPEG'
            
            a=2
            if qual==75:
                q=96
            elif qual==50:
                q=92
            else:
                q=75
            
        elif format=='png':
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
        
        resized_image.save(output, format=format.upper(), optimize=True, quality=q)
        return True
    except :
        sg.popup_error(f"Error: An error has occured")
        return False





def main():
    sg.theme("Dark Grey 15")

    layout = [
        [sg.Text("Compress Your JPEG or PNG Images", font=("Helvetica", 20), justification="center")],
        [sg.Text("Select an image file:"), sg.Input(key="input_file"), sg.FileBrowse(file_types=(("Image files", "*.png;*.jpg;*.jpeg"),))],
        [sg.Text("Output folder:"), sg.Input(key="output_folder"), sg.FolderBrowse()],
        [sg.Text("Compression Quality :"), sg.Combo([f"75 % of original size",f"50 % of original size",f"25 % of original size"], default_value=f"75 % of original size",  key="quality")],
        [sg.Button("Compress",button_color=('white', 'blue'), change_submits=True), sg.Button("Exit",button_color=('white', 'blue'), change_submits=True)],
    ]

    window = sg.Window("Image  Compressor", layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Compress":
            try:
                input_file = values["input_file"]
                image=Image.open(input_file)

                output_folder = values["output_folder"]
                if values['quality']==f"75 % of original size":
                    quality=75
                elif values['quality']==f"50 % of original size":
                    quality=50
                else:
                    quality=25
                image_format = image.format
                if image_format=='JPEG':
                    image_format='jpg'
                else:
                    image_format='png'
            
                output_file = os.path.join(output_folder, f"compressed_img.{image_format.lower()}")

                if compress(image, output_file, quality, image_format):
                    sg.popup(f"Image compressed successfully. Saved to:\n{output_file}")
            except:
                
                sg.popup_error(f"Error: Make sure the files are Selected")

    window.close()

if __name__ == "__main__":
    main()