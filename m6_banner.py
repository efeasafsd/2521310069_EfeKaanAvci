import socket

def grab_banner(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024).decode(errors="ignore")
        s.close()
        return banner if banner else "No banner"
    except:
        return "No banner"
