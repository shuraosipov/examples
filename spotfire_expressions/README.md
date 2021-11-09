# Spotfire expressions

## Check if a given date-time value older than 30 days

```
If(DateDiff('day',[OriginalDate],DateTimeNow()) > 30, 1, 0)
```

Calculates the difference between two Date, Time or DateTime columns. The result is presented either as a TimeSpan or as a real value representing a specified time part (e.g., number of days). 

If two arguments are used, then the first argument is the stop date column and the second argument is the start date column. In this case, the result will be a TimeSpan value displaying the total difference.

If three arguments are used, the first argument should be the part to compare. The second argument is the start date column and the third argument is the stop date column. The result of the operation is a real value.

```
Valid arguments for Arg1 are:
'year' or 'yy' - The year.
'quarter' or 'qq' - The quarter.
'month' or 'mm' - The month.
'day' or 'dd' - The day.
'week' or 'wk' - The week.
'hour' or 'hh' - The hour.
'minute' or 'mi' - The minute.
'second' or 'ss' - The second.
'millisecond' or 'ms' - The millisecond. 

Example:
DateDiff([Order Date], [Delivery Date])
DateDiff('day', [Order Date], [Delivery Date])
```