

def main(columnTitle):
    length = len(columnTitle)
    return sum(
            [ 
                ( ord(columnTitle[i]) - ord('A') + 1) * 26** ( length - i - 1) 
            for i in range( length ) 
            ]
        )