import src.clippy as clippy

def test_clippy_can_greet():
    clpy = clippy.Clippy()
    assert clpy.greet() == "Hello Nils, I'm Clippy!"

def test_clippy_can_farewell():
    clpy = clippy.Clippy()
    assert clpy.farewell() == "Goodbye, old friend!"