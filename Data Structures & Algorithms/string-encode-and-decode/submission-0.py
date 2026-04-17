class Solution:

    def encode(self, strs: List[str]) -> str:
        single_str = " ".join(strs)
        print(single_str)

    def decode(self, s: str) -> List[str]:
        str_arr = s.split(" ")
        return str_arr
