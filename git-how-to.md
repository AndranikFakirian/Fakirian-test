How to create a ssh key:
Terminal:
1. ssh-keygen -t rsa
2. (name of file)
3. cat (name of file).pub
4. copy ssh-key (public)
How to add ssh-key (public) in GitHub:
1. go to settings
2. go to ssh and GPG keys
3. add ssh-key (public)
How to add ssh-key (private) in system:
Terminal:
1. ssh-add (name of file)
How to clone new Repo:
Terminal:
1. git clone git@github.com:username/name_of_repo.git