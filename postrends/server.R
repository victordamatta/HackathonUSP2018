
shinyServer(function(input, output, session) {
  
  dados <- reactive({
    
    if (!is.null(input$query) && input$query != '') {
      
      base <- "https://usppostrends.herokuapp.com/search/"
      query <- stringr::str_squish(stringr::str_to_lower(input$query))
      
      out <- httr::GET(stringr::str_c(base, URLencode(query)))
      
      res <- tibble::as_tibble(jsonlite::fromJSON(rawToChar(out$content)))
    } else{
      res <- readr::read_rds("compsci_com_cc_e_resumo.rds")
    }
    
    if (nrow(res) == 0) {
      showModal(modalDialog(
        title = "Sem Resultados",
        "A busca não retornou resultados. Por favor refaça a sua pesquisa!"))
      return(readr::read_rds("compsci_com_cc_e_resumo.rds"))
    }
    
    if (input$origem != "Todas") {
      res <- dplyr::filter(res, area_do_conhecimento == input$origem)
    }
    
    res <- res %>%
      dplyr::mutate(
        data_de_defesa = lubridate::as_date(data_de_defesa)) %>%
      dplyr::filter(data_de_defesa >= input$corte[1], data_de_defesa <= input$corte[2])
    
    return(res)
  })
  
  output$valor_a <- renderValueBox({
    valueBox(
      nrow(dados()), "Número de Defesas",
      icon = icon("hashtag"),
      color = "aqua")})
  output$valor_b <- renderValueBox({
    valueBox(
      sum(dados()$documento == "Dissertação de Mestrado"), "Dissertações de Mestrado",
      icon = icon("hashtag"),
      color = "red")})
  output$valor_c <- renderValueBox({
    valueBox(
      sum(dados()$documento == "Tese de Doutorado"), "Teses de Doutorado",
      icon = icon("hashtag"),
      color = "olive")})
  output$valor_d <- renderValueBox({
    
    q <- sum(dados()$documento == "Dissertação de Mestrado")/nrow(dados())
    
    valueBox(
      stringr::str_c(round(q*100, 2), "%"), "% de Dissertações",
      icon = icon("percent"),
      color = "purple")})
  
  output$ultimos <- DT::renderDataTable({
    
    df <- dados() %>%
      dplyr::select("Autor" = autor, "Orientador" = orientador, "Título" = titulo_em_portugues, "Data de Defesa" = data_de_defesa, "Palavras-Chave" = palavras_chave_em_portugues)
    
    DT::datatable(df,
      options = list(
        searching = FALSE, lengthChange = FALSE, pageLength = 5,
        processing = TRUE, ordering = FALSE,
        language = list(url = '//cdn.datatables.net/plug-ins/1.10.11/i18n/Portuguese-Brasil.json')),
      style = 'bootstrap', class = 'compact')
  }, server = TRUE)
  
  output$mestrado <- renderPlotly({
    
    temp <- dados() %>%
      dplyr::mutate(year = lubridate::year(data_de_defesa)) %>% 
      dplyr::filter(documento == "Dissertação de Mestrado") %>%
      dplyr::group_by(year) %>%
      dplyr::summarise(n = n())
    
    dplyr::tibble(year = min(temp$year):max(temp$year)) %>%
      dplyr::left_join(temp) %>%
      dplyr::mutate(n = dplyr::if_else(is.na(n), 0L, n)) %>%
      plot_ly(
        x = ~year, y = ~n, type = "scatter", mode = "lines",
        line = list(width = 3)) %>%
      layout(xaxis = list(title = ""), yaxis = list(title = "Número de Defesas"))
  })
  
  output$doutorado <- renderPlotly({
    
    temp <- dados() %>%
      dplyr::mutate(year = lubridate::year(data_de_defesa)) %>% 
      dplyr::filter(documento == "Tese de Doutorado") %>%
      dplyr::group_by(year) %>%
      dplyr::summarise(n = n())
    
    dplyr::tibble(year = min(temp$year):max(temp$year)) %>%
      dplyr::left_join(temp) %>%
      dplyr::mutate(n = dplyr::if_else(is.na(n), 0L, n)) %>%
      plot_ly(
        x = ~year, y = ~n, type = "scatter", mode = "lines",
        line = list(width = 3)) %>%
      layout(xaxis = list(title = ""), yaxis = list(title = "Número de Defesas"))
  })
  
  
  
  gerar_grafo <- function() {
    
    temp <- dados() %>% 
      dplyr::mutate(
        palavras = stringr::str_split(palavras_chave_em_portugues, "\n+")) %>% 
      tidyr::unnest(palavras) %>%
      dplyr::mutate(
        palavras = stringr::str_to_lower(palavras),
        palavras = abjutils::rm_accent(palavras)) %>%
      dplyr::filter(palavras != "") %>% 
      dplyr::mutate(data = lubridate::ymd(data_de_defesa)) %>% 
      dplyr::filter(documento != "Tese de Livre Docencia") %>%
      dplyr::filter(palavras != "nao disponivel")
    
    assuntos <- names(sort(-table(temp$palavras))[1:6])
    
    nodes <- assuntos %>% stringr::str_c("' ", ., " '", collapse = "\n")
    edges <- stringr::str_c("' ", assuntos[2:6], " '->' ", assuntos[1], " '", collapse = "\n")
    
    a <- "digraph {

      # graph attributes
      graph [layout = twopi, overlap = FALSE]

      # node attributes
      node [shape = oval, style = filled, fontname = Helvetica, fillcolor = LightCyan, color = LightCyan3]

      # node statements
    "
    
    b <- "
      # edge attributes
      edge [color = LightCyan3]

      # edge statements
    "
    
    c <- "
    }"
    
    stringr::str_c(a, nodes, b, edges, c)
  }

  output$mapa <- renderGrViz({grViz({gerar_grafo()})})
  
})
