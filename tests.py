import behave

@given('we have behave installed')
def step_impl(context):
    pass

#convertimos el numero 5 de string a int
@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number >= 0
    context.tests_count = number


@then('behave will test it for us')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0