import subprocess
#command = "ps -A|grep 'chrome'"
list_name = ["nautilus", "chrome", "firefox", "bash", "gnome-system-monitor", "pulseaudio", "cat", "sublime_text"]
for i in list_name:
    ps_name = i
    command = "ps -A|grep {}".format(ps_name)
    process_list = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = process_list.communicate()[0]
    print(output)

#comment
