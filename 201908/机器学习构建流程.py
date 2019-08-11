# --encoding:utf-8 --

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.externals import joblib

# 1. 数据的读取
df = pd.read_csv("")

#  2. 数据清洗，比如异常数据过滤
df.replace('?', np.nan, inplace=True)
datas = df.dropna(axis=1, how='any')

# 3. 构建特征矩阵X和目标数据矩阵Y, 如果不是数值型的，需要转换为数值型的
X = datas.iloc[:, 0:2]
Y = datas['xx']

# 4. 数据分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 5. 特征工程（中间可以有多个），比如这里的进行数据的标准化
one_hot = OneHotEncoder() # 哑编码模型对象构建<具体的后面会说>
one_hot.fit_transform(X_train, Y_train)
ss = StandardScaler()  # 构建模型对象
ss.fit(X_train, Y_train)  # 模型训练
X_train = ss.transform(X_train)  # 使用训练好的模型对训练集数据进行转换操作
# X_train = ss.fit_transform(X_train) # 即训练模型，同时又使用训练好的模型对训练集数据进行转换操作，等价于上面的两步#

# 6. 算法模型构建, 比如：这里是一个线性回归
lr = LinearRegression()  # 算法模型对象构建
lr.fit(X_train, Y_train)  # 模型训练

# 7. 使用训练集数据对算法模型的效果进行判断（要求测试集必须和训练集采用相同的操作）
# 7.1 对训练集进行特征工程转换
X_test = one_hot.transform(X_test)
X_test = ss.transform(X_test)
# 7.2 计算评估指标（模型自带的评估指标，比如：回归算法中是R^2，分类算法是准确率）
print(lr.score(X_test, Y_test))
# 7.3 计算其它评估指标(需要根据预测值和实际值进行计算)
y_hat = lr.predict(X_test)  # 获取预测信息
print("mse:", end='')
print(mean_squared_error(y_true=Y_test, y_pred=y_hat))
print("mae:", end='')
print(mean_absolute_error(y_true=Y_test, y_pred=y_hat))

# 8. 如果模型效果不错，进行模型输出（"所有模型都需要输出的"）
joblib.dump(one_hot, "model/one_hot.m")
joblib.dump(ss, "model/ss.m")
joblib.dump(lr, "model/lr.m")

# 9. 如果模型效果不好，进行模型的调整(特征工程、参数、算法重新选择)
