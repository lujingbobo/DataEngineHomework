# 对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('E:\code\python\Data_Engine_with_Python-master\Data_Engine_with_Python-master\L1\car_data_analyze\car_complain.csv',encoding='gbk')

print(result)

# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
#result.to_csv('E:\code\python\Data_Engine_with_Python-master\Data_Engine_with_Python-master\L1\car_data_analyze\car_problem.csv')
print(result.columns)
tags = result.columns[7:]
#print(tags)
#求各品牌的投诉总数
df_bd_comp= result.groupby('brand')['id'].agg(['count'])
#求各品牌各车型的投诉数
df_md_comp= result.groupby(['brand','car_model'])['id'].agg(['count'])
#求各品牌的车型总数
#df_bd_md= result.groupby('brand')['car_model'].nunique
func={
    #投诉总数
    'brand':'count',
    #车型种类数
    'car_model':'nunique'
}
df_bd_md=result.groupby('brand').agg(func)
#求哪个品牌的平均车型投诉最多，各品牌平均车型投诉量=各品牌投诉总数/各品牌车型种类数
df=df_bd_md['brand']/df_bd_md['car_model']
print(df)