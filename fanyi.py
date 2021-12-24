import requests
import os
#获取Access_token

class Get_Fanyi(object):
    def  __init__(self):
        print("开始测试!")

    # # 判断首字母是否是英文字母从而判断是英译汉or汉译英
    # def is_eng(self,ch):
    #     if ord(ch) not in range(97, 122) and ord(ch) not in range(65, 90):
    #         return 'zh', 'en'
    #     return 'en', 'zh'

    def get_content(self,aim_path):
        #获取token
        api_key = 'G5jsCMCkK52uGcbP4G8cUeV4'
        secret_key = 'ZSpo8fHMU0MHMkrcWKdbvtq975s0qdvK'
        # 将网址与两个Key组合
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
               api_key + '&client_secret=' + secret_key

        response = requests.get(host)
        if response:
            token = response.json()['access_token']

            # 打开目标文件
            with open(aim_path, 'r', encoding="gbk") as fp:
                for eachLine in fp:  # 按行读入文件
                    line = eachLine.strip()  # 去除每行首尾可能的空格等
                    if line == "":  # 去掉无法翻译的空行
                        pass
                    else:
                        q = line
                        print(line)
                        # 下面是翻译

                        # 查看输入的内容首字是否为英文字母
                        fr, tr = 'zh', "en"
                        # 将Access_token+from+to整合到网址url中
                        url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + \
                              token + '&q=' + q + \
                              '&from=' + fr + '&to=' + tr
                        # 用get方式获取响应内容
                        response = requests.get(url)
                        result = response.json()
                        '''可先打印输出响应内容，格式如：
                        {"result":{"from":"en","trans_result":[{"dst":"你好","src":"hello"}],"to":"zh"},"log_id":470906}
                        '''
                        # print('翻译后的内容：', end=' ')
                        aim_result = response.json()['result']['trans_result'][0]['dst']
                        print(aim_result)

                        # 写入翻译的文本,写入路径是之前得到的目标路径后面加几个东西，追加模式
                        with open(aim_path + '译文.txt', 'a+', encoding="gbk") as fp:
                            fp.write(aim_result)  # 按行写入文件
                            fp.write("\r\n")

