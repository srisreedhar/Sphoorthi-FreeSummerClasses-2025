Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
0*2
0
0+2
2

"IN12345678"[0]
'I'
"IN12345678"[1]
'N'
"IN12345678"[0]
'I'


"IN12345678"[0:1]
'I'
"IN12345678"[0:2]
'IN'

"Indexing"[0:2]
'In'
"Indexing"[0:3]
'Ind'

"Indexing"[::-1]
'gnixednI'




import os

dir(os)
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']


os.getcwd()
'C:\\Users\\srisreedhar\\AppData\\Local\\Programs\\Python\\Python311'

os.chdir("D:\SphoorthiFreeClasses\python")

os.getcwd()
'D:\\SphoorthiFreeClasses\\python'


os.listdir("D:\SphoorthiFreeClasses\python")
['And-OR-Operators-ClassWorkout.py', 'average_v2.py', 'average_v3.py', 'average_v4.py', 'average_v5.py', 'collect-store-list.py', 'collect-store-list_v2.py', 'divisible-by.py', 'divisibleby.py', 'if-condition-classworkout.py', 'if_even_odd_num.py', 'interview_v1.py', 'Loops-Counter-TextProcessing-IF-ELIF.py', 'Loops_classWorkout.py', 'Loops_Stringmethods_classWorkout.py', 'nested-if-example.py', 'textprocessing.py', 'typecasting-dir-len-strings-classworkout.py']

os.mkdir("thisisatestfoldericreatednow")
os.listdir("D:\SphoorthiFreeClasses\python")
['And-OR-Operators-ClassWorkout.py', 'average_v2.py', 'average_v3.py', 'average_v4.py', 'average_v5.py', 'collect-store-list.py', 'collect-store-list_v2.py', 'divisible-by.py', 'divisibleby.py', 'if-condition-classworkout.py', 'if_even_odd_num.py', 'interview_v1.py', 'Loops-Counter-TextProcessing-IF-ELIF.py', 'Loops_classWorkout.py', 'Loops_Stringmethods_classWorkout.py', 'nested-if-example.py', 'textprocessing.py', 'thisisatestfoldericreatednow', 'typecasting-dir-len-strings-classworkout.py']
>>> os.chdir("DD:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    os.chdir("DD:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'DD:\\SphoorthiFreeClasses\\python\thisisatestfoldericreatednow'
>>> 
>>> os.chdir("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    os.chdir("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'D:\\SphoorthiFreeClasses\\python\thisisatestfoldericreatednow'
>>> 
>>> 
>>> os.chdir("D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow")
"\n"
'\n'
"\t"
'\t'

os.chdir(r"D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow")

os.getcwd()
'D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow'


# import json

d={}
d.loads()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d.loads()
AttributeError: 'dict' object has no attribute 'loads'
