import boto3

def list_eips():
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        print(f"Scanning region: {region}")
        ec2 = boto3.client('ec2', region_name=region)

        try:
            addresses = ec2.describe_addresses()['Addresses']
            if not addresses:
                print(f"No EIPs found in region {region}")
                continue

            for address in addresses:
                eip = address.get('PublicIp', 'N/A')
                instance_id = address.get('InstanceId', 'N/A')
                print(f"EIP: {eip} is associated with Instance: {instance_id} in region {region}")

        except Exception as e:
            print(f"Error in region {region}: {e}")

if __name__ == "__main__":
    list_eips()