import nmap

def nmap_scan(target):
    nm = nmap.PortScanner()

    
    nm.scan(hosts=target, arguments="-Pn -sT -p 1-1000")

    return nm


def extract_ports(nm):

    results = []

    for host in nm.all_hosts():

        for proto in nm[host].all_protocols():

            ports = nm[host][proto].keys()

            for port in ports:

                state = nm[host][proto][port].get("state", "")

                if state == "open":

                    results.append({
                        "port": port,
                        "service": nm[host][proto][port].get("name", "unknown"),
                        "version": nm[host][proto][port].get("version", "unknown")
                    })

    return results
