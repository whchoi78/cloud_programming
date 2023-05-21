# boto3-stubs boto3라이브러리를 힌트를 준다.

import boto3
from pprint import pprint 

'''
client = boto3.client('sts')
response = client.get_caller_identity()
#print(response["UserId"], response["Account"], response['Arn'])

if "root" in response["Arn"] :
    print("root 계정 입니다.")
else :
    print("iam 계정 입니다.")    
'''    
#client = boto3.client('iam')    
#username = "rex"
'''
try:
    response = client.create_user(
        UserName=Username,
        Tags=[
            {
                'Key': 'Name',
                'Value': 'test'
            },
        ]
    )
except client.exceptions.EntityAlreadyExistsException:
    print("사용자가 이미 존재 합니다.".format(Username))
else:        
    pprint(response)   

try:    
    response = client.delete_user(
        UserName=Username
    )    
except client.exceptions.NoSuchEntityException:
    print("{} 사용자가 존재 하지 않습니다.".format(Username))
else:
    print(f"{Username} 사용자가 정상적으로 삭제되었습니다.")        
    '''
 
client = boto3.client('iam')    
username = "rex"
    
def del_user(client, username):
    if not username:
        raise Exception(f"{username}이 존재하지 않습니다.")
    try:
        client.delete_user(UserName=username)
    except client.exceptions.NoSuchEntityException:
        return True, None
    except Exception as e:
        print(e)
        
print(del_user(client, username))        