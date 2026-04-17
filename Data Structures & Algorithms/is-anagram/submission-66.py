class Solution:
    
    def mapToHashMap(input_string: str) -> {} :
        stored_char = {}
        for char in input_string:
            if char not in stored_char:
                stored_char[char] = 1
            else:
                stored_char[char] += 1
        return stored_char
        


    
    def isAnagram(self, s: str, t: str) -> bool:
        
        POTENTIAL_ANAGRAM = False

        if len(s) != len(t):
            return False
        
        if len(s) == len(t):
            POTENTIAL_CANDIDATE = True
        
        if POTENTIAL_CANDIDATE:
            s_Map = self.mapToHashMap(s)
            t_Map = self.mapToHashMap(t)
            
            if s_Map.values() == t_Map.values():
                return True
            return False



        