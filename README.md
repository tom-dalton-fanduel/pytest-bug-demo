# pytest-bug-demo
Minimal example of https://github.com/pytest-dev/pytest/issues/2836

Create a new virtualenv and `pip install pytest`. Run `py.test`.

Expected behaviour:
* One test should pass and one test should **error**, saying it can't find a fixture `fix`.

Actual behaviour:
* The second test (`test_food`) runs and gets to the 'this shouldn't have worked' exception and fails there.
