# user configuretion change 
#  login with the holberton user and open a file without any error message.

exec {'replace-first':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-second'],
}

exec {'replace-second':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 40000/" /etc/security/limits.conf',
}
