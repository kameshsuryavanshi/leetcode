class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        m =[]
        i,j = 0,0
        while i < len(word1) or j < len(word2):
            if i<len(word1): 
                m.append(word1[i]) 
                i+=1
            if j < len(word2):
                m.append(word2[j])
                j+=1
        return "".join(m)
        