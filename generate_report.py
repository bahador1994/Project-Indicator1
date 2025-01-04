from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Spacer
# File paths
output_path = "data-report.pdf"
pipeline_image_path = "pipeline_diagram.png"  # Path to the pipeline figure image

# Create the PDF
doc = SimpleDocTemplate(output_path, pagesize=letter)
elements = []

# Styles
title_style = ParagraphStyle(name="Title", fontSize=14, leading=22, spaceAfter=20, fontName="Helvetica-Bold")
header_style = ParagraphStyle(name="Header", fontSize=14, leading=18, spaceAfter=12, fontName="Helvetica-Bold")
content_style = ParagraphStyle(name="Content", fontSize=12, leading=16)
bullet_style = ParagraphStyle(
    name="BulletStyle",
    fontSize=12,
    leading=16,
    leftIndent=20,  # Indent for bullet points
    bulletIndent=10,  # Indent for bullet symbols
)

# Title
elements.append(Paragraph("Analyzing the Effect of U.S. Public Debt on Economic Growth", title_style))

# 1. Introduction
elements.append(Paragraph("1. Introduction", header_style))
elements.append(Paragraph("1.1 Motivation for Analyzing the U.S. Economy", header_style))
elements.append(Paragraph("""
The U.S. economy is a cornerstone of global financial stability and has undergone significant changes over time. Understanding the dynamics between key indicators, 
such as GDP, public debt, inflation, and unemployment, provides valuable insights for policymakers, economists, and researchers. This project investigates how the 
growth of the U.S. economy is related to the increase in government borrowing, aiming to uncover trends and relationships that influence economic health.
""", content_style))
elements.append(Spacer(1, 20))
elements.append(Paragraph("1.2 Main Research Question", header_style))
elements.append(Paragraph("""
The central question this project seeks to answer is:
""", content_style))

elements.append(Paragraph("""
• "Is the growth of the U.S. economy related to the increase in government borrowing over time?"
""", bullet_style))
elements.append(Spacer(1, 20))
# 2. Datasets
elements.append(Paragraph("2. Datasets", header_style))
elements.append(Paragraph("""
For this project, we have identified two primary datasets to analyze the relationship between economic growth and government borrowing over time:
""", content_style))
elements.append(Spacer(1, 20))
# 2.1 U.S. Economic Indicators
elements.append(Paragraph("2.1 U.S. Economic Indicators (1974–2024)", header_style))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Datasets", header_style))
elements.append(Paragraph("""
The U.S. Economic Indicators dataset provides detailed data on key economic trends in the United States from 1974 to 2024. 
Key attributes include monthly measurements of GDP, inflation (CPI), and unemployment rates. These indicators are crucial 
for understanding the performance of the U.S. economy and assessing its stability over time.
""", content_style))
elements.append(Spacer(1, 20))
metadata_html = '<b>• MetaData URL:</b> <a href="https://www.kaggle.com/datasets/alfredkondoro/u-s-economic-indicators-1974-2024" color="blue">U.S. Economic Indicators Dataset</a>'
elements.append(Paragraph(metadata_html, bullet_style))
data_url_html = "<b>• Data URL:</b> Available for download via Kaggle API (data from 1974 to 2020 is used in this project)."
elements.append(Paragraph(data_url_html, bullet_style))
usability_html = "<b>• Usability : 10.00</b>"
elements.append(Paragraph(usability_html, bullet_style))
description_html = "<b>• Description: </b>This dataset is complete, well-structured, and requires minimal preprocessing."
elements.append(Paragraph(description_html, bullet_style))
license_html = '<b>• License: </b><a href="https://opendatacommons.org/licenses/pddl/1-0" color = "blue"> Open Data Commons Public Domain Dedication and License (PDDL) v1.0</a>'
elements.append(Paragraph(license_html, bullet_style))
elements.append(Paragraph("• CPIAUCSL: Consumer Price Index.", bullet_style))
elements.append(Paragraph("• UNRATE: Unemployment rate.", bullet_style))
elements.append(Paragraph("• GDP: Gross Domestic Product in millions.", bullet_style))
elements.append(Paragraph("""
Data spans from 1974 to 2024, offering a comprehensive view of economic trends.
""", content_style))
elements.append(Spacer(1, 20))
# 2.2 U.S. Public Debt vs. GDP
elements.append(Paragraph("2.2 U.S. Public Debt vs. GDP (1947–2020)", header_style))
elements.append(Paragraph("""
Dataset: Provides quarterly data on GDP and public debt in the U.S.
Source: Kaggle Dataset
License: Standard Kaggle license.
Description:
""", content_style))
elements.append(Paragraph("• Quarter: Date of the quarter.", bullet_style))
elements.append(Paragraph("• Gross Domestic Product ($mil): GDP in millions.", bullet_style))
elements.append(Paragraph("• Total Public Debt ($mil): Public debt in millions.", bullet_style))
elements.append(Paragraph("""
Data spans from 1947 to 2020.
""", content_style))
elements.append(Spacer(1, 20))
# 3. Data Pipeline
elements.append(Paragraph("3. Data Pipeline", header_style))
elements.append(Paragraph("""
The data pipeline processes datasets on U.S. Economic Indicators and Public Debt using the Kaggle API. The pipeline involves steps such as data extraction, 
preprocessing, quarterly aggregation, and merging. Figure 1 illustrates the pipeline.
""", content_style))

# Add the Pipeline Figure
elements.append(Paragraph("Figure 1: Data Pipeline", content_style))
elements.append(Image(pipeline_image_path, width=5 * inch, height=3 * inch))
elements.append(Spacer(1, 12))

elements.append(Paragraph("""
Transformations and Cleaning Steps:
""", content_style))
elements.append(Paragraph("• Monthly data on CPI, GDP, and Unemployment aggregated to quarterly intervals.", bullet_style))
elements.append(Paragraph("• Public Debt data merged with quarterly aggregated economic indicators.", bullet_style))
elements.append(Paragraph("• Calculated metrics: Debt-to-GDP Ratio, GDP Growth Rate, and Debt Growth Rate.", bullet_style))
elements.append(Paragraph("• Missing values handled using forward and backward filling.", bullet_style))

# 4. Results and Limitations
elements.append(Paragraph("4. Results and Limitations", header_style))

# Results
elements.append(Paragraph("""
4.1 Output Data Description
The final dataset includes:
""", content_style))
elements.append(Paragraph("• Quarterly data on CPI, GDP, Unemployment, Public Debt, and Debt-to-GDP Ratios.", bullet_style))
elements.append(Paragraph("• Derived metrics: GDP Growth Rate and Debt Growth Rate.", bullet_style))
elements.append(Paragraph("• The dataset is stored in an SQLite database (`final_dataset.sqlite`).", bullet_style))

# Limitations
elements.append(Paragraph("""
4.2 Data Quality and Limitations
The dataset is well-prepared and normalized, but some limitations exist:
""", content_style))
elements.append(Paragraph("• Temporal mismatch: Economic Indicators extend to 2024, while Public Debt data ends in 2020.", bullet_style))
elements.append(Paragraph("• Derived metrics (e.g., Growth Rates) may introduce minor inaccuracies due to aggregation.", bullet_style))

# Generate the PDF
doc.build(elements)
print(f"Data report successfully saved as '{output_path}'.")
