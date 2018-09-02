import github3

second_stage_code = input

def github_login():
    code = ''
    while not code:
        code = second_stage_code('Enter 2FA code: ')
    return code

g = github3.login('raduiman', 'Zo9o6i994qwe', two_factor_callback=github_login)

riman = g.me()

print(riman.name)
print(riman.login)
print(riman.url)

