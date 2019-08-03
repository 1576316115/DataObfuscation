from obfuscation_code.config import *
from obfuscation_code.basicmodule import *
import re

class DeObfuscation(object):
    """
    反向混淆，恢复混淆文件
    根据混淆文件+混淆字典 => 源文件
    """
    def __init__(self, DICT_FILEPATH, RECOVER_FILEPATH):
        """
        """
        self.DICT_FILEPATH = DICT_FILEPATH
        self.RECOVER_FILEPATH = RECOVER_FILEPATH

    def deobfuscation(self):
        """
        恢复程序
        :return:
        """
        read_list = read(self.DICT_FILEPATH)
        var_dict = eval(str(read_list[0]))
        print('var_dict => ', var_dict)
        content = self.deob(var_dict)  # 返回反向混淆代码内容
        write(self.RECOVER_FILEPATH, content)  # 将内容写至recover_file

    def deob(self, var_dict):
        """
        反向混淆并输出反向混淆内容
        :return: content
        """
        content = read(SAVE_FILEPATH)
        # print('content => ', content)
        s = '>>>'.join(content)
        # print('s => ', s)
        for key, value in var_dict.items():
            print(key, value)
            # s = re.sub(r'\b'+value+r'\b', key, s)  # Match the whole word
            s = re.sub(value, key, s)  # Match the whole word
            content = s.split('>>>')
            # print('content => ', content)
        return content

if __name__ == '__main__':
    deo = DeObfuscation(DICT_FILEPATH, RECOVER_FILEPATH)
    deo.deobfuscation()

