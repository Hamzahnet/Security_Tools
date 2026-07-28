#soc alert triage system

class AlertSystems:
    def __init__(self):
        self.alerts = {}                                   #empty  dictionary
        self.nextID = 1                                     # set id value for alerts

    def addAlert(self, description, severity):
        self.alerts[self.nextID]= {  
            "id" : self.nextID,
            "description" : description,                  #dictionary 
            "severity" : severity,
            "status" : "open",
        }
        self.nextID += 1                                 #iterated the value of id for every alert added

    def viewAlerts(self):
        for alert in self.alerts.values():                  #method that allows us to view details of the alerts
            if alert["status"] == "open":                 
                print(f"ID: {alert['id']} | {alert['severity'].upper()} | {alert['description']} | {alert['status']}")

    def closealert(self, alert_id):
        if alert_id in self.alerts:
            self.alerts[alert_id]["status"] =  "closed"         #method to set an alert from open to closed status
            print(f"Alert {alert_id} closed")
        else:
            print("Alert not found")

    def get_critical(self):
        for alert in self.alerts.values():                   #implimentation of triage to show critical alerts
            if alert["severity"] == "critical": 
                print(f"ID: {alert['id']} | {alert['severity'].upper()} | {alert['description']} | {alert['status']}")


def main():
    system = AlertSystems()
    system.addAlert("Suspicious login attempt on port 22", "critical")
    system.addAlert("Failed password attempts from 192.168.1.105", "high")
    system.addAlert("Port scan detected from unknown IP", "medium")
    system.viewAlerts()
    system.addAlert("Disk space low on server", "low")
    system.addAlert("Malware detected on endpoint", "critical")
    system.closealert(4)
    system.viewAlerts()
    system.get_critical()
    system.viewAlerts()
main()