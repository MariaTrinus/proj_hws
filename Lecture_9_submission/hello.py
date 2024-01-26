"""
    function hello()

    This function should accept a
      single string parameter name
      print the text
          Hello {name}!
      to the interactive window with {name}
      replaced with the function argument.
"""


def hello(name: str) -> None:
    print(f" Hello {name}!")
