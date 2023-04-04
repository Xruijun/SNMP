#!/usr/bin/perl

use strict;

my $file="file.trap";

open(HANDOUT,">>./$file");

while()
{
print HANDOUT "$_";
}
