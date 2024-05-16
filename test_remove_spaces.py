from utils import space_remove

def test_remove_spaces():
    assert space_remove.remove_spaces("hello world") == "helloworld"
    assert space_remove.remove_spaces("   remove  spaces  ") == "removespaces"
    assert space_remove.remove_spaces("no_spaces_here") == "no_spaces_here"