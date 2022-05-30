# App

- [ ] Front-end and Back-end in progress.
- [ ] Create a MongoDB database for the app.
  - [ ] Will store each user's name, email, goals, weight, height, custom workouts, progress data and so on.

## Front-end

- [ ] Make it so that given a list of workouts, the app displays all the workouts neatly along each of its exercises.
- [ ] If we hover our mouse over one of the calendar days, the image should pop up.
- [ ] Create a schedule functionality
  - [ ] Where the user can schedule specific workouts.
- [ ] Create the graphed data screen, where the user can see their progress.
- [ ] Create a profile screen, where the user could upload a photo and see a few stats such as their current goals.

## Specifications

- [ ] Make it so the user can choose what exercises he'd like to do at the time, so it isn't preset that they have to do legs, chest, pull.

## Back-end

- [ ] ExpressJS implementation in progress.
- [ ] Create a MongoDB database for the app.
  - [ ] Will store each user's name, email, goals, weight, height, custom workouts, progress data and so on.

## Android

- [ ] When the app is first launched, it runs very slowly. However, it runs really smoothly after the user has touched through each screen. App runs really fast on Windows but Android needs work.
- [ ] We need the app to remember the user's account. In it will remember a copy of the User class. It will contain the user's name, email, goals, weight, height, custom workouts and so on.
  - [ ] We should find a way to store the user's details on their device.
  - [ ] As well as online using MongoDB.

## iOS

- [ ] Configure buildozer such that it will distribute an iOS version of the app. May need to use Myungsan's MacOS to do so.

## Design

- [ ] We need a logo for our app.
- [ ] We need a splashscreen for our app. Splashscreen is the first screen that every android app displays.
- [ ] In the starting screen, it doesn't feel like we're properly explaining what the goals. How would I know what I'd like to strive for Hypertrophy? Strength? Or performance?

## Optimization

- [ ] The app is currently around 50 MB.
  - [x] The main issue is likely due to many python modules in the buildozer.spec file that are included, but are not actually being used. They take up a lot of space. [RESOLVED]
- [ ] The app needs to run smoothly and comfortably. It may be worthwhile to look through the kivy docs or ask around the kivy Discord for some strategies and ways to make our app faster.
  - [ ] Python apps in general are fairly slow. We may have to look at some ways to speed up python apps in general.
- [x] Attempt resolving Critical Warning, too much iteration done before the next frame. <https://www.reddit.com/r/kivy/comments/pmxoft/critical_clock_warning_too_much_iteration_done/>
