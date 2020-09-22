import os 

with open('step3.txt', 'r') as f:
    data = f.readlines()
    for x in data:
      print("Read Line: %s" % (x))
      f.seek(f+1, os.SEEK_CUR)
      pos = f.tell()
      print("Current Position: %d" % (pos))
