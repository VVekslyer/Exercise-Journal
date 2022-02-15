### App
- [ ] UI coding in progress.
- [ ] Create a MongoDB database for the app.
    - [ ] Will store each user's name, email, goals, weight, height, custom workouts, progress data and so on.

### Specifications
- [ ] Make it so the user can choose what exercises he'd like to do at the time, so it isn't preset that they have to do legs, chest, pull.
- [ ] If we hover our mouse over one of the calendar days, the image should pop up.

### Android
- [ ] When the app is first launched, it runs very slowly. However, it runs really smoothly after the user has touched through each screen. So we need to have a loading screen and in the background loop through each screen in the app so that it's very fast when the user first starts it up.
- [ ] We need the app to remember the user's account. In it will remember a copy of the User class. It will contain the user's name, email, goals, weight, height, custom workouts and so on. 
    - [ ] We should find a way to store the user's details on their device.
    - [ ] As well as online using MongoDB.

### iOS
- [ ] Configure buildozer such that it will distribute an iOS version of the app. May need to use Myungsan's MacOS to do so.

### Design
- [ ] We need a logo for our app.
- [ ] We need a splashscreen for our app. Splashscreen is the first screen that every android app displays.

### Optomization
- [ ] The app is currently around 50 MB. That is way too much for such a simple app!
    - [ ] The main issue is likely due to many python modules in the buildozer.spec file that are included, but are not actually being used. They take up a lot of space.
- [ ] The app needs to run smoothly and comfortably. It may be worthwhile to look through the kivy docs or ask around the kivy Discord for some strategies and ways to make our app faster. 
    - [ ] Python apps in general are fairly slow. We may have to look at some ways to speed up python apps in general.