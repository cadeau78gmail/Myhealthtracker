from PIL import Image
import os
src = os.path.join('public', 'images', 'pills.jpg')
dst = os.path.join('public', 'images', 'pills-transparent.png')
img = Image.open(src).convert('RGBA')
pixels = img.load()
w, h = img.size
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if r > 240 and g > 240 and b > 240:
            pixels[x, y] = (255, 255, 255, 0)
img.save(dst)
print('saved', dst)
