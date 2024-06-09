import os

directory = ""

albedo = ['albedo','basecolor']
#for each file in the directory check if it has the word albedo in it
for filename in os.listdir(directory):
    for word in albedo:
        if word in filename:
            print(f'{filename} :: ALBEDO')