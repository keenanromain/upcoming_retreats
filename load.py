def center_list():
    return ([
    ["en-US/schedules/schdelaware", ", Delaware"],
    ["en-US/schedules/schmahavana", ", California"],
    ["en-US/schedules/schdhara", ", Massachusetts"],
    ["en-US/schedules/schsiri", ", Texas"],
    ["en-US/schedules/schmanda", ", California"],
    ["en-US/schedules/noncenter/rockies.us", ", Colorado"],
    ["en-US/schedules/schpatapa", ", Georgia"],
    ["en-US/schedules/schpasava", ", Idaho"],
    ["en-US/schedules/schpakasa", ", Illinois"],
    ["en-US/schedules/schvaddhana", ", California"],
    ["en-US/schedules/schkunja", ", Washington"],
    ["en-US/schedules/schvisuddhi", ", Wisconsin"]
    ])

def prewritten_html():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>
    Upcoming Vipassana Retreats
    </title>
    <link href="https://fonts.googleapis.com/css?family=Poly: 100,300,400,700|Luckiest+Guy|Oxygen:300,400" rel="stylesheet">
    <link href="style.css" type="text/css" rel="stylesheet">
    </head>
    <body>
    <ul class="navigation">
    <li>
    <img src="./logo.png" height="30px;">
    </li>
    </ul>
    <table>
    <thead>
    <tr>
    <th scope="col">
    Start Date
    </th>
    <th scope="col">
    End Date
    </th>
    <th scope="col">
    Location
    </th>
    <th scope="col">
    Course Type
    </th>
    <th scope="col">
    Application Link
    </th>
    <th scope="col">
    Course Status
    </th>
    <th scope="col">
    Additional Comments
    </th>
    </tr>
    </thead>
    <tbody>
    '''

def html_footer():
    return '''
    </tbody>
    </table>
    <footer class="search">
    <p>
    The information provided by this website is for the purpose of helping meditators find a retreat to attend. All data originates from <a href="https://www.dhamma.org">dhamma.org</a>. 
    </p>
    <p>
    The existence of this website does not imply any affiliation with or endorsement by the official Dhamma.org organization.
    </p>
    <p>
    For more information, feel free to research Vipassana Mediation or click <a href="https://www.dhamma.org">here</a> to get started.
    </p>
    <p>
    Source code can be found <a href="https://github.com/upcomingretreats/upcomingretreats.github.io">here</a> and all credits go to <a href="https://logomakr.com/">Logomakr</a> for the logo design.
    </p>
    </footer>
    </body>
    </html>
    '''
