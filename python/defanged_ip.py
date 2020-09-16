# https://leetcode.com/problems/defanging-an-ip-address/
# COMPLETE
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


print(Solution().defangIPaddr("1.1.1.1"))
print(Solution().defangIPaddr("255.100.50.0"))
