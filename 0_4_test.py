from xlwt import Workbook
import xlwt

# эта программа соединяет три csv файла сопостовляя по столбцу "код"

MMI_file = open("MMI_НЗ.csv", 'r')
GPS_file = open("GPS_Points.csv", 'r')
GH_file = open("Маршруты_ГХ.csv", 'r')

###############################################################################
# создаю mmi список
###############################################################################
MMI_list = []

# создаю список, где каждый элемент это список, элементом которого является значание ячейки [[1,2,3],[1,2,3],[1,2,3]]
for line in MMI_file:
    # разбивка строки на список по разделителю
    mm = line.strip().split(';')
    # добавляю вспомогательный список в основной массив
    MMI_list.append(mm)

###############################################################################
# создаю список строк jps
###############################################################################
GPS_list = []

for line in GPS_file:
    mm = line.strip().split(';')
    GPS_list.append(mm)

###############################################################################
# создаю список строк гх
###############################################################################
GH_list = []

for line in GH_file:
    mm = line.strip().split(';')
    GH_list.append(mm)

###############################################################################
# создаю листы для итогового файла
###############################################################################
book = Workbook()
sheet1 = book.add_sheet('Sheet 1', cell_overwrite_ok=True)
book.add_sheet('Sheet 2', cell_overwrite_ok=True)

# создаю разные стили оформления ячейки. задаю цвет числом(см. скриншот с таблицей цветов в папке с программой)
style_1 = xlwt.easyxf('pattern: pattern solid;')
style_1.pattern.pattern_fore_colour = 42

style_2 = xlwt.easyxf('pattern: pattern solid;')
style_2.pattern.pattern_fore_colour = 26

style_3 = xlwt.easyxf('pattern: pattern solid;')
style_3.pattern.pattern_fore_colour = 41

###############################################################################
# запись в листы итогового файла
###############################################################################
for i in range(len(MMI_list)):

    ###########################################################################
    # записываю все элементы главного файла mmi_нз как они есть в итоговый файл
    ###########################################################################
    for k in range(len(MMI_list[i])):
        sheet1.write(i, k, MMI_list[i][k], style_2)

    ###########################################################################
    # сверяю каждый код из файла с jps только с i-тым кодом списка mmi
    ###########################################################################
    for j in range(len(GPS_list)):
        if GPS_list[j][0] == MMI_list[i][7]:
            # записываю подходящие строки со сдвигом в лево
            for n in range(len(GPS_list[j])):
                # записываю подходящие строки со сдвигом в лево
                sheet1.write(i, n + 17, GPS_list[j][n], style_1)

    ###########################################################################
    # сверяю каждый код из файла гх только с i-тым кодом списка mmi
    ###########################################################################
    for l in range(len(GH_list)):
        if MMI_list[i][7] == GH_list[l][3]:
            # записываю все элементы одной строки списка гх в итоговый файл
            for k in range(len(GH_list[l])):
                # записываю подходящие строки со сдвигом в лево
                sheet1.write(i, k + 22, GH_list[l][k], style_3)

    # счетчик
    print(str(len(MMI_list)) + '___' + str(i))

# запись листов в итоговый файл
# писать каждый раз новое название файла с расширением .xls - в него запишется результат
book.save('itog.xls')
