import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))

        banner = s.recv(1024).decode(errors="ignore")
        s.close()

        return f"{port} -> {banner}"

    except:
        return f"{port} -> No banner"

