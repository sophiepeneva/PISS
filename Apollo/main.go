package main

import (
	"./service"
	"fmt"
)

func main() {
	params, err := service.BuildServiceParams()
	if err != nil {
		fmt.Println("Failed to start service")
		fmt.Println(err)
	}
	service.RunApolloService(*params)
}