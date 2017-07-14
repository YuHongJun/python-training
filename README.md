# python-training
python-training

### create my.cnf for MYSQL

在mac上：MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：

但是mac中在/etc/ 可能不存在my.cnf 或/mysql/my.cnf： 可以自己创建；

我在/etc/ 中创建/mysql/my.cnf， 并输入内容如下：
```
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
```
### 命令行：
```
$ alias mysql=/usr/local/mysql/bin/mysql

$ alias mysqladmin=/usr/local/mysql/bin/mysqladmin

$ mysqladmin -u root -p password new_password

mysql -u root -p

mysql> show variables like '%char%';


+--------------------------+-----------------------------------------------------------+
| Variable_name            | Value                                                     |
+--------------------------+-----------------------------------------------------------+
| character_set_client     | utf8                                                      |
| character_set_connection | utf8                                                      |
| character_set_database   | utf8                                                      |
| character_set_filesystem | binary                                                    |
| character_set_results    | utf8                                                      |
| character_set_server     | utf8                                                      |
| character_set_system     | utf8                                                      |
| character_sets_dir       | /usr/local/mysql-5.7.18-macos10.12-x86_64/share/charsets/ |
+--------------------------+-----------------------------------------------------------+
8 rows in set (0.00 sec)
```
看到utf8字样就表示编码设置正确

### MySql 5.7中添加用户,新建数据库,用户授权,删除用户,修改密码

#### 新建用户
创建test用户，密码是password。

mysql -u root -p

mysql> CREATE USER "test"@"localhost” IDENTIFIED BY "password"; #本地登录
mysql> CREATE USER "test"@"%" IDENTIFIED BY "password"; #远程登录
mysql> quit

mysql -u test -p #测试是否创建成功

#### 为用户授权

1. 登录MYSQL，这里以ROOT身份登录：
```
mysql -u root -p
```
2. 为用户创建一个数据库(testDB)：
```
create database testDB;
create database testDB default charset utf8 collate utf8_general_ci;
```
3. 授权test用户拥有testDB数据库的所有权限：

授权格式：grant 权限 on 数据库.* to 用户名@登录主机 identified by “密码”;　
```
grant all privileges on testDB.* to "test"@"localhost" identified by "password";
flush privileges; #刷新系统权限表
```
4. 指定部分权限给用户:
```
grant all privileges on testDB.* to "test"@"localhost" identified by "password";

flush privileges; #刷新系统权限表
```
5. 删除用户
```
drop user 用户名@'%';
drop user 用户名@ localhost;
```
6. 修改指定用户密码
```
mysql -u root -p
update mysql.user set authentication_string=password(“新密码”) where User="test" and Host="localhost";
flush privileges;
```