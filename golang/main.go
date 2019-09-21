package main

import (
	"./algorithms"
	"fmt"
)

func main() {
	//fmt.Println(algorithms.FactorialRec(10))
	//fmt.Println(algorithms.FactorialIter(10))

	fmt.Println(algorithms.FastPowerRec(2, 10))

	fmt.Println(algorithms.FastPowerIter(2, 10))
}
