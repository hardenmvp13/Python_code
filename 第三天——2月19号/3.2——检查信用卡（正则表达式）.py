'''
2.检查信用卡

给定一个信用卡号码，我们可以通过一些基本知识来确定发行人/供应商是谁。

完成get_issuer()将使用下面显示的值的功能来确定给定卡号的发卡机构。如果数字不匹配，则该函数应返回该字符串Unknown。

  Card Type     Begins With             Number Length
  AMEX          34 or 37                15
  Discover      6011                    16
  Mastercard    51, 52, 53, 54 or 55    16
  VISA          4                       13 or 16

'''
#1，自己的代码
#记得要用字符串的内置函数  startwith
def get_issuer(nums):
    nums = str(nums)
    length = len(nums)
    if nums[0] == '4' and length <= 16 and length >= 13:
        print("%s == VISA" % nums)
    elif nums[0:2] == '51' and length == 16:
        print("%s == Mastercard" % nums)
    elif nums[0:4] == '6011' and length == 16:
        print("%s == Discover " % nums)
    elif nums[0:2] == '34' or '37' and length == 15:
        print("%s == AMEX   " % nums)
    else:
        print('Unknown')
if __name__ =="__main__":
    get_issuer(4111111111111111)
    get_issuer(5105105105105106)
    get_issuer(6011151615155117)
    get_issuer(375659626259595)
    get_issuer(921111111111111111111)

#2，别人的代码（正则表达式）

import re
def get_issuer1(nums):
    nums = str(nums)
    if re.match(r'3[47]\d{13}$',nums):
        return "AMEX"
    elif re.match(r'6011\d{12}$',nums):
        return "Discover"
    elif re.match(r'5[12345]\d{14}$',nums):
        return "Mastercard"
    elif re.match(r'4(?:\d{12}|\d{15})$',nums):
        return "VISA"
    else:
        return "Unknown"

if __name__ =="__main__":
    print(get_issuer1(4111111111111111))
    print(get_issuer1(5105105105105106))
    print(get_issuer1(6011151615155117))
    print(get_issuer1(375659626259595))
    print(get_issuer1(921111111111111111111))