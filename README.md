                                        "BRM - Book, Report, Monitor"
                                                Final Project

While taking CS50 course I had an opportunity to meet an old friend who manages training and consultation centre based in one of the universities here in Lithuania. This centre provides psychological consultations and support for students, teachers and everyone else in need. It has come to my attention that they do not have a unified database or an application that could be used for booking consultation cabinets, reporting about the consultations and reviewing all this data. The tools used now (Excel tables, Google Forms, etc.) require a lot of manual work checking information afterwards, consultants lack possibility to review their report submissions and therefore some reports are submitted twice or not submitted at all, etc.

Therefore my Final Project for the CS50 course is a web application called BRM – Book, Report, Monitor.

Functionality and structure of the website is related to two BRM user types and is as follows:

        1. Admin:
                o Can add available dates and times for each of the 3 cabinets to the booking calendar;
                o Can create new users, indicating their type;
                o Can view summary reports (all bookings, all non-reported consultations, history of all reported consultations);
                o Delete bookings of other users;
                o Make bookings;
                o Fill-in reports about the consultations;
                o Monitor own bookings, reports and history separately from all reports;
                o Review and change profile information;
                o Change password.

        2. Consultants:
                o Make bookings for consultations in 3 cabinets for the current and upcoming month;
                o Fill-in reports about the consultations (client, date, time, duration, consultation type, consultation price (depending on client type), comments);
                o Monitor own bookings,  non-reported consultations, and history;
                o Review and change profile information;
                o Change password.

BRM web application was build using:
        1. Python;
        2. SQL (3 tables);
        3. JavaScript (function changing background colour in the cabinet booking tables, depending on the availability: booked – red, available – green);
        4. HTML;
        5. CSS.


Thank you for this amazing experience and opportunity to learn!
