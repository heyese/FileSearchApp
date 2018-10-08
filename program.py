"""File Searcher App"""
import os.path
import collections

SearchResult = collections.namedtuple('SearchResult', ['path', 'line_number', 'line'])

def main():
    print_header('File Searcher App')

    directory = get_search_directory()

    search_string = input('What string would you like to search for? : ')

    print('\nWill search .txt files under:\n{}\nfor the given string:\n{}\n'.format(directory, search_string))

    for i in search(directory, search_string):
        print('Path: {} ; Line number: {} ; Text: {}'.format(
            i.path, i.line_number, i.line
        ))


def search(directory, search_string):

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            # USE RECURSION to examine subdirectories
            # This is memory intensive
            yield from search(full_path, search_string)

        if os.path.splitext(full_path)[1] == '.txt':
            with open(full_path, 'r') as f:
                i = 0
                for line in f:
                    i += 1
                    if line.lower().find(search_string.lower()) != -1:
                        result = SearchResult(full_path, i, line.strip())
                        yield result

def get_search_directory():
    while True:
        dir = input('What directory do you want to search? : ')
        if not os.path.isdir(dir):
            print('{} is not a valid directory'.format(dir))
        else:
            break
    return os.path.abspath(dir)


def print_header(name):
    print('{0:-<{w}}\n{1:^{w}}\n{0:-<{w}}\n'.format('', name, w=2 * len(name)))


if __name__ == '__main__':
    main()
