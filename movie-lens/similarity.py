import numpy as np
from pprint import pprint
from typing import List


def l1_norm_similarity(r1: int, r2: int) -> int:
    return np.abs(r1 - r2)


def l2_norm_similarity(norm: int) -> float:
    return 1. / (norm + 1)


def sad(data: dict) -> float:
    """[Summary]
       data [dict]

       :return:
       --------
       Soma das diferenças absolutas
    """
    return NotImplemented

def cos_similarity(data: dict) -> float:
    """[summary]
    """
    return NotImplemented

def build_vectors(data: dict) -> List[int]:
    names = data.keys()
    return names


def main():
    r1: int = 5
    r2: int = 8

    data: dict = {'lets': {'Comédia': 5,
                           'Ação': 3,
                           'Drame': 5,
                           'SciFi': 1},
                  'Bob': {'Comédia': 3,
                          'Ação': 5,
                          'Drame': 1,
                          'SciFi': 5},
                  'Jane': {'Comédia': 4,
                           'Ação': 3,
                           'Drame': 5,
                           'SciFi': 1},
                  'Sara': {'Comédia': 3,
                           'Ação': 5,
                           'Drama': 4,
                           'SciFi': 1}
                  }

    l1_norm: int = l1_norm_similarity(r1, r2)
    sim: float = l2_norm_similarity(l1_norm)
    pprint(sim)
    pprint(l1_norm)
    pprint(data)
    pprint(data['lets']['Comédia'])
    pprint(data.get('lets'))
    for key, value in data.items():
        for kk, vv in value.items():
            pprint(f'{key}: {kk}  rating: {vv}')

    pprint(cos_similarity(data))
    sum = 0
    for key in data.items():
        for kk, vv in value.items():
            sum += vv

    print(sum)

    vec_bob = [x for x in data['Bob'].values()]
    pprint(vec_bob)

    test = build_vectors(data)
    for k in test:
        print(k)

if __name__ == '__main__':
    main()
