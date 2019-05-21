library(data.table)
library(magrittr)
Sys.setlocale("LC_CTYPE", locale = "Japanese")
aimer_cnt_tb <- fread("data/aimer_cnt.csv", encoding = "UTF-8")

