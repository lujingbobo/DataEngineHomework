import numpy as np
#创建numpy的type类型
persontype = np.dtype({
    'names':['name', 'chinese', 'math', 'english'],
    'formats':['U32','i', 'i', 'i']})
#录入学生成绩
peoples = np.array([("张飞",68,65,30),("关羽",95,76,98),("刘备",98,86,88),("典韦",90,88,77),("许褚",80,90,90)],dtype=persontype)
#创建三科的成绩列表
chinese=peoples['chinese']
math=peoples['math']
english=peoples['english']

#求各科的最小成绩
chinese_min=np.argmin(chinese)
math_min=np.argmin(math)
english_min=np.argmin(english)
#求各科的最大成绩
chinese_max=np.argmax(chinese)
math_max=np.argmax(math)
english_max=np.argmax(english)

print('平均成绩：')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.mean(chinese),np.mean(math),np.mean(english)))

print('\n最小成绩：')
print('语文：{}, {}'.format(peoples[chinese_min]['chinese'], peoples[chinese_min]['name']))
print('数学：{}, {}'.format(peoples[math_min]['math'], peoples[math_min]['name']))
print('英语：{}, {}'.format(peoples[english_min]['english'], peoples[english_min]['name']))

print('\n最大成绩：')
print('语文：{}, {}'.format(peoples[chinese_max]['chinese'], peoples[chinese_max]['name']))
print('数学：{}, {}'.format(peoples[math_max]['math'], peoples[math_max]['name']))
print('英语：{}, {}'.format(peoples[english_max]['english'], peoples[english_max]['name']))

print('\n方差：')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.var(chinese), 	np.var(math), np.var(english)))
print('\n标准差')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.std(chinese), 	np.std(math), np.std(english)))

#创建一个字典用于存放每个人的总成绩
total = {}
for i in range(len(peoples)):	total[peoples[i][0]] = peoples[i][1] + peoples[i][2] + peoples[i][3]
# 对总成绩排序，名字也随之排序
total = sorted(total.items(), key = lambda x: x[1], reverse = True)
print('\n总成绩排序：')
for i in range(len(total)):
    print("第{}名： {}\t总成绩： {}".format(i+1, total[i][0], total[i][1]))
