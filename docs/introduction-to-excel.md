#Introduction to spreadsheets

Before getting started on developing the core areas of excel,

### What are spreadsheets? What is Excel? What other programs could I use?

Spreadsheets are a particular type of application which allow users to store, manipulate, and present data all within the paradigm of a two dimensional grid. Spreadsheets are ubiquitous in corporates and used (and misused) for a bunch of stuff.

[Excel][excel] is the most well known and capable spreadsheet program, and it is widely available due to being part of Microsoft Office used by most companies (and easy to obtain illegally). It is a fantastic tool – possibly the best part of the Microsoft Office suite – and becoming proficient in Excel regardless of your profession will help you stand out in any office environment.

Spreadsheets can be used for:

- lists
- planning/project management
- collecting data
- reports and summarising data
- statistical analysis
- modelling, especially in a financial context
- creating an awesome and intense personal budget to take control of your finances!

The strength and weakness of spreadsheets are that they enable you to store, calculate, and display information in the same place. You can build formulas to display information in the structure and formatting you want easily. However, this makes the reports a lot harder to audit, check, and modify. In contrast, most commercial software separates the data storage in a database, and the reporting and formatting in the application.

I will assume that you have easy access to Excel (either on mac or PC) otherwise, check out the alternatives [below](#excel-alternatives).

### How to get started?

Open up Excel and have a look!

![Picture of Excel][excelpic]

The larger part of the window is taken up by a large grid – this is where you can enter data, headings/text, or formulas.

In newer versions, at the top you can see a ribbon toolbar where you can access different commands. Try clicking on the different headings to see what types of things are available for you. While starting out, it is useful to be able to find out what Excel can do through these different icons, however, keyboard shortcuts are *very* useful in Excel to perform repetitive operations.

### Workbook structure

A spreadsheet file is usually called a *workbook* which is made up of *sheets*. Each sheet is a large array of cells which is essentially unlimited in size (millions of rows in modern Excel). However, things can get unwieldy putting too much on one sheet (especially ensuring that column widths are appropriate for multiple reports). Using different sheets allows us to clearly distinguish between different reports or tables of data.

Within each sheet is a grid of *cells*. You will see a ruler on the top and the side which notates the columns (ABCD), and rows (1234). Combined, these can give us the position or *reference* for cells or *ranges* (groups of cells). You can see the reference for the selected cell in the *name box* in the top left.

```text
A1     The cell in the top left
C2     The cell in the third column and the second row
C:C    The third column
4:4    The fourth row
B4:D8  A block of cells in a square from B4 to D8 (example below)
```

![Example selection][es]


### Entering data

Click on a cell and start typing. Let's type in a bit of data for some test scores. Start entering some names. Every time you are finished, hit `enter`. You can enter a set of data very quickly this way.

If you are entering a row at a time, you can move across with `tab`, then `enter` will take you to the beginning of the line. Add a few more names, but this time, `tab` and add a score number before hitting `enter`. Flesh out the scores once you are finished.

![Some data entered][ed]

Let's add some formatting to the heading. Select the headers, then click the bold button under the home tab.

![Bolded headers][eb]

You can see the active cursor – the dark box around the active cells. You can move this around with the arrow keys, or with `enter` (usually moves the cursor down), or `tab`, (which moves to the right). Moving this around while holding shift allows you to select a *range* of cells.

You can select a whole column or row at once by clicking on the ruler (click on the A in the column header for example). Once this is selected, you can right click to add `insert` or remove `delete` rows or columns. `Ctrl+a` will select the active [data range](#data-ranges-and-tables), and if you hit it again, you can select the whole sheet.


### Simple formulas

The power of Excel begins when we start doing calculations. Let's start with math. Try entering these into the cell of your choosing.

```text
= 1 + 2         => 3
= 4 / 2         => 2
= (5 + 3) * 2   => 16
= 3 ^ 2         => 9 ("^" is the same as "to the power of")
= (B3 + B4) * 2 => The result of the two cells added together
                   multiplied by 2. Yes you can (and should)
                   directly reference cells in calculations.
```

Great! So powerful! How wonderful! OK – let's go ahead and do some analysis of this small set of data we have entered.

Firstly, let's get the total of the scores – not very meaningful in this context, but very common and useful. Type the following formula in cell B6: `=SUM(B2:B5)` (no need to enter in upper case). I've also added some bold formatting to differentiate the result from the data. Note that the formula is visible in the *formula bar*, just above the ruler.

![Totalling the data][sf]

This is an Excel *formula* or *function*. It takes an *argument* (the stuff in between the brackets) which can be cell references or values. Then usually outputs a value. Some formulas take multiple *arguments*, separated by commas, which mean different things based on the order entered. In this case, `=SUM()` can take multiple cell references and numbers, and will add them all up.

There are a few different ways of entering formulas. In this case we entered it straight in with text. However, you can also get to it by using the formula builder by clicking on the `fx` button by the formula bar. Or, you can hit the formulas tab and select a formula from one of the dropdown menus. These methods guide you through easily entering in a formula's arguments one by one.

![Ways of accessing formulas][fm]

Summing is *so* common, that there is a feature called *AutoSum*, with the Σ symbol, also accessed via `alt+=`. This will not only insert the `=SUM()` formula for you, but will guess at the range you want to sum. Very handy!

Let's get rid of this though, and replace it with something more relevant – the average. Delete the value with the backspace key, then click the down arrow next to the `Σ AutoSum` button. There are a bunch of alternatives to `=SUM()`, including `=AVERAGE()`, which calculates the mean of the selected range. Click it while the cursor is on B6 and you will see that it automagically selects the correct range.

![Averaging the data][af]

Great! Now we can see that the average score of these students is **6.25**!... not fantastic. However, we have forgotten to add the score of our star student, Rambo. Let's add him in to the bottom of the table.

Select row 6 by clicking on the 6 on the left, then click `Insert` (note: if there is anything copied, it will be pasted. Hit `esc` to clear the clipboard if this is an issue). For the keyboard shortcut people, navigate to a cell in row 6, hit `shift+space`, then `ctrl+=`.

Go ahead and enter Rambo in column A, and 10 in column B in the newly created row. What!? Our average still shows 6.25. A closer analysis shows that the cell reference in (now) B7 has not automatically updated for the new row, as it was placed at the end of the reference! Go ahead and manually update the formula to include the new row by amending `B2:B5` to `B2:B6`. There we go, now the average correctly shows 7.

![New row issue][rowissue]

This is a common pitfall in Excel and happens often, so be aware of this – the most simple work around generally is to insert a row or column in the middle of a range rather than at the end or the beginning. [Excel tables](#data-ranges-and-tables) are one great way to solve this issue.


### Data types and number formatting

One key concept in Excel is that the presentation of what is in the cells can be customised. What you see in the cell may not accurately represent the data contained.

This is both dangerous and useful. Dangerous, because what looks like a number might actually be stored as text, and it is impossible to easy see what is a formula and what is a value. Also, a number might only show a certain level of precision: `0.52`, for example, might display as `1`. Useful, because it enables use to use math in cells with only the results displayed, and it enables us to store dates as numbers, which allows all kinds of useful operations.

To easy see the underlying details, use the key-board shortcut ``ctrl+` `` to toggle into *view values* mode.

One good way to get an indication of what type of information is in the underlying cell is the *alignment*, although be careful, as this can be overridden:

```text
Numbers:                 right aligned
Dates:                   right aligned (dates are just numbers with a custom format)
Text (strings):          left aligned
Trues/falses (booleans): mid-aligned
```


### References

Now that we know how to build [simple formulas](#simple-formulas), we can start to look at how to use references in a more powerful way.

We already know that we can use *references* to link cells together to build powerful and dynamic formulas. For example, above we created a formula that adds up (`=SUM()`s) all numbers within a range – any time any of those numbers change, our total will update. Another example is if we want to multiply price by quantity to get the total revenue for a transaction.

![Picture of single P*Q=R calculation][ref-single]

This is great for if we only want to do this calculation once, but what if we want to do this calculation for a whole *column* of values. Do we have to manually enter each cell in the column? H to the *no*! It turns out Excel is smart enough to make the cell references *relative* – if you copy-paste the cell to the whole the column or drag the cell down to the bottom using the square in the bottom-right corner of the cell, Excel will do all the hard work to move the references too. Although the cell reference might look like `=A2 * B2`, it *actually* means `= the cell two to the left times the cell one to the left`.

![Picture of a column of P8Q=R calculations][ref-column]

This is very powerful! However, there are two main situations that we might not want this default *floating reference* behaviour, and instead want a *fixed*, or *absolute* reference.

1. We may want all formulas in a range to reference the same value – for example, perhaps the price is the same for everything, but the quantity could change.
2. We want to cross-tabulate data in a nicely displayed two-dimensional table. One reference in a formula links to the column headings (and should have the row fixed and the column floating) and one reference links to the row headings (which should have the column fixed and the row floating).

The way Excel lets us tell it that a reference should be fixed is with `$` signs:

```text
A1      relative
$A$1    fixed
$A1     fixed column, floating row
A$1     fixed row, floating column
```

It is fairly onerous to key in these `$` signs, so Excel gives us a great keyboard shortcut. When I learnt this shortcut when I was an accounting graduate, it changed my life. I pried off the `$` key in a burst of freedom and joy (well, I would have if it wasn't also the `4` key).

It is `F4`. Use it wisely. You're welcome.

Anyway, let's see those examples. Firstly, let's see a column where we have one constant value and one floating value. To reiterate, the beauty of these cell references is that you just have to get them right in the top cell, then you can copy-paste down to the whole column.

![Picture of a column with a fixed value][ref-fixed]

Now, let's see that cross-tabulated table – this is the advanced case where we mix floating and fixed within the *same reference*. You can continue to hit `F4` to iterate around the various combinations of fixed and floating within a cell refrence.

![Picture of cross-tabulated table][ref-cross]


### Data ranges and tables

When you get spreadsheets, usually they are a mix of headings, subtotals, calculations, explanatory text, and other information all right up next to each other. This is fine for reports, however, something magical happens when we take care to structure data in a special way.

Excel has the capabilities to do some really exciting stuff with *data*. Well presented data usually has a *headings* row at the top, with a series of rows underneath with the information that we are interested in, ideally with one row per transaction or record. You may have used the *autofilter* to sort or filter data.

![Picture of filter][filter]

It can be a hassle to select the correct range for the autofilter in the first place. What if I told you that you could autofilter with one single shortcut/click **and** you *didn't even need to autofilter in the first place* to do simple filters and sorts? All you need to do is follow these simple rules:

1. Make sure that there is *empty space* around the data. The top and left sides of the spreadsheet count as empty space.
2. Differientiate the headings via formatting (I suggest bold)
3. Ensure that there are no empty cells within the table (not strictly required, but a great idea and helps when, for example, displaying pivot table contents correctly). The data should be tightly packed (no subheadings, for example).

![Picture of a data range][data-range]

If you have these things, then you can do some awesome stuff:

* You can make the selected data into a pivot table or autofilter without having to select the range – Excel can detect the correct range as long as any cell is selected.
* You can right click in a column to sort that column *without the autofilter*.
* You can right click in a cell to filter *the whole table* by that cell's value! That's *better* than autofilter!

![Context menu][dr-right-click]

Now that the data is in a format that Excel loves, we can (if we want to) convert it into an official *Excel Table*. To do this, go to `Home > Format as Table`, or `Insert > Table`, or simply hit `Ctrl+t`.

Why would we do this? Well, where do we start!?

* You can easily format the table in a multitude of great looking styles, or build your own style! This means that the formatting won't break when your users add rows or copy paste into your table.
* Excel Tables are filtered by default, and allow you to have multiple filtered ranges per sheet.
* If you add a row between your data and the total, the range for the data automatically picks up the new row (see the end of the [formula](#simple-formulas) section for why this is useful.
* Ever had a problem where you had to manually change a pivot table or chart range once you have added new rows to your data? No more! References to Excel Tables *automatically expand* when adding new rows to your tables! You can add new rows by hitting tab in the last row of the table, or by dragging the bottom right corner.
* You can make use of table *nomenclature* (special way of naming things). For example, instead of summing `A2:A43`, you can sum `transactions["Amounts"]`. (Usually I don't type these out – Excel automatically puts these in formula when you select a range. Nice!)
* Excel Tables are the main and best way to get information from your spreadsheet to Power Pivot or Power Query (advanced).

![Picture of an Excel table][excel-table]

I strongly suggest that you rename tables from the default `Table1` to something more meaningful as soon as you create them.


### The F2 key – Excel modes

The F2 key is magic sauce in Excel, and knowing it will make your life easier and more productive. Seriously, this is almost the top secret trick of Excel pros.

There are two modes for entering data in Excel. *Enter* mode and *edit* mode. If the cursor is on a cell with data in it, when you start typing the default behaviour is to *overwrite* the cell in *enter* mode. However, if you hit `F2`, you can start editing the cell in `edit mode`, which leaves the contents intact and allows you to move around within the cell using the arrow keys.

*Enter* mode is primarily useful as it allows you to insert *cell references* by using the arrow keys. The mode you are in can be found in the bottom left of the window and can be switched with `F2`.

![Enter vs. edit mode in Excel][ee]

Seriously, I cannot emphasise how much I use this keyboard shortcut – this is how I start editing cells from the keyboard without overwriting the cell or reaching for the mouse. Once I am in the cell, I can effortlessly switch between enter mode (for selecting close cell references), and edit mode (for making tweaks to the formula).


### Excel alternatives

If you do not have access to Excel, there are some free alternatives, including [Google Sheets][sheets] (online only but with great collaborative features) and [Open Office][oo] (fully featured and more traditional).

I have also used Apple's [Numbers][numbers]. The main difference is that Numbers does not have the infinitely large grid of cells like most spreadsheets applications – instead directing you to organise your data in separate tables which can be formatted separately. This is great when displaying different sets of data above each other where the column sizes don't match up. People are moving towards using tables in Excel for storing data, so Numbers is ahead of the curve here.

![Numbers example][numberspic]

This is an example from the included templates (which, unlike Excel, are useful and usable). Having the GPA table and the Grade Scale stacked like that in Excel would be much harder and unwieldy, often requiring merged cells. Unfortunately, I have found Numbers slow and clunky for larger scale data analysis, including for home budgets which often accumulate to tens of thousands of rows.


### Resources

If your thirst for Excel has not been satiated and you want to continue your Excel knowledge journey, I have found the following Excel resources incredibly useful.

- [Chandoo's blog][chandoo], which covers a wide variety of Excel topics written in an easy to understand manner.
- [Excelisfun youtube channel][eif], an amazing resource for more visual learners. Mike is a very enthusiastic teacher who makes learning about Excel exciting and engaging.
- [Contextures.com][cntx], which has all kinds of useful tips. The blog is especially interesting, and often has a round-up of useful articles published across the interwebs.
- [Ken Pul's blog][ken], which focuses primarily on Power Pivot/Power Query (which are amazing, but definitely more advanced).
- [Modeloff][mo] is an Excel financial modelling competition. The great thing about this site is all of the past questions – if you really want to challenge your Excel capabilities in a practical way, this is a great resource with some worked answers by big-shot consulting companies.


### Key learnings

What have we covered in this article?

* What is a spreadsheet, and how are they used
* How to get into a spreadsheet
* How is a spreadsheet structured and what are they made up of
* How to enter data into a spreadsheet
* How to create simple formulas like `=SUM()` or `=AVERAGE()`
* Why the data that you see in a cell might not actually reflect the underlying data
* Fixed vs. floating references, and why you would want to use each in different situations to a avoid manual work
* How Excel has an implicit format that it wants you to use to present data, and how you can make that explicit using Excel Tables
* How Excel has different editing modes and how you can easy switch between these to take advantage of different ways to edit formulas.
* Some Excel alternatives, most of which work in a very similar way.

[excel]: https://products.office.com/en-nz/excel
[sheets]: https://www.google.com/sheets/about/
[oo]: https://www.openoffice.org
[numbers]: https://www.apple.com/nz/numbers/
[chandoo]: http://chandoo.org/wp/
[eif]: https://www.youtube.com/user/ExcelIsFun
[ken]: https://www.excelguru.ca/blog/
[mo]: https://www.modeloff.com
[cntx]: http://www.contextures.com

[excelpic]: images/excelpic.png
[numberspic]: images/numberspic.png
[ee]: images/enteredit.png
[ed]: images/entereddata.png
[eb]: images/enteredbold.png
[es]: images/exampleselection.png
[fm]: images/formulas.png
[sf]: images/sum.png
[af]: images/average.png
[rowissue]: images/newrowissue.png
[filter]: images/filter.png
[data-range]: images/data-range.png
[dr-right-click]: images/data-range-right-click.png
[excel-table]: images/excel-table.png
[ref-single]: images/rsingle.png
[ref-column]: images/rcolumn.png
[ref-fixed]: images/rfixed.png
[ref-cross]: images/rcross.png
