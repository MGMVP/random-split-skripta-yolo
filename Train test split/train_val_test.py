import glob
import random
import os
filelist  = glob.glob('obj/*.txt')
test = random.sample(filelist, int(len(filelist)*0.2))
output_path = 'test/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

for file in test:
    txtpath = file
    impath = file[:-4] + '.jpg'
    out_text = os.path.join(output_path, os.path.basename(txtpath))
    out_image = os.path.join(output_path, os.path.basename(impath))
    print(txtpath,impath,out_text,out_image)
    os.system('powershell mv ' + txtpath + ' ' + out_text)
    os.system('powershell mv ' + impath + ' ' + out_image)