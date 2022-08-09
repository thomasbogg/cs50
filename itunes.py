"""
Sends request to Apple Itunes Library to download and print all albums
in order of year of release of a given Artist, speacified at the start
of the program
"""

import requests
import sys
import json


def main():

    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get(
        'https://itunes.apple.com/search?entity=album&term=' +
        sys.argv[1]
    )

    dict = response.json()

    results_list = list()
    for lst in dict['results']:

        if lst['artistName'] == sys.argv[1]:

            results_list.append(
                    lst['artistName']       +
                    ' - '                   +
                    lst['collectionName']   +
                    ' - '                   +
                    lst['releaseDate'][:4]
            )

    results_list.sort(key=year)

    for item in results_list:
        print(item)


def year(item):
    return item[-4:]


if __name__ == '__main__':
    main()
