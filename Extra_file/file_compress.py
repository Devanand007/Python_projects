import PySimpleGUI as Sg
from zip_creater import make_archive

label1 = Sg.Text("Select file to compress:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose", key="files")

label2 = Sg.Text("Select destination folder:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="Folder")

compress_button = Sg.Button("Compress")
output_label = Sg.Text(key="Output")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['Folder']
    make_archive(filepaths, folder)
    window["Output"].update(value="Compression Completed")

window.close()
