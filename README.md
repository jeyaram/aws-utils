# aws-utils
AWS Utilities

* reregister-instances-to-elbs.py

ELBs treat instances as stopped even after starting them. This scripts reregisters the instances back to ELBs by deregistering & registering. The scripts uses boto aws library and requires list of ELBs as a parameter enclosed with double quotes and separated by space.

```
reregister-instances-to-elbs.py "elb-name-1 elb-name-2"
```
