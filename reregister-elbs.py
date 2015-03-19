#!/usr/bin/python
# reregister current instances to elbs
import sys
import time
import boto
import boto.ec2

region = '<your-region-here>'

def reregister_instances_to_elbs():
    global elb_names

    elb_conn = boto.ec2.elb.connect_to_region(region)
    elbs = elb_conn.get_all_load_balancers(elb_names);

    for elb in elbs:
        print elb.name
        print elb.instances
        for instance in elb.instances:
            #TODO make this into a single call with all instance ids and forgo the inner loop
            elb_conn.deregister_instances(elb.name, [instance.id])
            elb_conn.register_instances(elb.name, [instance.id])
            time.sleep(1); #to avoid elb rate limit throttling

def main(argv):
    global elb_names

    elb_names = argv[0].split()
    reregister_instances_to_elbs()

if __name__ == "__main__":
    main(sys.argv[1:])

