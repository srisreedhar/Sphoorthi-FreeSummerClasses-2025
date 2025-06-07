Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
numbers = [1,2,3,4,5,6,7,8,9]

newlist=[]

for everynumber in numbers:
    t = everynumber + 100
    newlist.append(t)

    
newlist
[101, 102, 103, 104, 105, 106, 107, 108, 109]


[everynumber + 100 for everynumber in numbers]
[101, 102, 103, 104, 105, 106, 107, 108, 109]

import sys
sys.sizeof()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sys.sizeof()
AttributeError: module 'sys' has no attribute 'sizeof'. Did you mean: 'getsizeof'?
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_vpath', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> 
>>> 
>>> 
>>> sys.getsizeof(numbers)
136

numbers1000=list(range(1:10001))
SyntaxError: invalid syntax

numbers1000=list(range(1,10001))

len(numbers1000)
10000


sys.getsizeof(numbers1000)
80056


range(1,10001)
range(1, 10001)

len(range(1,10001))
10000

sys.getsizeof(range(1,10001))
48

for i in 1234:
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for i in 1234:
TypeError: 'int' object is not iterable



s = lambda x:x in numbers


s = lambda x:x.upper()

s('sri')
'SRI'

numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]


map(str,numbers)
<map object at 0x00000141507B23B0>

list(map(str,numbers))
['1', '2', '3', '4', '5', '6', '7', '8', '9']


list(map(lambda x:x+100,numbers))
[101, 102, 103, 104, 105, 106, 107, 108, 109]


def add100(n):
    return n+100

add100(100)
200


