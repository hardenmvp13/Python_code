'''
2.人性化的可读性时间

编写一个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（HH:MM:SS）

- HH =小时，填充到2位数，范围：00 - 99
- MM =分钟，填充到2位数，范围：00 - 59
- SS =秒，填充到2位数，范围：00 - 59

最长时间永远不会超过359999（99:59:59）
'''

def make_readable(req):
    second = "%02d"%(req%60)
    minute = "%02d"%(req%3600//60)
    hour = "%02d"%(req//3600)
    return '{}:{}:{}'.format(hour,minute,second)

if __name__ == "__main__":
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(59))
    print(make_readable(359999))