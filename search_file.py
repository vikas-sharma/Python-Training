import os

for root_dir, sub_dir, files in os.walk(r'C:\Users\Admin\Desktop\Laxman'):
    # Read all files in direcoty and sub dir
    # print('-'*40)
    # print('Root Dir=',root_dir,'\n')
    # print('Sub directories:',sub_dir,'\n')
    # print('files:',files,'\n')

    # read only files ends with .py
    # for each_file in files:
    #     if each_file.endswith('.py'):
    #         fullpath=root_dir +'\\' + each_file
    #         print('File name=',each_file)
    #         print('Full Path to file:',fullpath)


    # search for single file named 'pack.py'
    for each_file in files:
        if each_file == 'pack.py':
            fullpath=root_dir +'\\' + each_file
            print('File found is: ',each_file)
            print('Full path to file is :',fullpath)
