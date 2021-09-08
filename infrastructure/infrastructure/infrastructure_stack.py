from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
    aws_s3_deployment as deployment
)


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class InfrastructureStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        #code for s3 bucket.
        bucket= s3.Bucket(self, id='s3bucket02', bucket_name='my-profile-application-py',
            website_index_document= "index.html",
            public_read_access= True
        )

        deployment.BucketDeployment(self, 'my-profile-bucket-deployment-py', sources= [deployment.Source.asset("../website")],
        destination_bucket= bucket)

        #, {
           # public_read_access: true,
        #    removal_policy:core.RemovalPolicy.DESTROY,
         #   website_index_document: "../website/index.html"
        #}
