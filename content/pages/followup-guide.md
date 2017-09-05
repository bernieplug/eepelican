Title: Using the Email Automation Tool
save_as: followup-guide/index.html

With Efficient Era's Email Automation you can:

1. Monitor email open rates
2. Create Email Campaigns
3. Design Email Themes
4. Set up Bulk Order Notifications
5. Attach documents
6. Add marketplace Emails to a blacklist
7. Set a reply-to email
8. Attach automated VAT Invoices (EU only)

### The Dashboard

The first thing you’ll notice as you head to the Efficient Era dashboard is the Email Automation at a glance tile.

![Order Automation Panel](/images/pages/postorder-panel.png)

This tile shows you the number of emails sent (orange) per day over various time ranges, as well the number of that were emails opened (cyan).

Now, if you click on <font color="FF751A">**See More**</font> in the top right of that window, or click on <font color="FF751A">**Email Automation**</font> in the top navigation bar, you’ll reach the Email Automation tool. This is where you can start creating your follow-up emails.

### How the Tool Works

You’ll notice the two main tabs in the tool are Email Campaigns and Email Themes. Let’s go over exactly what those are.

#### Email Campaigns

Email campaigns are the bread and butter of our tool — they’re the things that actually send out follow-up emails. 

You can add any number of products to a campaign, and any product can belong to as many campaigns as you want. At the end of the day, however, if a product belongs to a campaign, and someone orders that product, the campaign will send that customer an email based on the rules you set.

#### Email Themes

An email theme is a sort of “wrapper” that can be applied to any campaign, purely for formatting and sharing common bits of content across campaigns.

Themes are great for generic messages that you want to include in a large number of your campaigns. These are a great placeholders for a company message or logo.

Now, let’s go over how to set up a campaign and start sending follow-up emails! In order to do that, we’ll need to start by creating a theme.

### 1) Creating a Theme

1. Navigate to the <font color="FF751A">**Email Themes**</font> tab. Click <font color="FF751A">**New Theme**</font> in the upper left-hand corner.

2. Give your theme a name — this is just for identification purposes.

3. Add the contents of your theme! Your theme can be mostly text, but basic HTML tags and inline CSS are also supported, so you can customize it to your liking. You can also upload images — include your company logo, if you like.  
	1. Along the edit bar at the top, you'll see this icon: ![Placeholder Icon](/images/pages/placeholder-icon.png). This contains all of our **Placeholders**. These are codes which will automatically be replaced with the indicated customer- or product-specific information when the email is sent out. Use them to reference specific pieces of information, all from the comfort of a generalized theme. You can also use our **Predefined Links** ![Predefined Links Icon](/images/pages/predefined-links-icon.png) to automatically create common links, such as a request to leave a review.
	
	2. Example: *“Thanks for your purchase, [Name]! We hope you enjoy your [ProductTitle]. If we ever ask, your product’s model is [SellerSKU] and your order number is [OrderId].”*  

4. **IMPORTANT:** You’ll see that the theme already includes the placeholder `$email_body`. This is a placeholder for the body text of any campaign that uses this theme. **Do not delete this placeholder, or the campaign message will not be displayed in the email.**

5. Hit <font color="FF751A">**Submit**</font>, and your theme is created! Now, whenever you create a campaign, you can select this theme, and the theme’s content will be displayed around that campaign’s message.

6. If you want to edit the theme any time after it’s created, simply select it from the menu and press <font color="FF751A">**Edit**</font>.

### 2) Creating a Campaign

1. Navigate to the <font color="FF751A">**Email Campaigns**</font> tab. Click <font color="FF751A">**New Campaign**</font> in the upper left-hand corner.

2. Give your campaign a name — again, choose something that you can identify later.

3. Choose which products you’d like to add under this campaign. You can add any number of products: anywhere between a single item and your entire catalog.  
	1. Whenever any of these products are ordered, this campaign will send the same email(s), with the exception of text placeholders. Choose closely related products for the best results.  
	
	2. Note that you must have listed the product within Efficient Era in order to add it here. If you haven’t done that yet, click on the <font color="FF751A">**Products**</font> tab on the top navigation bar and create a new product there.

4. Choose the marketplace(s) for which you want this campaign to be active.

5. Press <font color="FF751A">**Submit**</font> and you will be taken to the Editing panel. This is where you can add content to your campaign.

6. First, select a theme for this campaign using the <font color="FF751A">**Email Theme**</font> drop-down menu. For now, you can select the theme you just created. You can also select “Plain Text”, which will display just your campaign’s body text and no theme content.

7. Fill in the <font color="FF751A">**Email Title**</font> field, which will be the subject line of any emails this campaign sends.

8. Fill in the <font color="FF751A">**Email Body**</font> field. This is the campaign-specific message you want to send within an email. Just like a theme, you can use text, images, or basic HTML tags to customize your message.  

	1. Remember that the contents of the theme you chose will also be included in the email, so you don’t need to repeat any information you already included in your theme.  
	
	2. To see what the full email will look like, with campaign and theme together, submit your edits and click on the campaign’s name in the menu to the left.
	  
	3. Again, remember that the email body will be displayed wherever *$email_body* appears in the chosen theme. **If you deleted this placeholder, the campaign’s text will not appear in the email.**
	
9. Finally, edit your <font color="FF751A">**Event Triggers**</font>, which indicate what time(s) the campaign should send an email. 
 
	1. Choose a baseline event of *“Confirmed”*, *“Shipped”*, or *“Delivered”*, then set a delay in days. An email will be sent that many days after the event.  
	
	2. For example, if you want an email to be sent two days after the product has been shipped, set *“Shipped”* as the Event and *“2”* as the delay.
  
	3. By default, each campaign only has one trigger, meaning it sends one email. However, you can create up to 5 event triggers, all of which will send the same email. ***We don’t recommend this.*** 
	
10. Once everything is to your liking, flip the <font color="FF751A">**Enabled**</font> switch to *“On”* and hit <font color="FF751A">**Submit**</font>. Your campaign is now active!

Your email campaign is live! When a product associated with the campaign is ordered, it will send out emails based on the triggers and delays you set.  

Don’t stop here — you can add as many campaigns as you like, and and even have multiple campaigns for the same product! Adding one product to multiple campaigns is a great way to provide multi-stage support: you can provide a product manual in the first email after the product ships, then a link to leave a review in the second email a few weeks after it was delivered. 

If you have any other questions or suggestions (we always welcome feedback!), feel free to contact us at [support@efficientera.com](mailto:support@efficientera.com) Thanks for using Efficient Era!