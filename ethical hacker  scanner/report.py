import json
from datetime import datetime


class Report:

    def save(self, results):

        report = {
            "scan_time": str(datetime.now()),
            "results": results
        }

        with open("scan_report.json", "w") as file:

            json.dump(report, file, indent=4)

        print("\n[+] Report Saved Successfully")