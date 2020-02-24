<h1>Meyita Analytics Dashboard</h1>

<h3>Purpose</h3>
    <p>
        It seems that everyday I see someone post a "study" on social media which magically proves all their views
        However, everytime I dig into the logic and math which the study bases its claims there is always
        blantant issues which, in my academic and professional experience, would be grounds for expolsion 
        or termination of employment.  Instead of agruing with people I hope that these dashboards can help
        either prove their opinions or help them see truth in the confusion that is the modern media.  I am 
        going to forgo adding my opinion or bias and just present facts.  I am not a democrat or republican and have 
        true disbain for both political parties.  Questions, concerns and comments are always welcome.  All data gathered 
        for this dashboard will be available in it's raw format with references to where I got it from.  Lastly, if
        anybody has problems with anything presented please email said concern to ryan.j.schulte@gmail.com.
    </p>
    
<h3>Web Application</h3>
    <p>
        This website was built using plotly's dash library.  Dash is basically an awesome graphing 
        library similar to D3.js built on top of flask.  I am also using a dash-bootstrap theme for
        the css.
    </p>
    
    - Database 
        
        An AWS postgres database was created for this dashboard but was not included in the finished
        product.  I basically used it for etl purposes as I am comfortable with sql / T-sql.  The queries
        were ran and dumped to csv files.  If anybody wants a copy of the db I can send you the pg_dump file.  
        
    - Calculations
        
        The majority of calculations were made using python pandas.  Pandas is the standard for this 
        type of dashboard.  
        
<h2>Dashboards</h2>

    <p>Dashboards are selected by the public.  If you have a topic you would like to see please contact via email, social media or              create a request in this repository</p>
    
    <h4>Big Pharma Dashboard</h4>
        
        <p>This dashboard provides basic info for big pharma companies incorporated within the United States.  Along with basic company          preformance metrics, it also displays employee ratings in various categories.</p>
