
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import A4

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=A4)

    def add_image(self, image_path, x, y, width, height, alpha):
        self.pdf.setFillColorRGB(1, 1, 1, alpha)  # Встановлюємо колір фігури (білий) та альфа-канал
        self.pdf.drawImage(image_path, x, y, width, height, mask='auto')  # Викликаємо метод drawImage з аргументом mask='auto'

    def add_table(self, data, col_widths, row_heights):
            table = Table(data, colWidths=col_widths, rowHeights=row_heights)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                # ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            table.wrapOn(self.pdf, 100, 50)
            table.drawOn(self.pdf, 30, 290)
        
    def add_text(self, text, x, y, width, height, font_name='Helvetica', font_size=10, is_bold=False):
        if is_bold:
            font_name += '-Bold'
        self.pdf.setFont(font_name, font_size)
        lines = self.wrap_text(text, width, font_name, font_size)
        for line in lines:
            self.pdf.drawString(x, y, line)
            y -= height

    def wrap_text(self, text, width, font_name, font_size):
        lines = []
        current_line = ""
        words = text.split()
        for word in words:
            if self.pdf.stringWidth(current_line + " " + word, font_name, font_size) < width:
                current_line += " " + word
            else:
                lines.append(current_line.strip())
                current_line = word
        if current_line:
            lines.append(current_line.strip())
        return lines



    def save(self):
        self.pdf.showPage()
        self.pdf.save()