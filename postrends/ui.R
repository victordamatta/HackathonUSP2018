
header <- dashboardHeader(
  title = tags$span('PósTrends', tags$sup('\u03b2')),
  tags$li(class = 'dropdown', style = 'position:absolute;left:40%;top:0px;height:100%'))

sidebar <- dashboardSidebar(
  
  sidebarMenu(id = "tabs",
    menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
    searchInput('query', 'Busca: ', placeholder = 'Digite Sua Busca', btnSearch = icon("search"), btnReset = icon("remove"), width = "100%")),
  
  dateRangeInput('corte', 'Data de Defesa Entre', min = data_min, max = data_max, start = data_min, end = data_max, format = 'dd/mm/yyyy', language = 'pt-BR', separator = ' e '),
  
  tags$div(class = 'especial', selectInput('origem', label = 'Área do Conhecimento', choices = areas, selected = "Todas"),
  tags$style(type = 'text/css', HTML(".especial > div > div > div > div.selectize-input {max-height:60px;}"))))

dash <- tabItem(tabName = 'dashboard',
  
  fluidRow(
    valueBoxOutput('valor_a', width = 4),
    valueBoxOutput('valor_b', width = 4),
    valueBoxOutput('valor_c', width = 4)),

  fluidRow(
    
    tabBox(
      id = 'grafs_tempo', title = h5("Número de Defesas por Ano"), width = 7,
      tabPanel('Mestrado', plotlyOutput('mestrado')),
      tabPanel('Doutorado', plotlyOutput('doutorado'))),
    
    box(title = "Assuntos Relacionados", width = 5, grVizOutput('mapa')),
    
    box(title = 'Defesas Relevantes', width = 12, DT::dataTableOutput("ultimos"))))

bod <- dashboardBody(tabItems(dash))
dashboardPage(header, sidebar, bod, skin = 'blue', title = 'PósTrends')

# shiny::runApp("~/Desktop/carf/")