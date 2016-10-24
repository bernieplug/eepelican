Title: MWS Authorization and Seller Central Integration
Author: Bruce O.
Slug: registering-your-amazon-account-with-mws
Category: How-to
Date: 2015-08-25 8:00
Tags: Customer Service, Amazon, Getting Started
Summary: Efficient Era accesses your Amazon Seller account by using Marketplace Web Services. In order to connect the services, here’s what you need to do.
Status: published

In order to use Efficient Era's services, you will need to provide us developer access to your Amazon Marketplace Web Services (MWS) accounts for each geography. 
We are very serious about your privacy and your data is safe with us. Here are three parts to the complete integration process. 

### Part 1: Grant Efficient Era Developer Access to your MWS Account


There are two pieces of information that you will need from this MWS Account Authorization step: 1) MWS Authorization Token and 2) Seller ID. Here’s a step-by-step guide on how to get them. 

1. Go to [Amazon's MWS page for North America](https://developer.amazonservices.com/){:target="_blank"} and click [**Sign up for MWS**](https://developer.amazonservices.com/gp/mws/registration/register.html){:target="_blank"}.  
If you would like Efficient Era to access your MWS Europe account, please click [here](https://developer.amazonservices.co.uk/){:target="_blank"} and follow the same steps.

2. Select the option **“I want to give a developer access to my Amazon seller account with MWS.”**

3. Input the Developer Name as **“Efficient Era”.**

4. Input our Developer Account Number based on which region you’re registering for:  
For North America (amazon.com/.com.mx/.ca) please use: **2546-9853-2013**  
For Europe (amazon.co.uk/.fr/.de/.it/.es) please use: **0585-4477-0074**  

5. Make sure your page looks like the image below.
![MWS Registration Page](/images/blog/2015/08/registering_amazon_mws_1.jpg)  

6. Hit Continue.

### Part 2: Provide Efficient Era your MWS Authorization Token and Seller ID

1. The next page you see should have the information (see below) we need to connect our service to your MWS account (separate for each geography).
![MWS Information Page](/images/blog/2015/08/registering_amazon_mws_2.jpg)

2. At this point, navigate to your Efficient Era dashboard and locate the settings gear icon in the top right corner to access the **Account Settings**. Next, scroll down to the **Amazon Marketplace Web Service Credentials (Amazon MWS)** sub-section and expand it.
![Settings](/images/blog/2015/08/SettingsPanel.png)

3. Click the **Edit** button on the right for the correct marketplace — Amazon.com if you're a US-based seller, Amazon.co.uk if you're a UK-based seller, or both as needed.

4. Copy your **Seller ID** number from the previous steps and paste it into the **Seller ID** field.

5. Copy your **MWS Auth Token** number and paste it into the **MWS Authorization Token** field.

6. Hit **Submit**



### Part 3: Integrate Efficient Era services in Seller Central 

Next, navigate to your Seller Central account and give the correct access permissions to Efficient Era. Here are the steps:

1. Log in to your Amazon Seller Central account.
2. Click on **Settings** in the top right corner, then click on **User Permissions**.
3. Click **Add a New Seller Central User**.
4. Under the email field, enter **services@efficientera.com**.
5. Click **Send Invitation**.
6. Once the invitation is sent, you should receive an email from services@efficientera.com containing a confirmation code. This process could take from 24-48 hours.
7. Return to the User Permissions page. You should now see **services@efficientera.com** as a pending user with a confirmation code displayed.
8. Verify that the code in the email you received is the same as the one displayed on the User Permissions page, then click **Confirm**.
9. In the Efficient Era user, click **Add User Permissions**. 
10. By default, all permissions should be set to None. There are three permissions that you need to change. Make sure you do this step carefully following the red arrows in the images below.
11. Under the Orders section, set **Manage Orders** to View & Edit, as shown below.
![Settings](/images/blog/2015/08/SellerCentral_1.png)
12. Under the Reports section, set **Feedback** to View & Edit and set **Fulfillment Reports** to View, as below.
![Settings](/images/blog/2015/08/SellerCentral_2.png)
13. Once you’ve confirmed that every setting matches the images above, click **Continue**.
14. You’re done!


