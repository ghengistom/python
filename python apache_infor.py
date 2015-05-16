'''CPSC 254 - Spring 2015 - Apache Log Analyzer Project

This module is to create generator for apache log info.
'''

import os
import fnmatch
import bz2
import re


def gen_matched_files(top_dir, file_pattern):
    '''Given the top directory path and a file pattern, create a generator
    of all the file paths that are matched with the given file pattern.

    Note:
    - See os.walk function
        https://docs.python.org/3.4/library/os.html#os.walk
    - See filter function of fnmatch module
        https://docs.python.org/3.4/library/fnmatch.html

    Keyword arguments:
    top_dir -- top directory path
    file_pattern -- file pattern

    Yield: matched file
    '''
    # +++your code here+++
    for path, dirs, files in os.walk(top_dir):
        for name in fnmatch.filter(files, file_pattern):
    	    yield os.path.join(path, name)

def gen_file_objects(file_paths):
    '''Given the file path generator, create a generator of all file objects.
    There are 2 types of files: bzip2-compressed files, which has bz2 file
    extension, and other text files. Use appropriate functions to open them.

    Note:
    - See bz2.open function:
        https://docs.python.org/3/library/bz2.html#bz2.open

    Keyword arguments:
    file_paths -- the file path generator

    Yield: file object
    '''
    # +++your code here+++
    for path in file_paths:
        if path.endswith('.txt'): yield txt.open(path)
        elif path.endswith('.bz2'): yield bz2.open(path)
        else: yield open(file_paths)
       

def gen_lines(file_objects):
    '''Given the file object generator, create a generator of all lines.

    Keyword arguments:
    file_objects -- file object generator

    Yield: line from a file object
    '''
    # +++ your code here+++
	
    """(generator) to read a file piece by piece.
    Default size: 1k."""
    while True:
        lines = file_object.read(file_size)
        if not data:
            break
        yield lines


    f = open('access_log')
    for piece in read_in_chunks(f):
        process_data(piece)

def gen_log_infos(lines):
    '''Given the line generator, create a generator of a dictionary of info
    in each line of apache log. Here's what each line of apache log looks
    like in the access.log file:

    cys-cap-9.wyoming.com - - [31/Aug/1995:23:55:51 -0400] "GET /shuttle/missions/sts-71/movies/sts-71-launch-3.mpg HTTP/1.0" 200 49152
    tia1.eskimo.com - - [31/Aug/1995:23:55:53 -0400] "GET /software/winvn/wvsmall.gif HTTP/1.0" 200 13372
    ...

    The return info should be like below:
    {
        'host'    : 'cys-cap-9.wyoming.com',
        'referrer': '-',
        'user'    : '-',
        'datetime': '31/Aug/1995:23:55:51 -0400',
        'method'  : '',
        'request' : '',
        'protocol': '',
        'status'  : '200',
        'size'    : 49152
    }

    Note:
     - size: If no bytes are sent, it shows '-' instead of 0. You need to
             check that and convert to integer.

    Keyword arguments:

    Yield: Log info dictionary
    '''
    # +++your code here+++


def apache_log_infos(top_dir, file_pattern):
    '''Given the top directory and file pattern, return the generator object
    of the apache log info dictionaries. You should combine from all other
    generators (gen_matched_files, gen_file_objects, gen_lines, gen_log_infos)
    in this function so that we can use this generator object to create report.

    Keyword arguments:
    top_dir -- path of top directory to search
    file_pattern -- pattern of filename

    Return: generator object of info dictionaries
    '''
    # +++your code here+++
