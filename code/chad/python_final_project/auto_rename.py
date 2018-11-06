import os, datetime, PyPDF2

print(f'You Are Working In A {os.name} EnVironment')

#Ask User To Set The Path Where PDFs Are Stored:
#path_input = input('What Path Are The PDFs Stored That You Would Like To Rename? > ')
path_input = input('What Is The Source Folder You Would Like To Work In? > ')
file_name = input('What Is the File Name You Would Like To Rename? > ')

# Function To keyword Map
def keyword_map():
    with open('/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/keywords.csv', 'r') as keywords:
        keyword_map = keywords.read().strip('\n').split('\n')
    keywords.close()
    return keyword_map

# Parse key_map into dictionary
def make_dict(keyword_map):
    final_listOfDic = []
    make_list = []

    # Loop over each index and split each index into a list
    for eachindex in keyword_map:
        make_list.append(eachindex.split(','))
    # Loop over each index and make a dictionary from each
    for eachindex in make_list:
        final_listOfDic.append({eachindex[0]:(eachindex[1], eachindex[2])})
    return final_listOfDic
    
# Open Pdf and extract useful data
def open_pdf():
    # with open('/tmp/doc_send/nwebill.pdf', 'rb') as pdf:
    #     pdfread = PyPDF2.PdfFileReader(pdf)
    # return pdfread
    #Had to resort to this way because the with open did not work
    f = open(source_file, 'rb')
    pdfread = PyPDF2.PdfFileReader(f)
    f.close
    return pdfread

def find_matches(keywords, ocrdata):
    #[{'keyword': ('type', 'to_dir')}, {'Northwestern Energy': ('Bill', '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_receive')}]
    #Extract ocr text from ocrdata
    page = ocrdata.getPage(0)
    extract_text = page.extractText()
    #For each dictionary in keywords
    for listindex in keywords:
        #For each keyword in dictionary
        for in_dict in listindex:
            #If key in dictionary (keyword) the extracted ocr text then return that whole dictionary
            if in_dict in extract_text:
                return listindex
        # if keys in extract_text:
        #     print('you found a match')

def file_format(keyword_match, ocrdata):
    final_filename = ''
#Get Creation Date For Rename Function
    final_date = ''
    page = ocrdata.getDocumentInfo()
    date = (page['/CreationDate'])
    print(date)
    date = date[2:12]
#I added two more characters on the timestamp to avoid any duplicates
    final_date += date[0:4] + '-' + date[4:6] + '-' + date[6:8] + '-' + date[8:10]
#Get type for file in dictionary from keyword
    file_type = list(keyword_match.values())
    final_type = str((file_type[0][0]))
#Get company name for file in dictionary from keyword
    keyword_name = list(keyword_match.keys())
    final_name = str(keyword_name[0])
#Construct string together for file rename operation
    final_filename += final_date + ' - ' + final_type + ' - ' + final_name

#Funciotn To Auto Rename File 
def auto_rename(file_formated):
#Source of File To Rename
    src =   
    os.rename(file_formated)

#Open keyword csv and split into a dictionary with key being the company.
#This will be used for the autorename and file move functions
keyword_map = keyword_map()
made_dict = make_dict(keyword_map)

#Open pdf file and return variable containing all the ocr information needed
opened_pdf = open_pdf()

#Compare ocr data with keywords to match
found_match = find_matches(made_dict, opened_pdf)

#Use matched data to generate file format for autorename function
file_formated = file_format(found_match, opened_pdf)

#Send file_formated into function to do actual file rename
auto_renamed = auto_rename(file_formated)