import boto3
from Config import ACCESS_SECRET_KEY, ACCESS_KEY_ID, REGION_NAME


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
        Key={
            'user': username
        }
    )
    return pw['Item']['password']