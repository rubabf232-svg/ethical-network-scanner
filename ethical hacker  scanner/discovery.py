import nmap


class HostDiscovery:

    def __init__(self):
        self.scanner = nmap.PortScanner()

    def discover(self, network):

        print(f"\n[*] Discovering hosts on {network}...\n")

        self.scanner.scan(
            hosts=network,
            arguments="-sn"
        )

        hosts = []

        for host in self.scanner.all_hosts():

            if self.scanner[host].state() == "up":

                print(f"[+] Host Found : {host}")

                hosts.append(host)

        return hosts