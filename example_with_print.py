def add(a, b):
    print(a+b)
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def main():
    add(3,3)
    add("stall","warth")
    

if __name__ == '__main__':
    main()