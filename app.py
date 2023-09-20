from PIL import Image
import os

input_dir = r'C:\imageconverter\images\jpg'
output_dir = r'C:\imageconverter\images\tif' 

for filename in os.listdir(input_dir):
    if filename.endswith('.jpeg'):
         input_path = os.path.join(input_dir, filename)
         output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.tif')
         
         img = Image.open(input_path)  
         img.save(output_path)
         
print('Conversion done!')
