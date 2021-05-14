from time import sleep


class corronometro():
	def __init__(self,seg=int, mini=None,hour=None):
		self.seg  = seg
		self.min  = mini
		self.hour = hour

	def seg(self):
		pass


def seg(seg=int):
	stad = seg
	__seg  = 0

	for i in range(seg):

		sleep(0.8)

		if __seg == 60:
			print ("are you raedy?")
			break

		elif __seg <= 60:
			__seg += 1
			print(i, end=" ")

seg(70)