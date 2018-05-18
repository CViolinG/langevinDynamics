#!/usr/bin/perl

#very simply, need to divide up the toy.* files into their respective bins to produce input files similar to the inputs for moradi's data
#
#the bins will be 40 * 0.1 = 4 total, spanning from -2 to +2.

#output data to output.txt
open FO,">Output24.txt" or die;
select FO;
foreach (@ARGV){#pass in input files as argument names
#	print $_;
	open FH, $_ or die;
	print "\n";#new line for each run, should be n+1 lines
	while(<FH>){
	#discard first 12 lines by skipping lines with comments
	@line = split;
	if($line[0] eq '#'){}
	else{#grab the second value, bin it, then print it.
		
        
        
        
        #Math for binning is on this line.  currently makes 160 bins.x
        $bin = (($line[1]+2)*6)%24;
        
        
        
        
        
		print "$bin, ";#csv of bins
	}}
	close FH;
}

