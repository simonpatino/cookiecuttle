import subprocess

print("Just wait a minute")

subprocess.call(["git","init"])
subprocess.call(["git","add","*"])
subprocess.call(["git","commit","-am","Initial commit"])


print("you are ready to program")

print("bye world ")