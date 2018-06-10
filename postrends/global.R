# data(cadmun, package = 'abjutils')

library(shiny)
library(shinydashboard)
library(shinyWidgets)

library(ggplot2)
library(plotly)
library(DiagrammeR)

library(dplyr)
library(tidyr)

library(lubridate)
library(stringr)

library(abjutils)

#-------------------------
options(shiny.trace = TRUE)

df <- readr::read_rds("compsci_com_cc_e_resumo.rds")

areas <- sort(unique(df$area_do_conhecimento))
areas <- c("Todas", areas)

data_min <- min(lubridate::as_date(df$data_de_defesa))
data_max <- max(lubridate::as_date(df$data_de_defesa))
