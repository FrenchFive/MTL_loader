import os

directory = ""

albedo = ['albedo','basecolor']
metal = ['metalness', 'metallic']
rough = ['roughness']
normal = ['normal']
height = ['height']

list_albedo = []
list_metal = []
list_rough = []
list_normal = []
list_height = []


# for each file in the directory and subdirectory check if it has the word albedo in it
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        for word in albedo:
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: ALBEDO')
                list_albedo.append(os.path.join(dirpath, filename))
        for word in metal:  
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: METAL')
                list_metal.append(os.path.join(dirpath, filename))
        for word in rough:
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: ROUGH')
                list_rough.append(os.path.join(dirpath, filename))
        for word in normal:
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: NORMAL')
                list_normal.append(os.path.join(dirpath, filename))
        for word in height:
            if word in filename:
                print(f'{os.path.join(dirpath, filename)} :: HEIGHT')
                list_height.append(os.path.join(dirpath, filename))
    
#for each element in the list albedo, check if the others elements have the same name following the pattern [name]_[number].[extension]
if len(list_albedo) > 0:
    for i in list_albedo:
        index = list_albedo.index(i)
        actual_fn = list_albedo[index].split('/')[-1].split(".")[0]
        next_fn = list_albedo[index+1].split('/')[-1].split(".")[0]
        if actual_fn == next_fn:
            #delete next_fn from the list
            list_albedo.pop(i+1)

print('----')