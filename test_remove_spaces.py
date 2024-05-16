from utils import string_operations

def test_remove_spaces():
    assert string_operations.remove_spaces("hello world") == "helloworld"
    assert string_operations.remove_spaces("   remove  spaces  ") == "removespaces"
    assert string_operations.remove_spaces("no_spaces_here") == "no_spaces_here"