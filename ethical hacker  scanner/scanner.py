from report import ReportGenerator
from utils import resolve_hostname
import nmap
import json


class EthicalNetworkScanner:

    def __init__(self):
        self.results = {}

    def discover_hosts(self, network):

        print("\n[*] Discovering Hosts...")

        scanner = nmap.PortScanner()

        scanner.scan(hosts=network, arguments="-sn")

        hosts = []

        for host in scanner.all_hosts():

            if scanner[host].state() == "up":

                hosts.append(host)

        return hosts

    def scan_ports(self, host):

        print(f"\n[*] Scanning {host}")

        scanner = nmap.PortScanner()

        scanner.scan(host, "1-1000", arguments="-sV")

        ports = []

        if host in scanner.all_hosts():

            for protocol in scanner[host].all_protocols():

                for port in scanner[host][protocol]:

                    service = scanner[host][protocol][port]

                    if service["state"] == "open":

                        ports.append({
                            "port": port,
                            "protocol": protocol,
                            "service": service["name"]
                        })

                        print(
                            f"  {port}/{protocol}  {service['name']}"
                        )

        self.results[host] = ports

    def save_report(self):

        with open("scan_report.json", "w") as file:

            json.dump(self.results, file, indent=4)

        print("\nReport Saved -> scan_report.json")

    def run(self, network):

        hosts = self.discover_hosts(network)

        print(f"\nFound {len(hosts)} Active Hosts\n")

        for host in hosts:

            self.scan_ports(host)

        self.save_report()