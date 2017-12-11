import boto3

ACCESS_KEY_ID = 'AKIAJZHAPZRIRTBEQU4A'
ACCESS_SECRET_KEY = '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'
REGION_NAME = 'us-east-1'

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = ACCESS_KEY_ID,
                          aws_secret_access_key = ACCESS_SECRET_KEY,
                          region_name = REGION_NAME)

table = dynamodb.Table('sudoku')

print(table.creation_date_time)

response = table.get_item(
    Key = {
        'user': 'justin'
    }
)
item = response['Item']
print(item)

def add_user(id, pw, fullname) :
    table.put_item(
        Item={
            'user': id,
            'password': pw,
            'fullname': fullname
        }
    )

def user_login(username) :
    pw = table.get_item(
        Key = {
            'user': username
        }
    )
    return pw['Item']['password']