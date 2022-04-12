from PIL import Image

img = Image.open("sqd.jpg")
out = img.convert("L")
# out.show()
print(out.size)

width, height = out.size
out = out.resize((width // 8, height // 8))
width, height = out.size
print(out.size)

print(out.getpixel((0, 0)))     # getpixel函数 可以选取某一个坐标位置的pixel， 需注意，坐标位置需要是元祖

ascii = "$@%#&*+=/!;-,. "
texts = ""

for row in range(height):
    for col in range(width):
        gray = out.getpixel((col, row))
        texts += ascii[int(gray / 255 * len(ascii))]
    texts += '\n'

with open('./ascii.txt', "w") as file:
    file.write(texts)