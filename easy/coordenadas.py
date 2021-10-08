class Coordenadas:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def diferencia(self, otro_objeto):
		x_diff = (self.x - otro_objeto.x)
		y_diff = (self.y - otro_objeto.y)
		return x_diff * y_diff
	

objeto1 = Coordenadas(23, 34)
objeto2 = Coordenadas(21, 98)
print(objeto1.diferencia(objeto2))