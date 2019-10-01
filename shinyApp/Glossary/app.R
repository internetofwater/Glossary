  #
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#


# load the required packages
library(shiny)
library(shinydashboard)
library(rdflib)


## Add icon along with the title in the shinydashboard header
# title <- tags$a(href='https://www.google.com',
#                 tags$img(src="rsudio.jpg", height = '200', width = '200')
#                 icon("diamond"),
#                 'Diamonds Explorer', target="_blank")

#Adding image or logo along with the title in the header
title <- tags$a(href='https://internetofwater.org',
                tags$img(src="iow_logo_horizontal_rgb.png", width = '95', height ='36'),
                'Glossary')

## ui code starts here
ui <- fluidPage(
    dashboardPage(skin="black",
        dashboardHeader(title = title), 
        dashboardSidebar(),
        dashboardBody(
            # add reference to CSS file
            # ensure that CSS file is in the www folder of the working directory
            tags$head(
                tags$link(rel = "stylesheet", type = "text/css", href = "custom1.css")
            )
        )
    )
)


server<- function(input, output, session) {}


shinyApp(ui, server)