import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Program arguments')
parser.add_argument('--from', 
                dest = 'file_from', 
                default = 0,
                help = 'File with original content')
parser.add_argument('--to', 
                dest = 'file_to', 
                default = 0,
                help = 'Target file')
parser.add_argument('--arr', 
                dest = 'array_name', 
                default = 0,
                help = 'Array name')
parser.add_argument('--def', 
                dest = 'define_name', 
                default = 0,
                help = 'Define name')
parser.add_argument('--end', 
                dest = 'end', 
                default = 'LF',
                help = 'String end')
args = parser.parse_args()

# Check arguments
if 0 == args.file_from:
    print("File with original content are neccesary to descript")
    sys.exit(0)
if 0 != args.array_name and 0 != args.define_name:
    print("Choose array or define, not both")
    sys.exit(0)
if 'CRLF' != args.end and 'crlf' != args.end and 'LF' != args.end and 'lf' != args.end:
    print("Invalid string end")
    sys.exit(0)

if 0 == args.file_to:
    args.file_to = args.file_from
    print("Target file are same as original")

file_from = open(args.file_from, 'r')
content_from = file_from.readlines()
file_from.close()

# Remove all CR and LF symbols
for i in range(0, len(content_from)):
        while '\r' == content_from[i][-1] or '\n' == content_from[i][-1]:
            content_from[i] = content_from[i][:-1]

# Add array/define identifier
content_to = []
if 0 != args.array_name:
    array_size = 0
    for i in range(0, len(content_from)):
        array_size += len(content_from[i])
    array_size += len(content_from)
    if 'CRLF' == args.end or 'crlf' == args.end:
        array_size += len(content_from)

    content_to += 'const char ' + args.array_name + f'[{array_size + 1}]' + ' = \n{\n'
elif 0 != args.define_name:
    content_to += '#define ' + args.define_name + ' \\\n'

# Bing strings
for i in range(0, len(content_from)):
    content_from[i] = '"' + content_from[i]

    if 'LF' == args.end or 'lf' == args.end:
        content_from[i] += '\\n'
    elif 'CRLF' == args.end or 'crlf' == args.end:
        content_from[i] += '\\r\\n'

    content_from[i] += '"'

    if 0 != args.array_name:
        content_from[i] = '    ' + content_from[i]
    elif 0 != args.define_name:
        content_from[i] = '    ' + content_from[i]
        if (len(content_from) - 1) > i:
            content_from[i] = content_from[i] + ' \\'

    content_from[i] += '\n'
    content_to += content_from[i]

# Add ending brace for array
if 0 != args.array_name:
    content_to += '};'

file_to = open(args.file_to, 'w')
file_to.writelines(content_to)
file_to.close()
