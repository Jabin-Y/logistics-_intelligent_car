import shutil

file_dir ='/home/meroke/图片/test/xml(复件)/'
save_dir = '/home/meroke/图片/test/ttt_xml/'
xml_num = 874
for i in range(170,198):
    file = file_dir + '{}.xml'.format(i)
    for j in range(1,5):
        save_file = save_dir + '{}.xml'.format(xml_num )
        xml_num += 1
        shutil.copyfile(file,save_file)
