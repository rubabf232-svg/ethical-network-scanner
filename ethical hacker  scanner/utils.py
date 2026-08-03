import socket


def resolve_hostname(ip):

    try:
        return socket.gethostbyaddr(ip)[0]

    except:
        return "Unknown"


def banner():

    print("=" * 60)
    print("        ETHICAL NETWORK SCANNER")
    print("=" * 60)
    