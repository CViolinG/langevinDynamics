#!/usr/bin/perl
#use Math::Round;
#very simply, need to divide up the toy.* files into their respective bins to produce input files similar to the inputs for moradi's data
#
#the bins will be 40 * 0.1 = 4 total, spanning from -2 to +2.

#output data to output.txt
$divisor = shift;
$fo = ">Output24_$divisor.txt";
open FO,"$fo" or die;
$max = 0;
$min = 0;
$finishLine = 1000001/$divisor;#Total Lines : 1000001
$lineCount = 0;
foreach (@ARGV){#pass in input files as argument names
	print $_;
	open FH, $_ or die;
        $lineCount = 0;
        print "\n";
        select FO;
	print "\n";#new line for each run, should be n+1 lines

	while(<FH>){
	#discard first 12 lines by skipping lines with comments
	@line = split;
	if($line[0] eq '#'){}
	else{#grab the second value, bin it, then print it.
        $lineCount++;
	if($lineCount<$finishLine){	
        
        
        
        #Math for binning is on this line.  currently makes 26 bins.x
        $float = ($line[1] + 2) * 6;
        $bin = int($float + $float/abs($float*2 || 1))%24;
        
        
        $max = $line[1] if $line[1]>$max;
        $min = $line[1] if $line[1]<$min;
        
        
        
		print "$bin, ";#csv of bins
	}
        
}

}
	close FH;
        select STDOUT;
}


#print "$max\n";
#print "$min\n";
