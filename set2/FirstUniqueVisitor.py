def firstuniquevisitor(arr):
    visitor_count = {}
    
    # Count the occurrences of each visitor
    for visitor in arr:
        if visitor in visitor_count:
            visitor_count[visitor] += 1
        else:
            visitor_count[visitor] = 1
    
    # Find the first unique visitor
    for visitor in arr:
        if visitor_count[visitor] == 1:
            return visitor
    
    return None  
arr=[17,23,17,8,23,42,8,5,42,17]
print(firstuniquevisitor(arr))