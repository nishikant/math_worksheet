#!/usr/bin/env python3

import argparse
import random
import logging
from fpdf import FPDF


logging.basicConfig(level=logging.DEBUG)


def multiplication(pages, start, end):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)

    loop_count = pages * 5 + 1

    for i in range(1, loop_count):
        loop_count = pages * 5 + 1
        num1 = random.randint(start, end)
        num2 = random.randint(start, end)
        num3 = random.randint(start, end)
        num4 = random.randint(start, end)
        num5 = random.randint(start, end)
        num6 = random.randint(start, end)
        num7 = random.randint(start, end)
        num8 = random.randint(start, end)

        padding = len(str(start)) if start > end else len(str(end))

        line1_space = 27
        line2_space = 23
        line3_space = line2_space + padding - 3
        dash_count = 3 + padding + 3

        padding = '0'+str(padding)

        add = " "*4 + "{:{}}".format(num1, padding) + \
            " "*line1_space + "{:{}}".format(num2, padding) + \
            " "*line1_space + "{:{}}".format(num3, padding) + \
            " "*line1_space + "{:{}}".format(num4, padding)

        pdf.cell(95, 8, txt=add,  ln=1, align='L')

        sub = "x  {:{}}".format(num5, padding) + " "*line2_space + \
            "x   {:{}}".format(num6, padding) + " "*line2_space + \
            "x  {:{}}".format(num7, padding) + " "*line2_space + \
            "x  {:{}}".format(num8, padding)

        pdf.cell(95, 8, txt=sub,  ln=1, align='L')

        dash = "-" * dash_count + " "*line3_space + "-"*dash_count + " " * \
            line3_space + "-"*dash_count + " "*line3_space + "-"*dash_count

        pdf.cell(95, 8, txt=dash,  ln=1, align='L')

        if (i % 5 != 0):
            pdf.cell(95, 30, txt=" ",  ln=1, align='L')
        elif i != loop_count - 1:
            pdf.add_page()

    pdf.output("questions.pdf")

    pdf.cell(95, 8, txt=add,  ln=1, align='L')

    pdf.cell(95, 8, txt=sub,  ln=1, align='L')

    dash = "-" * dash_count + " "*line3_space + "-"*dash_count + " " * \
        line3_space + "-"*dash_count + " "*line3_space + "-"*dash_count

    pdf.cell(95, 8, txt=dash,  ln=1, align='L')

    if (i % 5 != 0):
        pdf.cell(95, 30, txt=" ",  ln=1, align='L')
    elif i != loop_count - 1:
        pdf.add_page()

    pdf.output("questions.pdf")


def mixed_pdf(pages, start, end):
    """
    Math Worksheet creator.

    Creates a MATH PDF worksheets for addition,
    subtraction, multiplication and division

    """
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)

    loop_count = pages * 5 + 1

    for i in range(1, loop_count):
        num1 = random.randint(start, end)
        num2 = random.randint(start, end)

        padding = len(str(num1)) if num1 > num2 else len(str(num2))

        line1_space = 27
        line2_space = 23
        line3_space = line2_space + padding - 3
        dash_count = 3 + padding + 3

        padding = '0'+str(padding)

        divident = num1 if num1 > num2 else num2
        divisor = num2 if num1 > num2 else num1

        add = " "*4 + "{:{}}".format(num1, padding) + \
            " "*line1_space + "{:{}}".format(num1, padding) + \
            " "*line1_space + "{:{}}".format(num1, padding) + \
            " "*line1_space + "{:{}}".format(divident, padding)

        pdf.cell(95, 8, txt=add,  ln=1, align='L')

        sub = "+  {:{}}".format(num2, padding) + " "*line2_space + \
            "-   {:{}}".format(num2, padding) + " "*line2_space + \
            "x  {:{}}".format(num2, padding) + " "*line2_space + \
            "{}  {:{}}".format(chr(247), divisor, padding)

        pdf.cell(95, 8, txt=sub,  ln=1, align='L')

        dash = "-" * dash_count + " "*line3_space + "-"*dash_count + " " * \
            line3_space + "-"*dash_count + " "*line3_space + "-"*dash_count

        pdf.cell(95, 8, txt=dash,  ln=1, align='L')

        if (i % 5 != 0):
            pdf.cell(95, 30, txt=" ",  ln=1, align='L')
        elif i != loop_count - 1:
            pdf.add_page()

    pdf.output("questions.pdf")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--pages",
                        default=2,
                        type=int,
                        help="number of pages, default:2",
                        action="store")
    parser.add_argument("--start",
                        default=0,
                        dest="start",
                        type=int,
                        help="Random starting nos. default:0",
                        action="store")
    parser.add_argument("--end",
                        default=100,
                        dest="end",
                        type=int,
                        help="Randmon ending nos. default:100",
                        action="store")
    parser.add_argument("--type",
                        default=100,
                        dest="type",
                        type=str,
                        choices=['mixed', 'mul'],
                        help="Type of worksheet to generate. Mixed or \
                        multiplication only",
                        action="store")
    args = parser.parse_args()
    if args.type == "mul":
        multiplication(args.pages, args.start, args.end)
    else:
        mixed_pdf(args.pages, args.start, args.end)
