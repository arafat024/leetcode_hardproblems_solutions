class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy_distributions = [1 for i in range(len(ratings))]
        if len(ratings)>1:
            #left to right pass
            for i in range(len(ratings)):
                if i==0:
                    continue
                else:
                    if ratings[i-1]<ratings[i]:
                        candy_distributions[i] = candy_distributions[i-1]+1
            #right to left pass
            for i in range(len(ratings)):
                reverse_index = len(ratings)-1-i
                if reverse_index==len(ratings)-1:
                    continue
                else:
                    if ratings[reverse_index]>ratings[reverse_index+1]:
                        candy_distributions[reverse_index] = max(candy_distributions[reverse_index],candy_distributions[reverse_index+1]+1)
        #final result
        return sum(candy_distributions)

        

        
        
        

                
            



        