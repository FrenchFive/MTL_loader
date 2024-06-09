import os

directory = ""

albedo = ['albedo','basecolor']
list_albedo = []

# for each file in the directory and subdirectory check if it has the word albedo in it
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        for word in albedo:
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: ALBEDO')
                list_albedo.append(os.path.join(dirpath, filename))

print('----')
print(list_albedo)