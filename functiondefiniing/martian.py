import sys, requests,json,os,urllib,ezgmail
from PIL import Image
import shutil
import urllib


api_key = 'qWngT2sHFzb7K2WW9Kwzor1xs7w10rkDu6LDXfNX'

# rover=input('Enter the rover name ').lower()
# camera=input("Enter the camera ").lower()
earth_date='2021-1-1'
rover='curiosity'
camera='fzah'
# sol='1000'

res=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=qWngT2sHFzb7K2WW9Kwzor1xs7w10rkDu6LDXfNX')

res.raise_for_status()

os.makedirs('rover_images',exist_ok=True)
# print(res.text)

rover_data=json.loads(res.text)

images=rover_data['photos']

sources=[]
for i in images:
    for j in i:
        if j=='img_src':
            sources.append(i[j])

print(sources)
n=0



for x in sources:
    img=Image.open(requests.get(x,stream=True).raw)
    os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
    img.save(f'attachments{n}.jpg')
    n+=1




attachments=os.listdir(r'/home/programmer/The-Martian-Chronicles/rover_images')

print(attachments)
# for i in range(len(attachments)):
#     attachments[i]=str(r'/home/programmer/The-Martian-Chronicles/rover_images/'+attachments[i])
# print(attachments)
os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
ezgmail.send('sachin.shreekumar@gmail.com','Mars Rover images','Here are the images',attachments)


