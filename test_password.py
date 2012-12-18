#!/usr/bin/python
#
#(c) Ramki (ramki_b@acm.org), all rights reserved.
#License: Apache Software License, leave this notice intact.
#
def  get_from_password_file():
    f=open('/etc/passwd')
    output = []
    for line in f.xreadlines():
        line = line.rstrip()
        fields = line.split(":")
        output.append([ fields[0], "\t", fields[-1]])
    return output

def test_password():
  values = get_from_password_file()
  for entry in values:
    assert(len(entry) == 3)
    assert(entry[1] == '\t')

def main():
  values = get_from_password_file()
  for entry in values:
    print ''.join(entry)

if __name__ == "__main__":
    main()
