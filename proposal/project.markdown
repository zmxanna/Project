# **Project: Portfolio Generator**
**Members: Brandon Hoang, Anna Zou, Rae Zhang**

### **The Big Idea:** 	
	
	    Our project aims to build a traditional investment portfolio generator that helps users explore and learn about potential investments and portfolio management. We will explore multiple asset classes within traditional investments, scraping data from sites like Yahoo Finance, performing data analytics on data extracted from sites, and outputting potential portfolios with data analytics results. The project will focus mainly on generating a portfolio consisting of stocks, ETFs, and treasury bills based on users’ unique profiles and investment needs. 
        The minimum viable product would be a simple generator that takes inputs such as: age, capital available, lock-up period, risk tolerance, and returns a rough portfolio for users to explore from. A stretch goal would be a more sophisticated generator that takes inputs such as: age, capital available, lock-up period, risk tolerance, specific sectors preferred/more concentrated, number of stocks preferred, market cap preference, beta preference, and returns a portfolio with corresponding performance measures like past performance against benchmarks, its probability of beating benchmarks, historical beta, and etc. 

### **Learning Goals:**

        One of our shared learning goals is to successfully design software that will help solve a defined problem that people may have utilizing Python. As a team, we have had little to no exposure to Python before this course. We hope that this project will be able to challenge us and facilitate a deeper understanding and application of Python. Another one of our shared learning goals is to learn how to web scrape or gather data online so that we can apply it, later on, to not only our professional lives but even also our personal lives. Since web scraping can potentially get very complicated and detailed, another one of our shared learning goals is to learn how to create programs utilizing APIs that are provided or are available to make the project feasible and our lives easier. We will also be able to learn and experience a complete software development cycle that includes planning before writing code, managing the coding process, and updating software. On a secondary note, another shared learning goal is to learn more about finance and investing by building an investment portfolio generator. As young adults, we believe learning about finance and investing as soon as possible is highly beneficial for our growth and development.

### **Implementation Plan:** 
 
**Step 1 Figure out financial part of project**
* Inputs, outputs, external data sources, financial analysis

**Step 2 Define sites and data needed**
* What websites to scrap and what data is being scraped

**Step 3 Set up project framework and start working**
* Libraries:
    * Accessing: Request
    * Parsing: Beautiful Soup or lxml 
    * Clicking needed: Selenium
    * Calculating: Numpy, Scipy, Pandas
    * Financial Analysis: QuantPy, empyrical
* **3.1 Accessing**
    * Establish connection with websites needed, request information
* **3.2 Parsing**
    * Extract data needed for project
* **3.3 Clicking needed**
    * Extract data that can only be accessed after clicks
* **3.4 Calculating**
    * Get input from users to calculate investments that suit their profiles
* **3.5 Financial Analysis**
    * Present some performance measures based on investments selected

**Step 4 Finalize project and start building website interface**
* Web design
* Interface design
* Connecting to program in Python
 
### **Project schedule:**

    Week 1 2/22     Step 1 & 2
    Week 2 3/1      Step 3.1 & 3.2
    Week 3 3/8      Step 3.3
    Week 4 3/15     Step 3.4
    Week 5 3/22     Step 3.4 (simplify model if necessary)
    Week 6 3/29     Step 3.5 (optional if 3.4 is complicated)
    Week 7 4/5      Step 4
    Week 8 4/12     Step 4, modifying, and finalizing



### **Collaboration plan:**

        As a team, we have already been functioning by splitting tasks up, completing them independently, and then integrating them. So far, this has worked well for us as we have slightly different schedules and are sometimes busy. This gives us the flexibility to work on our time while still ensuring things get done when they need to. As the project progresses and moves along the software development cycle, we may need to alter how we collaborate to something along the lines of pair programming if things become too complicated or difficult working individually. We communicate closely utilizing a Facebook messenger group chat and we frequently have calls to check-in and distribute work. 
        Based on how our team has been functioning already, a software development methodology that may suit us is agile development as we like to divide up the work but work cross-functionally at times to help each other out. As we continue to learn more about Python, we will surely have to plan adaptively and continue to improve in response to change or obstacles. After reading “Step-By-Step Team Workflow with Github Desktop”, we have identified ourselves to each of the three roles. Anna is the Organization/Club Lead who has set up the platform for our team and started the project. She is the repository owner and has given us access to the project. Rae is the Project Manager who will be mainly responsible for managing the pull requests. Brandon will be the Project Contributor who will be adding features and/or modifying the code. All three of us will actually be contributing to the projecting simultaneously.

### **Risks:**

        We are at the beginning stage of learning python therefore we may over expect our ability to carry out the project. Because this is our first time doing a project like this, it is easy to run into difficulties and challenges that we did not think of in the beginning. For example, before meeting with the professor, we did not consider web scraping may require knowledge of web design or some understanding of the web’s front end. Similar challenges may also arise when we go from project planning to the actual hands-on design of the project. 
        Furthermore, inaccurate estimation of our ability or what python can do may lead to the risk of running out of time. We don’t know what we don’t know, and we may not know what the right answer is to solve it because we have not learned that much about python yet. Last but not least, if we were able to successfully design and execute the codes, there are also risks of poor quality or the cleanliness of the code. But we believe working together as a team, asking the Professor for help, as well as self-learning on Google we can conquer these risks and challenges.  

### **Additional Course Content:** 

        One topic that we might cover in class that we think would be especially helpful for our project is working with APIs in Python. Another topic that might be helpful is going into a little bit of detail regarding Python interacting with HTML and CSS to understand web design aspects. Additionally, covering other complex libraries with professional applications such as math, statistics, tables, and visual modeling may be beneficial to our project.
