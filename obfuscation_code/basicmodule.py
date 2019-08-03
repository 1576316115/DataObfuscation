def write(filepath, content):
    """
    写入文件
    :param filepath:
    :param filecontent:
    :return:
    """
    try:
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.writelines(content)
            f.close()
            print(filepath, '& write success')
    except:
        print(filepath, '& write fail')

def read(filepath):
    """
    读取文件
    :param filepath:
    :param filecontent:
    :return:
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.readlines()  # 读取文件内容并赋值
            f.close()  # 关闭文件
            print(filepath, '& read success')
            return content
    except:
        print(filepath, '& read fail')
        return