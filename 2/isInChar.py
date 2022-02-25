def isIn(char, aStr):
    if len(aStr) == 1:
      return aStr == char 
    if len(aStr) == 0:
        return False    
    middlechar = len(aStr) // 2 
    if char == aStr[middlechar] :
        return True    

    else:
        if char > aStr[middlechar]:            
            return isIn(char, aStr[middlechar:]) 
        else: 
            return isIn(char, aStr[0:middlechar])
print(isIn('x', 'adios'))


#another test
