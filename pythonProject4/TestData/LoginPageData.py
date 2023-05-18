import openpyxl


class LoginPageData:
    test_name_cases = [{"Username": "rahul", "Password": "rahulshettyacademy"},
                       {"Username": "neha", "Password": "rahulsshettyacademy"}]

    @staticmethod
    def foo():
        # Dict = {}
        book = openpyxl.load_workbook("C:\\Users\\Sreenath\\Documents\\testCases.xlsx")
        sheet = book.active
        final_list = []
        for row in range(2, sheet.max_row + 1):
            Name = sheet['A' + str(row)].value
            Username = sheet['B' + str(row)].value
            Password = sheet['C' + str(row)].value

            final_list.append(
                {'Name' : Name, 'Username': Username, 'Password': Password})
        return final_list
