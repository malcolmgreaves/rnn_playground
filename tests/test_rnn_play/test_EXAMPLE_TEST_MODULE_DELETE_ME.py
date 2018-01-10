from pytest import fixture, raises

@fixture(scope='module') # options for scope are: 'session', 'class', or completely omit
def resource():
    return "Hello world"

@fixture(scope='session')
def spacy_eng_model():
    return spacy.load('en')

def _raises_value_error():
    raise ValueError()

# Test functions _MUST_ start with "test_"
# Using a fixture is as simple as including it by name in the test function's
# parameter list!

def test_using_simple_fixture(resource):
    assert resource == "Hello world"

def test_fn_raises_err():
    with raises(ValueError):
        _raises_value_error()
