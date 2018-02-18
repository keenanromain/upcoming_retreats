# upcoming_retreats

This project was built for good fun as an excercise in web scraping via Python's Beautiful Soup module.


The idea was to build a simple website that houses the data for all continental US 10-day Vipassana retreats.

## Key Details
The project was accomplished fairly quickly due to the reliability of <a href="https://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a> and the consistent design behind every meditation center's website. The back-end worked by first parsing the relevant data of each 10-day retreat, regardless of location. Then, the content is sorted by a numerical inventory unit based on the starting date of each retreat. Next, this information is passed on to the front-end which loads an HTML stub (with previously thought out CSS features) as a string and appends the scraped data as HTML table data. The HTML table is subsequently followed with a footer (which includes my non-affiliated disclaimer!) to seal up the content. Finally, the content is then passed back to Beautiful Soup to be prettified and written out to the index.html file.
