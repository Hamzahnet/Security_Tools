#contains duplicate leet code
class solution:
    def contains_dupicate(self , nums: list[int]) -> bool:
        hashset = set

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            return False



class PortScanner:
    def __init__(self, target, ports: list[int]):
        self.target = target
        self.ports = ports

    def scan_port(self, ports):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((self.target, ports))
        sock.close()
        return result == 0

    def run(self):
        self.open_ports = []                                       #PORT SCANNER
        print(f"scanning {self.target}...")
        for ports in self.ports:
            if self.scan_port(ports):
                self.open_ports.append(ports)
        print("scan complete.")
        
    def display_results(self):
       if not self.open_ports:
           print("no open ports found")
       else:
           for ports in self.open_ports:
            print(f"ports {ports} is open")

def main():
    scanner = PortScanner("127.0.0.1", [22, 80, 135, 443, 445, 3306, 8080, 8888])
    scanner.run()
    scanner.display_results()

main()






class PasswordAuditor:
    def __init__(self, password):
        self.password = password
        

    def check_length(self):
        return len(self.password) >=8
        
    def check_uppercase(self):
        has_upper = any(char.isupper() for char in self.password)

        if has_upper:
            return True
        else:
            return False

    def check_numbers(self):
        return any(char.isdigit() for char in self.password)
                                                                             #PASSWORD AUDITOR
    def check_special(self):
        special_chars = ['!','@','#','$','%','^','&']
        return any(char in special_chars for char in self.password)
    
    def calculate_score(self):
        results =  [
            self.check_length(),
            self.check_numbers(),
            self.check_special(),
            self.check_uppercase()
        ]
        return results.count(True)
        

    def display_rating(self, results):
        if results == 4:
            print("very strong")
        elif results == 3:
            print("strong")
        elif results == 2:
            print("Medium")
        else:
            print("weak")


    def audit(self):
        score = self.calculate_score()
        print(f"score: {score}")
        self.display_rating(score)
        

def main():
    password = input("Enter password: ")
    auditor = PasswordAuditor(password)
    auditor.audit()

main()







































