import sys
import datetime
from rembg import remove
from PIL import Image

input_path = sys.argv[1]
output_path = f'{str(datetime.datetime.now().timestamp())}.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print(output_path)
print('Done')