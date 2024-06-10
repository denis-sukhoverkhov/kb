class Solution:
    def longestPalindrome(self, s: str) -> str:

        ln = len(s)

        answ = ''
        ln_answ = 0
        for i in range(ln):

            # odd
            l, r = i, i
            while l >= 0 and r <= ln -1:
                if s[r] == s[l]:
                    curr_len = r - l + 1
                    if curr_len > ln_answ:
                        answ = s[l: r+1]
                        ln_answ = curr_len
                else:
                    break

                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r <= ln - 1:
                if s[r] == s[l]:
                    curr_len = r - l + 1
                    if curr_len > ln_answ:
                        answ = s[l: r + 1]
                        ln_answ = curr_len
                else:
                    break

                l -= 1
                r += 1

        return answ


if __name__ == "__main__":
    obj = Solution()
    s = "uzhynqvopdbnkvuxizirzjsslptlhmvyfqhqvqffmqldkrrdwapbdcxqbchvxqixmvbbtalrgzvkobyxlkonkfknabjwzeoazankqzuhexhcwkbvwtioubrcujqqeqoedhploqklhgeilwwnndbnzeadzefkcvaxdhgnmocadvvzjocoweyoidhleuwhmavpdiizbwkukpstyorlwwyiwwyyyzqqgipzzlxsgcdjscdfvrrrqmllbdjkkuisxeqaprfblvjuixajhucmcvffmevaztvadrujbthlnsdrxzvbldwxbazxmilpkbccigkihcgjbtpvignmrgzdqnufaacxtihfgwrllrwgfhitxcaafunqdzgrmngivptbjgchikgiccbkplimxzabxwdlbvzxrdsnlhtbjurdavtzavemffvcmcuhjaxiujvlbfrpaqexsiukkjdbllmqrrrvfdcsjdcgsxlzzpigqqzyyywwiywwlroytspkukwbziidpvamhwuelhdioyewocojzvvdacomnghdxavckfezdaeznbdnnwwlieghlkqolphdeoqeqqjucrbuoitwvbkwchxehuzqknazaoezwjbankfknoklxybokvzgrlatbbvmxiqxvhcbqxcdbpawdrrkdlqmffqvqhqfyvmhltplssjzrizixuvknbdpovqnyhzu"
    assert obj.longestPalindrome(s) == s
    assert obj.longestPalindrome('cbbd') == 'bb'
    assert obj.longestPalindrome('babad') == 'bab'


