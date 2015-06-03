# To Setup Project:

## Postgres
```zsh
brew update
brew doctor
brew install postgresql

#install lunchy
gem install lunchy
mkdir -p ~/Library/LaunchAgents
cp /usr/local/Cellar/postgresql/{version NO.}/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
#start postgres
lunchy start postgres
#stop
lunchy stop postgres
```

### Postgres configuration

* [reference](https://www.digitalocean.com/community/tutorials/how-to-use-roles-and-manage-grant-permissions-in-postgresql-on-a-vps--2)

```zsh
#superuser
createdb `whoami`
createuser joyceful
#go to postgres command line
psql 
CREATE DATABASE joycefuldb OWNER joyceful;
#add password to role
\password joyceful
```


## Migrations

```zsh
./manage.py syncdb
./manage.py schemamigration photography --initial
./manage.py migrate photography
```
