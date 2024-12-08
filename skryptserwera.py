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
            try:
                # Wprowadzenie komendy
                command = input(">> ")
                if command.lower() == "exit":
                    conn.send(b"exit")
                    break

                # Wysłanie komendy
                conn.send(command.encode("utf-8"))

                # Odbieranie odpowiedzi
                response = conn.recv(4096).decode("utf-8")
                print(response)
            except Exception as e:
                print(f"Błąd w trakcie komunikacji: {e}")
                break
    except Exception as e:
        print(f"Ogólny błąd serwera: {e}")
    finally:
        sock.close()
        print("Serwer został zamknięty.")

# Zmień adres ip i port na odpowiednie
start_server("0.0.0.0", 4444)
