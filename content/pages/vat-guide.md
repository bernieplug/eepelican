Title: VAT Tool Guide: Automating Invoices
save_as: guide-vat/index.html

We’ve just revamped our VAT Invoice Tool, and we wanted to walk you through all the new features and show you how the tool works now!

To recap, our VAT Invoice Tool automates the time-consuming process of creating a VAT invoice for every EU customer who requests one. Instead of a back-and-forth email confirmation to collect all the customer’s information and create a VAT invoice by hand, all you have to do is send the customer a link. They can follow that link, fill in their information, and have our tool automatically generate a VAT invoice and send it to them. You don’t have to lift a finger!

### New Features

* **Automatic VAT Rates**
	* We keep track of the VAT rates for each country you’re registered in, so you don’t have to update that information yourself.
* **Seller-Specific Invoice Generation**
	* Simply send your unique invoice generation link, found at the top of the VAT Invoices Tool page, to your customers who request VAT invoices. They will be taken to a seller-specific page, personalized with your company logo, and only have to fill in a simple form to receive their VAT invoice instantly.  
* **Customizable, Marketplace-Specific HTML Templates**
	* Tailor-make the VAT invoice experience across all marketplaces. You have full control over the emails sent out after an invoice request — create a simple plaintext message, or use HTML and inline CSS to make them pop. You can add a different template for each European marketplace, ensuring the customer always gets an email in their native language.  
* **Email Previews and Invoice Tester**
	* You can preview each invoice email from within the editor to make sure everything looks right, but you can also go one step further. With our VAT Invoice Tester, you can quickly send yourself a test invoice to see the message from the customer’s perspective and verify everything is the way you want it.  

### How to Use the Tool

To access the new VAT tool, start from the [Efficient Era homepage](app.efficientera.com/dash/){:target="_blank"}. You can either click on <font color="FF751A">**VAT Invoices**</font> on the top navigation bar or <font color="FF751A">**VAT Settings**</font> in the top right corner of the At-A-Glance panel for VAT Invoices.

#### Adding Registrations

First, you can add all your different VAT registrations for the EU countries in which you’ve registered. To do this, click <font color="FF751A">**Add VAT Registration**</font> for every country you want to add, and fill in all the fields.  

Once you’ve finalized all your registration details, click <font color="FF751A">**Submit**</font>.

#### Default Emails and Registration

Next, set your default emails and VAT registration. To do this, click <font color="FF751A">**Settings**</font> in the top right corner of the VAT Invoices Tool. Once here, you can do several things:  

* Upload a seller logo, which will appear at the top of your customer-facing invoice page. There are no size restrictions on the image — it will automatically be adjusted to fit the page.

* Add your VAT notification email: whenever a customer requests a VAT invoice, a notification will be sent to this address.

* Add your VAT support email: if customers have any questions about the VAT invoices, they will be directed to this email, which will be displayed on the invoice generation page.

* Add your default VAT registration, which is usually the country where your goods are warehoused if you’re using Amazon FBA.  
	* If a customer makes a purchase from an EU country in which you are not registered, and the customer themselves is not VAT registered, VAT will be invoiced under this default VAT registration number and its value will be zero.

#### Email Templates

Finally, you can edit your invoice email templates.

We provide you with a default template, but you can edit it as you like, writing in plaintext or HTML. This default template will be the standard email response to all invoice requests, along with the attached invoice.

However, you can also add marketplace-specific templates for all EU marketplaces, which will override the default template for that marketplace. If you have translations ready, you can create email templates written in all your customers’ native languages.

To finalize your changes, click <font color="FF751A">**Submit**</font>.

#### Invoice Tester

Editing templates is all well and good, but what if you want to see what the actual email will look like? Fortunately, there’s a solution — the invoice tester. 

To use the invoice tester, click on <font color="FF751A">**Test VAT Invoices**</font> in the top right corner of the VAT Invoices page. In order to send yourself a test invoice, you’ll have to provide:  

* A valid Amazon order ID from a purchase made in the EU, in the format 123-1234567-1234567 (including dashes).
* A valid email address, which the test invoice will be sent to.
* Any valid VAT registration number.

Once you fill out these fields, click <font color="FF751A">**Submit**</font> and a test invoice will be sent to the provided email address. You can then see what the invoice will look like as an actual email.

#### How Customers Get Their Invoices

Any time a customer requests a VAT invoice, you can refer them to your personalized link, found at the top of the VAT Invoices page. The link should look like this: <font color="FF751A">**https://app.efficientera.com/en/vat/tool/ABCDEFGHI/**</font>.

When a customer clicks the link, it will take them to this page:

![Customer-Facing Invoice Page](/images/pages/customer-invoice.png)

They will have to input:

* Their Amazon Order ID.
* The email address where they want the invoice to be sent.
* Their VAT registration number, if they have one.
* Their home/business address.

*A note on the customer’s VAT registration number:*

* If a customer makes an order from an EU country where you, the seller, are **NOT** registered, **AND** the customer has their own VAT registration number, the invoice will be zero-rated, meaning the seller is not responsible for charging or remitting VAT.

* However, if the customer does **NOT** input a VAT registration number (i.e. they are not VAT registered), and they are from a country where you, the seller, are not registered, they will be invoiced for the default VAT rate, which is indicated by your Default VAT Registration under VAT Settings.

Once the customer has filled in every field, they just have to click <font color="FF751A">**Submit**</font> and they will be sent their VAT invoice automatically!