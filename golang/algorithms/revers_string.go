package algorithms

import "unicode/utf8"

func ReverseString(s string) string {
	newString := ""

	for i := utf8.RuneCount([]byte(s)) - 1; i >= 0; i-- {
		newString += string(s[i])
	}

	return newString
}
