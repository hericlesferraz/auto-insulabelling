import os

count_mark = 0
count_rgb = 0

paths_imgs = "../512x/"

for name_img in os.listdir(paths_imgs):
    print(name_img)
    if name_img.endswith(".png"):

        if name_img.find("_mask_") != -1:
            os.system("mv " + paths_imgs + str(name_img) + " " + paths_imgs + "mask/")
            count_mark += 1

        else:
            os.system("mv " + paths_imgs + str(name_img) + " " + paths_imgs + "images/")
            count_rgb += 1
