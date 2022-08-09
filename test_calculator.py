from calculator import square


def main():
    test_square_conditionals()
    print('//////')
    test_square_asserts()


def test_square_conditionals():

    if square(2) != 4:
        print('Error: 2 squared was not 4')
    else:
        print('Success: 2 squared was 4')

    if square(100) != 10000:
        print('Error: 100 squared was not 10,000')
    else:
        print('Success: 100 squared was 10,000')


def test_square_asserts():

    assert square(100) == 10000, f''
    assert square(8) == 64



if __name__ == '__main__':
    main()
