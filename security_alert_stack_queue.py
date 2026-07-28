
class SecurityStack:
    def __init__(self):
        self.alert = []

    def push(self, alert):
        self.alert.append(alert)

    def pop(self):
        if not self.alert:
            print("No Alerts")
            return None
        return self.alert.pop()

    def peek(self):
        if not self.alert:
            print("empty")
            return None
        return self.alert[-1]
    
    def is_emtpy(self):
        return len(self.alert) == 0

    def display(self):
        print(self.alert)

def main():
    stack = SecurityStack()
    stack.push("SQL injection")
    stack.push("Brute force attack on port 22")
    stack.push("Suspicious IP: 192.168.1.105")
    stack.display()
    print(stack.peek())
    print(stack.pop())
    stack.display()

main()








class SecurityQueue:
    def __init__(self):
        self.task = []

    def enqueue(self, task):
        self.task.append(task)

    def dequeue(self):
        if not self.task:
            print("Empty")
            return None
        return self.task.pop(0)
    
    def peek(self):
        if not self.task:
            print("Empty")
            return None
        return self.task[-0]
    
    def is_empty(self):
        return len(self.task) == 0
    
    def display(self):
        print(self.task)

def main():
    task = SecurityQueue()
    task.enqueue("Scan network for vulnerabilities")
    task.enqueue("Patch firewall rules")
    task.enqueue("Investigate suspicious login attempt")
    task.enqueue("Update antivirus signatures")
    task.display()
    print(task.peek())
    print(task.dequeue())
    task.display()

main()




