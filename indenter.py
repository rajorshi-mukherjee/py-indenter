__doc__ = ''' This module is used to perform indentation with four spaces.
We created this module to ease the burden of indentation in a small enterprise system 
where indenting will have to be done manually.
We want to ease the burden of doing manual labour. 
             Meh!

             Automation Ka Zamana Hai Bhai..!
'''
def indentation():
    indent_depth = 0
    src_file_name = raw_input('Please Enter your source file name : ')
    tar_file_name = raw_input('Please Enter your target file name : ')

    src_file = open(src_file_name, 'r')
    tar_file = open(tar_file_name, 'w')

    data = src_file.readlines()

    for items in data :

        items = items.strip()

        if len(items) > 0 :

            if items[0] == '#' :
                if items[1] == '{' :
                    spaces = ' '*4*indent_depth
                    items = spaces + items
                    tar_file.writelines(items + '\n')
                    indent_depth +=1
                    continue

                if items[1] == '}' :
                    indent_depth -=1
                    spaces = ' '*4*indent_depth
                    items = spaces + items
                    tar_file.writelines(items + '\n')
                    continue

        spaces = ' '*4*indent_depth
        items = spaces + items
        tar_file.writelines(items + '\n')

    src_file.close()
    tar_file.close()


indentation()
