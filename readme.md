# Homework 10

## Closed Issues

Issue 1  

Problem: Username/nickname did not check for uniqueness. This allows users to create username/nickname that were the same.  

Steps: Under Class UserService I changed the create class method. The changes made was a separation of concerns between checking the email and username/nickname uniqueness. It also generates one if user does not provide while ensuring it is not taken. I included two new classes called EmailAlreadyExistsException and NicknameAlreadyExistsException. I included these new exceptions in the routers file. I added testing to the behavior of checking username/nickname uniqueness was passing.  

Outcome: With these new changes, the program ensures that users are creating or generates a username/nickname that is unique and cannot be used by others.

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/services/user_service.py#L60-95)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/tests/test_api/test_users_api.py#L196-205)  

[Closed Issue 1 Link](https://github.com/ipl2/event_manager_hw10/issues/1)  



Issue 2  

Problem: Password was missing some additional. For instance, checks for length or symbols.  

Steps: In the user_schemas file, I added these missing checks in the class UserCreate(UserBase). Additionally, I had errors running saying I was on pydantic v2 so i had to adjust the code to be recognized by it. I included testings to verify the behaviors of the checks were running correctly. Alongside checking the behavior, I also checked the errors were also outputting correcty.  

Outcome: These new changes allow for a more secure password that checks and include these complex changes. This enchances the users security.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/schemas/user_schemas.py#61-78)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/tests/test_api/test_users_api.py#L210-238)  

[Closed Issue 2 Link](https://github.com/ipl2/event_manager_hw10/issues/3)  



Issue 3  

Problem: There are gaps needed to be covered when updating certain fields of profile like entering empty strings and string lengths.  

Steps: For the class UserBase(BaseModel), I updated the lengths to nickname, first, and lastname. Bio did not have any lengths so I added minimum and max lengths for users to enter. Following that, I added an error to be raised when users enter an empty string. Testing was added to ensure these behaviors are outputting correctly in the test_schemas file.  

Outcome: These coverages for updating profile no longer accepts empty strings and can not surpass certain lengths for a valid profile.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/schemas/user_schemas.py#L29-56)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/tests/test_schemas/test_user_schemas.py#L64-114)  

[Closed Issue 3 Link](https://github.com/ipl2/event_manager_hw10/issues/5)  



Issue 4  

Problem: Case sensitivity was not enforced for username/nickname uniquess allowing duplications for these edge cases.  

Steps: More enhancements were made for uniqueness in username/nickname by using a direct SQLAlchemy to be case sensitive. This update is found in the class method create for UserService class. There is additional testing to check this behavior will run correctly. This is located in the test_api file. There is a check for exact matches of duplication but this new test checks duplication of different casing.  

Outcome: This new check ensures no duplication to occur since it now recognizes that a nickname/username like "Isabel123" and "isabel123" are the same. This input will fail and not allow this to be reused by other users.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/services/user_service.py#L60-98)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/tests/test_api/test_users_api.py#L241-255)  

[Closed Issue 4 Link](https://github.com/ipl2/event_manager_hw10/issues/7)  



Issue 5  

Problem: Password was not being validated during the reset process and did not follow same security rule when validated during user registration.  

Steps: To include this validation during reset, logic was added and UserPasswordUpdate was reused. This schema enforces password complexity checks. This now applies during the passsword reset. Testing was added to ensure this behavior is outputting correctly. This first test checks when a password is valid to reset while the second is a invalid password.  

Outcome: During the reset process, password now follows thesame checks as registration. Invalid passwords get rejected enforcing consistency of password checks.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/schemas/user_schemas.py#L62-78)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/tests/test_schemas/test_user_schemas.py#L116-137)  

[Closed Issue 5 Link](https://github.com/ipl2/event_manager_hw10/issues/9)  

## Project Image Deployed to Dockerhub

[Image](./docker_img.png)

## Reflection Paragraph

This assignment helps put in perspective the role of a software QA analyst. Before diving into the assignment, I had to familiarize myself with the new functionalities. I detected several issues along the way and used my technical skills to resolve them. In addition to learning these new functionalities, I also learned about the compare and pull request from Github. This part of the assignment was a bit of a challenge, as I came across problems trying to close out my issues. My solution was starting over and realizing my mistake of pushing after merging when that had to be done after closing an issue.  The steps taken to open and then close an issue were crucial. When it came to resolving an issue, I made sure to create a separate branch everytime.  

Within these branches I resolved five issues, including the one stated in the instructor's video. With each of these issues, I made sure to have a separation of concerns and place tests in their relevant files. These issues also aligned with the “specific issues to address,” targeting these problems in the code. Every change made was committed and recorded to continue in the progression of the code. There are resolutions to username validation that ensure there are no duplications, and it remains unique to one another. Password validation that followed the same checks in the registration process for the reset process. Finally, updating the profile fields also have checks to ensure empty strings are not accepted and follow a length max and min.  