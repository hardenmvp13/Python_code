'''
##############  继承  ###############
'''
#父类的父类
class Animal:
    def eat(self):
        print("————吃————")
    def sleep(self):
        print("————睡觉————")
#父类，（定义一个狗类）
class Dog(Animal):
    def bark(self):
        print("————吠叫————")
#子类（定义一个哈士奇类）
class Husky(Dog):
    def catch(self):
        print("————哈士奇很傻很帅————")

wangcai = Dog()
wangcai.bark()
wangcai.eat()
wangcai.sleep()
'''
————吠叫————
————吃————
————睡觉————
'''

erha = Husky()
erha.catch()
erha.bark()
erha.eat()
erha.sleep()
'''
————哈士奇很傻很帅————
————吠叫————
————吃————
————睡觉————
'''