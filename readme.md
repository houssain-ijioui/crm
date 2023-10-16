Customer Relationship Management (CRM) system for order management:

- Distinctiveness and Complexity:

The CRM web application I have developed showcases a high degree of distinctiveness and complexity, leveraging the power of Django, JavaScript, and Bootstrap to create a seamless user experience with enhanced functionality and visual appeal. At the core of the application is the dynamic dashboard, built using Django and Bootstrap, where all customers and their corresponding phone numbers are displayed. Additionally, a link is provided to navigate to each customer's profile page, enriching the user's ability to access detailed information.

Within the dashboard, Django's templating engine and JavaScript are employed to exhibit all orders in an organized manner. Each order includes crucial information such as the associated product, the customer who placed the order, the order date, and its delivery status. With the aid of JavaScript, interactive buttons for updating and deleting orders are integrated, allowing users to efficiently modify and manage order data.
To enhance the user experience further, Bootstrap's alert component is utilized to display three cards on the dashboard. These cards dynamically present key insights, including the number of delivered orders, pending orders, and the total count of orders. By leveraging JavaScript and Bootstrap's alert functionality, the application provides real-time information to users, enabling them to make informed decisions based on order statuses With each user command, such as deleting an order or adding a customer, an alert is displayed at the top of the page to provide immediate feedback and ensure important actions are acknowledged.
 
In addition to the dashboard, the CRM web application incorporates a dedicated products page, developed using Django and Bootstrap, where users can conveniently view and manage the product inventory. By utilizing Bootstrap's responsive design and interactive elements, such as buttons and forms, users can easily add new products, ensuring a seamless product management experience.
 
The customer profile page, also built with Django and Bootstrap, showcases crucial customer details such as their name, email, and phone number. Leveraging Bootstrap's alert component, the application presents alerts for any relevant updates or notifications pertaining to the customer, ensuring effective communication and prompt action.
 
- File Structure:
app/migrations migrations for this project
app/static folders with css.
app/templates folder with 7 .html files and the javascript at the top so that the user can delete, update orders, add new products without needing to reload the page.
app/models.py file with the definition of models: Order, Customer, Product and User.
app/urls.py file with define URLs for the views,
app/views.py that handles C R U D operations for signing up, login, order operations as well as managing customer profile page and products page.
crm/urls main urls
crm/setting application settings

- How to run:

py manage.py makemigrations
py manage.py migrate
py manage.py runserver

