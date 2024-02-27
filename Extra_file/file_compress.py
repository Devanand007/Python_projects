import PySimpleGUI as Sg

label1 = Sg.Text("Select file to compress:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose")

label2 = Sg.Text("Select destination folder:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose")

compress_button = Sg.Button("Compress")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()