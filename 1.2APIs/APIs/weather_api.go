package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	var userText string
	fmt.Print("Please enter your city: ")
	fmt.Scanln(&userText)

	response, err := http.Get(fmt.Sprintf("https://goweather.herokuapp.com/weather/%s", userText))
	if err != nil {
		fmt.Println("Error while fetching data:", err)
		os.Exit(1)
	}
	defer response.Body.Close()

	var data map[string]interface{}
	if err := json.NewDecoder(response.Body).Decode(&data); err != nil {
		fmt.Println("Error while decoding JSON:", err)
		os.Exit(1)
	}

	fmt.Println(data)
}
