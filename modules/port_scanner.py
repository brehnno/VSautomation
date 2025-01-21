import socket

def scan_ports(target):
    open_ports = []
    try:
        # Verificar se target já é um IP ou domínio
        if target.startswith("http://") or target.startswith("https://"):
            target = target.split("//")[1]  # Remove o http:// ou https://
        socket.gethostbyname(target)  # Resolva o endereço IP antes de escanear portas
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Timeout para conexões lentas
                result = sock.connect_ex((target, port))
                if result == 0:  # Porta aberta
                    open_ports.append(port)
    except socket.gaierror:
        print(f"Erro: Não foi possível resolver o endereço '{target}'. Verifique o IP ou domínio fornecido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return open_ports
