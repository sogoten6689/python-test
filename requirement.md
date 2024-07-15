 We build a service that collects hourly search volume of different keywords.
 Daily data will be the record of 9:00AM every day or nearest time of the day if 9:00AM data is not available.
 Users can subscribe and query the search volume hourly or daily in a range of time of any keyword.
 Users can subscribe to the overlap timeline of a keyword and will see the union range of them.
 Users who subscribe daily will not see data hourly but users who subscribe hourly will see the daily data.
 ---------------------
 
 Original 2 tables for record metrics look like this:
 
 1. keyword:
 keyword_id - bigint
 keyword_name - varchar(255)
 primary key (keyword_id)
 
 2. keyword_search_volume:
 keyword_id - bigint
 created_datetime - datetime (hourly format - yyyy-MM-dd HH:00:00)
 search_volume - bigint
 primary key (keyword_id, created_datetime)
 
 ---------------------
 
 Requirement:
 1. Redesign database to support above use case (Make a MySQL schema script, add new required tables and columns).
 2. Write a script in Python or Java to generate data for 10 keywords, 3 months.
 3. Insert subscribe examples for all cases you can think about.
 4. Write HTTP service in Python or Java to support query data
     Input in JSON:
         - user ID
         - list keywords
         - timing (hourly/daily)
         - start time
         - end time
     Return in JSON:
         - the search volume in the time range of input keywords following user subscription
 5. Write the unit test for all cases you can think about.
 6. Write readme.md
     - How to run the test
     - Explain your design
     - Tell us the challenge that you have overcome
     - Tell us the challenge that you could not make it work and would like to learn more
 7. Record a video of how you run the test, explain your design by voice or subtext.
 
 Note that: you do not have to do all the requirements, just do the best that you can.
 You can deliver the test in a zip file (not rar file), upload to Google Drive and share us through this email.
 
 Good luck, have fun.