
from aws_cdk import (    
    aws_ec2 as ec2,           
    core as cdk
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkImageLookupPyStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        # filter = { 'description': ['*AdditionalSoftware=Vanilla'] }
        
        # filter = { 'root-device-type': ['*ebs*'] }
        
        filter = { 'description': ['*ClouEndureWorkshop-webserver'] }
        # filter = { 'description': ['02h-ClouEndureWorkshop-webserver'] }
        # filter = { 'description': ['*-ClouEndureWorkshop-webserver'] }
        
        # image = ec2.MachineImage.lookup(name='*CentOS*', filters=filter)
        
        image = ec2.MachineImage.lookup(name='*webserver', filters=filter)
        
        default_vpc = ec2.Vpc.from_lookup(self, 'default-vpc', is_default=True)
        
        ec2_instance = ec2.Instance(self, "EC2",                                
                                machine_image=image,
                                vpc=default_vpc,
                                instance_name='Bastion Host',
                                instance_type=ec2.InstanceType(instance_type_identifier='t3.micro')
                                )