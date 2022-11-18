import requests
from behave import *
from utilities.resources import *
from utilities.configurations import *


@given('the search stories begins')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.getStories
    context.response = requests.get(context.url)
    #print(context.response.json())


@when('the search returns status should be 200')
def step_impl(context):
    response_json = (context.response.json())
    context.code = response_json['code']
    assert response_json["code"] == 200
    print(context.code)


@then('returns five records')
def step_impl(context):
    response_json = (context.response.json())
    context.count = response_json['data']['count']
    # assert response_json['data.limit'] == 5
    assert context.count == 5
    print(context.count)


@then('returns records titles')
def step_impl(context):
    response_json = (context.response.json())
    context.firstTitle = response_json['data']['results'][0]['title']
    context.secondTitle = response_json['data']['results'][1]['title']
    context.thirdTitle = response_json['data']['results'][2]['title']
    context.fourthTitle = response_json['data']['results'][3]['title']
    context.fifthTitle = response_json['data']['results'][4]['title']
    print(context.firstTitle)
    print(context.secondTitle)
    print(context.thirdTitle)
    print(context.fourthTitle)
    print(context.fifthTitle)
