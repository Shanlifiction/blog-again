import time 
import datetime

all_blog_posts = [] #global variabel

#Menyval
def main():
    while True: 
        answer = input("WELCOME TO THIS BLOG\n 1. skriv inlägg\n 2. visa inlägg\n 3. ta bort inlägg\n\n\tQ to quit\n") 
        if answer.upper() == "Q":
            break
        elif answer == "1":
            create_post()
        elif answer == "2":
            all_posts()
        elif answer == "3":
            delete_post()
        else:
            print("Enter a valid input.") 

def create_post():
    post_title = input("Title: ")
    post_content = input("Content: ")
    post_date = datetime.datetime.now().date()
    post_time = time.time()
    print("Your blog post " + post_title + " published " + str(post_date))
        #(f"Your blog post {post_title} published {post_date}")
    post_created = [post_title, post_content, post_date, post_time]
    all_blog_posts.append(post_created)

def all_posts():
    print("All posts:")
    for post_created in all_blog_posts:
        print(post_created[0] + " " + str(round(time.time() - post_created[3])) + " sec")

def delete_post():
    all_posts()
    print("To delete a blog post write: del")
    ears_title = input("Please enter blog title: ")
    for post in all_blog_posts:
        if ears_title == post[0]:
            all_blog_posts.remove(post)
            print("Now " + ears_title + " will be deleted.")
            break
main()
