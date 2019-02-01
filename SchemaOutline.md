# Planned Schema

## Functions of a Derby League
* Basic Member Info
* Teams/Officials/Volunteers
* Dues
* Attendance
* Jobs

Thus table structure should start with this.
* Members
* Teams
* Team Members
* Attendance
* Jobs
* Dues

From there we will likely have some additional linked tables and tables for details. Thus far I've got:

* injury_reports
* schedule (for practices and games)
    * Eventually involve API integration with Google Calendar
* bout_jobs
* officials (for position tracking/rosters)
* rosters
* paperwork
    * Planned on just populating a link to each type of paperwork. Link would go to a doc storage like s3.

There will also likely need to be some helper tables to define options for data validation.
* dues_structure (rates for injured skaters, full time skaters, skaters on leave, BOD, officials, etc.)
* employees (Jobs will define the jobs that exist and descriptions and so forth. This will be a table that can be in flux and will dictate who is actually assigned what job)

## Column details for major tables
I've started detailing the actual columns and data types at least for the major tables.

Some of the types below are based on standard database types and some are features of Django plugin (it's the multiple choice option)

### Members
This is all of the detailed information likely on someone's intake form or google sheet.
* full_name
    * varchar
    * NOT NULL
* derby_name
    * varchar
    * nullable
* derby_number
    * int
    * nullable
* phone_number
    * int
    * nullable
* email
    * varchar
    * NOT NULL
* member_type
    * multiple choice
        * volunteer, official, bootcamp, skater
* status
    * multiple choice
        * active, injured, inactive, bod member, etc. (for dues)
* emergency_contact_name
    * varchar
    * NOT NULL
* emergency_contact_number
    * int
    * NOT NULL
* teams
    * foreign key to TeamMembers
* jobs
    * foreign key from employees table
* date_joined
    * date

### Teams
This defines home teams/travel teams.
* Name
    * NOT NULL
    * UNIQUE
    * varchar
* date_created (does anyone care? Maybe not)
    * date
* Type
    * Single choice/option (ie Travel/Home/A/B/C, etc.)

### TeamMembers
Intermediate table joining Member name with Team data.  
Lists the member and team they belong to.  
If a member belongs to multiple teams, they will have multiple entries in this table.

* member
    * foreign key to Members
* team
    * foreign key to Teams
* role
    * multiple choice option (jammer, pivot, blocker, coach, captain)
(Should I add bench/third base coach separately?)

### Jobs
Defines the name, purpose, reporting structure of various jobs
* name
    * varchar
    * NOT NULL
* committee
    * varchar
    * nullable?
* manager
    * foreign key to employees probably or members
* commitment (number of hours)
    * int
* duties
    * large varchar

### Dues_structure
* amount
    * int (or currency if supported)
* type
    * limited choice (same as member_status: active, inactive, injured, etc.)
    * varchar

### Dues or dues_status
* member
    * foreign key to Members
* amount_owed
    * int or currency
* bill_date
    * date
* paid
    * binary

### Paperwork
Many of these are binary fields basically saying "DID YOU FILL IT OUT?"
* member
    * foreign key to Members
* WFTDA_Insurance
    * binary
* liability_waiver
    * binary
* liability_waiver_url
    * link to storage with copy of waiver
    * varchar
* media_waiver
    * binary
* media_waiver_url
    * varchar
    * link to storage with copy of waiver.

### Injury_reports
This report contains a lot of details that should be stored in its own table. This could be useful for dues calculation functions or ensuring skaters are not skating when they shouldn't be.
* member
    * foreign key to member
* incident_date
    * date
* injury
    * varchar
* witness
    * foreign key to members 
* full_report_link
    * varchar
    * link to storage

Whatever else is on this doc

### Attendance
Did you go to practice HMMM?
* event_date
    * date
* attendance_value
    * varchar or int (ie assign a value to "full" "partial" "none" or use those strings)
* skater
    * foreign key to members

### Schedule
Games, practices, etc.  
Integrate with a calendar app. Basically might use this for joins with attendance.  
Also, I have team hosting and match information for attendance calculations.
* event_date
    * date
* event_type
    * single choice (practice, game, scrimmage, etc.)
* team_hosting
    * foreign key to teams (multiple choice for combined, solo team practices, or open league practices)
    * nullable
* coach
    * foreign key to members
* match_one
    * multiple choice foreign key to teams, limit 2
    * nullable (for scrimmages)
* match_two
    * multiple choice foreign key to teams, limit 2
    * nullable
* start_time
    * time or timestamp
* end_time
    * time or timestamp

### Bout_jobs
For leagues that assign jobs to skaters during games.  
This table tracks what bout jobs exists and how many people are required to do a job (such as 5 for security or 2 for merch)
* description
    * varchar
* duties
    * large varchar
* manager (coordinator?)
    * foreign key to members
* num_required
    * int
* length
    single choice (1st game, 2nd game, full night, half to half, etc.) or int