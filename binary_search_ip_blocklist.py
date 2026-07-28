#binary search

def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if  arr [mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7)) 
print(binary_search(arr, 11)) 
print(binary_search(arr, 4))  





class IPBlocklist:
    def __init__(self):
        self.blocklist = []
     
    def ip_add(self, ip):
        self.blocklist.append(ip)
        self.blocklist.sort()
        

    def is_block(self, ip):
         left = 0
         right = len(self.blocklist) - 1

         while left <= right:
             mid = (left + right) //2
             if self.blocklist [mid] == ip:
                 return True
             elif self.blocklist [mid] < ip:
                 left = mid + 1
             else:
                 right = mid -1
         return False
                
    def display(self):
        for ip in self.blocklist:
            print(f"blocked: {ip}")

def main():
    lst = IPBlocklist()
    lst.ip_add("10.0.0.1")
    lst.ip_add("172.16.0.5")
    lst.ip_add("192.168.1.105")
    lst.ip_add("8.8.4.4")
    lst.ip_add("45.33.32.156")
    lst.display()
    print(lst.is_block("192.168.1.105"))
    print(lst.is_block("8.8.8.8"))

main()
        