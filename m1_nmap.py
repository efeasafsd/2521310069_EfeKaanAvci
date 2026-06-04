import nmap

def nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments="-Pn -sT -sV -p 1-1000")
    return nm


def extract_ports(nm):
    results = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                data = nm[host][proto][port]

                if data.get("state") == "open":
                    results.append({
                        "port": port,
                        "service": data.get("name", "unknown"),
                        "version": data.get("version", "unknown")
                    })

    return results
