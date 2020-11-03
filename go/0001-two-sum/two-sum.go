// Problem: https://leetcode.com/problems/two-sum/
package main

import "fmt"

func twoSum(nums []int, target int) []int {
	tmp := make(map[int]int)
	for i, num := range nums {
		if pos, ok := tmp[target-num]; ok {
			return []int{pos, i}
		}
		tmp[num] = i
	}
	return []int{-1, -1}
}

func main() {

	nums := []int{2, 7, 11, 15}
	target := 9
	output := twoSum(nums, target)
	fmt.Println("output:", output)
}
