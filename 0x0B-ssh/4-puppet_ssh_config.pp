# puppet script that changes lines in a ssh config file.

file_line { 'indentity_file':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/.ssh/config',
}

file_line { 'pwd_aut':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/.ssh/config',
}