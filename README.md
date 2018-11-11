##### 1. path in Python is always relative to cwd, `cwd` parameter of `subprocess.check_call` can explicitly change `cwd`.

```bash
localhost:~/subProcPath$ tree
.
├── init_op.py
├── main.py
├── outter14:35:14.637519
└── subdir
    ├── inner14:35:14.652851
    └── sub.py

localhost:~/subProcPath$ python init_op.py
localhost:~/subProcPath$ tree
.
├── init_op.py
├── main.py
└── subdir
    └── sub.py

localhost:~/subProcPath$ python main.py
~/subProcPath
~/subProcPath/subdir

localhost:~/subProcPath$ tree
.
├── init_op.py
├── main.py
├── outter14:35:35.084011
└── subdir
    ├── inner14:35:35.101082
    └── sub.py
```
<br>

##### 2. `subprocess.run`
- `shell` argument
  - Setting the `shell` argument to a **true** value causes subprocess to spawn *an intermediate shell proces**, which then runs the command. *The default is to run the command directly.*
  - Using *an intermediate shell* means that variables, glob patterns, and other special shell features in the command string are **processed before the command is run**.

The below example:
```python
completed = subprocess.run('echo $HOME')
```
will raise `[Errno 2] No such file or directory: 'echo $HOME': 'echo $HOME'`

To alleviate this problem:
```python
completed = subprocess.run('echo $HOME', shell=True)
```
In this way, `$HOME` will be replaced with real path.
<br>

- `check`
  - Passing `check=True` to `run()` makes it equivalent to using `check_call()`
  - Using `run()` without passing `check=True` is equivalent to using `call()`, which returns only the exit code from the process.

If the `check` argument to `run()` is **True**, the exit code is checked. If it indicates an error happened, then a `CalledProcessError` exception is raised.

The below example:
```python
import subprocess

try:
    completed = subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)

print('END')
```
The `false` command always exits with a **non-zero** status code
1. `check=True`: `subprocess.CalledProcessError` is raised. `completed` is not defined. `completed` is available only if no exception is available.
2. `check=False`: no exception will be raised but `completed` is available.

<br>
##### credts:
- The Python 3 Standard Library by Example