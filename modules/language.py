from nltk.tokenize import word_tokenize

class LanguageModule:
    def __init__(self):
        self.intent_dictionary = {
            "password_management": ["password"],
            "network_security_monitoring": ["network", "security", "monitor", "intrusion"],
            "encryption_decryption": ["encrypt", "decrypt", "cipher", "secret"],
            "intrusion_detection": ["intrusion", "detect", "alert", "anomaly"],
            "siem_operations": ["siem", "analyze", "event", "log"],
            "honeypot_analysis": ["honeypot", "analyze", "capture", "malicious"],
            "digital_forensics": ["forensics", "investigate", "evidence", "analyze"],
            "security_analysis": ["security", "analyze", "assessment", "risk"],
            "reporting_and_visualization": ["report", "visualize", "graph", "dashboard"],
            "automation": ["automate", "task", "routine", "script"]
        }

    def load_resources(self):
        pass

    def tokenize_query(self, query):
        tokens = word_tokenize(query.lower())
        return tokens

    def determine_intent(self, query):
        tokens = self.tokenize_query(query)

        for intent, keywords in self.intent_dictionary.items():
            if all(token in tokens for token in keywords):
                return intent

        return None  # Return None if no matching intent is found
