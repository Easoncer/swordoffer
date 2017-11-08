def VerifySquenceOfBST( sequence):
        # write code here
        if len(sequence)==0:
            return False
        root=sequence[-1]
        i=0
        while root>sequence[i]:
            i+=1
        temp=i

        
        while sequence[i]>root :
            i+=1
        print i
        if (len(sequence)-1)!=i:
            return False
        left=True
        right=True
        if temp>0:
            left=VerifySquenceOfBST(sequence[:temp])
        if len(sequence)-temp>1:
            right=VerifySquenceOfBST(sequence[temp:-1])

        return left and right
if __name__=="__main__":
    # a=[4,8,6,12,16,14,10]
    a=[4,6]
    print VerifySquenceOfBST(a)