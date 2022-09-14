from openpyxl import load_workbook

class Para:
    def __init__(self,file):
        self.file = file

    def nose(self):
        wb = load_workbook(self.file)
        ws = wb.active

        nose_para = {
            'shape_nose'     : ws['D6'].value,
            'shape_coef'     : ws['D7'].value,
            'length_nose'    : ws['D8'].value  / 10,
            'diameter_nose'  : ws['D9'].value  / 10,
            'thickness_nose' : ws['D10'].value /10
        }
        return nose_para
    
    def body(self):
        wb = load_workbook(self.file)
        ws = wb.active

        body_para = {
            'quantity_body' : ws['D22'].value,
            'diameter_body' : ws['D23'].value / 10
        }
        for i in range(1,body_para['quantity_body']+1):
            bodytube = {
                'lenght_body' : ws[f'D{25+(i-1)*3}'].value / 10,
                'inner_diameter' : ws[f'D{26+(i-1)*3}'].value / 10
            }
            body_para[f'body{i}'] = bodytube
        return body_para

    def fin(self):
        wb = load_workbook(self.file)
        ws = wb.active

        fin_para = {
            'shape_fin'          : ws['D12'].value,
            'quantity_fin'       : ws['D13'].value,
            'inclination'        : ws['D14'].value,
            'root_chord'         : ws['D15'].value / 10,
            'tip_chord'          : ws['D16'].value / 10,
            'span'               : ws['D17'].value / 10,
            'leading_edge_chord' : ws['D18'].value / 10,
            'offset_fin'         : ws['D19'].value / -10,
            'thickness_fin'      : ws['D20'].value / 10
        }
        return fin_para