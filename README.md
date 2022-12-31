# E-shop - Book store
This is a store i created for my 5th project in the Code Institute Software Development Course. It is a simple book store with a small selection of books. It is called Dino's book store, after my cat. 

## UX - User Experience
### User Stories
Site user:
- Easily use and understand the website.
- Create account where they can see previous purchases.
- See products available. Including status and options.
- Add products to cart.
- Remove product from cart.
- Search for products.
- Navigate categories and get relevant results.
- Pay for products.

Admin user:
- Add/edit/remove products.
- See and cancel orders.
- Change stock numbers.

### Colour
I chose to make this e-store in blue- green shades. These colours were chosen due to it being a bit different than the online book-stores where i live (sweden), and due to a bluer green being appealing to the eye. The reason for the combination of the two was that it would help this store to differentiate itself from other similar stores, chich mostly use red or some shade of blue (for example royal blue). Another reason for my choice was the fact that the blue colour (according to, among others, the website [colour-meanings](https://www.color-meanings.com)) symbolices security and trust, and green symbolices harmony and safety. All the colour choices was checked in [accessibility checker](https://www.accessibilitychecker.org/color-contrast-checker/)'s contrast checker.

![colour-palette](misc/book-store-palette.png)
![colour-checker-blue-green](misc/colour-check-dark-green.PNG)
![colour-checker-light-green](misc/colour-check-light-green.PNG)

### Structure and typography 

#### Structure
I chose to create a simple structure, since the products are the thing that should attract attention. All products have a green background in the photos. This is so that they fit into the colour-palette while also attracting attention. Right below the navigation bar there is a darker field telling the user the name of the page. 

The base of the website is a simple navigation-bar with dropdown menues for products and accounts, and links for articles and home. These menues are in a dropdown-menue on the mobile version. I chose to place the search bar right below the dropdown menue and brand-name on the mobile view. That way there is no need to open a dropdown just to search for a product.

![Desktop nav]()
![Mobile nav]()

#### Typography
I chose to use the font "Rubik Bubbles" for the store name and main page titles. For everything else I used the font "Istok Web". Both of these are from [Google Fonts](). The fonts are also san-serif, which is easier to read on a screen than serif fonts.

The reason I chose these fonts were that they worked well with the colour palette. "Rubic Bubbles" is a softer font that also draws attention. "Istok Web" is inconspicous while also telling the user that effort was put into the website.

## Features
### Shop
The products in the shop can be shown based on their categories or the user can choose to show all the products in alphabetic order. When all products in a category is show they are sorted alphabetically by default. From the product card you can go to the product detail page. This is where the user can add products to the shopping bag.

There is also a search bar where users can find products. 

![Shop image](misc/shop-image.PNG)

#### Product card
A product card is created for each product found on the database. Each card shows an image. Either a specific product image, or if none is found, a placeholder image telling the user that there is no product image. They also show the name of the product, the author and the price. There is also a button for opening the product details. Below the button there is some muted text telling the user if the item is in stock or not. 

![product card image]()

#### Product details
When the user clicks on the button to get more information about a product, a page showing the information for the specific product opens. It shows the product image to the left, and all the other information about the product to the right (in the mobile view the image is above the information). Below the pruduct information is the quantity selector, "add to cart"/"out of stock" and "add to wishlist" buttons. If the stock numbers are below 1, the "out of stock" will show up. This button does not link to the shopping cart. If the product is in stock, the "add to cart" button will appear. This button will add the chosen quantity of an item to the cart. The wishlist button only appears if the user is signed in. 

![product detail image]()

### Bag

### Checkout

### Articles
The articles work similarly to the products. A preview of each article is shown on the articles page, and when the user click on an article they are sent to a page with the full article. The preview contains the title, the author, an introduction of the article (first paragraph) and a "read more" button. The page with the full article shows an image at the top (if there is one), the title, author and full article.

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
    - The products page shows which products exist and if they are in stock or not. If the user is loged in, they can also add a product to their wish-list.
- Add and remove products in the cart.
    - The user can add products to the cart from the product-detail page. They can remove them from the bag by going to the bag and clicking "remove" on the item they no longer want.
- Search for products.
    - The user can search for products thru the search-bar. When this is done, the program searches for matches in, among others, the title and the description for the book. Only the books with a match to the search term shows up.
- Navigate categories and get relevant results.
    In the shop dropdown the user can choose to either show all products, or show the products in a specific category. If the user chooses "history", only the history books will show up. 
- Pay for products.

Admin user:
- Add/edit/remove products.
    - Thru the admin page the admin has the option to easily add, edit and delete products. They just need to input the information about the book and add the product. Every piece of information is specified by the input field.
- See and cancel orders.
- Change stock numbers.
    - On the page where the admin can manipulate the products, there is a field for each product called "stock". Here the admin can input the available stock. If the stock is 0, the user can not add the item to their cart.

### Device Testing
The website was natively tested on these devices:
- Acer Aspire 5
- 1440p monitor (hooked up to a tower pc)


The website was also tested on these devices thru Mozilla Dev Tools:
- Ipad
- 

### Browser Testing
The website was tested on these browsers:
- Mozilla Firefox
- Google Chrome
- Safari
- DuckDuckGo (mobile)

### Peer Review
- I showed the front-end to my dad, and he thought it looked good. The thing he asked about was the lack of images, which I had not yet gotten to. Other than that he thought it looked good and was easy to use. 

### Validator Testing

### Manual testing
- Tested the models by creating instances. This was to make sure the fields looked like they should and that everything worked as expected.
- Tested if the database and the frontend was propperly connected by trying to show part of the data in the frontend. 
- Made sure the search bar works by searching for words found in book titles, descriptions, languages and authors. The expected results were showed.
- While implementing the add-to-bag functionality, I first printed the values of the items to the consol, to make sure everyhting was working. After that I could make sure everything was working thru the bag itself, since it shows both the item, the total price, delivery price and the quantity.
- For the remove-from-bag functionality, I tested if it worked in the same way I did the add-to-bag function.

### Software Testing
#### JavaScript Testing - Jest

#### Python Testing

### Bugs
#### Fixed Bugs
- I had a bit of trouble getting the product view to work. The products would not show up on the website. I solved it when i realised the problem was caused by a spelling error. After i fixed the spelling, it all worked as expected. I later had a similar problem when i implemented the ability to filter by category. The first letter in the category needed to be upper-case, which i had forgotten.
- When I wrote the link to the product_details of the bag items, I could not get the product id to work. After a while i realised that i had been referencing the wrong id. Had similar problems later in the project too.

#### Unfixed bugs
- It is possible to add more products than there is in stock to the bag. If you do all you get is a message saying you added a higher amount than the current stock and that the shipping of these products will be delayed due to this.

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
- Create an account on ElephantSQL. Do not forget to confirm your e-mail.
- Click on "create a new instance" (it is a green button at the top right corner).
- Give the information about the instance.
    - Choose a name.
    - Choose a plan (tiny turtle is free, and the one i used for this project).
    - Add potential tags (not necessary)
    - Select a region and data center. Choose one close to you for the best connection.
- Preview the information to make sure everything is correct.
- Create instance.
- Click on your instance to see the information. 
- Copy the url and add it

## Credits
### Code
A lot of the backend code is based on the [boutique ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project from the Code Institute fullstack developer course. The code is adapted to fit my project.

For the frontend I used the [Shop Homepage](https://startbootstrap.com/template/shop-homepage) from [Start Bootstrap](https://startbootstrap.com). It is used for the navbar and footer, as well as for the product cards.

Some of the code is based on the code snippets provided in the [bootstrap](), and [django]() documentation.

### Content and Media
All pictures on the website are taken by me, and information about who wrote and published the book can be found on the [live site]() on each book's product page. The publisher can be seen on the covers. The description for the books also tells the user where the description was copied from. 

Erik Vodopivec Forsman, 2022
