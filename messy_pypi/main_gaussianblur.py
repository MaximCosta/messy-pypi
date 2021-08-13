from PIL import Image
import cv2

# A faire une fonction de sténographie

# PNG ←→ RGB
if True:
	def array_to_tuple(image_data: list[list]):
		return [[tuple([j[2], j[1], j[0]]) for j in i] for i in image_data]  # Because with cv2 the order is B, G, R, A


	def png_to_rgb(path):  # need cv2
		image = cv2.imread(path)  # cv2.IMREAD_UNCHANGED → ALPHA
		print(image.shape)
		return array_to_tuple(image), len(image), len(image[1])


	def rgb_to_png(rgb_array):
		new_image = Image.new('RGB', (len(rgb_array[0]), len(rgb_array)))  # type, size
		new_image.putdata([tuple(p) for row in rgb_array for p in row])
		new_image.show()  # save("filename.png")  # takes type from filename extension
# RGB → Hex
if True:
	def rgb_to_hex(r, g, b):  # https://www.codeunderscored.com/convert-rgb-to-hex-color-code/
		def decimal_to_hex(n):
			hex_decimal_number = ['0'] * 100
			i = 0
			while n != 0:
				_temp = 0
				_temp = n % 16
				if _temp < 10:
					hex_decimal_number[i] = chr(_temp + 48)
					i = i + 1
				else:
					hex_decimal_number[i] = chr(_temp + 55)
					i = i + 1
				n = int(n / 16)
			hex_code: str = ""
			if i == 2:
				hex_code = hex_code + hex_decimal_number[0]
				hex_code = hex_code + hex_decimal_number[1]
			elif i == 1:
				hex_code = "0"
				hex_code = hex_code + hex_decimal_number[0]
			elif i == 0:
				hex_code = "00"
			return hex_code

		if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
			hexadecimal_code = "#"
			hexadecimal_code = hexadecimal_code + decimal_to_hex(r)
			hexadecimal_code = hexadecimal_code + decimal_to_hex(g)
			hexadecimal_code = hexadecimal_code + decimal_to_hex(b)
			return hexadecimal_code

		# If the hexadecimal color code does not exist, return -1
		else:
			return "-1"
# Array ←→ Array of Array
if True:
	def a_to_aa(m: list, size_x: int, size_y: int) -> list:
		n = []
		for i in range(size_x):
			n += [m[size_y * i:size_y * (i + 1)]]
		return n


	def aa_to_a(m: list) -> list:
		n = []
		for i in m:
			n += i
		return n
# Show Image in terminal
if True:
	def plus_grand_de_3_valeur(a, b, c):
		if a + b + c == 0:
			return 4, "black 000"
		if a > b and a > c:
			return 0, a
		if b > a and b > c:
			return 1, b
		if c > a and c > b:
			return 2, c
		return 3, "Error"


	def show_image(image_data, image_x, image_y):
		if not (image_x * image_y - 1 <= len(image_data) <= image_x * image_y + 1):
			return "Not good size"
		for i in range(len(image_data)):
			i_data = image_data[i]
			if i % image_x == image_x - 1:
				print("")
			plus_grand = plus_grand_de_3_valeur(i_data[0], i_data[1], i_data[2])
			print(["\033[31mR", "\033[32mG", "\033[34mB", "?", " "][plus_grand[0]], end="\033[0m")
# Useless for now
if not True:  # Useless for now or for future
	def load30x30_rgb_file(path, in_one_tuple: bool = False) -> list:
		# return tuple de 30 tuple de 3 tuple
		# [[[1,1,1],[1,1,1], [1,1,1] *30], *30]
		m = []
		with open(path, "rb") as f:
			l: list[bytes] = f.readlines()

		for i in l:
			a = []
			for j in i:
				a += [j]
				if len(a) == 3:
					m = m + [tuple(a)]
					a = []
		if in_one_tuple:
			return m
		size_x = 30
		size_y = 30
		return a_to_aa(m, size_x, size_y)


	def turtle_show_image(image_data, image_x, image_y):
		import turtle
		size = 10
		if not (image_x * image_y - 1 <= len(image_data) <= image_x * image_y + 1):
			return "Not good size"
		wm = turtle.Turtle()
		wm.pensize(size)
		for i in range(len(image_data)):
			i_data = image_data[i]
			wm.pendown()
			wm.pencolor(rgb_to_hex(i_data[0], i_data[1], i_data[2]))
			if i % 30 == 0:
				wm.penup()
			wm.setpos((i % 30) * size, -(i // 30) * size)
			i_data = image_data[i]

			plus_grand = plus_grand_de_3_valeur(i_data[0], i_data[1], i_data[2])
			print(["\033[31mR", "\033[32mG", "\033[34mB", "?", " "][plus_grand[0]], end="\033[0m")

		input()


def gauss_function(size: int, hauteur, precision):
	# Generation du tuple formant la courbe gaussienne
	# Fonction de gauss utilisé
	#   -x²
	# ab
	# with a = hauteur maximale
	# Generate a list with size "size"
	if size % 2 == 0:
		size -= 1
	# This list ↓
	# Need to be size length
	# With minimum -1 and max 1 and same espacement between values
	x_values = [-1]
	add_value = 2 / (size - 1)
	for i in range(size - 1):
		x_values += [x_values[-1] + add_value]
	x_values = [round(i, 4) for i in x_values]
	# gauss = [precision * (((size/precision)+1) ** -(i ** 2)) for i in list(range(-size // 2 + 1, size // 2 + 1))]
	gauss_list = []
	for i in x_values:
		gauss_list += [round(hauteur * (precision ** -(i ** 2)), 3)]
	return gauss_list


# Main Function
def blur(image_data: list, size: int = 3):  # image need to be an array of array, of color
	precision = 10
	hauteur = 5
	# size need to be odd
	size = max(3, int(size))
	if size % 2 == 0:
		size -= 1
	gauss = gauss_function(size, precision, hauteur)
	print(gauss)
	entier_gauss = list(range(-size // 2 + 1, size // 2 + 1))
	new_image_data = image_data
	# for i in gauss:
	for x in range(len(image_data)):
		print(x)
		for y in range(len(image_data[x])):
			for i in range(len(entier_gauss)):
				for j in range(len(entier_gauss)):
					#if not (0 <= len(image_data[x]) + entier_gauss[i] < len(image_data[x]) + 2 and 0 <= len(
							#image_data[x][y]) + entier_gauss[i] < len(image_data) + 2):
						# if 0 <= image_data[x] + entier_gauss[j] < len(image_data) and 0 <= len(image_data[x][y]) + entier_gauss[j] < len(image_data):
						try:
							new_color = []
							for c in range(3):
								new_color += [int((new_image_data[x][y][c]+int(new_image_data[x+entier_gauss[c]][y+entier_gauss[j]][c])*gauss[i]*gauss[j])%256)]
							# [new_image_data[x][y][c]+int(new_image_data[x+entier_gauss[c]][y+entier_gauss[j]][c])*gauss[i]*gauss[j])%256]
							new_image_data[x][y] = new_color
							#print(f"changedata {x=}, {y=}")
						except IndexError:
							pass
							#print(f"IndexError at {x=} {y=} {i=}")
	# for color in y:
	# 	pass
	# image_data = [[[k//30 for k in j] for j in i]for i in image_data]
	return new_image_data


def main():
	data_image, size_x, size_y = png_to_rgb("/home/ay/0001.png")
	blur_data_image = blur(data_image)
	rgb_to_png(blur_data_image)


# print(data_image)


if __name__ == "__main__":
	debug = False
	main()

"""
rgb_to_png(print(a_to_aa(image_data, 30,30))
# print(blur(image_data, 30, 30, 1))
"""
