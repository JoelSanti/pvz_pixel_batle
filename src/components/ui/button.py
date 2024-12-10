class Button():
	"""
	Clase para crear un botón interactivo en la interfaz de usuario.

	Atributos:
		image (Surface): Imagen del botón.
		x_pos (int): Posición X del botón.
		y_pos (int): Posición Y del botón.
		font (Font): Fuente del texto del botón.
		base_color (tuple): Color base del texto.
		hovering_color (tuple): Color del texto al pasar el ratón por encima.
		text_input (str): Texto del botón.
		text (Surface): Superficie del texto renderizado.
		rect (Rect): Rectángulo que contiene la imagen del botón.
		text_rect (Rect): Rectángulo que contiene el texto del botón.
	"""

	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		"""
		Inicializa un nuevo botón.

		Parámetros:
			image (Surface): Imagen del botón.
			pos (tuple): Posición (x, y) del botón.
			text_input (str): Texto del botón.
			font (Font): Fuente del texto del botón.
			base_color (tuple): Color base del texto.
			hovering_color (tuple): Color del texto al pasar el ratón por encima.
		"""
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		"""
		Dibuja el botón en la pantalla.

		Parámetros:
			screen (Surface): Superficie en la que se dibuja el botón.
		"""
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		"""
		Verifica si una posición está dentro del área del botón.

		Parámetros:
			position (tuple): Posición (x, y) a verificar.

		Retorna:
			bool: True si la posición está dentro del botón, False en caso contrario.
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		"""
		Cambia el color del texto del botón dependiendo de la posición del ratón.

		Parámetros:
			position (tuple): Posición (x, y) del ratón.
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)