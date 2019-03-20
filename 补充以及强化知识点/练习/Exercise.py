class Sum(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s的年龄是%d" % (self.name, self.age)

