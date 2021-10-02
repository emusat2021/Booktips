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

