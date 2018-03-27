# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:50:06 2018

@author: Ser
"""
"""
Доводит до конца экспорт файлов xmind в mmap, выполняемый программой xmind.
После экспортирования из программы xmind в mmap не отображаются заметки к узлам, хотя они имеются в 
файле Document.xml. Эта программа вносит необходимые изменения в Document.xml, чтобы заметки отображались.

"""
def listFindPos(text,strFind):
    startList = []
    start = 0
    while text.find(strFind,start) != -1:
        start = text.find(strFind,start) 
        startList.append(start)
        start = start+len(strFind)
    return startList

def remfile(text, strFind):
    startList = listFindPos(text,strFind) #находим позиции PreviewPlainText и заносим их в список
    if len(startList) == 0:
        print("Файл остался без изменений")
        return 0
 
        
    
    readingStart = 0
    resStr = ''
    for start in startList: #для каждой позиции списка

        #считываем значение
        startVal = start + len(strFind) + len('="')
        endVal = text.find('"',startVal)
        val = text[startVal:endVal]
        print(startList.index(start))
        
        if text.find(val,endVal) == -1: #если это значение не встречается второй раз
            startEdit = text.find('<',startVal) #находим позицию внесения изменений                
            resStr = resStr + text[readingStart:startEdit]
            
            
            
            stopFind = startEdit + len('<html xmlns="http://www.w3.org/1999/xhtml"><p>')                
            if text.find('<html xmlns="http://www.w3.org/1999/xhtml"><p>',startEdit,stopFind) == -1:    
                pastStr = '<html xmlns="http://www.w3.org/1999/xhtml"><p>' + val + '</p></html>'            
                resStr = resStr + pastStr
           
            readingStart = startEdit            
            
            stopFind = startEdit + len('<xhtml:html xmlns:xhtml="http://www.w3.org/1999/xhtml"/>')
                
            if text.find('<xhtml:html xmlns:xhtml="http://www.w3.org/1999/xhtml"/>',startEdit,stopFind) != -1:
                startDel = text.find('<xhtml:html xmlns:xhtml="http://www.w3.org/1999/xhtml"/>',startEdit,stopFind)
                endDel = startDel + stopFind -startEdit
                readingStart = endDel
                
                

                
                
        
    resStr=resStr+text[readingStart:]
    return resStr
    
myfile = open("D:/nets/Document.xml")
strtext = myfile.read()
#print(strtext) 

#print "количество=".str(len(strtext))
myfile.close()

strfile = remfile(strtext,'PreviewPlainText')

f = open("D:/nets/DocumentRec.xml",'w')
f.write(strfile)
f.close()

print("Файл исправлен!")
