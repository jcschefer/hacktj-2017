package main

import(
   "fmt"
)

type Question struct {
   Prompt      string      `json:prompt`
   Answer      string      `json:answer`
}

type Tournament struct {
   Round       string      `json:roundname`
   Questions   []Question  `json:questions`
}

type JSONData struct {
   Id          string `json:date`
   Hours int `json:hours`
}

func main(){
   fmt.Println("begin")
}
