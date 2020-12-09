# conect to shh server eith no keys
file_line { 'IdentityFile':
    ensure  => present,
    replace => true,
    path    => 'etc/ssh/ssh_config',
    line    => 'identityFile ~/.ssh/holberton',
}

file_line { 'PasswordAuthentication':
    ensure  => present,
    replace => true,
    path    => 'etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
}
