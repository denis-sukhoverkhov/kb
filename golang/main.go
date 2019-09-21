package main

import (
	"./algorithms"
	"fmt"
)

func main() {
	//fmt.Println(algorithms.FactorialRec(10))
	//fmt.Println(algorithms.FactorialIter(10))

	//fmt.Println(algorithms.FastPowerRec(2, 10))
	//fmt.Println(algorithms.FastPowerIter(2, 10))

	//fmt.Println(algorithms.IsPrimeNumber(29))

	//fmt.Println(algorithms.FibRec(7))
	//str := "qwerty"
	//utf8.RuneCount([]byte(str))

	fmt.Println(algorithms.FibIter(12))

	fmt.Println(algorithms.ReverseString("i am programmist"))
	//fmt.Println(algorithms.ReverseString2("i am programmist"))
}
