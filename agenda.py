# agenda
from time import gmtime, strftime

# lista de tareas
class agenda:
	def __init__(self, user):
		self.name = user
		self.take = {}

	def listar(self):
		print("listar.\n")
		for i in self.take :
			print(
			f"title:\t {i}",
			f"\ndetail:  {self.take[i][0]}",
			f"\ndate:\t {self.take[i][1]}")
			print()

	def add(self, title, detail=str):
		"""
		add new note list the take
		"""
		t = strftime("%a, %d %b %Y %H:%M", gmtime())
		self.take[title] = detail, t
		print(f"nueva tarea: \n{title}", t)


	def delete(self, id):
		if id in self.take:
			del(self.take[id])

		
	def modifile(self, id, content=str,title=None ):
		try:
			if title is None:
				self.take[id] = content 
			else:
				self.delete(title)
				self.take[title] = content 


		except KeyError as e:
			print("tarea no exite")




if __name__ == '__main__':
	a = agenda("")
	a.listar()
	a.add("prueba", 1)
	a.add("qq", 1)
	
	a.listar()
	a.delete("prueba")
	a.modifile("qq", )

	a.listar()



		