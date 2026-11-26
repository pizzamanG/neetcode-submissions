class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            encoded += str(i)
            encoded += '😀'
        return encoded




    def decode(self, s: str) -> List[str]:
        decoded = []

        arr = ""
        for char in s:
            if char == '😀':
                decoded.append(arr)
                arr = ""
            else:
                arr += char
        return decoded
        

