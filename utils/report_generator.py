from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import json
import os

def generate_pdf(results, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph("<font size=18>OSINT404 Scan Report</font>", styles["Title"]))
    story.append(Spacer(1, 12))
    
    # Content
    for section, data in results.items():
        story.append(Paragraph(f"<b>{section.upper()}</b>", styles["Heading2"]))
        
        if isinstance(data, list):
            items = [[item] for item in data]
            tbl = Table(items, colWidths=[400])
            story.append(tbl)
        elif isinstance(data, dict):
            items = [[k, v] for k, v in data.items()]
            tbl = Table(items, colWidths=[150, 250])
            story.append(tbl)
            
        story.append(Spacer(1, 12))
        
    doc.build(story)
    return filename

def generate_json(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
    return filename