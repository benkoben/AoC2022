package main

import (
	"fmt"
	"net/http"
)

type Input struct {
    content string
}

func main() {
   var caloriesLog Input
   url := "https://adventofcode.com/2022/day/1/input"
   resp, err := http.Get(url)

   if err != nil {
       fmt.Println("Error occured while fetching url: ", err)
   }

  caloriesLog.content = resp.Body.Read()

  fmt.Println(
      caloriesLog.content,
  )
}
