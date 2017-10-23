def test_food(fix):
    # This test should error because it shouldn't be able to see any fixture 'fix'
    assert fix == 1
    assert False, "This test should have errored, because it shouldn't be able to see any fixture 'fix'"
