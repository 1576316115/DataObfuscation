import re
import os
import random
import shutil
import string
import sys
from obfuscation_code.config import *


class PyObfuscation(object):
    """
    Obfuscation the code of Python
    """

    def __init__(self, FILEPATH):
        self.FILEPATH = FILEPATH
        # Check the file's type, if not '.py', raise error.
        if os.path.splitext(FILEPATH)[-1] != '.py':
            raise TypeError("The file's type is not Python file")
        with open(FILEPATH, 'r', encoding='utf-8') as f:
            self.content = f.readlines()  # 读取文件内容并赋值
            f.close()  # 关闭文件
        print(self.filecopy(FILEPATH, NEW_FILEPATH))  # 复制源文件到相应文件夹


    def filecopy(self, FILEPATH, NEW_FILEPATH):
        """
        拷贝文件函数
        :param FILEPATH:
        :param NEW_FILEPATH:
        :return:
        """
        try:
            shutil.copy(FILEPATH, NEW_FILEPATH)
        except IOError as e:
            return "Unable to copy file. %s" % e
        except:
            return "Unexpected error:", sys.exc_info()

    def savedict(self, var_dict):
        """
        保存变量混淆字典
        导入字典并存放到相应文件
        :param dict:
        :param DICT_FILEPATH:
        :return: None
        """
        try:
            with open(DICT_FILEPATH, 'w+', encoding='utf-8') as f:
                f.write(var_dict)
                f.close()
                print(DICT_FILEPATH, '&字典写入成功')
        except:
            print(DICT_FILEPATH, '&字典写入失败')


    def changevariable(self):
        """
        变量混淆函数
        :return: content
        """
        var_dict = {}  # 创建字典来保存被修改的变量
        reg = re.compile('(\s*)([a-zA-Z,]*?)\s*=\s*(.*)', re.S)  # 用正则表达式来匹配声明变量的语法
        lines = self.content[:]  # 创建列表存储改变之后的内容
        content = []
        for line in lines:  # 遍历每一行
            match = re.match(reg, line)  # 匹配声明变量的语法
            if match:  # 成功匹配到声明变量的语法
                block = match.group(1)
                vars = re.findall('\w+', match.group(2))  # 匹配一个或重复个字符，即变量名
                print('vars: ', vars)
                values = match.group(3)  # 变量所对应的值
                print('values: ', values)
                for index, var in enumerate(vars[:]):  # 枚举变量名
                    new_variable = var_dict.get(var)  # 从字典中查找键var，不存在时返回none
                    if not new_variable:
                        # Randomly select 16 letters as variable names
                        new_variable = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))
                        print('new_variable (if): ', new_variable)
                    # If the name conflicts
                    while new_variable in var_dict:
                        new_variable = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))
                        print('new_variable (while): ', new_variable)
                    var_dict[var] = new_variable  # 增加变量键值对
                    vars[index] = new_variable  # 更改变量名
                # Change to new string
                line = block + ','.join(vars) + '=' + values  # 对line内容进行重整
                content.append(line)  # 新增line
            else:
                content.append(line)
        # 变量字典转化为字符串后存放至对应文件中
        self.savedict(str(var_dict))
        print('var_dict => ', str(var_dict))
        # Change all the variable name which in the dictionary
        s = '>>>'.join(content)
        # print('s => ',s)
        for key, value in var_dict.items():
            s = re.sub(r'\b'+key+r'\b', value, s)  # Match the whole word
            # s = re.sub(key, value, s)  # Match the whole word
            content = s.split('>>>')
            # print('content => ', content)
        return content




if __name__ == '__main__':
    pyo = PyObfuscation(FILEPATH)
    new_content = pyo.changevariable()
    # print('new_content : ',new_content)
    try:
        with open(SAVE_FILEPATH, 'w+', encoding='utf-8') as fp:
            fp.writelines(new_content)
            fp.close()
            print(SAVE_FILEPATH, '&写入文件成功')
    except:
        print(SAVE_FILEPATH, '&写入文件失败')

