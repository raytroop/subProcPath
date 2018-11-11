import os

o_name = [fname for fname in os.listdir('.') if fname.startswith('outter')]
i_name = [os.path.join('subdir', fname) for fname in os.listdir('subdir') if fname.startswith('inner')]

for dir in o_name + i_name:
    if os.path.isdir(dir):
        os.removedirs(dir)
