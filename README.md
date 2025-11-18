Learning Python

Python is a programming language that lets you work quickly and integrate systems more effectively.

Benefits:
- Easy to use
- Quick learning
- Dynamic type(based on value)
- Great documentation and community

Installation

1 - Download and extract the tar.gz file from https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tar.xz

2 - Go to extracted folder
```
cd Python-3.14.0
```
3 - Open the terminal and run the following command to install dependencies
```
sudo pacman -S base-devel gdb lcov pkg-config \
      bzip2 libffi gdbm  xz \
      ncurses readline sqlite openssl \
      tk haskell-uuid zlib mpdecimal zstd \
      inetutils
```
4 - Execute the configure command
```
sudo ./configure
```
5 - Perform the compilation process
```
sudo make -j "$(nproc)"
```
6 - Install python using make(choice one of them)
```
sudo make altinstall # Keep the python current version from SO and install new version
sudo make install # Overrides the python current version from SO to new version
```
7 - Check python path
```
which python3.14
```
8 - Verify if python is working fine
```
cat > hello_world.py << EOF
print("Hello World!!!")
EOF
python3.14 hello_world.py
```
9 - Install module using pip
```
python3.14 -m pip install module_name
python3.14 -m pip install pandas
```

10 - Install ipython(Python interpreter with more features)
```
python3.14 -m pip install ipython
```

11 - Open a new terminal and type ipython

Features:

F-Strings:Formatted string literals (also called f-strings for short) let you include the value of Python expressions 
inside a string by prefixing the string with f or F and writing expressions as {expression}.

IDEs: 

VSCode and Pycharm

References:

https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
https://docs.python.org/3/reference/lexical_analysis.html#f-strings
