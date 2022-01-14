# flatten_json_specific

This python code has been developed to work with nested Json data. There are few standard libraries like Json_normalize which are developed, but in my view they don't quite suit for all use cases and moreover we need to perform some extra task if we want to extract deeply nested fields.

However the python code which I created can extract deeply nested json fields upto any level. The beauty of this code is, it wraps everything into a list and place it into a dataframe cell by preserving the data structure (Note: all the missing values at any level will be replaced with None).

All deeply nested key names will be appended with '.' and saved as a column name.

### Extracted the fields!!! What's Next?

Well!!! this is the main the reason why I came up with this code. Working with dataframes, list by using apply functions to transform and enrich the data is much easier. 

In many ETL tasks, this code can be used to extract the nested and deeply nested and create a normalized dataframe which can be further used in enriching and transforming the data. Since, we are preserving the structure also it should be pretty easy to use the index of the values inside the list to perform required tasks.

I have also created an example python notebook file, *initial_file.ipynb* which contains four examples that you can refer to. The main code for handling the json resides here **utils/flatten_json.py**

### Please contribute
If you see some flaws, or errors, or any modifications that can be done. Please feel free to update the code by creating a pull request. (please ensure you follow git standard procedure for merging the code into master branch)
