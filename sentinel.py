from modules.language import LanguageModule
from modules.detection import IntrusionDetectionSystem
from modules.analysis import SecurityAnalyzer
from modules.automation import AutomationModule
from modules.encryption import EncryptionDecryptionTool
from modules.honeypot import HoneypotAnalyzer
from modules.network import NetworkSecurityMonitor
from modules.password import PasswordManager
from modules.reporting import ReportingModule
from modules.forensics import DigitalForensicsTool
from modules.system import SIEMSystem


class SentinelPrime:
    def __init__(self):
        self.language_module = LanguageModule()
        self.password_manager = PasswordManager()
        self.network_monitor = NetworkSecurityMonitor()
        self.encryption_tool = EncryptionDecryptionTool()
        self.ids_system = IntrusionDetectionSystem()
        self.siem_system = SIEMSystem()
        self.honeypot_analyzer = HoneypotAnalyzer()
        self.forensics_tool = DigitalForensicsTool()
        self.security_analyzer = SecurityAnalyzer()
        self.reporting_module = ReportingModule()
        self.automation_module = AutomationModule()

    def start(self):
        print("Initializing SentinelPrime Cyber AI...")
        self.language_module.load_resources()
        print("SentinelPrime is ready for operation.")

    def process_query(self, query):
        # Process user query and invoke appropriate module
        intent = self.language_module.determine_intent(query)

        if intent == "password_management":
            response = self.password_manager.process_query(query)
        elif intent == "network_security_monitoring":
            response = self.network_monitor.process_query(query)
        elif intent == "encryption_decryption":
            response = self.encryption_tool.process_query(query)
        elif intent == "intrusion_detection":
            response = self.ids_system.process_query(query)
        elif intent == "siem_operations":
            response = self.siem_system.process_query(query)
        elif intent == "honeypot_analysis":
            response = self.honeypot_analyzer.process_query(query)
        elif intent == "digital_forensics":
            response = self.forensics_tool.process_query(query)
        elif intent == "security_analysis":
            response = self.security_analyzer.process_query(query)
        elif intent == "reporting_and_visualization":
            response = self.reporting_module.process_query(query)
        elif intent == "automation":
            response = self.automation_module.process_query(query)
        else:
            response = "I'm sorry, I didn't understand that request."

        return response


# Main entry point
if __name__ == "__main__":
    sentinel = SentinelPrime()
    sentinel.start()

    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = sentinel.process_query(user_input)
        print("SentinelPrime:", response)

