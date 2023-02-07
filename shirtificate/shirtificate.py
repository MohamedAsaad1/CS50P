from fpdf import FPDF

class PDF(FPDF):
    


def main():
    name = input("Name:").strip()
    pdf = FPDF()
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()