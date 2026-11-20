import fitz

svg_test = '<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg"><rect width="200" height="100" fill="white"/><circle cx="100" cy="50" r="40" fill="red"/></svg>'

doc = fitz.open(stream=svg_test.encode('utf-8'), filetype='svg')
pix = doc[0].get_pixmap()
print('Pixmap rendered:', pix.width, pix.height)

