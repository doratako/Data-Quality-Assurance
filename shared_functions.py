import pandas as pd
import chardet
import sys

raw_files_folder = "Source"    



"""OPEN FILE"""

def read_files(source, notebook):
    try:
        with open(source, "rb") as f:
            file_encoding = chardet.detect(f.read())
        
        return pd.read_csv(source, encoding=file_encoding["encoding"])
    
    except FileNotFoundError as e:
        print(f"An error occured running the <{notebook}>. {e}>")




"""VALIDATE COLUMN NAMES IN THE SOURCE"""

def source_columns_name_check(source_colums_list, expected_columns_list, notebook):

    result = []

    for e_col in expected_columns_list:
        if e_col in source_colums_list:
            result.append(True)
        else:
            result.append(False)

    for s_col in source_colums_list:
        if s_col in expected_columns_list:
            result.append(True)
        else:
            result.append(False)

    try: 
        if False in result:
            raise ValueError
    except Exception as e:
        print(f"An error occured running the <{notebook}>. {e}>")





"""REMOVE LEADING, TRAILING WHITESPACES"""

def strip_df(dataframe):
    return dataframe.applymap(lambda x: x.strip() if isinstance(x, str) else x)



"""REMOVE ROWS WHERE MANDATORY DATA ARE MISSING"""

def mandatory_columns_null_handling(dataframe, mandatory_columns_list, notebook):
    null_indicators_list = ["?", " ", "*", "-"] 

    try:
        missing_madanatory_bool = dataframe[mandatory_columns_list].applymap(lambda x: x in null_indicators_list).any(axis=1)
        missing_madanatory_ind = missing_madanatory_bool.loc[lambda s: s].index.tolist()

        return dataframe.drop(missing_madanatory_ind, axis=0)
    
    except (AttributeError, ValueError) as e:
        print(f"An error occured running the <{notebook}>. {e}>")
        



"""HANDLE MISSING DATA IN OPTIONAL COLUMNS"""

def optional_columns_null_handling(dataframe, mandatory_columns_list, notebook):
    null_indicators_list = ["?", " ", "*", "-"] 

    try:
        optional_cols_df = dataframe.loc[:, ~dataframe.columns.isin(mandatory_columns_list)]
        
        # drop rows where all optional columns are empty
        all_opt_cols_null = optional_cols_df.applymap(lambda x: x in null_indicators_list).all(axis=1)[lambda x: x].index
        dataframe_null = dataframe.drop(all_opt_cols_null, axis=0)

        # replace special characters that indicate null values
        return dataframe_null.applymap(lambda x:  "N/A" if x in null_indicators_list else x)

    except (AttributeError, ValueError) as e:
        print(f"An error occured running the <{notebook}>. {e}>")




"""REMOVE LEADING AND TRAILING WHITESPACES, REPLACE SPECIFIED CHARARACTERS, CAPITALISE FIRST LETTER"""

def format_columns(dataframe, columns, replace_char_dict, notebook):

    try:
        dataframe.update(dataframe[columns].apply(lambda x: x.replace(replace_char_dict, regex=True).str.strip().str.title()))
        return dataframe

    except (AttributeError, ValueError) as e:
        print(f"An error occured running the <{notebook}>. {e}>")

  

        



