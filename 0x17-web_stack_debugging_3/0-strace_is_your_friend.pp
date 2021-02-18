exec { 'best_dbugg':
path     => '/usr/bin/:/bin/:/usr/sbin/',
provider => 'shell',
command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
