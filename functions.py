
"""
Returns list: [size,color from last element]
"""
def fileLen(filepath):
    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 0
        while line:
            color = int(line)
            cnt += 1
            line = fp.readline()
    return [cnt, color]
    
"""
Returns: color
"""
def fileLineColor(searched_line,filepath):
    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 0
        while cnt <= searched_line:
            color = int(line)
            cnt += 1
            line = fp.readline()
        
        if cnt != searched_line+1:
            print ("ERROR! Line doesn't exist")
            return -1
    return color
    