import socket

def start_server(server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((server_ip, server_port))
        sock.listen(1)
        print(f"Nasłuch na {server_ip}:{server_port}")

        conn, addr = sock.accept()
        print(f"Połączono z {addr}")

        while True:
            command = input(">> ")
            if command.lower() == "exit":
                conn.send(b"exit")
                break

            conn.send(command.encode("utf-8"))
            response = conn.recv(1024).decode("utf-8")
            print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

# Zmień IP i port na odpowiednie
start_server("0.0.0.0", 4444)
