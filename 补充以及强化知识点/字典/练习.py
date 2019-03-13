'''字典里面的嵌套序列'''
dict = {
    "nba": {
        "rocket": "火箭",
        "lakers": "湖人",
        "others": {
            "坦克队伍": "灰熊",
            "潜力队伍": [
                "太阳",
                "独行侠队"]}}}
print(dict["nba"]["others"]["潜力队伍"][-2])
# 太阳

'''字典外面叠加for循环'''
name_dict = ["AA", "BB","CC"]
logs_dict = ["A", "B"]
name = {}
ret = {name: {
    'status': "1",
    'crane_status': "2",
    'material': "3",
    'logs': [{
        'material': "6",
        'quantity': "7",
    } for log in logs_dict]
} for name in name_dict}
print(ret)
# {'AA': {'status': '1', 'crane_status': '2', 'material': '3', 'logs': [{'material': '6', 'quantity': '7'}, {'material': '6', 'quantity': '7'}]},
# 'BB': {'status': '1', 'crane_status': '2', 'material': '3', 'logs': [{'material': '6', 'quantity': '7'}, {'material': '6', 'quantity': '7'}]},
#  'CC': {'status': '1', 'crane_status': '2', 'material': '3', 'logs': [{'material': '6', 'quantity': '7'}, {'material': '6', 'quantity': '7'}]}}
