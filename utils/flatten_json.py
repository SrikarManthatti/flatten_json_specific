import json
import pandas as pd
import numpy as np

def flatten_outer (data):
    """
    Description: This is upper level function which has a list that stores each row values dictionary
    Parameters: data, accepts each record of a json file
    """
    full_list = []
    def flatten_inner(sub_data,first_level_key='',index=0,tot_len=0):
        
        """
        Description: This function iterates through each and every key value pair in a JSON record. If any key has a list of items
                     then this function will preserve the structure of the data and creates a row value as a list for each column. 
                     In this way, there will be no change in the number of rows of a dataframe, and it will be easy to perform some 
                     further cleaning and transformation tasks
        Parameters: sub_data - for each key which has a dictionary or list value will be passed again to this function as a part of recursion.
                                This parameter contains the dict or list value
                    first_level_key - first level key in the json file
                    index - this index value is used to send the item position if a value is a list, otherwise it will be 0
                    tot_len - if any key has a list nested value, then the length of list nested value will be passed in here. This value will be used to created a placeholder list
        """
        for k,v in sub_data.items():
            full_key = first_level_key+'.'+k if first_level_key !='' else k
            if isinstance(v, dict): 
                flatten_inner(v, full_key)
                
            elif isinstance(v, list):
                for i in range(0, len(v)): 
                    if (isinstance(v[i], dict)):
                        flatten_inner(v[i], full_key,index=i, tot_len=len(v))
                    else: 
                        new_list = value_list[full_key] if full_key in value_list.keys() else []
                        new_list.append(v)
                        value_list[full_key] = new_list
                        break
            else:
                if full_key in value_list.keys():
                    placeholder_list = value_list[full_key]
                    if index == 0:
                        placeholder_list.append(v)
                    else:
                        placeholder_list[index] = v
                    value_list[full_key] = placeholder_list
                else:
                    if index == 0:
                        if tot_len == 0:
                            value_list[full_key] = [v]
                        else:
                            placeholder_list = [None]*tot_len
                            placeholder_list[0] = v
                            value_list[full_key] = placeholder_list
                    else:
                        
                        dif = tot_len - index - 1
                        placeholder_list = [None] * index
                        placeholder_list.append(v)
                        placeholder_list = placeholder_list + [None] * dif
                        value_list[full_key] = placeholder_list
        return value_list
        
    for row in data:
        value_list = dict() #creating a value_list to store key value pairs(column values) for each record
        cv =  flatten_inner(row)
        full_list.append(cv)
        
    return full_list

def df_create_clean(full_list):
    df = pd.DataFrame(full_list)
    df = df.where(pd.notnull(df),None)
    cols = df.columns
    for col in cols:
        df[col] = df[col].apply(lambda x: None if (isinstance(x,list) and len(x)==0) else x)
        df[col] = df[col].apply(lambda x: x[0] if (isinstance(x,list) and len(x)==1) else x)
    return df


def flatten_json(data):
    df = pd.DataFrame(flatten_outer(data))
    cleaned_df = df_create_clean(df)
    return cleaned_df