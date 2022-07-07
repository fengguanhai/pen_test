import socket

def get_ips_for_host(host):
    try:
        ips = socket.gethostbyname(host)
    except socket.gaierror:
        ips = []
    return ips



if __name__ == '__main__':
    ip = get_ips_for_host('113.98.245.218:8181/coolead')
    print(ip)