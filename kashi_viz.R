library(data.table)
library(magrittr)
library(highcharter)
source("viz_func.R")

Sys.setlocale("LC_CTYPE", locale = "Japanese")
aimer_cnt_tb <- fread("data/aimer_cnt.csv", encoding = "UTF-8") %>% 
  .[, V1 := NULL]
aimer_cnt_tb <- aimer_cnt_tb[, pos := ifelse(word %in% c("read", "feel"), "verb", pos)] %>% 
  .[, pos := ifelse(word %in% c("crazy"), "adj", pos)]
# noun
aimer_noun <- aimer_cnt_tb[pos == "noun"] %>% head(20)

thm <- hc_theme_merge(
  hc_theme_db(),
  hc_theme(
    chart = list(
      backgroundColor = "transparent",
      divBackgroundImage = "https://3.bp.blogspot.com/-XLimq4u5_HQ/XA3NOhRwfoI/AAAAAAAAIqQ/heW7g_pYYxw31kPW_HDtOv7lO2VYOzx7ACEwYBhgL/s1600/Aimer_-_I-beg-you_-_Hanabiratachi-no-March_-_Sailing.jpg"
    )
  )
)

high_bar_chart(
  aimer_noun$word,
  aimer_noun$cnt,
  "Aimer Top 20 名詞",
  "",
  "",
  "Count",
  inverted = T,
  thm
)
