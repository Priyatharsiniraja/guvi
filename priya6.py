pi=str(input())
if (pi=='a' or pi=='A' or pi=='e' or pi=='E' or pi=='i' or pi=='I' or pi=='o' or pi=='O' or pi=='u' or pi=='U'):
    print('Vowel')
elif (pi>='a' and pi<='z') or (pi>='A' and pi<='Z'):
    print('Consonant')
else:
    print('invalid')
