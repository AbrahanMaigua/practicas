
"""
que es un decorador?

un decorador sirve para esteder la funcion
"""
# a(b) > c
def pais(func):
	def estado():
		func()
		print()

	return estado

