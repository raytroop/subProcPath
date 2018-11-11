import subprocess

cwd = '.'   # default
cmd = 'python subdir/sub.py outter'
subprocess.check_call(cmd, cwd=cwd, shell=True)

# explicitly change current working directory
cwd="subdir"
cmd = 'python sub.py inner'
subprocess.check_call(cmd, cwd=cwd, shell=True)
