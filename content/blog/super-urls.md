Title: The Lowdown on Super URLs
Author: Bruce O.
Category: News
Date: 2016-07-18 11:00
Image: super-urls.jpg
Tags: Amazon, Keywords, News
Summary: Super URLs - a tool celebrated by many sellers that has now fallen into controversy. Find out what they are and why we think you shouldn't use them.
Status: published

If you’ve been in the Amazon business for a while, you may have heard of Super URLs, a tool that some Amazon sellers are using in an attempt to boost their rankings for select keywords. Although many are touting them as a magic bullet, we at Efficient Era are skeptical—about both their effectiveness and their safety.

First, however, let’s take a look at what exactly a Super URL is.

### What Is a Super URL?

Let’s start with some background.

#### The Original Idea 

Try going to [amazon.com][]{:target="_blank"} right now, typing any keywords into the search bar, and clicking on a random product that pops up.

[amazon.com]: http://www.amazon.com/ 

Now, take a look at the URL. Near the end, there should be a field that looks like this:

![URL Example - Keywords](/images/blog/2016/07/keywords-url-example.png)

As you can see, the URL of the product itself, after the search has been completed, still contains the keywords you used to get there. Of course, the product page is always the same—the content won’t change based on the keywords used. 

However, the keywords do matter for Amazon’s ranking system. Amazon keeps the inner workings of their search algorithm tightly under wraps, so sellers like us are left to guess at its inner workings. However, the following explanation for keywords in the URL makes a fair bit of sense:

* When a customer searches for a keyword, let's say "stopwatch," then clicks on and buys product A, product A must have been highly relevant to their search of "stopwatch."
* Therefore, if product A gets a large number of sales from searches for "stopwatch," product A should rank higher for the "stopwatch" keyword.

Theoretically, this explains the presence of keywords in product page URLs—but again, we can’t know anything for sure. There is one other system at play with these keyword URLs—don't touch that dial.

#### One Extra Thing

The system is set up to track keywords from organic searches—*but what if someone posts a link to a product URL on a different site?* 

In this case, the linked URL would contain whatever keywords were used to find the product in the first place. However, a user comes to the product through that link, they never performed a search themselves. If they buy the product after following the link, that sale should not count towards the product's ranking for those keywords.

Amazon’s solution: add a timestamp to the URL so that each organic search would only count once. 

Here’s the URL from the same product as above, searched for with the same keywords, but performed about an hour later.

![URL Example - qid](/images/blog/2016/07/qid-url-example.png)

Notice that every field is the exact same, but the “qid” field has changed. This qid field is a Unix timestamp—it’s simply the number of seconds that have passed since January 1st, 1970. You can test this yourself, by simply performing the same search and clicking on the same object twice in two different tabs. Everything should be same except for the qid field.

Here's the idea: if a keyword search produces a sale *and* has a unique timestamp, that product will get a rankings boost for that keyword, because it was a truly organic search. However, if the timestamp has appeared before, that sale will not generate a keyword ranking boost—it was not an organic search.

#### The Super URL

With knowledge of these two fields, here’s where sellers got “creative,” so to speak.

The idea was: “*What if we could make links to our product pages appear to be organic searches?*” Enter the Super URL.

A Super URL is a link, usually shortened, that actually quickly redirects a user through a dynamic URL generation service before arriving at that unique URL. This URL points to the product page of the desired Amazon product, but it also contains a dynamically generated qid field and the seller-specified keywords to make it look like an organic search occurred. 

Theoretically, whenever a customer clicks on a Super URL link—through an email promotion, coupon offer, or otherwise—and makes a purchase, the product gets a boost for the selected keywords, because Amazon is tricked into thinking that purchase was made through an organic search.

If this "tool" really worked, it could generate huge keyword ranking swings. Despite this, **we strongly advise against using Super URLs**. Here’s why.

### The Unfortunate Truth

Our first argument against Super URLs is pretty straightforward—**they don’t work**.

Now, many sellers have raved about the ranking boosts they’ve received directly after integrating Super URLs into their business. And yes, it is likely that Super URLs did work at some point—many of the positive reports come from a time when Super URLs were recently introduced. 

However, Amazon is a huge, highly aware company. If you think about it, it’s unlikely that they would store valuable keyword ranking data—usually kept far away from the public eye—directly in the URLs of product pages. Normally, this information would be logged to a secure database. Ultimately, it’s surprising that Amazon sourced this data from URLs at all—they did at some point, as evidenced by early reports of Super URLs’ effectiveness.

These days, however, it would seem that they’ve caught on. There are many reports of significantly reduced effectiveness, and although there is still disagreement on this front, the general consensus is that Super URLs are completely defunct.

#### Policy Violation?

Another consideration—a recent Amazon policy change, although not directly addressing Super URLs, seems to be targeting “manipulative” behaviors. 

Last year, Amazon added a number of phrases to their Prohibited Seller Activities page, mostly related to manipulating product ranking and “intent.” The phrase we’ll look at is this:

“*You may not intentionally manipulate your products’ rankings, including by offering an excessive number of free or discounted products, in exchange for a review.*”

Evidently, nothing specific about Super URLs or even keywords is mentioned here. However, the first part of the phrase—“*You may not intentionally manipulate your products’ rankings*”—communicates a larger concern on Amazon’s part. They likely want sellers to avoid *all* intentional manipulation, whether it’s for product rankings, keyword placement or everything in between.

Super URLs, no matter your opinion on them, are an obvious attempt at manipulation. They attack a perceived exploit in order to boost your rankings in a manner that Amazon did not intend. While Super URLs are not literally prohibited, they are certainly against the spirit of the Amazon marketplace.

Amazon seller bans are rare and unpredictable, but they can happen. Amazon may change their policy or suddenly crack down on Super URL users—there’s no way to know. At the end of the day, if there’s no benefit to using Super URLs and you’re at danger of getting your account suspended… why bother? Our advice is to stay away.

However, your business is your business. If Amazon believes they have fixed the problem and Super URLs have no effects on rankings, then they may have little incentive to go after sellers who continue to use them. The uncertainty and the message of recent policy changes have us worried, but it’s ultimately up to you. 

Have any questions or comments? Let us know below!

