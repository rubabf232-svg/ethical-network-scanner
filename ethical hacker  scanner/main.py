from scanner import EthicalNetworkScanner

def main():
    print("=" * 60)
    print("      ETHICAL NETWORK SCANNER")
    print("=" * 60)

    print("\nThis tool is for AUTHORIZED security testing only.\n")

    consent = input("Do you have authorization to scan this network? (yes/no): ")

    if consent.lower() != "yes":
        print("\nUnauthorized scanning is illegal.")
        return

    target = input("\nEnter Target Network (Example: 192.168.1.0/24): ")

    scanner = EthicalNetworkScanner()
    scanner.run(target)


if __name__ == "__main__":
    main()