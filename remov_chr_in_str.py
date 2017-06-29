#!/usr/bin/env python


cmd = "0x02 0x13 0x44 0x55"

# cmd_nop = cmd.rstrip(' ')
# cmd_nop = cmd.strip()
# cmd_nop = cmd.strip().lstrip().rstrip('0x')

cmd = cmd.replace(' ','')
cmd = cmd.replace('0x','')



print cmd
