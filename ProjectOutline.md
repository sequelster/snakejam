# Project Outline
The final product should have the below (and maybe the "nice to haves" also detailed below):
## Requirements:
- Authentication
  - View/Edit/Delete/Add Permissions based on authentication
    - Certain sensitive data needs to be hidden from non-leadership roles (things like home address, insurance information, etc.)
- Reporting
  - Ability to run reports such as:
    - "Who the heck is on this team?"
    - "What the heck are people's email addresses?"
    - "Who hasn't paid dues?"
- Easy to navigate GUI for entering and validating information.
- Minimum Tables:
  - main table:
    - Members
    - Teams
  - Derivative tables:
    - TeamMembers
    - Officials
    - Volunteers
    - Dues
 ## Nice to haves:
 - Report Automation
   - Email people automatically if they are on a report or meet some criteria (ie haven't paid dues.)
 - Calendar/Attendance tracking
   - How do calendars *even* work?
 - Really pretty UI.
   - I like design okay.
 - Customization
   - Ability for users to *add* their own fields, reports, etc.
 - Document tracking/upload
   - Ability to upload documents (like signed documents)
   - Ability to upload photos. Maybe you could have fancy shmancy headshots tracked here. Also, so your admins know who the hell these people are.
- Auto-conversion of Google Sheets.
  - This sounds....challenging. But maybe! Or at the least maybe I could template general/basic mapping for others to build off.
## Project Phases
#### Phase 1: How do I even?
- Figure out Django
- Figure out all of the database objects, relationships and structures.
  - Difficulty: where the many to many and one to many relationships will be and how we want to break down certain information (or not)
- Get a basic POC of HTML requests > Django > Mysql backend.
#### Phase 2: Basic Implementation
- Define and implement all of the database objects in Django.
- Configure the actual webpage/front end to access and manipulate these objects.
- Setup basic auth (maybe not HTTP basic auth, but some sort of auth)
#### Phase 3: Make it pretty!
- Get crackin' on CSS and Javascript to make nicer menus, buttons, headers, etc.
- Add in reporting here as well.
- Better Authentication (if I implemented something haphazardly)
#### Phase 4: Make it better
If I haven't been sucked into a blackhole at this point...
- Calendar/Attendance tracking
- Dues tracking (Paypal/Stripe API?)
- Customization/templating
- Document tracking (Support local storage, S3, and maybe Google's S3-like thing...whatever it is (Can you tell I use AWS?))
- Whatever other functionality I inevitably missed at this point.
