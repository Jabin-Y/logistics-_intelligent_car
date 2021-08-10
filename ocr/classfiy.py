# coding=utf-8
# 随机生成训练集和测试集
# 对一个文件夹下的图像生成txt，然后随机选取里面的内容，然后保存到不同的文件夹。
# coding=utf-8
import os, random, shutil


def moveFile(mode):
    pathDir = os.listdir(ori_path)  # 取图片的原始路径
    filenumber = len(pathDir)
    picknumber = int(filenumber * ratio)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    split_JPEG = split_Dir + '/JPEGImages'
    split_XML = split_Dir + '/Annotations'
    for name in sample:
        behind = name.split('.')[0]
        xml = behind + '.xml'
        # print(name)
        # print(os.path.join(xml_path, xml))
        # print(os.path.join(split_Dir,'xml'))
        # print(os.path.join(ori_path,name))
        shutil.move(os.path.join(xml_path, xml), os.path.join(split_XML,mode))
        shutil.move(os.path.join(ori_path, name), os.path.join(split_JPEG,mode))
    return


if __name__ == '__main__':
    ori_path = '/home/meroke/图片/test/Complete/Image'  # 总文件图片路径
    xml_path = '/home/meroke/图片/test/Complete/Annotations' # 总文件夹xml文件

    split_Dir = '/home/meroke/图片/test/mydata'  # 移动到新的文件夹路径
    mode = 'test'
    ratio = 0.2  # 抽取比例
    moveFile(mode)

    mode = 'val'
    ratio = 0.25
    moveFile(mode)
    # for firstPath in os.listdir(ori_path):
    #     fileDir = os.path.join(ori_path, firstPath)  # 原图片文件夹路径
    #     tarDir = os.path.join(split_Dir, firstPath)  # val下子文件夹名字
    #     behind = firstPath.split('.')
    #     xml_file = behind + '.xml'
    #     xmlDir = os.path.join(split_Dir,xml_file)
    #     print(behind[0])
        # print(tarDir)
        # if not os.path.exists(tarDir):  # 如果val下没有子文件夹，就创建
        #     os.makedirs(tarDir)
        # moveFile(fileDir)  # 从每个子类别开始逐个划分
