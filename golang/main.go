package main

import (
	"./algorithms"
	"fmt"
)

func main() {
	//fmt.Println(algorithms.FactorialRec(10))
	//fmt.Println(algorithms.FactorialIter(10))
	//
	//fmt.Println(algorithms.FastPowerRec(2, 10))
	//fmt.Println(algorithms.FastPowerIter(2, 10))
	//
	//fmt.Println(algorithms.IsPrimeNumber(29))
	//
	//fmt.Println(algorithms.FibRec(7))
	//
	//fmt.Println(algorithms.FibIter(12))
	//
	//fmt.Println(algorithms.ReverseString("i am programmist"))
	//fmt.Println(algorithms.ReverseString2("i am programmist"))
	//
	//fmt.Println(algorithms.SquareRoot(56))
	//fmt.Println(algorithms.BSquareRoot(56))

	//algorithms.MinionGame("SUkhoverkhov")
	//
	//str := "domclick"
	//for pos, char := range str {
	//	fmt.Printf("character %#U starts at byte position %d\n", char, pos)
	//}
	//
	//arr := []int{10, 45, 56, 57, 91, 92, 100, 500}
	//fmt.Println(search.BSearch(arr, 100))
	//
	//var d sandbox.Direction = sandbox.North
	//fmt.Print(d)

	fmt.Println(algorithms.FibIter(5))
	fmt.Println(algorithms.FibIter2(1200))
}
