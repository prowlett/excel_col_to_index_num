import xlrd

def excel_col_to_index_num(col_name):
    """
    Converts Excel column letter to zero-indexed number.
    e.g. "A" - > 0, "Z" -> 25, "AA" -> 26, etc.
    """
    col_num = 0
    for i in range(0,len(col_name)):
        col_num += (ord(col_name[len(col_name)-i-1])-64)*26**i
    return col_num-1

# # For testing
# column_letters = []
# for i in range(0,702):
#     thiscolname = xlrd.colname(i)
#     print("------------------")
#     print("Input: {} converts to {}".format(i,thiscolname))
#     rtn_num = excel_col_to_index_num(thiscolname)
#     print("Returned col number: {}".format(rtn_num))
#     print("------------------")
# print("What about bigger numbers, for which `colname` throws an IndexError?")
# for inputltr in ("AAA","AAB","AMJ","ZZZ"):
#     print("Input {} returns index {}".format(inputltr,excel_col_to_index_num(inputltr)))
