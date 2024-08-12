import paramiko

def try_login(username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect("127.0.0.1", username=username, password=password)  # Replace with your target IP
        return True
    except paramiko.AuthenticationException:
        return False
    finally:
        ssh.close()
