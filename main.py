import pyperclip
from dict_journal import dict_journal

def get_file_from_input(input_file):
    # obtain content from the input file
    file_list = []
    with open(input_file, "r",encoding= 'utf-8' ) as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            # line = line.split('.')[0]
            line = line + ".md"
            file_list.append(line)
    return file_list

# obtain content from the clipboard
def paste_content_from_clipboard(_quiet=True):
    content = pyperclip.paste()
    if _quiet == True:
        print(content)
    return content

def copy_content_to_clipboard(content):
    pyperclip.copy(content)

def access_content_from_md(md_file):

    folder_path = "C:/Users/admin/Nutstore/1/Gnote/02_science/Paper_link/"
    file_path = folder_path + md_file

    # read
    with open(file_path, "r",encoding= 'utf-8') as f:
        content = f.read()
    return content

def search_item_from_content(item,item_next,content,_quiet=True):
    # search item from content
    item_posi_start = content.find(item)
    item_posi_end = content.find(item_next)
    len_item = len(item)
    len_item_next = len(item_next)
    item_content = content[item_posi_start+len_item+2:item_posi_end-3]
    if _quiet == True:
        print(item_content)
    return item_content

def get_abbrev_from_journal(journal):
    # get the abbreviation from the journal
    # check if the journal is in the dict
    if journal in dict_journal.keys():
        journal_abbrev = dict_journal[journal]
        return journal_abbrev
    else:
        print("GYC: The journal is not in the dict.")
        print("GYC: The missing journal is: ",journal)
        exit()

def count_author(author,_quiet=True):
    # count the number of authors
    count = author.count(";")
    if _quiet == True:
        print(count)
    return count

def get_author(author,_quiet=True):
    # get the author
    author_list = author.split(";")
    if _quiet == True:
        print(author_list)
    return author_list

def generate_author_in_citation(author_list,count,_quiet=True):
    # generate the author in citation
    if count == 1:
        author_abbrev = author_list[0].split(",")[0].strip().split(" ")[0]
        author_in_citation = author_abbrev
    elif count == 2:
        author_abbrev_1 = author_list[0].split(",")[0].strip().split(" ")[0]
        author_abbrev_2 = author_list[1].split(",")[0].strip().split(" ")[0]
        author_in_citation = author_abbrev_1 + " & " + author_abbrev_2
    elif count >= 3:
        author_abbrev = author_list[0].split(",")[0].strip().split(" ")[0]
        author_in_citation = author_abbrev + " *et al.*"
    if _quiet == True:
        print(author_in_citation)

    return author_in_citation

def convert_into_italics(content):
    # convert into italics
    content = '*'+content+'*'
    return content


if __name__ == "__main__":

    input_file = "in.txt"
    quiet      = True
    file_list  = get_file_from_input(input_file)
    # print(file_list)

    for file in file_list:
        content                = access_content_from_md(file)
        title                  = search_item_from_content("**Title**", "**Author**", content, quiet).strip()
        journal                = search_item_from_content("**Journal**", "**DateAdded**", content, quiet).strip()
        year                   = search_item_from_content("**Year**", "**Journal**", content, quiet).strip()
        author                 = search_item_from_content("**Author**", "**Year**", content, quiet).strip()
        author_list            = get_author(author, quiet)
        journal_abbrev         = get_abbrev_from_journal(journal)
        journal_abbrev_italics = convert_into_italics(journal_abbrev)
        author_in_citation     = generate_author_in_citation(author_list, len(author_list), quiet)
        citation               = author_in_citation + ", " + journal_abbrev_italics + ", " + year

        # write citation to the clipboard
        copy_content_to_clipboard(citation)