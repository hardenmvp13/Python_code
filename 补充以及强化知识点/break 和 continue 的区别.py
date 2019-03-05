'''
################  break和continue  ##############
  1.break
        意思为结束循环

        例：
        i = 0
        while i<10:
            i+=1
            if i==5:  #当i=5时，结束整个循环
                break
            print("i=%d"%i)

        代码效果：
        i=1
        i=2
        i=3
        i=4


  2.continue
        意思为结束当前循环进入下一个循环

        例：
        i = 0
        while i<10:
            i+=1
            if i==5:  #当i=5时，结束当前循环进入下一个循环
                continue
            print("i=%d"%i)

        代码效果：
        i=1
        i=2
        i=3
        i=4
        i=6
        i=7
        i=8
        i=9
        i=10
        以上循环没有i=5
'''