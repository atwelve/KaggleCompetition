

import os
import sys
import pdb
import pandas as pd

os.chdir('./House_Price')

train_data_file = './wks/train.csv'
test_data_file  = './wks/test.csv'

all_train_data = pd.read_csv(train_data_file)
train_data_X = all_train_data.drop('SalePrice', axis=1)
train_data_Y = all_train_data.loc[:, ['SalePrice']]



# 1. clear data
need_drop_cols = []
for col_name in train_data_X.columns:
    miss_data_ratio = train_data_X[col_name].isnull().sum() / len(train_data_Y.index)
    print('%s miss radio : %f' % (col_name, miss_data_ratio))
    if miss_data_ratio > 0.75:
        need_drop_cols.append(col_name)
print('below col will be drop, because they have more 75% null data')
print(need_drop_cols)

train_data_X.drop(need_drop_cols, axis=1, inplace=True)



