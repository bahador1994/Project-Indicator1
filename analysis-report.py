from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Spacer
from reportlab.lib.enums import TA_CENTER

# File path
output_path = "analysis-report.pdf"
trend_analysis_image_path = "Trend_Analysis.png"  # Path to the pipeline figure image
debttoGDP_Ratio_image_path = "Debt-to-GDP_Ratio.png"  # Path to the pipeline figure image
correlation_Analysis_image_path = "Correlation_Analysis.png"  # Path to the pipeline figure image
economic_Events_Analysis_image_path = "Economic_Events_Analysis.png"  # Path to the pipeline figure image
economic_Indicator_Comparisons_image_path = "Economic_Indicator_Comparisons.png"  # Path to the pipeline figure image
seasonality_and_Cycles_image_path = "Seasonality_and_Cycles.png"  # Path to the pipeline figure image
debt_and_Inflation_image_path = "Debt_and_Inflation.png"  # Path to the pipeline figure image
economic_Health_Score_image_path = "Economic_Health_Score.png"  # Path to the pipeline figure image
# Create the PDF
doc = SimpleDocTemplate(output_path, pagesize=letter)
elements = []

# Styles
title_style = ParagraphStyle(name="Title", fontSize=18, leading=22, alignment=1, spaceAfter=20, fontName="Helvetica-Bold")
header_style = ParagraphStyle(name="Header", fontSize=14, leading=18, spaceAfter=12, fontName="Helvetica-Bold")
content_style = ParagraphStyle(name="Content", fontSize=12, leading=16)
bullet_style = ParagraphStyle(name="Bullet", fontSize=12, leftIndent=20, leading=16)

# Title
elements.append(Paragraph("How the U.S. Economy Has Changed Over Time", title_style))

# Introduction
elements.append(Paragraph("1. Introduction", header_style))
elements.append(Paragraph("""
The U.S. economy is one of the most important in the world and has changed a lot over time.
These changes are influenced by factors like how much the economy grows (GDP),
how much the government borrows (public debt), inflation, and unemployment.
Understanding these factors helps us see how the economy is doing and what challenges it might face.
This report looks at whether the growth of the U.S. economy is connected to the increase in government borrowing.
By analyzing trends in GDP, public debt, inflation, and unemployment, we aim to uncover patterns and relationships that explain how these factors work together.
The main question we want to answer is:
""", content_style))
elements.append(Paragraph("<b>Main Research Question:</b> Is the growth of the U.S. economy related to the increase in government borrowing over time?", content_style))
elements.append(Paragraph("""
Through this study, we hope to provide simple, clear insights about how the U.S. economy has changed and what these changes mean for the future.
""", content_style))
# Used Data
elements.append(Paragraph("2. Used Data", header_style))
elements.append(Paragraph("<b>Dataset 1:</b> U.S. Economic Indicators (1974–2024)", content_style))
elements.append(Paragraph("""
Attributes: GDP, CPI (inflation), and unemployment rates. Data is aggregated quarterly and normalized for comparisons.
""", bullet_style))
elements.append(Paragraph("<b>Dataset 2:</b> U.S. Public Debt vs. GDP (1947–2020)", content_style))
elements.append(Paragraph("""
Attributes: GDP, public debt, and calculated Debt-to-GDP ratio. Timeframes were aligned with Dataset 1, and growth rates were computed for analysis.
""", bullet_style))
elements.append(Spacer(10, 220))
# Analyses
elements.append(Paragraph("3. Analyses", header_style))

# Analysis 1: Trend Analysis
elements.append(Paragraph("3.1 Trend Analysis", header_style))
elements.append(Paragraph("""
Analyzed long-term trends in GDP, public debt, and Debt-to-GDP ratio using line plots. Key insights include a steady GDP growth and accelerated debt accumulation after 2000.
""", content_style))
elements.append(Image(trend_analysis_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 15))

# Analysis 2: Debt-to-GDP Ratio
elements.append(Paragraph("3.2 Debt-to-GDP Ratio", header_style))
elements.append(Paragraph("""
Examined changes in the Debt-to-GDP ratio as an indicator of fiscal sustainability. Findings suggest a rising ratio, indicating increased borrowing relative to economic output.
""", content_style))
elements.append(Image(debttoGDP_Ratio_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 50))

elements.append(Paragraph("3.3 Correlation Analysis", header_style))
elements.append(Paragraph("""
Quantified relationships between key indicators like GDP growth and public debt.
""", content_style))
elements.append(Image(correlation_Analysis_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

elements.append(Paragraph("3.4 Economic Events Analysis", header_style))
elements.append(Paragraph("""
Explored the impact of significant events like the 2008 financial crisis and COVID-19 on key indicators.
""", content_style))
elements.append(Image(economic_Events_Analysis_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

elements.append(Paragraph("3.5 Economic Indicator Comparisons", header_style))
elements.append(Paragraph("""
Compared growth rates of GDP, public debt, and inflation over decades.
""", content_style))
elements.append(Image(economic_Indicator_Comparisons_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

elements.append(Paragraph("3.6 Seasonality and Cycles", header_style))
elements.append(Paragraph("""
Detected seasonal patterns and cycles in GDP and unemployment data.
""", content_style))
elements.append(Image(seasonality_and_Cycles_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

elements.append(Paragraph("3.7 Debt and Inflation", header_style))
elements.append(Paragraph("""
Investigated the relationship between inflation rates and public debt accumulation.
""", content_style))
elements.append(Image(debt_and_Inflation_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

elements.append(Paragraph("3.8 Economic Health Score", header_style))
elements.append(Paragraph("""
Developed a composite score combining indicators to assess overall economic health.
""", content_style))
elements.append(Image(economic_Health_Score_image_path, width=8 * inch, height=7 * inch))

elements.append(Spacer(1, 70))

# Conclusions
elements.append(Paragraph("4. Conclusions", header_style))
elements.append(Paragraph("""
This analysis demonstrates significant relationships between GDP growth and public debt. The Debt-to-GDP ratio indicates rising fiscal pressure, particularly in recent decades. While trends and correlations provide useful insights, future work could focus on causal analysis to determine how specific policies influence economic outcomes.
""", content_style))

# Build the PDF
doc.build(elements)
print(f"Data report successfully saved as '{output_path}'.")
