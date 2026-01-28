from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from datetime import datetime
import io

class PDFReportGenerator:
    """Generate PDF reports for heart disease predictions"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#E74C3C'),
            spaceAfter=30,
            alignment=1
        )
        
    def generate_prediction_report(self, patient_name, patient_data, prediction, probability, risk_level):
        """Generate a PDF report for a single prediction"""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        
        # Title
        title = Paragraph("❤️ Heart Disease Prediction Report", self.title_style)
        elements.append(title)
        elements.append(Spacer(1, 0.3*inch))
        
        # Report Date
        date_text = Paragraph(f"<b>Report Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                             self.styles['Normal'])
        elements.append(date_text)
        elements.append(Spacer(1, 0.2*inch))
        
        # Patient Information
        patient_heading = Paragraph("<b>Patient Information</b>", self.styles['Heading2'])
        elements.append(patient_heading)
        elements.append(Spacer(1, 0.1*inch))
        
        patient_info = [
            ["Field", "Value"],
            ["Patient Name", patient_name if patient_name else "Not Specified"],
            ["Age", str(patient_data.get("age", "N/A"))],
            ["Gender", "Male" if patient_data.get("gender") == 1 else "Female"],
            ["Blood Pressure", f"{patient_data.get('trtbps', 'N/A')} mmHg"],
            ["Cholesterol", f"{patient_data.get('chol', 'N/A')} mg/dL"],
            ["Max Heart Rate", str(patient_data.get('thalachh', 'N/A'))],
        ]
        
        patient_table = Table(patient_info, colWidths=[2.5*inch, 2.5*inch])
        patient_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E74C3C')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(patient_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Prediction Results
        results_heading = Paragraph("<b>Prediction Results</b>", self.styles['Heading2'])
        elements.append(results_heading)
        elements.append(Spacer(1, 0.1*inch))
        
        result_color = colors.HexColor('#E74C3C') if prediction == 1 else colors.HexColor('#27AE60')
        prediction_text = "Heart Disease Detected ⚠️" if prediction == 1 else "No Heart Disease Detected ✓"
        
        results_data = [
            ["Metric", "Value"],
            ["Prediction", prediction_text],
            ["Confidence", f"{probability*100:.2f}%"],
            ["Risk Level", risk_level],
        ]
        
        results_table = Table(results_data, colWidths=[2.5*inch, 2.5*inch])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(results_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Recommendations
        recommendations_heading = Paragraph("<b>Recommendations</b>", self.styles['Heading2'])
        elements.append(recommendations_heading)
        elements.append(Spacer(1, 0.1*inch))
        
        if prediction == 1:
            recommendations = [
                "• Consult with a cardiologist immediately",
                "• Schedule comprehensive cardiac evaluation",
                "• Monitor blood pressure regularly",
                "• Reduce sodium and fat intake",
                "• Engage in regular physical activity (with doctor's approval)",
                "• Manage stress through meditation or counseling"
            ]
        else:
            recommendations = [
                "• Maintain current healthy lifestyle",
                "• Continue regular exercise (150 min/week recommended)",
                "• Monitor cholesterol and blood pressure annually",
                "• Maintain balanced diet rich in vegetables and whole grains",
                "• Avoid smoking and excessive alcohol",
                "• Schedule regular check-ups with your physician"
            ]
        
        for rec in recommendations:
            elements.append(Paragraph(rec, self.styles['Normal']))
            elements.append(Spacer(1, 0.05*inch))
        
        elements.append(Spacer(1, 0.3*inch))
        
        # Disclaimer
        disclaimer = Paragraph(
            "<i><b>Disclaimer:</b> This report is for informational purposes only and should not be considered "
            "as medical advice. Please consult with a qualified healthcare professional for proper diagnosis and treatment.</i>",
            self.styles['Normal']
        )
        elements.append(disclaimer)
        
        # Build PDF
        doc.build(elements)
        buffer.seek(0)
        return buffer

# Global instance
pdf_generator = PDFReportGenerator()
