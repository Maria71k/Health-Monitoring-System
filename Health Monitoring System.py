class HealthMonitor:
    def __init__(self):
        self.vital_signs = {}

    def record_vital_signs(self, date, vital_signs):
        self.vital_signs[date] = vital_signs

    def view_vital_signs(self, date):
        return self.vital_signs.get(date, "No data available")

# Example usage:
monitor = HealthMonitor()
monitor.record_vital_signs("2024-02-10", {"Heart rate": 75, "Blood pressure": "120/80"})
print(monitor.view_vital_signs("2024-02-10"))
