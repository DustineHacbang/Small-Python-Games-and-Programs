def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."
        
    
    string_of_num = ""
    for val in range(1,n+1):
        string_of_num = string_of_num + " " +str(val)
        # return string_of_num
    return string_of_num.strip()
