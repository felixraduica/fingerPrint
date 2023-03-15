from tkinter import *
from tkinter import ttk
from pywinauto.application import Application
import time

def INTERFACEinput():

    sti = time.time()

    #Creat a Tkinter instance frame
    w = Tk()

    #add title to frame bar
    w.title("fingerPrint")

    #define geometry of frame
    w.maxsize(900, 600)
    w.configure(bg="Lightgray")

    #add title to fram window
    title = Label(w, text="fingerPrint Application", bg="Lightgray")
    title.config(font=("courier",14))
    title.grid(padx=1, pady=1, row=0, column=0, columnspan=3)

    #input 1 Distal Length Dl
    ld1 = Label(w, text = 'Dl', bg="lightgray")
    ld1.config(font=("courier",14))
    ld1.grid(row=1, column=0, padx=15, pady=3)

    id1 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id1.config(font=("courier",14))
    id1.grid(row=1, column=1, padx=10, pady=3)

    #id1.insert(0,'30') #default value

    #input 2 Distal circumference
    ld2 = Label(w, text="Dc", bg="lightgray")
    ld2.config(font=("courier",14))
    ld2.grid(row=2, column=0, padx=10, pady=3)

    id2 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id2.config(font=("courier",14))
    id2.grid(row=2, column=1, padx=10, pady=3)

    #id2.insert(0,'15') #default value

    #input 3 Middle Length
    ld3 = Label(w, text="Ml", bg="lightgray")
    ld3.config(font=("courier",14))
    ld3.grid(row=3, column=0, padx=10, pady=3)

    id3 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id3.config(font=("courier",14))
    id3.grid(row=3, column=1, padx=10, pady=3)

    #id3.insert(0,'55') #default value

    #input 4 Middle Circumference
    ld4 = Label(w, text="Mc", bg="lightgray")
    ld4.config(font=("courier",14))
    ld4.grid(row=4, column=0, padx=10, pady=3)

    id4 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id4.config(font=("courier",14))
    id4.grid(row=4, column=1, padx=10, pady=3)

    #id4.insert(0,'15') #default value

    #input 5 Proximal Length
    ld5 = Label(w, text="Pl", bg="lightgray")
    ld5.config(font=("courier",14))
    ld5.grid(row=5, column=0, padx=10, pady=3)

    id5 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id5.config(font=("courier",14))
    id5.grid(row=5, column=1, padx=10, pady=3)

    #id5.insert(0,'55') #default value

    #input 6 Proximal Circumference
    ld6 = Label(w, text="Pc", bg="lightgray")
    ld6.config(font=("courier",14))
    ld6.grid(row=6, column=0, padx=10, pady=3)

    id6 = Entry(w, bg="White", fg="Green", bd=1, width=10)
    id6.config(font=("courier",14))
    id6.grid(row=6, column=1, padx=10, pady=3)

    #id6.insert(0,'15') #default value

    #Display entered values after pressing Send
    def printValue():
        global dl
        dl = id1.get()
        ida1 = Label(w, text=f'{dl}', bg='#ffbf00')
        ida1.grid(row=1, column=2, pady=10)
        global dc
        dc = id2.get()
        ida2 = Label(w, text=f'{dc}', bg='#ffbf00')
        ida2.grid(row=2, column=2, pady=10)
        global ml
        ml = id3.get()
        ida3 = Label(w, text=f'{ml}', bg='#ffbf00')
        ida3.grid(row=3, column=2, pady=10)
        global mc
        mc = id4.get()
        ida4 = Label(w, text=f'{mc}', bg='#ffbf00')
        ida4.grid(row=4, column=2, pady=10)
        global pl
        pl = id5.get()
        ida5 = Label(w, text=f'{pl}', bg='#ffbf00')
        ida5.grid(row=5, column=2, pady=10)
        global pc
        pc = id6.get()
        ida6 = Label(w, text=f'{pc}', bg='#ffbf00')
        ida6.grid(row=6, column=2, pady=10)

    #function  assign user values
    def getValue():
        #Get values and assign for use in CADscript
        global distalLength
        distalLength = 'height = '+ dl + ';'
        global distalCirc
        distalCirc = 'diameter = '+ dc + ';'
        global middleLength
        middleLength = 'height = '+ ml + ';'
        global middleCirc
        middleCirc = 'diameter = '+ mc + ';'
        global proximalLength
        proximalLength = 'height = '+ pl + ';'
        global proximalCirc
        proximalCirc = 'diameter = '+ pc + ';'
        a = [distalLength, distalCirc, middleLength, middleCirc, proximalLength, proximalCirc]
        return a

    #Send Button to send user data to label
    send = Button( w, text="Send", width=10, height=1, command=printValue)
    send.config(font=("courier",14))
    send.grid(row=7, column=0, pady=5)

    #Generate button to add measurements to CAD files input and generate CAD output files
    generate = Button(w, text="Generate", width=10, height=1, command=getValue)
    generate.config(font=("courier",14))
    generate.grid(row=7, column=1, pady=5)

    #Prepare button initiates CAMscript and outputs the GCODE files to CAM files
    prepare = Button(w, text="CAD", width=10, height=1, command=CADinput)
    prepare.config(font=("courier",14))
    prepare.grid(row=8, column=0, pady=5)

    #Prepare for manufacturing
    button_exit = Button(w, text="CAM", width=10, height=1, command=CAMinput)
    button_exit.config(font=("courier",14))
    button_exit.grid(row=8, column=1, pady=5)

    #Exit button
    button_exit = Button(w, text="Exit", width=10, height=1, command=w.destroy)
    button_exit.config(font=("courier",14))
    button_exit.grid(row=9, column=0, columnspan=2, pady=5)

    w.mainloop()

    eti = time.time()

    interface_execution_time = eti - sti
    print('Interface execution time: ', time.strftime("%H:%M:%S", time.gmtime(interface_execution_time)))

    a = [distalLength, distalCirc,
         middleLength, middleCirc,
         proximalLength, proximalCirc]
    return a

#CAD input

def CADinput():

    st = time.time()

    #START DISTAL

    #initialize and connect to app
    app = Application(backend='uia').start(r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    app = Application(backend='uia').connect(path=r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    #click on File item on the Menubar
    fileMenu = app.UntitledScadOpenScad.child_window(title="File", control_type="MenuItem").wrapper_object()
    fileMenu.click_input()

    #click on Open item in the File Menu
    fileOpen = app.UntitledScadOpenScad.child_window(title="Open File", auto_id="MainWindow.fileActionOpen", control_type="MenuItem").wrapper_object()
    fileOpen.click_input()

    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.UntitledScadOpenScad.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.UntitledScadOpenScad.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD input files folder
    fileOpenOSC = app.UntitledScadOpenScad.child_window(title="CAD input files", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenOSC.click_input(double = True)

    #double-click on Distal.scad file
    fileOpenDistal = app.UntitledScadOpenScad.child_window(title="Distal.scad", auto_id="0", control_type="ListItem").wrapper_object()
    fileOpenDistal.click_input(double = True)

    #insert measured height from Python script into CAD input script
    #distalLength = 'height = 30;'
    app.DistalScadOpenScad.type_keys(distalLength)

    #insert measured circumference from Python script into CAD input script
    #distalCirc = 'diameter = 15;'
    app.DistalScadOpenScad.type_keys(distalCirc)

    #click on the Design MenuItem on the Menubar
    designMenu = app.DistalScadOpenScad.child_window(title="Design", control_type="MenuItem").wrapper_object()
    designMenu.click_input()

    #click on the Render item from Menubar
    fileRender = app.DistalScadOpenScad.child_window(title="Render", auto_id="MainWindow.designActionRender", control_type="MenuItem").wrapper_object()
    fileRender.click_input()
    
    #wait 5 minutes to render before moving on
    time.sleep(360)
    #app.DistalScadOpenScad.print_control_identifiers()

    #click on Export as STL icon from Editor Menubar
    fileExportSTL = app.DistalScadOpenScad.child_window(title="Export as STL", control_type="Button").wrapper_object()
    fileExportSTL.click_input()

    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.DistalScadOpenScad.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.DistalScadOpenScad.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD output files folder
    fileOpenSTL = app.DistalScadOpenScad.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    fileOpenSTL.click_input(double = True)

    #click on the Save button
    fileSave = app.DistalScadOpenScad.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    fileSave.click_input()

    #click Yes button to accept overwrite
    fileAcceptOverwrite = app.DistalScadOpenScad.child_window(title="Yes", auto_id="CommandButton_6", control_type="Button").wrapper_object()
    fileAcceptOverwrite.click_input()

    #END DISTAL

    #---

    #START MIDDLE

    #initialize and connect to app
    #app = Application(backend='uia').start(r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    #app = Application(backend='uia').connect(path=r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    #click on File item on the Menubar
    fileMenu = app.DistalScadOpenScad.child_window(title="File", control_type="MenuItem").wrapper_object()
    fileMenu.click_input()

    #click on Open item in the File Menu
    fileOpen = app.DistalScadOpenScad.child_window(title="Open File", auto_id="MainWindow.fileActionOpen", control_type="MenuItem").wrapper_object()
    fileOpen.click_input()

    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.DistalScadOpenScad.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.DistalScadOpenScad.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD input files folder
    fileOpenOSC = app.DistalScadOpenScad.child_window(title="CAD input files", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenOSC.click_input(double = True)

    #double-click on Middle.scad file
    fileOpenMiddle = app.DistalScadOpenScad.child_window(title="Middle.scad", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenMiddle.click_input(double = True)

    #insert measured height from Python script into CAD input script
    #middleLength = 'height = 55;'
    app.MiddleScadOpenSCAD.type_keys(middleLength)

    #insert measured circumference from Python script into CAD input script
    #middleCirc = 'diameter = 15;'
    app.MiddleScadOpenSCAD.type_keys(middleCirc)

    #click on the Design MenuItem on the Menubar
    designMenu = app.MiddleScadOpenSCAD.child_window(title="Design", control_type="MenuItem").wrapper_object()
    designMenu.click_input()

    #click on the Render item from Menubar
    fileRender = app.MiddleScadOpenSCAD.child_window(title="Render", auto_id="MainWindow.designActionRender", control_type="MenuItem").wrapper_object()
    fileRender.click_input()

    #wait 5 minutes to render before moving on
    time.sleep(360)

    #click on Export as STL icon from Editor Menubar
    fileExportSTL = app.MiddleScadOpenSCAD.child_window(title="Export as STL", control_type="Button").wrapper_object()
    fileExportSTL.click_input()
    
    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.MiddleScadOpenSCAD.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)
    
    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.MiddleScadOpenSCAD.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD output files folder
    fileOpenSTL = app.MiddleScadOpenSCAD.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    fileOpenSTL.click_input(double = True)

    #click on the Save button
    fileSave = app.MiddleScadOpenSCAD.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    fileSave.click_input()

    #click Yes button to accept overwrite
    fileAcceptOverwrite = app.MiddleScadOpenSCAD.child_window(title="Yes", auto_id="CommandButton_6", control_type="Button").wrapper_object()
    fileAcceptOverwrite.click_input()

    #END MIDDLE

    #---

    #START PROXIMAL

    #initialize and connect to app
    #app = Application(backend='uia').start(r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    #app = Application(backend='uia').connect(path=r"C:\Program Files\OpenSCAD\OpenSCAD.exe")

    #click on File item on the Menubar
    fileMenu = app.MiddleScadOpenSCAD.child_window(title="File", control_type="MenuItem").wrapper_object()
    fileMenu.click_input()

    #click on Open item in the File Menu
    fileOpen = app.MiddleScadOpenSCAD.child_window(title="Open File", auto_id="MainWindow.fileActionOpen", control_type="MenuItem").wrapper_object()
    fileOpen.click_input()

    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.MiddleScadOpenSCAD.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.MiddleScadOpenSCAD.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD input files folder
    fileOpenOSC = app.MiddleScadOpenSCAD.child_window(title="CAD input files", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenOSC.click_input(double = True)

    #double-click on Proximal.scad file
    fileOpenProximal = app.MiddleScadOpenSCAD.child_window(title="Proximal.scad", auto_id="2", control_type="ListItem").wrapper_object()
    fileOpenProximal.click_input(double = True)

    #insert measured height from Python script into CAD input script
    #proximalLength = 'height = 55;'
    app.ProximalScadOpenScad.type_keys(proximalLength)

    #insert measured circumference from Python script into CAD input script
    #proximalCirc = 'diameter = 15;'
    app.ProximalScadOpenScad.type_keys(proximalCirc)

    #click on the Design MenuItem on the Menubar
    designMenu = app.ProximalScadOpenScad.child_window(title="Design", control_type="MenuItem").wrapper_object()
    designMenu.click_input()

    #click on the Render item from Menubar
    fileRender = app.ProximalScadOpenScad.child_window(title="Render", auto_id="MainWindow.designActionRender", control_type="MenuItem").wrapper_object()
    fileRender.click_input()

    #wait 5 minutes to render before moving on
    time.sleep(360)

    #click on Export as STL icon from Editor Menubar
    fileExportSTL = app.ProximalScadOpenScad.child_window(title="Export as STL", control_type="Button").wrapper_object()
    fileExportSTL.click_input()

    #navigate to libraries
    #app.UntitledScadOpenScad.print_control_identifiers()
    fileUp = app.ProximalScadOpenScad.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #double-click on fingerPrint folder
    fileOpenFingerPrint = app.ProximalScadOpenScad.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    fileOpenFingerPrint.click_input(double = True)

    #double-click on CAD output files folder
    fileOpenSTL = app.ProximalScadOpenScad.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    fileOpenSTL.click_input(double = True)

    #click on the Save button
    fileSave = app.ProximalScadOpenScad.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    fileSave.click_input()

    #click Yes button to accept overwrite
    fileAcceptOverwrite = app.ProximalScadOpenScad.child_window(title="Yes", auto_id="CommandButton_6", control_type="Button").wrapper_object()
    fileAcceptOverwrite.click_input()

    #click on File MenuItem on the Menubar
    fileMenu2 = app.ProximalScadOpenScad.child_window(title="File", control_type="MenuItem").wrapper_object()
    fileMenu2.click_input()

    #click on Quit MenuItem on the Menubar
    fileQuit = app.ProximalScadOpenScad.child_window(title="Quit", auto_id="MainWindow.fileActionQuit", control_type="MenuItem").wrapper_object()
    fileQuit.click_input()

    #click on Discard to live oscScrpt unedited and good for a new run
    fileDiscard = app.ProximalScadOpenScad.child_window(title="Discard", control_type="Button").wrapper_object()
    fileDiscard.click_input()

    #END PROXIMAL

    et = time.time()

    elapsedTime = et - st

    print('CAD execution time: ', time.strftime("%H:%M:%S", time.gmtime(elapsedTime)))

#CAM input

def CAMinput():

    st = time.time()

    #START DISTAL

    #Open Cura
    app = Application(backend='uia').start(r"C:\Program Files\Ultimaker Cura 5.1.0\Ultimaker-Cura.exe")
    app = Application(backend='uia').connect(path=r"C:\Program Files\Ultimaker Cura 5.1.0\Ultimaker-Cura.exe")

    #Wait 10 seconds for Cura to load
    time.sleep(10)

    #click File MenuItem from Menubar
    clickCuraFile = app.UltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    clickCuraFile.click_input()

    #click Open Files MenuItem from Menubar
    clickCuraOpen = app.UltimakerCura.child_window(title="&Open File(s)...", control_type="MenuItem").wrapper_object()
    clickCuraOpen.click_input()

    #navigate to Desktop
    fileUp = app.UltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #app.UltimakerCura.print_control_identifiers()

    #click on fingerPrint icon
    clickFingerPrint = app.UltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAD out files folder
    clickCADoutput = app.UltimakerCura.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    clickCADoutput.click_input(double = True)

    #click on Distal.stl file
    clickDistal = app.UltimakerCura.child_window(title="Distal.stl", auto_id="0", control_type="ListItem").wrapper_object()
    clickDistal.click_input(double = True)

    #click Slice button
    clickCuraSlice = app.CE3DistalUltimakerCura.child_window(title="Slice", control_type="Button").wrapper_object()
    clickCuraSlice.click_input()

    #wait 10 seconds to slice
    time.sleep(10)

    #click Save to Disk button
    saveCuraToDisk = app.CE3DistalUltimakerCura.child_window(title="Save to Disk", control_type="Button").wrapper_object()
    saveCuraToDisk.click_input()

    #navigate to Desktop
    directDesktop = app.CE3DistalUltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    directDesktop.click_input(double = True)

    #click on fingerPrint folder
    clickFingerPrint = app.CE3DistalUltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAM files folder
    clickCAM = app.CE3DistalUltimakerCura.child_window(title="CAM files", auto_id="3", control_type="ListItem").wrapper_object()
    clickCAM.click_input(double = True)

    #save G-code file
    saveGCODE = app.CE3DistalUltimakerCura.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    saveGCODE.click_input()

    #overwrite existing files
    sayYes = app.FileAlreadyExists.child_window(title="Yes", control_type="Button").wrapper_object()
    sayYes.click_input()

    #app.CE3DistalUltimakerCura.print_control_identifiers()

    #click on File MenuItem from Menubar
    clickFile = app.CE3DistalUltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    clickFile.click_input()

    #click New Project MenuItem
    clickProject = app.CE3DistalUltimakerCura.child_window(title="&New Project...", control_type="MenuItem").wrapper_object()
    clickProject.click_input()

    #click Yes button to accept New Project
    sayYes = app.CE3DistalUltimakerCura.child_window(title="Yes", control_type="Button").wrapper_object()
    sayYes.click_input()

    #app.CE3DistalUltimakerCura.print_control_identifiers()

    #END DISTAL

    #---

    #START MIDDLE

    #click File MenuItem from Menubar
    clickCuraFile = app.UntitledUltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    clickCuraFile.click_input()

    #click Open Files MenuItem from Menubar
    clickCuraOpen = app.UntitledUltimakerCura.child_window(title="&Open File(s)...", control_type="MenuItem").wrapper_object()
    clickCuraOpen.click_input()

    #navigate to Desktop
    fileUp = app.UntitledUltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #click on fingerPrint icon
    clickFingerPrint = app.UntitledUltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAD out files folder
    clickCADoutput = app.UntitledUltimakerCura.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    clickCADoutput.click_input(double = True)

    #click on Middle.stl file
    clickMiddle = app.UntitledUltimakerCura.child_window(title="Middle.stl", auto_id="1", control_type="ListItem").wrapper_object()
    clickMiddle.click_input(double = True)

    #click Slice button
    clickCuraSlice = app.CE3MiddleUltimakerCura.child_window(title="Slice", control_type="Button").wrapper_object()
    clickCuraSlice.click_input()

    #wait 10 seconds to slice
    time.sleep(10)

    #click Save to Disk button
    saveCuraToDisk = app.CE3MiddleUltimakerCura.child_window(title="Save to Disk", control_type="Button").wrapper_object()
    saveCuraToDisk.click_input()

    #navigate to Desktop
    directDesktop = app.CE3MiddleUltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    directDesktop.click_input(double = True)

    #click on fingerPrint folder
    clickFingerPrint = app.CE3MiddleUltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAM files folder
    clickCAM = app.CE3MiddleUltimakerCura.child_window(title="CAM files", auto_id="3", control_type="ListItem").wrapper_object()
    clickCAM.click_input(double = True)

    #save G-code file
    saveGCODE = app.CE3MiddleUltimakerCura.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    saveGCODE.click_input()

    #overwrite existing files
    sayYes = app.FileAlreadyExists.child_window(title="Yes", control_type="Button").wrapper_object()
    sayYes.click_input()

    #click on File MenuItem from Menubar
    clickFile = app.CE3MiddleUltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    clickFile.click_input()

    #click New Project MenuItem
    clickProject = app.CE3MiddleUltimakerCura.child_window(title="&New Project...", control_type="MenuItem").wrapper_object()
    clickProject.click_input()

    #click Yes button to accept New Project
    sayYes = app.CE3MiddleUltimakerCura.child_window(title="Yes", control_type="Button").wrapper_object()
    sayYes.click_input()

    #END MIDDLE

    #---

    #START PROXIMAL

    #click File MenuItem from Menubar
    clickCuraFile = app.UntitledUltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    clickCuraFile.click_input()

    #click Open Files MenuItem from Menubar
    clickCuraOpen = app.UntitledUltimakerCura.child_window(title="&Open File(s)...", control_type="MenuItem").wrapper_object()
    clickCuraOpen.click_input()

    #navigate to Desktop
    fileUp = app.UntitledUltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    fileUp.click_input(double = True)

    #click on fingerPrint icon
    clickFingerPrint = app.UntitledUltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAD out files folder
    clickCADoutput = app.UntitledUltimakerCura.child_window(title="CAD output files", auto_id="2", control_type="ListItem").wrapper_object()
    clickCADoutput.click_input(double = True)

    #click on Proximal.stl file
    clickProximal = app.UntitledUltimakerCura.child_window(title="Proximal.stl", auto_id="2", control_type="ListItem").wrapper_object()
    clickProximal.click_input(double = True)

    #click Slice button
    clickCuraSlice = app.CE3ProximalUltimakerCura.child_window(title="Slice", control_type="Button").wrapper_object()
    clickCuraSlice.click_input()

    #wait 10 seconds to slice
    time.sleep(10)

    #click Save to Disk button
    saveCuraToDisk = app.CE3ProximalUltimakerCura.child_window(title="Save to Disk", control_type="Button").wrapper_object()
    saveCuraToDisk.click_input()

    #navigate to Desktop
    directDesktop = app.CE3ProximalUltimakerCura.child_window(title="Start of Quick Access - Desktop (pinned)", control_type="TreeItem").wrapper_object()
    directDesktop.click_input(double = True)

    #click on fingerPrint folder
    clickFingerPrint = app.CE3ProximalUltimakerCura.child_window(title="fingerPrint", auto_id="1", control_type="ListItem").wrapper_object()
    clickFingerPrint.click_input(double = True)

    #click CAM files folder
    clickCAM = app.CE3ProximalUltimakerCura.child_window(title="CAM files", auto_id="3", control_type="ListItem").wrapper_object()
    clickCAM.click_input(double = True)

    #save G-code file
    saveGCODE = app.CE3ProximalUltimakerCura.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
    saveGCODE.click_input()

    #overwrite existing files
    sayYes = app.FileAlreadyExists.child_window(title="Yes", control_type="Button").wrapper_object()
    sayYes.click_input()

    #click on File MenuItem from Menubar
    closeCura = app.CE3ProximalUltimakerCura.child_window(title="&File", control_type="MenuBar").wrapper_object()
    closeCura.click_input()

    #click on Close MenuItem from Menubar
    quitCura = app.CE3ProximalUltimakerCura.child_window(title="&Quit", control_type="MenuItem").wrapper_object()
    quitCura.click_input()

    #END MIDDLE

    et = time.time()

    elapsedTime = et - st

    print('CAM execution time: ', time.strftime("%H:%M:%S", time.gmtime(elapsedTime)))

#call function
INTERFACEinput()