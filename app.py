import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

st.title("🧾 AI Invoice Generator")

# User Input
name = st.text_input("Customer Name")
product = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)
qty = st.number_input("Quantity", min_value=1)

total = price * qty
st.write(f"### Total Amount: ₹{total}")

# PDF Function
def create_pdf():
    file_name = "invoice.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, "INVOICE")
    c.drawString(100, 700, f"Customer: {name}")
    c.drawString(100, 670, f"Product: {product}")
    c.drawString(100, 640, f"Price: ₹{price}")
    c.drawString(100, 610, f"Quantity: {qty}")
    c.drawString(100, 580, f"Total: ₹{total}")
    c.save()
    return file_name

if st.button("Generate PDF Invoice"):
    pdf_file = create_pdf()
    with open(pdf_file, "rb") as f:
        st.download_button("Download Invoice PDF", f, file_name="invoice.pdf")
