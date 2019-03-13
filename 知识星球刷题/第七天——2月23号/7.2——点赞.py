'''
2.点赞

你可能知道Facebook和其他网页上的“点赞”系统。人们可以“喜欢”博客文章，图片或其他项目。我们想要创建应该在这样的项目旁边显示的文本。

实现一个函数likes :: [String] -> String，它必须包含输入数组，包含喜欢项目的人的名字。它必须返回显示文本，如示例所示：
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
对于4个或更多名称，数字and 2 others只会增加。
'''
#自己写的代码
def likes(names):
    nums = len(names)
    if nums == 0:
        print("must be "+"no one likes this")
    elif nums == 1:
        print("must be "+"%s likes this"%names[0])
    elif nums == 2:
        print("must be "+"%s and %s likes this"%(names[0],names[1]))
    elif nums == 3:
        print("must be "+"%s , %s and %s likes this"%(names[0],names[1],names[2]))
    else:
        print("must be "+"%s , %s and 2 others likes this"%(names[0],names[1]))

if __name__ == "__main__":
    likes(["Peter"])
    likes(["Jacob", "Alex"])
    likes(["Max", "John", "Mark"])
    likes(["Alex", "Jacob", "Mark", "Max"])
