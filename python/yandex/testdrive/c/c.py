import json


def solution(feeds):
    result = []
    for f in feeds:
        for o in f['offers']:
            result.append(o)

    result.sort(key=lambda k: (k['price'], k['offer_id']))

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        count_feeds = fi.readline().strip()

        feeds = []
        for i in range(int(count_feeds)):
            feeds.append(json.loads(fi.readline().strip()))

    res = solution(feeds)

    with open("output.txt", "w") as fo:

        fo.write(json.dumps({
            'offers': res
        }))
