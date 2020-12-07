package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	s := strconv.Itoa(x)
	length := len(s)
	for i := 0; i <= length/2; i++ {
		if s[i] != s[length-i-1] {
			return false
		}
	}
	return true
}

func main() {
	x := 121
	output := isPalindrome(x)
	fmt.Println(output)
}
