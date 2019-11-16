#!/usr/bin/env Rscript

# Install dependencies
install.packages("rvest")

# Load rvest library
library(rvest)

indexPageURL = "https://www.mass.gov/info-details/municipal-vulnerability-preparedness-mvp-program-planning-reports"


html = read_html(indexPageURL)

html[2]
