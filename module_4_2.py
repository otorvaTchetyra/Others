def test_function():
    def inner_function():
        print('Where are looking for? I am here!')
    return inner_function

new_function = test_function()
new_function()
