class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:

        sentence = ' ' + sentence
        arr = sentence.split(' $')

        for i in range(1, len(arr)):
                t = arr[i].split(' ')
                if t[0].isnumeric():
                    t[0] = "{:.2f}".format(int(t[0]) - int(t[0]) * discount / 100)
                arr[i] = ' '.join(t)

        res = ' $'.join(arr)
        return res[1:]


if __name__ == "__main__":
    obj = Solution()

    sentence = "$7383692 5q $2113353.36"
    discount = 64
    assert obj.discountPrices(sentence, discount) == \
           "$2658129.12 5q $2113353.36"

    sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
    discount = 100
    assert obj.discountPrices(sentence, discount) == \
           "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"

    sentence = "there are $1 $2 and 5$ candies in the shop"
    discount = 50
    assert obj.discountPrices(sentence, discount) == \
           "there are $0.50 $1.00 and 5$ candies in the shop"
