while(<>){
	@split = split /,/;
	foreach $value (@split){
		$array[$value] +=1;
	}
}$i=0;
foreach (@array){
$i+=1;
print "$i, $_\n";
}
