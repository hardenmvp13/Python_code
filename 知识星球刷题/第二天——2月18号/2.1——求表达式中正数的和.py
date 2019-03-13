'''
1.求表达式中正数的和

你得到一组数字，返回所有正数的总和。

示例[1,-4,7,12]=>1 + 7 + 12 = 20

注意：如果没有要求的总和，则默认值为0。
'''

def positive_sum(nums):
    sum_nums = 0
    for i in range(0,len(nums)):
        if nums[i] > 0:
            sum_nums = sum_nums + nums[i]
    print(sum_nums)

if __name__== '__main__':
    positive_sum([1,-4,7,12])