Mailchimp Double Opt-In Bypass
===================

-------------
####  Demo
***Demo in progress***

-------------
####  Configuring the server

First of all, you need to upload the contents of **server** folder to your server.

The *redirect.php* needs to be configured first.
You need to fill this two params.

> $data['**INPUT_TYPE_TEXT_NAME_VALUE**'] = "";
> 
> $url = '**MAILCHIMP_FORM_ACTION_URL**';

To get both values, 

 1. First, you will need to login to your **[Mailchimp](https://login.mailchimp.com)** account 
 2. Then, find the list where you want to get the subscribers, click the arrow and then *"Signup forms"*

![enter image description here](http://i.imgur.com/3lo1Mtr.png)
 3. Select *Embed Forms*
 4. Expand the textarea called ***Copy/paste onto your site***
 5. ***MAILCHIMP_FORM_ACTION_URL*** is the url located just inside the tag **action** of the **`<form>`** element.
 6. ***INPUT_TYPE_TEXT_NAME_VALUE*** is the value of the **name** tag of the **`<input type="text">`** element above. 

*** You can view both fields in this image***
![enter image description here](http://i.imgur.com/LrvjbLB.png)
 7. Now you can upload an image to **/img** folder. This image is usually a CTA picture, asking the user to click in the image to subscribe to the newsletter

----------
####  Configuring the email sender (Python)
***Tutorial in progress***

----------
