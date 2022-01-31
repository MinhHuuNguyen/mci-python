
def show_stars(rows):
    assert isinstance(rows, int), 'rows must be integer'

    for i in range(rows):
        print('*' * (i + 1))

if __name__ == '__main__':
    show_stars(5)