high_bar_chart <-
  function(x,
           y,
           title,
           xaxis_title,
           yaxis_title,
           series_name,
           inverted = F,
           thm) {
    highchart() %>%
      hc_title(
        text = title,
        style = list(fontSize = 18,
                     color = "white"),
        align = "left"
      ) %>%
      hc_yAxis_multiples(list(
        title = list(text = yaxis_title,
                     style = list(fontSize = 18)),
        labels = list(style = list(fontSize = 15,
                                   color = "white")),
        gridLineWidth = 0
      )) %>%
      hc_xAxis(
        categories = x,
        title = list(text = xaxis_title,
                     style = list(fontSize = 16)),
        gridLineWidth = 0,
        labels = list(style = list(fontSize = 16,
                                   color = "white"))
      ) %>%
      hc_add_series(
        name = series_name,
        data = y,
        type = "column",
        yAxis = 0,
        colorByPoint = T
      ) %>%
      hc_legend(enabled = F) %>%
      hc_chart(inverted = inverted) %>%
      hc_add_theme(thm)
  }
