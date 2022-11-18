import requests
from behave import *
from utilities.resources import *
from utilities.configurations import *


@given(u'the search character by 1011198 begins')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.getCharatersOne
    context.response = requests.get(context.url)
    print(context.response.json())


@when(u'the search returns 200')
def step_impl(context):
    response_json = (context.response.json())
    context.code = response_json['code']
    assert response_json["code"] == 200
    print(context.code)


@then('the character name must be Agents of Atlas')
def step_impl(context):
    response_json = (context.response.json())
    context.name = response_json['data']['results'][0]['name']
    assert context.name == 'Agents of Atlas'
    print(context.name)


@given(u'the search character by 1011297 begins')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.getCharatersTwo
    context.response = requests.get(context.url)
    print(context.response.json())


@then(u'the character name must be Agent Brand')
def step_impl(context):
    response_json = (context.response.json())
    context.name = response_json['data']['results'][0]['name']
    assert context.name == 'Agent Brand'
    print(context.name)


@given(u'the search character by 1011456 begins')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.getCharatersThree
    context.response = requests.get(context.url)
    print(context.response.json())


@then(u'the character name must be Balder')
def step_impl(context):
    response_json = (context.response.json())
    context.name = response_json['data']['results'][0]['name']
    assert context.name == 'Balder'
    print(context.name)


@given(u'the search non existent character begins')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.getCharatersNotFound
    context.response = requests.get(context.url)
    print(context.response.json())


@when('the search returns <Code>')
def step_impl(context):
    response_json = (context.response.json())
    context.code = response_json['code']
    assert response_json["code"] == 404
    print(context.code)


@then('the error message must be <Message>')
def step_impl(context):
    response_json = (context.response.json())
    context.status = response_json['status']
    assert response_json["status"] == "We couldn't find that character"
    print(context.status)
