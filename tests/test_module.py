from trepo.module import hello_world

def test_hello_world():
    assert hello_world() == "Hello, world!"