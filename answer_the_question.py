# -*- coding: utf-8 -*-

# @Author  : Allen_Liang
# @Time    : 2018/1/12 15:38

from aip import AipOcr  
import requests
import json
import time
from PIL import Image
import os
import matplotlib.pyplot as plt
import webbrowser
import urllib.parse


# 百度OCR_api定义常量 
# 在这里输入你的信息 
APP_ID = ''  
API_KEY = ''  
SECRET_KEY = ''  
# 初始化AipFace对象  
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)  
# 定义参数变量  
options = {  
  'detect_direction': 'true',  
  'language_type': 'CHN_ENG',  
}  


#利用adb从手机中获取屏幕事实截图，并pull到计算机上
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')
pull_screenshot()


#图片切割
def image_cut():
	img = Image.open("./screenshot.png")
	#区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)
	#问题区域
	question  = img.crop((0, 228, 480,401))
	question.save('question.png')
	#选线区域
	choices = img.crop((60, 422, 414, 771))
	choices.save('choices.png')
image_cut()


# 读取问题图片  
q_filePath = "question.png"  
def get_file_content(q_filePath):  
    with open(q_filePath, 'rb') as fp:  
        return fp.read()
# OCR识别问题文字
def question_words(q_filePath,options):
	# 调用通用文字识别接口
	result = aipOcr.basicGeneral(get_file_content(q_filePath), options)
	q_Result_s=''
	words_list=[]
	for word_s in result['words_result']:
		words_list.append(word_s['words'])
	q_Result_s = q_Result_s.join(words_list)
	#print(q_Result_s)
	return q_Result_s




# 读取选项图片  
c_filePath = "choices.png"  
def get_file_content(c_filePath):  
    with open(c_filePath, 'rb') as fp:  
        return fp.read()
# OCR识别问题文字
def choices_words(c_filePath,options):
	# 调用通用文字识别接口
	result = aipOcr.basicGeneral(get_file_content(c_filePath), options)
	c_Result_s=''
	words_list=[]
	for word_s in result['words_result']:
		words_list.append(word_s['words'])

	#c_Result_s = c_Result_s.join(words_list)
	#print(c_Result_s)
	#print(words_list)
	return words_list



#question_words(q_filePath,options)
#choices_words(c_filePath,options)

#网页分析统计
def count_base(question,choices):
    #print('题目搜索结果包含选项词频计数')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    #print(content)
    counts = []
    print('问题: '+question)
    print('————————————————————————————————————')
    if '不是' in question:
        print('请注意此题为否定题,选计数最少-最少-最少-最少-最少-的')
        print('—————————————————————————————————————')
    else:
        print('选计数最多-最多-最多-最多-最多-的')
        print('—————————————————————————————————————')
    for i in range(len(choices)):
        counts.append(content.count(choices[i]))
        print(choices[i] + " : " + str(counts[i]))



if __name__ == '__main__':
	#利用adb从手机（安卓）中获取屏幕实时截图，并pull到计算机上
	#pull_screenshot()
	#从实时截图中获取切割问题区、选项区
	#image_cut()
    #OCR问题区域
    question = question_words(q_filePath,options)
    #OCR选项区域
    choices = choices_words(c_filePath,options)
    #将题目提交到www.baidu.com,统计返回数据中的选项词频
    count_base(question, choices)