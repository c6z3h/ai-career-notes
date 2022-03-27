class Solution(object): 
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # from last letter to first.
        # last letter += [1-26] *26^0
        # 2nd-last += [1-26] * 26^1
        # 3rd-last += [1-26] * 26^2
        # assume subsequent are same
        dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        columnNumber = 0
        char_list = list(columnTitle[::-1])
        for i in range(len(char_list)):
            columnNumber += dict[char_list[i]] * (26**i)
        return columnNumber
        """
        A 1
        B 2
        Z 26
        
        AA 27
        AB 28
        AZ 52 (26+26)
        
        BA 53
        BB 54
        BZ 78 (26+26+26)
        
        ZZ 676 (26*26)
        
        AAA 677
        AAZ 677 (+25)
        ABA 704
        ABZ 729 (+25)
        ACZ 755 (+26)
        AZZ 1352 (676+676)
        
        BAA 1353
        BZZ 2028 (3*676)
        
        """
