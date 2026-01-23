# Rate My Dorm
## Inspiration
Every year, students at WPI have to make the arduous decision of where they should reside for the next year. Naturally, all kinds of questions come up when trying to decide.
**What kinds of rooms are there?**
**What are the amenities?**
**Do I have to share a bathroom with the whole floor?**

So, we have come up with a solution to help with mitigating student stress.

## What it does
With help from your fellow goats, Rate My Dorm helps you decide what on-campus residence best suits your needs. 

### Tag System
Each residence at WPI has been diligently labeled with different tags that you can sort by. This includes but isn't limited to:
- Years: Upper-class, First-year
- ADA friendly
- Room Types: Singles, Doubles, Triples, Suite-style

And more!

### Rating System
If you'd like to hear student perspectives, you can refer to each residence's reviews! Each residence has an overall score out of 5, calculated using the average of 4 rating scales:
- Room Size
- Proximity to dining options
- Proximity to academic buildings
- Building amenities

## How we built it
To start, we set up a database using MongoDB and creating tables. There were tables for organizing each different dorm, the user reviews, the individual ratings (based on the aforementioned scales) , and the overall ratings. 

The design and layout of the site was created using Figma. Then, we deployed it using Railway.

## Challenges we ran into
One of the main challenges that we ran into was implementing MongoDB into our backend. Some of our team members have experience using databases, but never using MongoDB, so there was a bit of a learning curve. 

We also ran into some issues with all of our teams members being able to connect to the database and host the server. However, we eventually found that it was necessary to whitelist ourselves in order to access the database, so we learned a lot of lessons about backend development. 

Additionally, we spent a lot of time trying to use Auth0 for our login functionality, but we had to table it due to limited time. However, we would love to be able to implement it in later versions.

## Accomplishments that we're proud of
For our team, this was our first time not only taking on such an intensive idea, it was our first time coordinating 5 developers simultaneously. We all had experience with Git, but there was a lot we had to learn regarding effective version control practices. Despite these challenges, we were able to accomplish 3 significant achievements:
- Designing and implementing a working UI, complete with even its own logo
- Integrating our database
- Deploying our website

We also had an amazing time! As previously stated, it was our first time coordinating as a team. The bonds that we built over the span of 24 hours will last beyond this weekend.

## What we learned
We learned many new things while working on this project, including being able to implement MongoDB, working with FastAPI, and backend development as a whole. We learned a lot of this through intensive research of documentation and Stack Overflow, which helped get through debugging.

## What's next for Rate my Dorm
- Utilize Auth0 to create a secure and functional login system
- Implementing an interactive map of campus with labelled dorms
- Implement a summary of student reviews using AI
- Feature for users to create tier lists
