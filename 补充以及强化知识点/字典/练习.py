'''字典里面的嵌套序列'''
dict = {"nba": {"rocket": "火箭", "lakers": "湖人", "others": {"坦克队伍": "灰熊","潜力队伍":["太阳","独行侠队"]}}}
print(dict["nba"]["others"]["潜力队伍"][-2])
