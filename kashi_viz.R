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
      divBackgroundImage = "http://st.cdjapan.co.jp/pictures/l/05/22/SECL-2421.jpg?v=1"
    )
  )
)

# word translation
noun_chinese <- 
  c(
    "爱",
    "言语",
    "世界",
    "脸颊",
    "愿望",
    "回想",
    "宝贝",
    "季节",
    "心",
    "身旁",
    "记忆",
    "没关系",
    "远处",
    "回忆",
    "一体",
    "现在",
    "意思",
    "不安",
    "喜欢",
    "日子"
  )

high_bar_chart(
  paste0(aimer_noun$word, "（", noun_chinese, "）"),
  aimer_noun$cnt,
  "Aimer Top 20 名詞",
  "",
  "",
  "Count",
  inverted = T,
  thm
)

# adj 
aimer_adj <- aimer_cnt_tb[pos == "adj"] %>% setorder(-cnt) %>% head(20)
adj_chinese <-
  c(
    "坚强",
    "怜爱",
    "温柔",
    "疯狂",
    "悲伤",
    "遥远",
    "寂寞",
    "脆弱",
    "白色",
    "怀恋",
    "冰冷",
    "蓝色",
    "幼小",
    "红色",
    "深",
    "虚幻",
    "甜蜜",
    "美丽",
    "苦闷",
    "怀念"
  )
high_bar_chart(
  paste0(aimer_adj$word, "（", adj_chinese, "）"),
  aimer_adj$cnt,
  "Aimer Top 20 形容詞",
  "",
  "",
  "Count",
  inverted = T,
  thm
)
