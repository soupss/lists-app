*i really need to organize this file*

+ Manipulate database from view

    - [x] Delete items
    - [x] Delete lists
    - [x] Rename lists
    - [x] Change item title and description

+ Style

    - [ ] Interactive dropdown icon

+ Sidebar

    - [ ] Make mobile friendly
    - [ ] Change sidebar nav to a better one

- [x] Use RESTful route naming convention
- [x] Display time correctly
- [ ] Display time relatively

    + '3 Days ago' instead of '04/20/20'
    + Display absolute time when item is older than 1 week

- [ ] Better route variables. 

    'list_id' & 'item_id' instead of 'id'

- [x] Built-in "Favorites" list. Items signified with a star

    + ~~List and item models currently have a one to many relationship. That needs to be changed.~~
    + ^favorite list does not need to be saved to db. nothing needs to be saved, can do logic in view
    - [x] Show which list the item is from when displayed in the favorite list.
    - [x] When editing/deleting items from favorite list, redirect properly

- [ ] Flash notification when creating, editing or deleting lists/items
- [ ] Sort list by time posted
- [ ] Add authentication
- [ ] Make ui mobile-friendly

    mostly sidebar, maybe proportion issues

- [ ] List group feature

    sort lists in group, maybe make new group model? or just add group flag to list model

- [ ] Dont remove whitespace in list description
- [ ] Feature to move items from one list to another
- [ ] Add icon. custom logo?
- [ ] Todo list feature

    When creating a list, choose list type.

    + List
	
	Bundles of Title + description

    + Todo
	
	Add tasks with due dates that you can tick off, automatically move to "done" section of list

**- [ ] Add User Authentication with accounts**

    Big feature. includes:

    + register + login
    + request a new password

#### Final step

- [ ] **Deploy!**

## Issues

1. a lot of repeated code in html files
