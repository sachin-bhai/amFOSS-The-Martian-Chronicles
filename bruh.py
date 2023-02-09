import ezgmail,os

attachments=os.listdir(r'/home/programmer/The-Martian-Chronicles/rover_images')

print(attachments)
# for i in range(len(attachments)):
#     attachments[i]=str(r'/home/programmer/The-Martian-Chronicles/rover_images/'+attachments[i])
# print(attachments)
os.chdir(r'/home/programmer/The-Martian-Chronicles/rover_images')
ezgmail.send('am.en.u4ece22138@am.students.amrita.edu','Mars Rover images','Here are the images',attachments)

# /home/programmer/The-Martian-Chronicles/rover_images/attachment0.jpg