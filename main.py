from m1_nmap import nmap_scan, extract_ports
from m6_banner import grab_banner
from ai_report import ai_analyze


def write_html(scan_results, banners, ai_result):
    with open("report.html", "w", encoding="utf-8") as f:
        f.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>AI Security Report</title>
</head>
<body>

<h1>AI Destekli Ağ Güvenlik Raporu</h1>

<h2>M1 Port Tarama</h2>
<pre>
""")

        for r in scan_results:
            f.write(f"{r['port']} | {r['service']} | {r['version']}\n")

        f.write("""
</pre>

<h2>M6 Banner Grabbing</h2>
<pre>
""")

        for b in banners:
            f.write(str(b) + "\n")

        f.write("""
</pre>

<h2>AI Analizi</h2>
<pre>
""")

        f.write(str(ai_result))

        f.write("""
</pre>

</body>
</html>
""")


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

    print("\n[+] Banner grabbing...\n")

    banners = []

    for r in scan_results:
        port = r["port"]
        banner = grab_banner(target, port)
        banners.append(banner)
        print(banner)

    print("\n[+] AI Analizi...\n")

    ai_input = "\n".join(
        [f"{r['port']} {r['service']} {r['version']}" for r in scan_results]
        + banners
    )

    ai_result = ai_analyze(ai_input)
    print(ai_result)

    write_html(scan_results, banners, ai_result)

    print("\n[+] report.html oluşturuldu")


if __name__ == "__main__":
    main()
