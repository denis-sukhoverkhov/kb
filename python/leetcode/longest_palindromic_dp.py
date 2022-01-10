class Solution:
    def longestPalindrome(self, s: str) -> str:

        _arr = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            _arr[i][i] = 1

        indices = (0, 0)

        w_s = 1
        while w_s < len(s):
            s_p = 0
            e_p = s_p + w_s
            while e_p < len(s):
                if s[s_p] == s[e_p] and e_p - s_p == 1:
                    _arr[s_p][e_p] = 1
                    if e_p - s_p > indices[1] - indices[0]:
                        indices = (s_p, e_p)
                elif s[s_p] == s[e_p] and _arr[s_p+1][e_p-1] == 1:
                    _arr[s_p][e_p] = 1
                    if e_p - s_p > indices[1] - indices[0]:
                        indices = (s_p, e_p)
                s_p += 1
                e_p += 1
            w_s += 1

        return s[indices[0]:indices[1]+1]


if __name__ == "__main__":
    obj = Solution()
    assert obj.longestPalindrome("uzhynqvopdbnkvuxizirzjsslptlhmvyfqhqvqffmqldkrrdwapbdcxqbchvxqixmvbbtalrgzvkobyxlkonkfknabjwzeoazankqzuhexhcwkbvwtioubrcujqqeqoedhploqklhgeilwwnndbnzeadzefkcvaxdhgnmocadvvzjocoweyoidhleuwhmavpdiizbwkukpstyorlwwyiwwyyyzqqgipzzlxsgcdjscdfvrrrqmllbdjkkuisxeqaprfblvjuixajhucmcvffmevaztvadrujbthlnsdrxzvbldwxbazxmilpkbccigkihcgjbtpvignmrgzdqnufaacxtihfgwrllrwgfhitxcaafunqdzgrmngivptbjgchikgiccbkplimxzabxwdlbvzxrdsnlhtbjurdavtzavemffvcmcuhjaxiujvlbfrpaqexsiukkjdbllmqrrrvfdcsjdcgsxlzzpigqqzyyywwiywwlroytspkukwbziidpvamhwuelhdioyewocojzvvdacomnghdxavckfezdaeznbdnnwwlieghlkqolphdeoqeqqjucrbuoitwvbkwchxehuzqknazaoezwjbankfknoklxybokvzgrlatbbvmxiqxvhcbqxcdbpawdrrkdlqmffqvqhqfyvmhltplssjzrizixuvknbdpovqnyhzu") == ''
    assert obj.longestPalindrome('cbbd') == 'bb'
    assert obj.longestPalindrome('babad') == 'bab'


