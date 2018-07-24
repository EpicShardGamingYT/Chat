from os import system
def exec(mass=None,one=None):
	if mass != None:
		for i in mass:
			system(i)
	else:
		system(one)

c = input("New install? (n/y)")
if c == "y":
	exec(mass=["mkdir Keys","GenKey.py"])
c = input("Do you have git? (n/y)")
if c == "n":
	exec(one="start https://github.com/git-for-windows/git/releases/download/v2.18.0.windows.1/Git-2.18.0-64-bit.exe")
print("Done!")
input("Press enter to exit...")