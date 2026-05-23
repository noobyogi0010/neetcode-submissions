class Solution:
    # i can use the concept of how data packets are transferred
    # the head consists of the length of the data and then rest of the packet has the data
    # so i can use the same concept, the encoded string starts with a set of digits
    # depicting the length of word which follows

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += f"{len(string)}_{string}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            # get the length of first string
            start = i
            length = 0
            while s[i] != "_":
                length = length*10 + int(s[i])
                i += 1
            # inc pointer to the start of string
            i += 1
            # get the encoded string
            res.append(s[i:i+length])
            # inc pointer to the end of string
            i += length

        return res
