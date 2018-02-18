from urllib.request import urlopen
from bs4 import BeautifulSoup
import load #local python file

#simple method to convert a month to it's numerical value
def month_to_number(string):
    m = {
        'jan': '1',
        'feb': '2',            
        'mar': '3',
        'apr': '4',
        'may': '5',
        'jun': '6',
        'jul': '7',
        'aug': '8',
        'sep': '9',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

#simple method to create a SKU value for later sorting
def date_to_sku(date):
    sku = ""

    #formatting month
    if len(date[0]) < 2:
        sku += "0"
    sku += date[0]

    #formatting day
    if len(date[1]) < 2:
        sku += "0"
    sku += date[1]

    return sku

#method for downloading templated HTML and appending container into the content
def render_html(container):
    #grabbing prewritten html
    html = load.prewritten_html()
    
    #parsing out container's data in HTML table form
    for row in container:
        #opening HTML table row
        html += '<tr>'

        #iterating over every data point except SKU as it's uneeded
        for data in row[1:]:
            #creating each HTML table data entry
            html += '<td>' + data + '</td>'

        #closing HTML table row
        html += '</tr>'

    #appending necessary closing tags
    html += load.html_footer()

    #passing html into BeautifulSoup before writting to file
    html_soup = BeautifulSoup(html, "html.parser")

    #converting the HTML string into an HTML file
    f = open("index.html", "w")
    f.write(html_soup.prettify())

    #closing file writer
    f.close()
    

def main():
    #site url for downloading web content and storing available application links
    site_url = "https://www.dhamma.org/"
    
    #creating the main container to hold sorted course data
    container = []
    
    #creating a list of all the meditation centers to be web scraped
    centers = load.center_list()
    for center in centers:
        #establishing connection to site and downloading page content
        url_connect = urlopen(site_url+center[0])
        page_html = url_connect.read()
        url_connect.close()

        #using beautiful soup to parse html
        page_soup = BeautifulSoup(page_html, "html.parser")

        #grabbing all table row data for 10-day courses
        rows = page_soup.findAll("tr", {"class":"10-Day"})

        for row in rows:
            #parsing course status
            status = ""
            for span in row.findAll({'span'})[2:]:
                status += span.text
                if span.text[-1] != '.':
                    status += '.'
                status += '\n'
            if "Completed" in status:
                continue

            #parsing application link
            if 'apply' in row.a.text.lower():
                course_link = str(row.a)
                #adding absolute URL where it doesn't already exist
                if course_link[9] == '/':
                    course_link = course_link[:9] + site_url[:-1] + course_link[9:]
            else:
                course_link = "Not available"

            #parsing course type
            course_type = row.findAll({'td'})[2].text

            #parsing start date
            start_date = row.findAll({'span'})[0].text
            
            #creating SKU number for easy look up when sorting
            date = start_date.split()
            date[0] = month_to_number(date[0])
            sku = date_to_sku(date)

            #parsing end date
            end_date = row.findAll({'span'})[1].text

            #parsing course location
            location = row.findAll({'td'})[-2].text.strip()
            if ',' not in location:
                location += center[1]

            #parsing comments
            comments = row.findAll({'td'})[-1].text.strip()
            if not comments:
                comments = "None."
            elif comments[-1] != '.':
                comments += '.'
            if comments == "Allergy Information.":
                comments = '<a href="http://www.kunja.dhamma.org/CourseInformation.html#allergies">'+comments+'</a>'

            #appending relevant data into sub-arrays to be stored into main container
            container.append([sku, start_date, end_date, location, course_type, course_link, status, comments])
    
    #sorting main container based on SKU results
    container.sort(key=lambda x: x[0])

    #passing sorted container to custom HTML builder method
    render_html(container)

if __name__ == "__main__":
    main()