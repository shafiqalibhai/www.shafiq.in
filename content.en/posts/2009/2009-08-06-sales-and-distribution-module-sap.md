---
title: Sales and Distribution module (SAP)
author: Shafiq Alibhai
date: 2009-08-06T06:12:49+00:00
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1253883331";}'
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1253883330";}'
categories:
  - Uncategorized
tags:
  - Business
  - company structures
  - copy
  - customer account
  - customer accounts
  - customer master
  - distribution channel
  - distribution module
  - document number
  - document types
  - ERP
  - fiscal year
  - incompleteness
  - Invoice
  - IP
  - Management
  - organizational element
  - Parameters
  - point determination
  - proposals
  - Requirement
  - Requirements
  - Sales order
  - sales organization
  - SAP
  - sap system
  - sed
  - shipping point
  - shipping points
  - variants

---

# SALES & DISTRIBUTION

## (SD)

### Table of Contents

1. Definition of Sales & Distribution. 2
2. Enterprise Structure. 3
   1. Client 5
   2. Company. 5
   3. Company Code. 6
      1. Create a Fiscal Year Variant 7
      2. Maintain Fiscal Year Variant 7
      3. Assign Company Code to Fiscal Year Variant 8
      4. Posting Periods. 9
      5. Define Variants for Open Posting Periods. 9
      6. Open and Close Posting Periods. 9
      7. Assign Variants to Company Code. 10
      8. Define Document Number Ranges. 10
      9. Define Document Types. 11
      10. Define Tolerance Groups for Employees. 12
      11. Assign User/Tolerance Group. 13
   4. Plant 13
      1. Assign plant to Company Code. 14
   5. Location. 14
   6. Division. 15
   7. Sales Organization. 15
      1. Assign Sales Organization to Company Code. 16
   8. Distribution Channel 16
      1. Assign Distribution Channel to Sales Organization. 17
      3. Set up Sales Area. 18
      4. Assign sales organization - distribution channel – plant 19
   9. Define Shipping Points. 20
      1. Assign Shipping point to plant 20
      2. Shipping point and goods receiving point determination:
         - Assign Shipping Point
3\. Customer Master
   - Creation of Customer Account Group.
   - Create Number Ranges for Customer Accounts.
   - Assign Number Ranges to Customer Account Groups.
   - Define Incompleteness Procedures.
   - Define Order Type.
   - Define Item Category.

#### Definition of Sales & Distribution

For the representation of your company structures in the SAP System, different organizational units are available for the areas of sales, shipping and billing.
First analyze the structure and process organization in your company and then compare them with the SAP structures.
In the standard version, different organizational elements are defined as examples. In general, these elements are not sufficient for individual demands. Extend the elements accordingly.

During the clarification phase, work with the structures delivered by SAP. Change the names if necessary in order to achieve a high degree of identification and acceptance with project members and user departments from the beginning. After having defined the organizational units, allocate the elements to each other in the menu option "Allocation". Then check the defined organizational units in the menu option "Check". Only a limited number of users should be given authorization to maintain organizational elements. Determine the authorization profiles accordingly. As soon as the processing of the menu item is completed, access should be blocked so that no further changes can be made.

The organizational units set up the framework of sales processing with the SD system. The master records of sales and distribution (for example, customer master records and pricing elements) as well as the documents used in processing (for example, orders and delivery documents) are entered in dependency with the organizational structures. The data in a master record is only valid within a certain part of the organization. The sales and distribution documents are entered in the respective sub area of the organization. The master data valid there is automatically included in the sales & distribution documents. Different control criteria are specified for the management and processing of the master data depending on the organizational units. In order to simplify master record and document entry, the organizational units can be stored as user parameters in the user master record. It is not necessary to specify the organizational units since the values are proposed automatically.

**
**

2          Enterprise Structure

ü  This helps us to portray the specific organizational structure of your business in the R/3 System.

ü  To portray your company structure, different Accounting, Logistics, and Human Resources organization units are provided.

ü  In the SAP R/3 system, organizational levels are structures that represent the legal or organizational views of a company. Defining organizational levels is an essential step in the project and is vital for all subsequent activities.

ü  First analyze the structures and procedures in your company, and then match them to the SAP structures. As soon as your organization units are ready, access should be locked.

SD is integrated in the R/3 system in the following way:

The following is the Organizational structure from SD perspective:

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="138" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Shipping Point
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="138" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Plant
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="162" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Credit Control Area
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="162" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Controlling Area
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="66" height="54" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Sales Area
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="138" height="54" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Dist Channel
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="126" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Sales Org
  </td>
</tr>

</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0" align="left">
<tr>
<td width="28" height="0">
</td>

<td width="316">
</td>

<td width="78">
</td>

<td width="150">
</td>
</tr>

<tr>
<td height="12">
</td>

<td rowspan="3" align="left" valign="top">
</td>
</tr>

<tr>
<td height="42">
</td>

<td>
</td>

<td width="150" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Loading Point
  </td>
</tr>

</td>
</tr>

<tr>
<td height="20">
</td>
</tr>

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="138" height="42" bgcolor="white">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
  <td>
    Division
  </td>
</tr>

</td>
</tr>

ü  One client can have ‘n' number of company codes

ü  One company code can have ‘n' number of sales organizations

ü  One sales organization is assigned to exactly one company code

ü  A sales organization is assigned to one or more plants

ü  Each sales organization has its own master data. Eg. Its own Customer and Material master data as well as condition records.

ü  A sales organization can have ‘n' number of distribution channels (you can vary master data relevant to sales such as customer master data, sales master data, prices, and surcharges/discounts for each sales organization/distribution channel.

ü  Sales area is a combination of sales organization, distribution channel, and

ü  division

ü  Sales document, delivery document, and billing documents are always assigned to a sales area.

ü  Every sales process always takes in a specific sales area.

ü  A sales office can be assigned to more than one sales area

ü  Sales groups are assigned to sales offices

ü  A sales group consists of a certain number of sales persons

ü  A sales person is assigned to a sales office and group in the sales employee master record

ü  One sales organization can sell the goods from several plants.

ü  A plant can be assigned to different sales organizations at any one-time all of which can sell from the plant.

ü  A sales organization can also sell products supplied by a plant which is assigned to a different company code0inter-complany sales processing.

ü  A broad product range can be divided into divisions.  In sap-system, you can also define a division-specific sales structure.

ü  You can make customer-specific agreements for each division.

Following organizational elements are required for the SD transactions:

ü  Client

ü  Company

ü  Company Code

ü  Plant

ü  Location

ü  Storage Location

ü  Sales Organization

ü  Distribution Channel

ü  Division

ü  Sales Area

ü  Shipping Point

2.1        Client

The client is a commercial organizational unit within R/3 system, with its own data, master records, and set of tables. From the business perspective, the client forms a corporate group.

2.2        Company

ü  A company is an organizational unit in Accounting which represents a business organization according to the requirements of commercial law in a particular country.

ü  You store basic data for each company in company definition

ü  A company can consist of one or more company codes.

ü  All company codes within a company must use the same transaction chart of accounts and the same fiscal year breakdown.

ü  The company code currencies can be different.

ü  A company has one local currency in which its transaction figures are recorded.

IMG

Definition

Financial Accounting

Define Company

New Entries

Company (Ex: 0002, Description – Test Company)

2.3        Company Code

ü  The company code is the smallest organizational unit for which you have an independent accounting department.

ü  Balance sheets, profit and loss statements required by law are created at company code level**.**

Following is the path to define a company Code:

IMG

Enterprise Structure

Definition

Financial Accounting

Edit, Copy, Delete, Check Company Code

Click **Edit, Copy, Delete, Check Company Code**to enter new company code details.

** **

**Steps to create a new company code:**

<ol>
<li>
Copy Company Code
</li>
<li>
Click  or F2
</li>
<li>
Enter From (Ex: US01) & To Company Code (Ex: 9999).
</li>
<li>
Enter the currency.
</li>
<li>
Save.
</li>
</ol>

<h3>
2.3.1         Fiscal Year Variant
</h3>

ü  Fiscal year is a period of usually 12 months, for which the company produces financial statements and takes inventory.

ü  A fiscal year consists of several posting periods and if necessary, special periods that can be posted to after a temporary year-end closing.

ü  You define how your fiscal year is set up in the SAP System by creating a fiscal year variant at client level. Each company code is assigned a fiscal year variant.

ü  Several company codes can use the same fiscal year variant. Following is the path to maintain a Fiscal Year Variant:

<h3>
2.3.2        Maintain Fiscal Year Variant
</h3>

IMG

****Financial Accounting

Financial Accounting Global Settings

Fiscal Year

Maintain Fiscal Year Variant

<ol>
<li>
Click New Entries to create a new Fiscal Year Variant or Use the Existing Variant
</li>
</ol>

(Ex: Z4).

<ol>
<li>
Select Z4 and click period texts under dialog structure
</li>
</ol>

<h3>
2.3.3      Assign Company Code to Fiscal Year Variant
</h3>

For every company code, you must specify which fiscal year variant is to be used.

IMG

****Financial Accounting

Financial Accounting Global Settings

Fiscal Year

Assign Company Code to Fiscal Year Variant

Steps to assign company code to a fiscal year variant:

<ol>
<li>
Enter fiscal year variant against company code
</li>
</ol>

<ol>
<li>
Save
</li>
</ol>

<h3>
2.3.4        Posting Periods
</h3>

It is possible to specify which company codes are open independent of a company code. Thus, as many company codes as required can use the same variants for open company codes. You make the necessary settings to be able to manage identical posting periods in several company codes. The following is the path to define, open, close and assign variants to posting periods:

IMG

****Financial Accounting

Financial Accounting Global Settings

Document

Posting Periods

<h3>
2.3.5        Define Variants for Open Posting Periods
</h3>

**Steps to define variants for open posting periods:**

<ol>
<li>
New Entries
</li>
<li>
Enter the Variant and Name (Ex: 9999 - Fiscal Year Variant 9999)
</li>
<li>
Save.
</li>
</ol>

<h3>
2.3.6        Open and Close Posting Periods
</h3>

**Steps to open and close posting periods:**

<ol>
<li>
Copy the existing periods by selecting the required periods.
</li>
</ol>

<ol>
<li>
Click  button to copy.
</li>
<li>
Rename the Variant (Ex: 9999).
</li>
<li>
Save.
</li>
</ol>

<h3>
2.3.7        Assign Variants to Company Code
</h3>

**Steps to assign variants to company code:**

<ol>
<li>
Enter the Variant against the Company Code (Ex: 9999 Variant to 9999 Company Code)
</li>
</ol>

<ol>
<li>
  Save
</li>
</ol>

<h3>
2.3.8        Define Document Number Ranges
</h3>

A number range is a range of numbers that you can assign to business objects (or their sub-objects) of the same type. The following is the path to define a number range:

IMG

****Financial Accounting

Financial Accounting Global Settings

Document

Document Number Ranges

Define Document Number Ranges

Check whether the number ranges are transported to company code 9999

<h3>
2.3.9        Define Document Types
</h3>

A document type is a classification for documents that can be stored using SAP Archive Link.

For example, incoming invoices can be of the following document types:

Incoming invoice without invoice check (FIIINVOICE)

Incoming credit memo without invoice check (FIICREDIT)

IMG

****Financial Accounting

Financial Accounting Global Settings

Document

Document Header

Define Document Types

** **

**Ex:**Document Type - SA****

** **

<h3>
2.3.10     Define Tolerance Groups for Employees
</h3>

Predefine various amount limits for your employees with which you determine:

ü  the maximum document amount the employee is authorized to post

ü  the maximum amount the employee can enter as a line item in a customer or vendor account

ü  the maximum cash discount percentage the employee can grant in a line item

ü  the maximum acceptable tolerance for payment differences for the employee.

Payment differences are posted automatically within certain tolerance groups. This way the system can post the difference by correcting the cash discount or by posting to a separate expense or revenue account. Following is the path to define tolerance groups for employees.

IMG

****Financial Accounting

Financial Accounting Global Settings

Document

Line Item

Define Tolerance Groups for Employees

**Steps to define Tolerance Group**

** **

1     Click New Entries.

2     Give the Tolerance Group and Company Code.

<h3>
2.3.11     Assign User/Tolerance Group
</h3>

IMG

****Financial Accounting

Financial Accounting Global Settings

Document

Line Item

Assign User/Tolerance Group

Steps to assign user/tolerance groups

<ol>
<li>
Against user  enter tolerance group
</li>
</ol>

Ex: User name – ABUSR01 and Tolerance Group – 9999.

<ol>
<li>
Save
</li>
</ol>

** **

** **

** **

** **

2.4        Plant

A plant is an operating area or branch within a company.  Following is the path to define a Plant

IMG

Enterprise Structure

Definition

Logistics general

Define, Copy, Delete, Check plant

Steps for defining a plant:

1.     Click Define, copy, delete, check plant

<ol>
<li>
Click Define Plant
</li>
<li>
New Entries
</li>
<li>
Enter the data for plant
</li>
<li>
Save
</li>
</ol>

<h3>
2.4.1         Assign plant to Company Code
</h3>

IMG

Enterprise Structure

Assignment

Logistics General

Assign plant to company code

** **

** **

Steps to assign Plant to Company Code:

<ol>
<li>
Delete the default assignments
</li>
<li>
Select the company code (eg:9999)
</li>
<li>
Click Assign
</li>
<li>
Check plant
</li>
<li>
Save
</li>
</ol>

2.5             Location

A location allows a plant to be classified according to spatial or situation criteria. Following is the path to define a Location.

IMG

Enterprise Structure

Definition

Logistics General

Define Location

Steps to define a Location

<ol>
<li>
Click New Entries
</li>
<li>
Enter Plant, Location, Name
</li>
<li>
Save
</li>
</ol>

2.6             Division

An organizational unit based on responsibility for sales or profits from saleable materials or services. A Division is a product group that can be defined for a wide-ranging spectrum of products. You can make customer-specific agreements for every division, such as partial deliveries, pricing, and terms of payment.  Within a division you can carry out statistical analyses or set up separate marketing.  Divisions are utilized in SD but they are defined and maintained under the following path.

IMG

Enterprise Structure

Definition

Logistics General

Define, copy, delete, check division

Steps to define Division:

<ol>
<li>
Click Define, copy, delete, check division
</li>
<li>
Click on Define division
</li>
<li>
New Entries
</li>
<li>
Enter the values for Division and Name
</li>
<li>
Save
</li>
</ol>

2.7             Sales Organization

Sales Organization is an organizational unit in Logistics that structures the company according to its sales requirements.  A sales organization is responsible for selling materials & services and to negotiate terms of sale. Following is the path to define a Sales Organization.

IMG

Enterprise Structure

Definition

Sales and Distribution

Define, Copy, Delete, Check Sales Organization

Steps to define a Sales Organization:

<ol>
<li>
Click Define Sales Organization
</li>
<li>
Click New Entries
</li>
<li>
Enter the values for Sales Organization, Name (eg: 9999, Sales Organization 9999)
</li>
<li>
Save
</li>
</ol>

2.7.1      Assign Sales Organization to Company Code

IMG

****Enterprise Structure

Assignment

Sales and Distribution

Assign Sales Organization to Company Code

Steps to assign sales organization to company code

<ol>
<li>
Select company code (eg:9999)
</li>
<li>
Click Assign
</li>
<li>
Check Sales Organization
</li>
<li>
Save
</li>
</ol>

2.8             Distribution Channel

A channel through which saleable materials or services reach customers.  Distribution channels include wholesale, retail, and direct sales. You can assign a distribution channel to one or more sales organizations.

Following is the path to define a Distribution Channel.

IMG

Enterprise Structure

Definition

Sales and Distribution

Define, Copy, Delete, Check Distribution Channel

Steps to define a Distribution Channel

<ol>
<li>
Click Define Distribution Channel
</li>
<li>
New Entries
</li>
<li>
Enter the data for Distribution channel and Name
</li>
<li>
Save
</li>
</ol>

2.8.1         Assign Distribution Channel to Sales Organization

IMG

****Enterprise Structure

Assignment

Sales and Distribution

Assign Distribution Channel to Sales Organization

Steps to assign distribution channel to sales organization:

<ol>
<li>
Click Assign distribution channel to sales organization
</li>
<li>
Select Sales organization
</li>
<li>
Click assign
</li>
<li>
Check Distribution Channel
</li>
<li>
Save
</li>
</ol>

** **

** **

** **

** **

** **

** **

** **

** **

** **

** **

** **

** **

** **

**2.8.2   Assign Division to Sales Organization**

IMG

****Enterprise Structure

Assignment

Sales and Distribution

Assign division to sales organization

Steps to assign division to sales organization:

<ol>
<li>
Select sales organization (eg:9999)
</li>
<li>
Click assign
</li>
<li>
Check division
</li>
<li>
Save
</li>
</ol>

2.8.3      Set up Sales Area

Sales Area is a combination of sales organization, distribution channel, and division.

Following is the path to set up sales area

IMG

Enterprise Structure

Assignment

Sales and Distribution

Set up sales area

Steps to set up sales area:

<ol>
<li>
  Select Sales Organization
</li>
<li>
  Click Assign
</li>
<li>
  Check Distribution Channel
</li>
<li>
  Select Distribution Channel
</li>
<li>
  Check Division
</li>
<li>
  Save
</li>
</ol>

<h3>
2.8.4      Assign sales organization - distribution channel – plant
</h3>

IMG

Enterprise Structure

Assignment

Sales and Distribution

Assign sales organization - distribution channel – plant

Steps to assign sales organization-distribution channel-plant:

<ol>
<li>
  Select Sales Organization
</li>
<li>
  Click Assign
</li>
<li>
  Check Plant
</li>
<li>
  Save
</li>
</ol>

2.9      Define Shipping Points

Shipping point is an organizational unit in Logistics that performs shipping processing.

The shipping point is the part of the company responsible for the type of shipping, the necessary shipping materials and the means of transport. Deliveries are always initiated from exactly one shipping point. A shipping point is assigned one or more plants and can be subdividing into several loading points.

**Example:**Shipping points are a company mail depot or plant rail station.

A loading point is a voluntary entry.  It is merely a subdivision of a shipping point.  A loading point is manually entered into the header data of the delivery.

Following is the path to define shipping point.

IMG

Enterprise Structure

<dl>
<dt>
  Definition
</dt>

<dd>
  Logistics Execution
</dd>
</dl>

Define, copy, delete, check shipping point

Steps to define shipping point:

<ol>
<li>
  Click Define shipping point
</li>
<li>
  Click New Entries
</li>
<li>
  Enter Shipping point, Description
</li>
<li>
  Save
</li>
</ol>

<h3>
2.9.1          Assign Shipping point to plant
</h3>

IMG

Enterprise Structure

Assignment

Logistics Execution

Assign Shipping Point to plant

Steps to assign shipping point to plant:

<ol>
<li>
  Select the plant
</li>
<li>
  Click Assign
</li>
<li>
  Check Shipping point
</li>
<li>
  Save
</li>
</ol>

<h3>
2.9.2         Shipping point and goods receiving point determination:
</h3>

<h3>
Assign Shipping Point
</h3>

IMG

Logistics Execution

Shipping

Basic Shipping functions

Shipping point and goods receiving point determination

Assign shipping points

3                    Master Data in Sales and Distribution

Customer Master

Material Master

Customer material Info Record

Item Proposals

BOM

Customer Master Record

Data record containing all the information necessary for any contact with a certain customer, in particular for carrying out business transactions.

This information includes, for example, address data and bank data.

The basic customer master records we create are

ü  Sold-to party record

ü  Ship-to party record

ü  Bill-to party record

ü  Payer record

Other important Customers master records are inter-company customers, one-time customer

Customer Master Data configuration includes:

<ol>
<li>
  A/C groups
</li>
<li>
  Number ranges
</li>
<li>
  Assign number ranges
</li>
<li>
  Partner Determination
</li>
</ol>

<h3>
3.1.1   Creation of Customer Account Group
</h3>

In this step, you determine the account groups for customers. You can also define reference account groups for one-time accounts. You can use these to control the fields of the one-time account screen so that, for example, certain fields are displayed as required fields or are hidden.

When creating a customer account, you must specify an account group. You can specify a reference account group under "Control" in the "General data" part of a one-time account's master data. If you do not specify a reference account group, then, as previously, all fields of the one-time account screen are ready for input during document entry.

You use the account group to determine:

ü  the interval for the account numbers

ü  whether the number is assigned internally by the system or externally by the user (type of number assignment)

ü  whether it is a one-time account

ü  which fields are ready for input or must be filled when creating and changing master records (field status)

ü  fields can be turn on and off by using the assigned account group.

You determine the account number interval and the type of number assignment using the number ranges.

The Account group defines which fields are available in the customer master records.

A sold-to party needs 3 views

ü  General data view

ü  Company Code data view

ü  Sales data view

A ship-to party needs 2 views

ü  General data view

ü  Sales data view

A bill-to party needs 3 views

ü  General data view

ü  Company Code data view

ü  Sales data view

A payer needs 2 views

ü  General data view

ü  Company code data view

The following is the path to create customer account group:

IMG

Financial Accounting

Accounts receivable and accounts payable

Customer Accounts

Master Data

Preparations for creating Customer Master Data

Define Account Groups with Screen Layout

Steps to create customer account group:

<ol>
<li>
  Click New Entries
</li>
<li>
  Enter Account group number starting with the letter Z (SAP uses prefix Z for all upgrades in order to ensure it does not overwrite client-specific entries)
</li>
<li>
  Enter Name
</li>
</ol>

eg. Z100 – Sold-to party

<ol>
<li>
  Set the field status of general data, company code data, sales data
</li>
</ol>

Eg: Steps to set the field status

<ol>
<li>
  Select General Data under Field Status
</li>
<li>
  Click Edit field status
</li>
<li>
  Select the field eg: Address under ‘select group'
</li>
<li>
  Click magnifying glass button
</li>
<li>
  Name 1 – You can make the filed ‘Name1' Suppress or  Required entry or
</li>
</ol>

Optional entry or Display

<ol>
<li>
  Save
</li>
</ol>

Like wise create account groups for ship-to party, bill-to party, payer and Turn the fields on/off as per the requirement

Z200 – Ship-to party

Z300 – Bill-to party

Z400 – Payer

<h3>
3.1.2         Create Number Ranges for Customer Accounts
</h3>

To do this, specify the following under a two-character key (number range interval key)

A number interval from which the account number for the customer accounts is to be selected

ü  The type of number assignment (internal or external number assignment)

ü  Allocate the number ranges to the account groups for customers.

The type of number assignment is especially important. The following are possible:

ü  Transferring the numbers of your customers/vendors from an existing system or a pre-system (external assignment: The system enables the user to specify the number in the number range he or she wishes to use).

ü  Creating the master records under new numbers assigned by the SAP system (internal assignment: the system assigns a number when creating the master records).

The following is the path to create number ranges for customer accounts:

IMG

Financial Accounting

Accounts receivable and accounts payable

Customer Accounts

Master Data

Preparations for creating Customer Master Data

Create Number Ranges for Customer Accounts

Steps to create number ranges for customer accounts:

<ol>
<li>
  Click
</li>
</ol>

<ol>
<li>
  Click
</li>
</ol>

<ol>
<li>
  Enter the number range
</li>
</ol>

<

p align="center">

<

p align="center">

<ol>
<li>
  Save
</li>
</ol>

<h3>
3.1.3         Assign Number Ranges to Customer Account Groups
</h3>

Assign the number ranges created in the preceding step to the account groups for customers. You can use one number range for several account groups. Following is the path to assign number ranges to customer account groups.

IMG

Financial Accounting

Accounts receivable and accounts payable

Customer Accounts

Master Data

Preparations for creating Customer Master Data

Assign Number Ranges to Customer Account Groups

Steps to assign number ranges to customer account groups:

<ol>
<li>
  Click Assign Number Ranges to Customer Account Groups
</li>
</ol>

<ol>
<li>
  Enter the number range key against group and save
</li>
</ol>

<h3>
3.1.4         Partner Determination
</h3>

When creating a customer master record, the SAP System proposes the allowed partner functions to be maintained. According to the rules defined here, the partners are adopted from the customer master records of the sold-to parties into the sales and distribution documents.

Partners such as the sold-to party, the bill-to party, and the payer are a necessary in the majority of document processing.  Automatic partner determination happens in the sales document, delivery and billing document, sales activities, and the customer master record.

<h3>
Define Incompleteness Procedures
</h3>

In an incompleteness procedure you group together the fields that are to be checked for completeness. If you have not entered data in one of the fields in the document, the document is incomplete. Depending on the status group you can block certain subsequent activities for the document.

For every field in the procedure you also have to define whether a warning message should be issued during processing if no data is entered in this field. This function does not exist in delivery processing. When you select the control field, it has no further consequences.

Following is the path to define incompleteness procedures:

IMG

Sales & Distribution

Basic Functions

Log of Incomplete Items

Define Incompleteness Procedures

Steps to Define incompleteness procedures:

<ol>
<li>
  Select A – Sales Header
</li>
<li>
  Click Procedures
</li>
<li>
  Select 11
</li>
<li>
  Click Fields
</li>
</ol>

Define Order Type

The sales document types represent the different business transactions in Sales and perform a central controlling function for the entire sales order process.  Following is the path to define sales document type:

IMG

Sales & Distribution

Sales

Sales Documents

Sales document Header

Define Sales Document Types

Steps to define sales document type:

<ol>
<li>
  Click New Entries (or) copy the existing std. order type (ex: select OR -std. order type, click copy as icon, give a name to order type ex.: ZOR)
</li>
<li>
  Enter the data
</li>
<li>
  Save
</li>
</ol>

<h3>
Define Item Category
</h3>

The item categories that are contained in the standard SAP R/3 System together with the sales document types represent the usual business transactions.

You have the following options for defining your own item categories:

<ul>
<li>
  Copy an existing item category and change it according to your requirements.
</li>
<li>
  Create a new item category.
</li>
</ul>

Following is the path to define item category:

IMG

Sales and Distribution

Sales

Sales document

Sales document Item                                                                                                               Define item categories

Steps to define item categories:

<ol>
<li>
  Click New Entries
</li>
<li>
  Enter the data
</li>
<li>
  Save
</li>
</ol>
