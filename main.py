from m1_nmap import nmap_scan, extract_ports
from m6_banner import grab_banner
from ai_report import ai_analyze


def write_html(target, scan_results, banners, ai_result):

    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>AI Security Report</title>
    </head>
    <body>
        <h1>AI Security Report</h1>

        <h2>Target</h2>
        <p>{target}</p>

        <h2>Open Ports</h2>
        <table border="1">
        <tr><th>Port</th><th>Service</th><th>Version</th></tr>
    """

    for r in scan_results:
        html += f"<tr><td>{r['port']}</td><td>{r['service']}</td><td>{r['version']}</td></tr>"

    html += "</table><h2>Banners</h2><pre>"

    for p, b in banners.items():
        html += f"{p} -> {b}\n"

    html += "</pre>"

    html += f"<h2>AI Analysis</h2><pre>{ai_result}</pre></body></html>"

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)


def main():

    target = input("Hedef IP gir: ")

    print("\n[+] Nmap taraması başlıyor...\n")

    nm = nmap_scan(target)
    scan_results = extract_ports(nm)

    if not scan_results:
        print("Port bulunamadı")
        return

    print("\n[+] Açık portlar:\n")

    for r in scan_results:
        print(f"{r['port']} | {r['service']} | {r['version']}")

    ports = [r["port"] for r in scan_results]

    print("\n[+] Banner grabbing...\n")

    banners = {}

    for p in ports:
        banners[p] = grab_banner(target, p)
        print(f"{p} -> {banners[p]}")

    scan_text = ""

    for r in scan_results:
        scan_text += f"{r['port']} {r['service']} {r['version']}\n"

    for p, b in banners.items():
        scan_text += f"{p} -> {b}\n"

    print("\n[+] AI Analizi...\n")

    ai_result = ai_analyze(scan_text)

    print(ai_result)

    write_html(target, scan_results, banners, ai_result)

    print("\n[+] report.html oluşturuldu")


if __name__ == "__main__":
    main()
