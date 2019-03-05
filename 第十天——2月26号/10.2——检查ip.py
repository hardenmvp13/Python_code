'''
2.检查ip
编写一种算法，以十进制格式识别有效的IPv4地址。如果IP由四个八位字节组成，其值在0和之间255，则应视为有效。
该函数的输入保证是单个字符串。
例子：有效输入
1.2.3.4
123.45.67.89

无效输入：
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

请注意，前导零（例如01.02.03.04）被视为无效。
测试用例：
Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
Test.assert_equals(is_valid_IP(''),                False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
Test.assert_equals(is_valid_IP('12.34.56'),        False)
Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'),        True)
Test.assert_equals(is_valid_IP('0.0.0.0'),          True)
Test.assert_equals(is_valid_IP('0.34.82.53'),       True)
Test.assert_equals(is_valid_IP('192.168.1.300'),   False)
'''

def is_valid_IP(seq):
    seq_split = seq.split('.')
    if len(seq_split) != 4:
        return False
    for i in seq_split:
        if not i.isdigit():
            return False
        elif int(i) <0 and int(i) >255:
            return False
        else:
            return True
    return seq_split
if __name__ == "__main__":
    print(is_valid_IP('12.255.56.1'))
    print(is_valid_IP(''))
    print(is_valid_IP('abc.def.ghi.jkl'))
