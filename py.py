import subprocess
command = "ps -A|grep 'chrome'"
process_list = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = process_list.communicate()[0]
print(output)

#comment