# Manifest that kills a process called killmenow
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin/:/root',
}