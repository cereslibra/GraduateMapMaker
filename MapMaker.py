import pandas as pd

citys = pd.read_excel(r'data.xlsx', sheet_name=0)
origin=citys['城市'].values
flyGeo=citys['城市经纬度'].values
flyVal = citys['人数'].values

schools = pd.read_excel(r'data.xlsx', sheet_name=1)
schoolName = schools['学校'].values
schoolGeo = schools['学校经纬度'].values
studentName = schools['学生姓名'].values

print(origin, flyGeo, flyVal)
print(schoolName, schoolGeo, studentName)

replaceOrigin = origin[0]

replaceFlygeo = ''
for i in range(len(origin)):
    s = "'{}':[{:.2f}, {:.2f}],".format(origin[i], float(flyGeo[i].split(',')[0]), float(flyGeo[i].split(',')[1]))
    print(s)
    replaceFlygeo += s

replaceFlyVal=''
for i in range(len(origin)):
    s = "[{{name:'{}'}}, {{name:'{}', value:{:d}}}],".format(origin[i], replaceOrigin, int(flyVal[i]))
    print(s)
    replaceFlyVal += s

print(replaceFlygeo)

replaceScatterGeo = ''
for i in range(len(schoolName)):
    s = '"{}":[{:.2f}, {:.2f}],'.format(schoolName[i], float(schoolGeo[i].split(',')[0]), float(schoolGeo[i].split(',')[1]))
    print(s)
    replaceScatterGeo += s

replaceScatterVal= ''
for i in range(len(schoolName)):
    s = '{{name:"{}", value:"{}"}},'.format(schoolName[i], studentName[i])
    print(s)
    replaceScatterVal += s

a = open(r'temp.html', 'r', encoding='utf-8')
string = a.read()
string = string.replace('replaceOrigin', replaceOrigin)
string = string.replace('replaceFlyGeo', replaceFlygeo)
string = string.replace('replaceFlyVal', replaceFlyVal)
string = string.replace('replaceScatterGeo', replaceScatterGeo)
string = string.replace('replaceScatterVal', replaceScatterVal)

b = open(r'index.html', 'w', encoding= 'utf-8')
b.write(string)
b.close()

