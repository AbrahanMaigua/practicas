from time import gmtime, strftime
from json import dumps, loads

class linetime:
	def __init__(self):
		self.line = {}
		self.date = strftime("%a, %d %b %Y %H:%M", gmtime())

	def add(self, title, detail=str):
		"""
		add new event the line time
		"""
		self.line[title] = detail, self.date

		return self.line[title]


	def modifile(self, title, content=str, delete=False):
		"""
		title=is title the event 
		content=str is opcional 
		1.verifica si exite la line a modificar
		2.vuelve a crear la line por ser una tupla

		"""
		if delete is not False:
			del(self.line[title]) 
			return f"del {title}"
		else:
			if title in self.line:
				add = self.add(title, content) 

				return add

	def jsonfile(self):
		j = dumps(self.line, ensure_ascii=True,indent=4)
		return j

		
a = linetime()
print(a.add("work", ""))
print(a.add("studt", "not "))

print(a.modifile("work", "holis"))
print(a.modifile("work", delete=True))

print(a.jsonfile())



