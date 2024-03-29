#!/usr/bin/env python3
##############################################################################
#
# An example of inserting images into a worksheet using the XlsxWriter
# Python module.
#
# Copyright 2013-2021, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('inserting_img_into_a_worksheet.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)

# Insert an image.
worksheet.write('A2', 'Insert an image in a cell:')
worksheet.insert_image('B2', 'python.png', {'object_position': 1})

# Insert an image offset in the cell.
worksheet.write('A12', 'Insert an image with an offset:')
worksheet.insert_image('B12', 'python.png', {'x_offset': 15, 'y_offset': 10, 'object_position': 1})

# Insert an image with scaling.
cell_format = workbook.add_format({'text_wrap': True})
cell_format.set_align('vcenter')
worksheet.write('A23', 'Insert a scaled image:', cell_format)
worksheet.set_row(22, 50, cell_format)
worksheet.insert_image(
    'B23',
    'python.png',
    {
        'x_scale': 0.5,
        'y_scale': 0.5
        # 'object_position': 1
    }
)


workbook.close()
