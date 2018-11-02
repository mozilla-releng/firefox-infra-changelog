import github3

second_stage_code = input
username = str(input("Enter your GitHub username:  \n"))
password = str(input('Enter yourGitHub password:  \n'))

def github_login():
    code = ''
    while not code:
        code = second_stage_code('Enter 2FA code: ')
    return code

g = github3.login(username, password, two_factor_callback=github_login)

username = g.me()

print(username.name)
print(username.login)
print(username.url)



