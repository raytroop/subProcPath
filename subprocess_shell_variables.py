import subprocess

# [Errno 2] No such file or directory: 'echo $HOME': 'echo $HOME'
# completed = subprocess.run('echo $HOME')

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)