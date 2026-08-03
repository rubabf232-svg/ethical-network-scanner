

import nmap


class PortScanner:

    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan(self, target, port_range="1-1000"):

        print(f"\n[*] Scanning Ports on {target}...")

        self.scanner.scan(
            hosts=target,
            ports=port_range,
            arguments="-sV"
        )

        results = []

        if target in self.scanner.all_hosts():

            for protocol in self.scanner[target].all_protocols():

                ports = self.scanner[target][protocol].keys()

                for port in sorted(ports):

                    service = self.scanner[target][protocol][port]

                    if service["state"] == "open":

                        info = {
                            "port": port,
                            "protocol": protocol,
                            "service": service["name"],
                            "version": service.get("version", "Unknown"),
                            "product": service.get("product", "Unknown")
                        }

                        results.append(info)

                        print(
                            f"[+] {port}/{protocol} | "
                            f"{service['name']} | "
                            f"{service.get('product','')} "
                            f"{service.get('version','')}"
                        )

        return results