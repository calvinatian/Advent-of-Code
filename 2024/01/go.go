package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func p1() {
	const filename = "./input"
	f, err := os.OpenFile(filename, os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatalf("open file error: %v", err)
		return
	}
	defer f.Close()

	// match number followed by 3 spaces and another number `123   56`
	rd := bufio.NewReader(f)
	left := make([]int, 0)
	right := make([]int, 0)
	re := regexp.MustCompile(`(?P<lnum>\d+)   (?P<rnum>\d+)`)
	for {
		line, err := rd.ReadString('\n')
		if err != nil {
			if err == io.EOF {
				break
			}
			log.Fatalf("read file line error: %v", err)
			return
		}
		matches := re.FindStringSubmatch(line)
		left_index := re.SubexpIndex("lnum")
		right_index := re.SubexpIndex("rnum")
		lnum := matches[left_index]
		rnum := matches[right_index]

		i, err := strconv.Atoi(lnum)
		if err != nil {
			log.Fatalf("error converting number %v", err)
		}
		left = append(left, i)

		i, err = strconv.Atoi(rnum)
		if err != nil {
			log.Fatalf("error converting number %v", err)
		}
		right = append(right, i)

		// fmt.Printf("%v %v\n", lnum, rnum)
		// fmt.Printf("%v\n", re.SubexpNames())
	}
	sort.Slice(left, func(i, j int) bool {
		return left[i] < left[j]
	})
	sort.Slice(right, func(i, j int) bool {
		return right[i] < right[j]
	})
	// fmt.Println(left, right)

	ans := 0
	for i := range left {
		lnum := left[i]
		rnum := right[i]

		diff := lnum - rnum
		if diff < 0 {
			ans += -diff
		} else {
			ans += diff
		}
	}
	fmt.Println(ans)
}

func p2() {
	const filename = "./input"
	f, err := os.OpenFile(filename, os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatalf("open file error: %v", err)
		return
	}
	defer f.Close()

	// match number followed by 3 spaces and another number `123   56`
	rd := bufio.NewReader(f)
	left := make([]int, 0)
	right := make([]int, 0)
	re := regexp.MustCompile(`(?P<lnum>\d+)   (?P<rnum>\d+)`)
	for {
		line, err := rd.ReadString('\n')
		if err != nil {
			if err == io.EOF {
				break
			}
			log.Fatalf("read file line error: %v", err)
			return
		}
		matches := re.FindStringSubmatch(line)
		left_index := re.SubexpIndex("lnum")
		right_index := re.SubexpIndex("rnum")
		lnum := matches[left_index]
		rnum := matches[right_index]

		i, err := strconv.Atoi(lnum)
		if err != nil {
			log.Fatalf("error converting number %v", err)
		}
		left = append(left, i)

		i, err = strconv.Atoi(rnum)
		if err != nil {
			log.Fatalf("error converting number %v", err)
		}
		right = append(right, i)
	}

	count := make(map[int]int)
	for _, n := range right {
		count[n] += 1
	}

	// fmt.Printf("Count: %v", count)

	ans := 0
	for _, n := range left {
		ans += count[n] * n
	}
	fmt.Println(ans)
}

func main() {
	p1()
	p2()
}
