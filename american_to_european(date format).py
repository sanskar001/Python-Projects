import re,os,shutil

file_path=input("Enter the file path:")

# this is function which convert the filename with american style date format (mm-dd-yyyy) to european style date format(dd-mm-yyyy)
def american_to_european(file_name):
    #  for finding month
    month_regex=re.compile(r".+\((\d+)-\d+-\d+\)\.[a-zA-Z]+")
    month_list=month_regex.findall(file_name)
    
    #  for finding date
    date_regex=re.compile(r".+\(\d+-(\d+)-\d+\)\.[a-zA-Z]+")
    date_list=date_regex.findall(file_name)
    
    #  for finding year
    year_regex=re.compile(r".+\(\d+-\d+-(\d+)\)\.[a-zA-Z]+")
    year_list=year_regex.findall(file_name)
    
    #  for finding the rest of filename
    rest_filename_regex=re.compile(r"(.+)\(\d+-\d+-\d+\)\.[a-zA-Z]+")
    rest_filename_list=rest_filename_regex.findall(file_name)
    
    #  for finding the type of extension file have
    extension_regex=re.compile(r".+(\.[a-zA-Z]+)")
    extension_list=extension_regex.findall(file_name)
    
    newfile_name=rest_filename_list[0]+"("+date_list[0]+"-"+month_list[0]+"-"+year_list[0]+")"+extension_list[0]
    return newfile_name
    
american_date_filelist=os.listdir(file_path)
print("american style filename:")
print("\n")
for x in american_date_filelist:
    print(x)

for american_file_name in american_date_filelist:
    european_file_name=american_to_european(american_file_name)
    previous_file_path=file_path+"\\"+american_file_name
    new_file_path=file_path+"\\"+european_file_name
    shutil.move(previous_file_path,new_file_path)

european_date_filelist=os.listdir(file_path)
print("\n")
print("European style filename:")
print("\n")
for x in european_date_filelist:
    print(x)
