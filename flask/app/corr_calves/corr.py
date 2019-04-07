# -*- coding: utf-8 -*- 
import pandas as pd

def readData(path):
    in_data = pd.read_csv(path, encoding='utf8')
    in_data[u'ИНВ №'] =  pd.to_numeric(in_data[u'ИНВ №'],errors="coerce", downcast='integer')
    in_data = in_data.dropna().reset_index(drop=True)
    return in_data

def corrsWithColumnsIn(x_data, y_data, corr_threshold =.7, join_key = u'ИНВ №', axis = 0):
    
    
    param_data = y_data.merge(x_data, on=join_key, how='left').dropna()
    y_columns = y_data.columns
    y_columns = y_columns[y_columns != join_key]
    
    
    key_corrs_with = {}
    for key in y_columns:
        key_corrs_with[key] = param_data.corrwith(param_data[key])
        
    diff_columns = [i for i in y_columns] + [join_key] # keys unnecessary for correlation purposes
    
    df = pd.DataFrame(key_corrs_with)
    df = df.drop(diff_columns)
    threshold_filter = df[df.abs() > corr_threshold].any(axis = 1)
    #print(threshold_filter)
    return df[threshold_filter]