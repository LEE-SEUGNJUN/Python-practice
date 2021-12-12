from tkinter import *
import os
import os.path
 
 
## 함수 선언 부분 ##
def clickListBox(evt) :
    global currentDir, searchDirList    # 변경될 전역변수 
    if (dirListBox.curselection() == ()) : # 다른 리스트 box를 클릭할 떄는 무시
        return
    dirName = str(dirListBox.get(dirListBox.curselection())) # 클리한 폴더명
    if dirName == '상위폴더' :
        if len(searchDirList) == 1 : # 상위 폴더를 클릭했는데 현재 C:\\면 무시
            return
        searchDirList.pop() # 상위 폴더 이동이라 마지막 검색 폴더(현재 폴더) pop 
    else :                  # pop : 맨마지막 인덱스를 보여주고 요소 삭제
        searchDirList.append(currentDir + dirName + '\\') #검색 리스트에 클릭한 폴더 추가
         
    fillListBox()
         
def fillListBox() :
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0 ,END)   # 폴더 리스트 box를 비움
    fileListBox.delete(0, END)  # 파일 리스트 box를 비움
 
    dirListBox.insert(END, "상위폴더") ##디렉토리 인덱스 끝에 "상위폴더" 라고씀, 그밑에 디렉토리들도 END로 계속 쌓아가며 쓸 예정
    currentDir = searchDirList[len(searchDirList) - 1]
    dirLabel.configure(text = currentDir)
    folderList = os.listdir(currentDir) ##현재 디렉토리의 리스트들(파일,디렉토리)을 변수에 담고 
 
    index = 0   # 파일 목록 위치
    for item in folderList : ## 그 list들을 item에 하나씩 담는다
        if os.path.isdir(currentDir + item) : ##만약 디렉토리경로+item명 이 dir라면 (isdir는 디렉토리일경우 참 반환)
            dirListBox.insert(END, item)      ##리렉토리리스트박스에 맨 밑에 추가한다.
        elif os.path.isfile(currentDir + item) : ##디렉토리가아니라 파일이라면! 
            ##연습문제의 수정부분## 
            fileSize = os.path.getsize(currentDir + item)    # 파일 사이즈를 받아서 filesize에 저장
            fileName, fileExt = os.path.splitext(item)  
            # 파일 이름과 확장자를 튜플로 분리 (filename엔 파일명, fileExt엔 .확장자 로 들어가있다.)
 
            if fileSize < 1000000 :   # 1MB 미만
                fileSize = fileSize // 1000     # KB 단위로 (소수점 x)
                fileListBox.insert(END, item + "   " + "[" + str(fileSize) + " KB]") 
                ##1MB미만인 파일은 아이템명에 KB파일크기까지 붙여서 파일리스트 맨밑에 insert 한다
            elif 1000000 <= fileSize :
                fileSize = fileSize // 1000000     # MB 단위로 (소수점 x)
                fileListBox.insert(END, item + "   " + "[" + str(fileSize) + " MB]")
                ##1MB이상이면 아이템명에 MB단위의 파일크기 붙여서 파일리스트 맨밑에 insert
            fileExt = fileExt.lower()     # 대문자 확장자일 경우 소문자로 변환
            if fileExt == '.exe' or fileExt == '.msi' :     # 확장자 별로 분류
                fileListBox.itemconfig(index, foreground = "green") ##인덱스 처음엔 0 ,for문이니까 하나씩 올라간다.
            elif fileExt == '.jpg' or fileExt == '.bmp' or fileExt == '.png' or fileExt == '.gif' :
                fileListBox.itemconfig(index, foreground = "red") 
            elif fileExt == '.py' :
                fileListBox.itemconfig(index, foreground = "blue")
            index += 1


## 전역 변수 선언 부분 ##
window = None
searchDirList = ['C:\\']    # 중요변수 ! 검색한 폴더 목록의 스택
currentDir = 'C:\\'
dirLabel, dirListBox, fileListBox = None, None, None
 
## 메인 코드 부분 ##
window = Tk()
window.title("폴더 및 파일 목록 보기")
window.geometry("300x500")
 
dirLabel = Label(window, text = currentDir)
dirLabel.pack()
 
dirListBox = Listbox(window)
dirListBox.pack(side = LEFT, fill = BOTH, expand = 1)
dirListBox.bind('<<ListboxSelect>>', clickListBox)
 
fileListBox = Listbox(window)
fileListBox.pack(side = RIGHT, fill = BOTH, expand = 1)
 
fillListBox()   # 초기에는 C:\\의 모든 폴더 목록 만들기
 
window.mainloop()