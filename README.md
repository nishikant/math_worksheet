# math_worksheet

Generate math worksheets in PDF format.

This script generates a PDF worksheet for kids to practice addition,
subtraction, multiplication and division. It generates two random
numbers and use those to create math problems for addition,
subtraction, multiplication and division. You can change the range of
random numbers using --start and --end parameters. By default it will
generate random number between 0 and 100. 2 pages are generated with
20 problems on each page. You can increase the number of pages using
--pages option.

This program will generate a "questions.pdf" file in current working
directory.

```
usage: math_questions.py [-h] [--pages PAGES] [--start START] [--end END]

optional arguments:
  -h, --help     show this help message and exit
  --pages PAGES  number of pages, default:2
  --start START  Random starting nos. default:0
  --end END      Randmon ending nos. default:100
  
eg: $>./math_questions.py --end 1000
$> ./math_questions.py --start 10 --end 399 --pages 6
```

