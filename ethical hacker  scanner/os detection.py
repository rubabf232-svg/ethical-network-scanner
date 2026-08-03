
import nmap


class OSDetection:

    def __init__(self):
        self.scanner = nmap.PortScanner()

    def detect(self, target):

        print(f"\n[*] Detecting Operating System of {target}")

        try:

            self.scanner.scan(
                hosts=target,
                arguments="-O"
            )

            if target in self.scanner.all_hosts():

                if "osmatch" in self.scanner[target]:

                    matches = self.scanner[target]["osmatch"]

                    if matches:

                        os_name = matches[0]["name"]

                        print(f"[+] OS : {os_name}")

                        return os_name

        except Exception:

            print("[-] OS Detection Failed")

        return "Unknown"