# conect to shh server eith no keys
file_line { 'identityFile':
    ensure  => 'present',
    line    => 'identityFile ~/.ssh/holberton',
    path    => 'etc/ssh/ssh_config',
    replace => true,
}

file_line { 'PasswordAuthentication':
    ensure  => 'present',
    line    => 'PasswordAuthentication no',
    path    => 'etc/ssh/ssh_config',
    replace => true,
}
