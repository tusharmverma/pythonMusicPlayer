import os
def main():
	try:
		try:
			import Tkinter
		except:
			import tkinter
		import pyglet
		os.system("cd Tools && python Gui.py")
	except Exception as e:
		print(e)
		input("")
if __name__=='__main__':
	main()
