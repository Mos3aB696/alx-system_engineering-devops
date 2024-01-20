# This Puppet Create The School File
file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'WWW-data',
  group   => 'WWW-data',
  content => 'I love Puppet'
}
