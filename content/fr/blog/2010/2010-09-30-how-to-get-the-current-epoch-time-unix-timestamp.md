---
title: How To Get The Current Epoch Time (Unix Timestamp)
author: Shafiq Alibhai
date: 2010-09-30T04:56:45+00:00
categories:
  - Development
tags:
  - bash
  - perl
  - java
  - erlang
  - how-to

disableHLJS: false
---
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

disableHLJS: false
---
- Perl :

```perl
time
```

- PHP :

```php
time()
```

- Ruby :

```ruby
Time.now # (ou Time.new). Pour afficher l'époque : Time.now.to_i
```

- Python :

```python
import time # tout d'abord, puis int(time.time())
```

- Java :

```java
long epoch = System.currentTimeMillis()/1000;
```

- Microsoft .NET C# :

```csharp
epoch = (DateTime.Now.ToUniversalTime().Ticks - 621355968000000000) / 10000000;
```

- VBScript/ASP :

```vbscript
DateDiff("s", "01/01/1970 00:00:00", Now())
```

- Erlang :

```erlang
calendar:datetime_to_gregorian_seconds(calendar:now_to_universal_time( now()))-719528*24*3600. # OU element(1, now()) * 10000 + element(2, now()).
```

- MySQL :

```sql
SELECT unix_timestamp(now())
```

- PostgreSQL :

```sql
SELECT extract(epoch FROM now());
```

- Oracle PL/SQL :

```sql
SELECT (SYSDATE - TO_DATE('01-01-1970 00:00:00', 'DD-MM-YYYY HH24:MI:SS')) * 24 * 60 * 60 FROM DUAL
```

- SQL Server :

```sql
SELECT DATEDIFF(s, '1970-01-01 00:00:00', GETUTCDATE())
```

- JavaScript :

```javascript
Math.round(new Date().getTime()/1000.0) // getTime() renvoie le temps en millisecondes.
```

- Unix/Linux Shell :

```shell
date +%s
```

- PowerShell :

```powershell
Get-Date -UFormat "%s" # Produit : 1279152364.63599
```

- Actionscript :

```actionscript
(new Date()).time
```

- Autres lignes de commande des systèmes d'exploitation :

```shell
perl -e "print time" # (Si Perl est installé sur votre système)
```

- ColdFusion (CFML) MX 6.1+ :

```cfml
#int( getTickCount() / 1000 )#
```

- Ligne de commande Bash :

```bash
date +%s
```
