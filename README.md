# E-shop - Book store
This is a store i created for my 5th project in the Code Institute Software Development Course. It is a simple book store with a small selection of books. It is called Dino's book store, after my cat. 

## UX - User Experience
### User Stories
Site user:
- Easily use and understand the website.
- Create account where they can see previous purchases.
- See products available. Including status and options.
- Add products to cart.
- Search for products.
- Navigate categories and get relevant results.
- Pay for products.

Admin user:
- Add/edit/remove products.
- See and cancel orders.
- Change stock numbers.

### Colour
I chose to make this e-store in blue and green shades. These colours were chosen due to it being a bit different than the online book-stores where i live (sweden), and due to blue being appealing to the eye. The reason for the combination of the two was that it would help this store to differentiate itself from other similar stores, chich mostly use red or some shade of blue (for example royal blue). Another reason for my choice was the fact that the blue colour (according to, among others, the website [colour-meanings](https://www.color-meanings.com)) symbolices security and trust, and green symbolices harmony and safety. All the colour choices was checked in [accessibility checker](https://www.accessibilitychecker.org/color-contrast-checker/)'s contrast checker.

![colour-palette](misc/book-store-palette.png)
![colour-checker-blue-green](misc/colour-check-dark-green.PNG)
![colour-checker-light-green](misc/colour-check-light-green.PNG)

### Structure and typography 

#### Structure
I chose to create a simple structure, since the products are the thing that should attract attention. All products have a green background in the photos. This is so that they fit into the colour-palette while also attracting attention. Right below the navigation bar there is a darker field telling the user the name of the page. 

The base of the website is a simple navigation-bar with dropdown menues for products and accounts. These menues are in a main dropdown-menue on the mobile version. I chose to place the search bar at the top of the dropdown menue for the products. In the mobile version it is at the top of the main dropdown menue. 

#### Typography
I chose to use the font "Rubik Bubbles" for the store name and main page titles. For everything else I used the font "Titillium Web". Both of these are from [Google Fonts](). The fonts are also san-serif, which is easier to read on a screen than serif fonts.

The reason I chose these fonts were that they worked well with the colour palette. "Rubic Bubbles" is a softer font that also draws attention. "Istok Web" is inconspicous while also telling the user that effort was put into the website.

## Features
### Shop
The products in the shop can be shown based on their categories or the user can choose to show all the products in alphabetic order. When all products in a category is show they are sorted alphabetically by default. 

There is also a search bar where users can find products based on key words.

[Shop image](misc/shop-image.PNG)

### Bag

### Checkout

### Messages

### Admin
The admin can add, edit and remove products thru the admin page. They input all the info about the books and then they show up in the category chosen. If needed they can also add more categories. The same goes for the articles.

### Potential Features
- If I had the time I would expand on the sorting options and other features making it easier for the user to find the right product.
- I would also want to expand on the admin features. For example, make it possible to answer incoming messages in the admin window. 

## Testing

### User Stories
Site user:
- Easily use and understand the website.
- Create account where they can see previous purchases.
- See products available. Including status and options.
- Add products to cart.
- Search for products.
- Navigate categories and get relevant results.
- Pay for products.

Admin user:
- Add/edit/remove products.
    - Thru the admin page the admin has the option to easily add, edit and delete products. They just need to input the information about the book and add the product. Every piece of information is specified by the input field.
- See and cancel orders.
- Change stock numbers.

### Device Testing

### Browser Testing

### Peer Review

### Validator Testing

### Software Testing
#### JavaScript Testing - Jest

#### Python Testing

### Bugs
#### Fixed Bugs

#### Unfixed bugs

### Deployment
This project was deployed with Heroku.

- Create an account at Heroku, and do not forget you need to confirm your e-mail to do this.
- Create a list of dependencies in a text file named requirements (pip3 freeze > requirements.txt).
- Create an app by clicking the "create a new app" button found on the dashboard.
    - Choose a unique app name.
    - Choose your region and click "create app"
- Click on settings (for the app).
    - Find the Config Vars section and add potential files that you cannot upload to github. For example API credentials. KEY is the title, and VALUE is the content. For thos project you need to add the Django key and the database-url.
    - Add buildpacks (below Config Vars). For this project, I installed Python and Node.js. Make sure they are in the correct order.
- Go to the deploy section.
    - Choose to deploy from GitHub.
    - Connect your account and choose a repository to deploy from.
    - Choose either Automatic or Manual deployment (recommended).
- Make sure the live site is working.

The database is on ElephantSQL.
- Create an account on ElephantSQL.

## Credits
### Code
A lot of the backend code is based on the [boutique ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project from the Code Institute fullstack developer course.

For the frontend I used the [Shop item template](https://startbootstrap.com/template/shop-item), and the [Shop Homepage](https://startbootstrap.com/template/shop-homepage) from [Start Bootstrap](https://startbootstrap.com). The first one is used for the specific items, and the second one is for the shop page.

### Content and Media
All pictures of the books are taken by me, and information about who wrote and published the book can be found on the [live site]() on each book's product page.

Erik Vodopivec Forsman, 2022
