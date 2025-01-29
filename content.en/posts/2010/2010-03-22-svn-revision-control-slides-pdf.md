---
title: SVN – revision control – slides – pdf
author: Shafiq Alibhai
draft: true
date: 2010-03-22T06:54:55+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269438320";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269524195";}'
tagazine-media:
  - 'a:6:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:7:"4390143";s:7:"blog_id";s:7:"4153392";}'
categories:
  - Development
tags:
  - copy
  - Database
  - developer
  - email
  - History
  - IP
  - Management
  - shafiq
  - URL

---
### SVN - revision control

Coordinating projects

●

Problem: How to coordinate and synchronize code



between multiple developers on a project?

– Work on the same computer, take turns coding



Nah...



– Send files by e-mail or put them online. Lots of



manual work.

– Put files on a shared disk. Files get overwritten or



deleted. Lots of direct coordination.

– In short: Error prone and inefficient.



What is a version control system?

A repository of files with monitored



access to keep track of who and what

changes were made to files

Version tracking



Collaboration and sharing files



Historical information



Retrieve past versions



Manage branches



Why use it?

In code development, a version control



system is, at this point, almost mandatory

With multiple developers impossible to keep



track of versions with out it

Must be able to roll back a version if a test



suite fails

Must be able to tag software releases



Coordinating projects (solution)

Solution: A source code management (scm) tool.



– Repository: Code stored on a central server.



– Working copy: The developer checks out a copy



of the code in the repository to his/her computer.

– Revision history: Every change to every file is



logged in a database. Can be rollbacked.

– Conflict handling: What happens when two



developers change the same file? The same line?

Basic Work Cycle

Checkout a working copy



Update a working copy



Make changes



Examine your changes



Commit your changes



Some Commands

Subversion commands communicating with the server:



svn checkout ...



svn commit



Offline Subversion commands:



svn add



svn delete



svn status     (high level compare)



svn diff    (low level compare)



svn rename



svn move



...



More information:



svn help [cmd]



Create Repository

Creating a repository:



/home/shafiqAlibhai> svnadmin create assignment1



...results in a repository directory:

/home/shafiqAlibhai/assignment1

What's inside the repository?



/conf/...



/dav/...



/db/...



/format



/hooks/...



/locks/...



/README.txt



Basic commands

svn checkout <source>

$ svn checkout <http://url/repos/projectA>

A projectA/file1

A projectA/file2

A projectA/file3

Checked out revision 28.

$

svn status

$ svn status

M projectA/file1

?    projectA/file4

$

Basic commands

svn add/delete/copy/move <filename>

$ svn add file4

A file4

$

svn commit <message>

$ svn commit –m "fix another bugs"

Sending         file1

Adding          file4

Transmitting file data.

Committed revision 29.

$

Basic commands

svn log

$ svn log

---------------------------

r29 | shafiq | Tue, 26 Dec 2006 18:03:46 +0900 | 1 line

fix another bugs

---------------------------

r28 | shafiq | Mon, 25 Dec 2006 13:01:24 +0900 | 1 line

Fixed some bugs.

---------------------------

r27 | jAlibhai | Mon, 25 Dec 2006 12:58:24 +0900 | 1 line

Some works.

Basic Commands

svn update

$ svn update

U file1

A file4

Updated to revision 29

$ svn update –r28

U file1

D file4

Updated to revision 28

$

Trunk, Branches, Tags

SVN project directories are structured by convention with three top-level

directories:

trunk/



Represents the 'main line' of development with an entire copy of the



project.

branches/



Contains subdirectories, each holding an entire copy of the project



Each branch constitutes a significant enhancement to the project that



can be worked on independently.

tags/



Contains subdirectories, each containing one snapshot of the project.



Each snapshot represents a "public release" or other archival



configuration of the project.

Trunk vs. Branch

Trunk represents the stable version of the



system. It should always work, without errors

ofcourse.

Branches represent temporary development



streams to implement significant new features.

This allows commits to repository without breaking



the trunk (stable) version.

Branches may contain error/warnings etc.



Queries / Feedback
