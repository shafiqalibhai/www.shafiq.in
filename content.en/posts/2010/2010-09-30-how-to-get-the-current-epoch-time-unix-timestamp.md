---
title: How To Get The Current Epoch Time (Unix Timestamp)
author: Shafiq Alibhai
date: 2010-09-30T04:56:45+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973442";}'
categories:
  - Development
tags:
  - bash
  - Epoch Time
  - erlang
  - IP
  - java
  - JavaScript shell
  - MySQL
  - oracle
  - PHP
  - PostgreSQL
  - powershell
  - Python
  - ruby
  - shell
  - sql server
  - unix
  - Unix Timestamp
  - vbscript

---

- Perl:

```perl
time
```

- PHP:

```php
time()
```

- Ruby:

```ruby
Time.now # (or Time.new). To display the epoch: Time.now.to_i
```

- Python:

```python
import time # first, then int(time.time())
```

- Java:

```java
long epoch = System.currentTimeMillis()/1000;
```

- Microsoft .NET C#:

```csharp
epoch = (DateTime.Now.ToUniversalTime().Ticks - 621355968000000000) / 10000000;
```

- VBScript/ASP:

```vbscript
DateDiff("s", "01/01/1970 00:00:00", Now())
```

- Erlang:

```erlang
calendar:datetime_to_gregorian_seconds(calendar:now_to_universal_time( now()))-719528*24*3600. # OR element(1, now()) * 10000 + element(2, now()).
```

- MySQL:

```sql
SELECT unix_timestamp(now())
```

- PostgreSQL:

```sql
SELECT extract(epoch FROM now());
```

- Oracle PL/SQL:

```sql
SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL
```

- SQL Server:

```sql
SELECT DATEDIFF(s, '1970-01-01 00:00:00', GETUTCDATE())
```

- JavaScript:

```javascript
Math.round(new Date().getTime()/1000.0) // getTime() returns time in milliseconds.
```

- Unix/Linux Shell:

```shell
date +%s
```

- PowerShell:

```powershell
Get-Date -UFormat "%s" # Produces: 1279152364.63599
```

- Actionscript:

```actionscript
(new Date()).time
```

- Other OS's Command line:

```shell
perl -e "print time" # (If Perl is installed on your system)
```

- ColdFusion (CFML) MX 6.1+:

```cfml
#int( getTickCount() / 1000 )#
```

- Bash Command Line:

```bash
date +%s
```
