import requests

# Simulated user database
users = {
    "1": {"email": "user1@email.com", "password": "1234"},
    "2": {"email": "user2@email.com", "password": "abcd"},
    "3": {"email": "user3@email.com", "password": "xyz"},
}

# Interaction counters
interactions = {
    "posts_viewed": 0,
    "comments_viewed": 0,
    "posts_created": 0
}

# Login function
def login():
    print("==== LOGIN ====")
    user_id = input("Enter your user ID: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = users.get(user_id)
    if user and user["email"] == email and user["password"] == password:
        print("Login successful!\n")
        return user_id
    else:
        print("Incorrect credentials. Exiting the program.")
        exit()

# Function to view posts and optionally view comments
def view_posts_and_comments():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    for post in posts[:5]:  # Show only the first 5 posts
        print(f"\nPost ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Content: {post['body']}")
        interactions["posts_viewed"] += 1

        see_comments = input("Do you want to see the comments? (y/n): ").lower()
        if see_comments == 'y':
            comments = requests.get(
                f"https://jsonplaceholder.typicode.com/posts/{post['id']}/comments"
            ).json()

            for comment in comments:
                print(f" - {comment['name']}: {comment['body']}")
                interactions["comments_viewed"] += 1

# Function to view logged user's own posts
def view_own_posts(user_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    )
    posts = response.json()

    print("\nYour posts:")
    for post in posts:
        print(f"- {post['title']}")
        interactions["posts_viewed"] += 1

# Function to view posts from another user
def filter_posts_from_other_user():
    other_id = input("Enter the other user's ID: ")
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts?userId={other_id}"
    )
    posts = response.json()

    if posts:
        print("\nPosts from the user:")
        for post in posts:
            print(f"- {post['title']}")
            interactions["posts_viewed"] += 1
    else:
        print("User not found or has no posts.")

# Function to create a new post (simulated)
def create_post(user_id):
    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")

    new_post = {
        "userId": user_id,
        "title": title,
        "body": content
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=new_post
    )

    if response.status_code == 201:
        print("Post created successfully!")
        interactions["posts_created"] += 1
    else:
        print("Failed to create the post.")

# ==== Main Program ====
logged_user = login()

while True:
    print("\n===== MENU =====")
    print("1 - View posts and comments")
    print("2 - View my posts")
    print("3 - View posts from another user")
    print("4 - Create a new post")
    print("5 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        view_posts_and_comments()
    elif option == "2":
        view_own_posts(logged_user)
    elif option == "3":
        filter_posts_from_other_user()
    elif option == "4":
        create_post(logged_user)
    elif option == "5":
        print("\n===== INTERACTION SUMMARY =====")
        print(f"Posts viewed: {interactions['posts_viewed']}")
        print(f"Comments viewed: {interactions['comments_viewed']}")
        print(f"Posts created: {interactions['posts_created']}")
        print("Thank you for using the system!")
        break
    else:
        print("Invalid option. Please try again.")
