# Homework 10

## Closed Issues

Issue 1  

Problem: Username/nickname did not check for uniqueness. This allows users to create username/nickname that were the same.  

Steps: Under Class UserService I changed the create class method. The changes made was a separation of concerns between checking the email and username/nickname uniqueness. It also generates one if user does not provide while ensuring it is not taken. I included two new classes called EmailAlreadyExistsException and NicknameAlreadyExistsException. I included these new exceptions in the routers file. I added testing to the behavior of checking username/nickname uniqueness was passing.  

Outcome: With these new changes, the program ensures that users are creating or generates a username/nickname that is unique and cannot be used by others.

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/services/user_service.py#L60-95)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/tests/test_users_api.py#L194-206)  

[Closed Issue 1 Link](https://github.com/ipl2/event_manager_hw10/issues/1)  



Issue 2  

Problem: Password was missing some additional. For instance, checks for length or symbols.  

Steps: In the user_schemas file, I added these missing checks in the class UserCreate(UserBase). Additionally, I had errors running saying I was on pydantic v2 so i had to adjust the code to be recognized by it. I included testings to verify the behaviors of the checks were running correctly. Alongside checking the behavior, I also checked the errors were also outputting correcty.  

Outcome: These new changes allow for a more secure password that checks and include these complex changes. This enchances the users security.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/schemas/user_schemas.py#L45-62)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/tests/test_users_api.py#L210-238)  

[Closed Issue 2 Link](https://github.com/ipl2/event_manager_hw10/issues/3)  



Issue 3  

Problem: There are gaps needed to be covered when updating certain fields of profile like entering empty strings and string lengths.  

Steps: For the class UserBase(BaseModel), I updated the lengths to nickname, first, and lastname. Bio did not have any lengths so I added minimum and max lengths for users to enter. Following that, I added an error to be raised when users enter an empty string. Testing was added to ensure these behaviors are outputting correctly in the test_schemas file.  

Outcome: These coverages for updating profile no longer accepts empty strings and can not surpass certain lengths for a valid profile.  

[Code with new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/schemas/user_schemas.py#L29-56)  

[Code for testing new solution](https://github.com/ipl2/event_manager_hw10/blob/main/app/tests/test_user_schemas.py#L64-114)  

[Closed Issue 3 Link](https://github.com/ipl2/event_manager_hw10/issues/5)  



Issue 4  

Problem:  

Steps:  

Outcome:  

[Code with new solution]()  

[Code for testing new solution]()  

[Closed Issue 4 Link]()  



Issue 5  

Problem:  

Steps:  

Outcome:  

[Code with new solution]()  

[Code for testing new solution]()  

[Closed Issue 5 Link]()  

## Project Image Deployed to Dockerhub

## Reflection Paragraph