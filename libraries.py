import os

libraries = ["pygame"]
for i in range(len(libraries)):
    os.system(f"pip install {libraries[i]}")

input("\nFinished installing libraries!\nPress Enter to terminate.")