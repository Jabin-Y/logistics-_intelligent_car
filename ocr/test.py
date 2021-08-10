
# import os
# import sys



# __dir__ = os.path.dirname(__file__)
# print(__dir__)
# # sys.path.append(os.path.join(__dir__, ''))
# print(__dir__)
# import cv2
# print(cv2.__file__)

# list = [2, 3, 4]
# for num in list:
#     print (num)
    # print("\n")

# def convertName(cityName):  
#     flag = True
    
#     if flag:
#         name = unicode(cityName, "utf-8")    
#         final_name = "None"
#         if name.find(u"省")!=-1: 
#             flag = False   
#             name=name.split(u'省')[0]
#             final_name = name[-2:len(name)]
      
#         elif name.find(u'自治区') != -1:
#             flag = False
#             name = name.split(u'自')[0]
#             final_name = name[-2:len(name)]
        
#         elif name.find(u'特别行政区') != -1:
#             flag = False
#             name = name.split(u'特')
#             final_name = name[-2:len(name)]

#         elif name.find(u"市")!=-1:
#             flag = False
#             name = name.split(u'市')[0]+"市"
#             final_name = name[-2:len(name)]

#         return final_name


# v1.0
# def convertName(cityName):  
#     flag = True
    
#     if flag:
#         # name = str(cityName, "utf-8") 
#         name = cityName   
#         final_name = "None"
#         if name.find("省")!=-1: 
#             flag = False   
#             name=name.split('省')[0]
#             final_name = name[-2:len(name)]
      
#         elif name.find('自治区') != -1:
#             flag = False
#             name = name.split('自')[0]
#             final_name = name[-2:len(name)]
        
#         elif name.find('特别行政区') != -1:
#             flag = False
#             name = name.split('特')
#             final_name = name[-2:len(name)]

#         elif name.find("市")!=-1:
#             flag = False
#             name = name.split('市')[0]
#             final_name = name[-2:len(name)]

#         return final_name

# # cityName = "中国浙江省宁波市江北区"
# # cityName = "中国宁夏回族自治区呼和浩特市"
# cityName = "收小明10000000000上海市"
# city = convertName(cityName)
# if city=="None":
#     print("未检测到正确地址信息！")
# else:
#     print(city)







