class ThreatTracker:
    
    def __init__(self):
        self.threat = {}
        
    def add_threats(self,ip,threat_type):
        self.threat[ip] = threat_type
        print(f"Threat added: {ip} - {threat_type}")

    def get_threats(self, ip):
        if ip in self.threat:
            print(f"threat found: {ip} - {self.threat[ip]}")
        else:
            print("no threat discovered for ip")

    def remv_threat(self,ip):
        if ip in self.threat:
            del self.threat[ip]
            print(f"{ip} has been removed")
        else:
            print("ip not found")
        
    def is_known(self, ip):
        if ip in self.threat:
            return(True)
        else:
            return (False)
        
    def display(self):
        for ip, threat_type in self.threat.items():
            print(f"{ip}: {threat_type}")

def main():
    tracker = ThreatTracker()
    tracker.add_threats("192.168.1.1", "SQL Injection")
    tracker.add_threats("10.0.0.5", "Brute Force")
    tracker.add_threats("172.16.0.3", "Port Scan")
    tracker.add_threats("192.168.1.105", "Malware")
  
    tracker.display()
    print(tracker.is_known("10.0.0.5"))
    tracker.get_threats("172.16.0.3")
    tracker.remv_threat("10.0.0.5")
    tracker.display()
main()