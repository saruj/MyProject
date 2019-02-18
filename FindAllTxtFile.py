import glob

dir_name = """D:\DMS\LMS-Project\SCRIPT_BACKUP\*.sql"""

for f in glob.iglob(dir_name): # generator, search immediate subdirectories
    print (f)