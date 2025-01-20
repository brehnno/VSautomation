import socket

def scan_ports(target):
    open_ports = []
    try:
        # Resolva o endereço IP antes de escanear portas
        socket.gethostbyname(target)  
        for port in range(1, 1025):  # Escaneando as primeiras 1024 portas
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
