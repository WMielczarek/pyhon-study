import glob
import os
pathToDir = '.\Data'
for filename in glob.glob(os.path.join(pathToDir, '*.csv')):
  (nazwa) = filename.split('\\')
  (roz, gowno) = nazwa[2].split('.')
  (name, date, hour) = roz.split('_')
  print(hour)

