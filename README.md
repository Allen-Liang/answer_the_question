# answer_the_question
冲顶大会、芝士超人、西瓜视频、头脑王者、百万英雄等答题辅助，瞬间打开chrome 百度，仅供娱乐学习交流使用！<br>

# 使用方法：<br>
1.环境安装 adb、python 、pip install 相关包<br>
2.注册百度OCRapi或者Face++的OCRApi <br>
3.根据自己手机（目前仅限安卓）的分辨率，调整image_cut()中的参数，可以用cut_images-size.py来慢慢调整。<br>
   区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)。（x0,y0）为起点坐标，（x1,y2）为终点点坐标。<br>
4.在百度OCR_api定义常量APP_ID 、API_KEY 、SECRET_KE换上你的账号信息，在你注册的平台上的控制台上可以查看<br>
5.安卓手机开启调试模式，USB连接电脑<br>
6. python answer_the_question.py 使用<br>
7.参考了这位[大牛](https://github.com/Skyexu/TopSup)的部分代码,感谢！<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/one.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/two.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/three.JPG)<br>

