import pytest

import boto3
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample


@mock_dynamodb2
def test_create_dynamo_table():
    '''
        Implement the test logic here for testing create_dynamo_table method
    '''
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1"
    )

    model = DynamodBExample()
    model.create_movies_table()

    table = dynamodb.Table("Movies")
    table.load()

    assert table.table_name == "Movies"
    assert table.table_status == "ACTIVE"


@mock_dynamodb2
def test_add_dynamo_record_table():
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1"
    )

    model = DynamodBExample()
    model.create_movies_table()

    model.add_dynamo_record(
        "Movies",
        {
            "year": 2024,
            "title": "Inception"
        }
    )

    table = dynamodb.Table("Movies")

    response = table.get_item(
        Key={
            "year": 2024,
            "title": "Inception"
        }
    )

    assert response["Item"]["title"] == "Inception"
    assert response["Item"]["year"] == 2024

@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    '''
        Implement the test logic here test_add_dynamo_record_table method for failures
    '''
    
    model = DynamodBExample()
    model.create_movies_table()

    with pytest.raises(Exception):
        model.add_dynamo_record(
            "Movies",
            {
                "year": "invalid",
                "title": "Inception"
            }
        )
