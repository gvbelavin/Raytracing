import sys
from PIL import Image
import time

def print_progress_bar(iteration, total, length=40):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '*' * filled_length + '-' * (length - filled_length)
    print(f'\r|{bar}| {percent:.2f}% Completed', end='')

def convert_ppm_to_png(input_file, output_file):
    try:
        print(f'Opening {input_file}...')
        
        with open(input_file, 'r') as f:
            header = f.readline()  
            dimensions = f.readline()  
            max_color_value = int(f.readline())  

            if max_color_value > 255:
                raise ValueError("Max color value must be <= 255")

            pixels = []
            for line in f:
                pixels.extend(map(int, line.split()))

            new_pixels = []
            for i in range(0, len(pixels), 3):
                r = min(pixels[i], 255)
                g = min(pixels[i+1], 255)
                b = min(pixels[i+2], 255)
                new_pixels.extend([r, g, b])
                
        img = Image.new('RGB', (int(dimensions.split()[0]), int(dimensions.split()[1])), "black")
        img.putdata([(new_pixels[i], new_pixels[i+1], new_pixels[i+2]) for i in range(0, len(new_pixels), 3)])

        print(f'Starting conversion...')
        total_steps = 100
        for i in range(total_steps):
            time.sleep(0.03)  
            print_progress_bar(i + 1, total_steps)

        img.save(output_file, "PNG")
        print(f'\nConverted {input_file} to {output_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input.ppm> <output.png>")
    else:
        input_ppm = sys.argv[1]
        output_png = sys.argv[2]
        convert_ppm_to_png(input_ppm, output_png)