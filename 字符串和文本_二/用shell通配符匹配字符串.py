from fnmatch import fnmatch, fnmatchcase

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
n = [name for name in names if fnmatchcase(name, 'Dat*.csv')]
print(n) # output ['Dat1.csv', 'Dat2.csv']