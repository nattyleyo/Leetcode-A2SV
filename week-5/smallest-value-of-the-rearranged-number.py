class Solution:
    def smallestNumber(self, num: int) -> int:
        flag=False
        if num<0:
            num=str(num)[1:]
            flag=True
        else:
            num=str(num)[0:]
        my_list=[int(n) for n in num]
        my_list.sort(reverse=True)
        if flag:
            my_list[0]=0-my_list[0]
        else:
            my_list.sort()
            if len(my_list)>2 and min(my_list)==0:
                for i in range(1,len(my_list)):
                    if my_list[i]!=0:
                        my_list[0],my_list[i]=my_list[i],my_list[0]
                        break
        my_list=[str(num) for num in my_list]
        return int(''.join(my_list))
        