import base64
import paramiko
key = paramiko.RSAKey(data=base64.b64decode(b'AAAAB3NzaC1yc2EAAAADAQABAAABAQChoyB79zANe/V798+DPFZpElO6uAM6EQzIsDaLUtjZVXsYzrW41iB6dY+xOlvbIIZElczwKzYFXiOPsefzLvsrMBKJp+fEdlpQQhUGDBWNkLHm7/swDpa6wHy1ncG6A6qAEu1DGfYqdNZAhPgGpLiwa9ECKL3xCARA+PDhyGfwM1Ig3RmNQvXLI3QkjYI4y26iMLce/C64kllzNN2eV3omDj/uhk9bZ76V6nraTF7367SIW52WpRuQylCNtIP5v3FJU8ea59QkzvGqLQUgUgAs/HMmS2j4SjDzQAfloQNhdhxEYn5JxB4qXZfnWqu4bG7xVvux/uPNH/R8UaXYIAnD'))
client = paramiko.SSHClient()
client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
client.load_system_host_keys()
client.connect('192.168.0.92', port=22118, username='', password='')
stdin, stdout, stderr = client.exec_command('cd ~/Programms ; ls')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()