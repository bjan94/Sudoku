import boto3
from Config import ACCESS_SECRET_KEY, ACCESS_KEY_ID, REGION_NAME


dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = ACCESS_KEY_ID,
                          aws_secret_access_key = ACCESS_SECRET_KEY,
                          region_name = REGION_NAME)

table = dynamodb.Table('sudoku')

print(table.creation_date_time)


def add_user(id, pw, fullname) :
    table.put_item(
        Item={
            'user': id,
            'password': pw,
            'fullname': fullname,
            'progress': '0'
        }
    )


def user_login(username) :
    pw = table.get_item(
        Key={
            'user': username
        }
    )
    if 'Item' in pw :
        print(pw['Item'])
        return pw['Item']
    else:
        return None

def updateLevel(id, currentLevel) :
    response = table.update_item(
        Key={
            'user': id
        },
        UpdateExpression="set progress = :r",
        ExpressionAttributeValues={
            ':r': currentLevel
        },
        ReturnValues="UPDATED_NEW"
    )