# This Puppet Create The School File
user { 'WWW-data':
  ensure => 'present',
}
group { 'WWW-data':
  ensure => 'present',
}
file { '/tmp/school':
  ensure  => 'present',
  owner   => 'WWW-data',
  group   => 'WWW-data',
  mode    => '0744',
  content => 'I love Puppet'
}
