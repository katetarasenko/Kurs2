import os
prjpath = os.getcwd()
print(prjpath)
print('sdfds\nswgg')
print(r'sdfds\nswgg')

newdir = prjpath + r"/dir3"
norm = os.path.normpath(newdir)
print(newdir)
print(os.path.abspath(newdir))
if os.path.exists(newdir):
     print("Path already exist")
else:
     os.mkdir(newdir)
os.rename('player_data','player-info')






# #os.mkdir("d:\dir1")
# p = r"d:\dir1\dir2"
# os.mkdir(p)