import os, random

source = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/'
destination = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/'
counter = 1
for filename in os.listdir(source):
    print(filename)
    src = source + filename
    dst = destination + 'testblank' + str(counter) + '.pdf'
    os.rename(src,dst)
    counter += 1
print(counter)
    
# for filename in os.listdir(src):
#     print(filename)


# print(os.listdir(src))
