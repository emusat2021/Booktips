# Booktips

This project is the third Milestone Project in the "Python and Data Centric Development" course at <a href="https://codeinstitute.net/" target="_blank">Code Institute</a>.

**Book Tips** compiles the best and most popular books and creative reviews.
It’s a fun and interactive way to geek out over your favorite reads and discover all the coolest new titles you won’t find anywhere else.

The live website of [**Book Tips**](https://booktips-em.herokuapp.com/) can be viewed [here](https://booktips-em.herokuapp.com/)


<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project goals 

- Making a full-stack site that allows users to manage a common dataset about a particular domain. 
- Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask and MongoDB.

- Creating a website as a discovery tool for readers, highlighting the best new books.
- Creating a website that is simple to understand and easy to navigate.
- The users of the website can make use of CRUD (create, read, update and delete) for the books and reviews. 

<span id="ux-stories"></span>

### 1.2 User stories 

**First-time visitor/unregistered user goals:**
As a... | I want to... | To be able to...
---------|--------------|--------------
First Time Visitor | visit the website | see a list of books.
First Time Visitor | visit the website | see reviews on books.
First Time Visitor | search for a book | quickly find what I'm looking for
First Time Visitor | register on the website | add new books and write reviews.
<br>

**Registered user goals:** 

As a... | I want to... | To be able to...
---------|--------------|--------------
Registered User | login into the website | add new book
Registered User | login into the website | add reviews on books
Registered User | login into the website | change my reviews on books
Registered User | login into the website | delete my reviews on books
Registered User | login into the website | change my profile (password, photo, name, email)
Registered User | login into the website | delete my accountas well as reviews and votes
Registered User | find a list of options in the menu | use the website anytime and anywhere
Registered User | access the website from any device | delete my reviews on books
<br>


<span id="ux-design"></span>

### 1.3 Design 

- #### Colour scheme 
    Main colour palette:
    - #5e35b1 deep-purple darken-1;
    - #311b92 deep-purple darken-4;
    - #ede7f6 deep-purple lighten-5;
    - #01579b light-blue darken-4;
    - 

- #### Icons
The icons used in the project are provided by [Font Awesome](https://fontawesome.com/). The Icons have functional purposes, such as the hamburger menu. 

- #### Images
The images I used for this project came from [OpenLibrary](https://openlibrary.org/). Images are used for the home page and all the reviews. 

- #### Defensive design 

    - The user is not able to break the site by clicking on buttons. 
    - The signup form: 
        - The username must be between 5-15 characters and must only contain letters and numbers. 
        - The password must be between 5-15 characters and must contain at least one number, one uppercase and one lowercase letter.
    - The email address must be in the following format: characters followed by a @ symbol, followed by more characters and then a ".".

- #### Interactive design 

  - The website has to be easy to navigate. 
  - The user can quickly find the information he/she wants to find. 


<span id="ux-architecture"></span>

### 1.4 Database architecture
The project has four collections in the database. The database structure in MongoDB is as follows: 
- there are 4 collections: books, profiles, reviews, users;
- there are 2 indexes on book_title and book_author_name
More details about the database structure is in the [Deployment section](#deployment)


<span id="ux-mockup"></span>

### 1.5 Mockup designs
Mockup designs are made with [Balsamiq.](https://www.balsamiq.com/)

Initial wireframes with some comments for both desktop and mobile devices can be found [here](https://github.com/emusat2021/Booktips/tree/main/wireframes).

<span id="features"></span>

<h1>2. Features</h1>

<span id="features-existing"></span>

### 2.1 Existing features 

#### 1. Design 
- An attractive and simple layout with consistency.
- Simple navigation throughout the website by using the navigation bar. 
- Showing added books simple and clearly

#### 2. General 
- The home page shows an introductory text followed by a search box. Underneath there is a list of all books.
- Unregistered users are able to register on the "Register" page

#### 3. Books and Reviews
- Books and reviews can be created, read, updated and deleted (CRUD) by the users. 
- Users can search for Books using the search bar. 
- Users have access to their profile, with an overview of all their added books and reviews. 

#### 4. Register, login and logout 
- An unregistered user can create a new account on the web application.
- Registered users can login with their existing accounts. 
- Registered users can easily log out.
- If a user creates a new account, logs in or logs out, a flash message will appear as feedback for the user. 

<span id="features-future"></span>

### 2.2 Features left to implement in the future 
- Adding votes. Users vote their favorite books and can see them on their profile page. 
- Add categories for books. 
- Instead of using URLs for the book covers, we could implement a new feature to upload the cover as an image. 
- A book or a review should not be deleted by just one click. If someone clicks on the delete button, there will be a pop-up with a confirmation.
- Add pagination for the list of books and the list of reviews
- Add functionality for an Administrator account which is able to delete any book, review or profile
- When the user is logged in, write the user's username on the navbar
<span id="technologies"></span>

<h1>3. Technologies used</h1>

#### Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 provides the structure and the content for my project. 
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 provides the style of the HTML5 elements.
- [jQuery](https://jquery.com/)
    - jQuery used as the JavaScript functionality.
- [Python](https://www.python.org/)
    - Python provides the backend of the project.

#### Frameworks, libraries & Other
- [Gitpod](https://www.gitpod.io/) 
    - The GitPod is used to develop the project.
- [Git](https://git-scm.com/)
    - The Git was used for version control to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
    - The GitHub is used to host the project.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts is used to provide the font roboto for all the text that is used in the project. 
- [Balsamiq](https://www.balsamiq.com/)
    - Figma is used to create the mockup designs for the project.
- [Materialize](https://materializecss.com/)
    - Materialize is used for the design framework.
- [MongoDB](https://www.mongodb.com/1)
    - MongoDB is the fully managed cloud database service used for the project.
- [Heroku](https://dashboard.heroku.com/)
    - Heroki is the cloud platform to deploying the app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is the web framework used to provide libraries, tools and technologies for the app.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Jinja is used for Python templating
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - Werkzeug is used for password hashing and authentication and autohorization.

#### Testing tools used 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) is used to detect problems and test responsiveness.
- [Autoprefixer](https://autoprefixer.github.io/)
    - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code. 
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
    - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code. 
- [PEP8](http://pep8online.com/)
    - The PEP8 validator is used to check whether there were any errors in the Python code.
- [Black](https://pypi.org/project/black/)
    - Black is the uncompromising Python code formatter.
