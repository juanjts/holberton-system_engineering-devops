# modify a line with puppet
exec { 'best_dbugg':
path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin',
'/usr/local/sbin'],
command => "sudo sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
