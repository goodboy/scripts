#!/bin/gawk -f

# Fields of the csv in order are:
# Netborder Call-id,Call Date,Reference ID,Campaign Name,Phone Number,
# NCA Engine Result,Time Dialing,Time Connected,Time NCA Engine Completed,
# Time Queued,Time Connected to Agent,Detailed Cpd Result
BEGIN { 

	# config output options
	stats = 0
	rando = 0
	output = 0
	output_file = "results.txt"

	FS="," 

	# hard code the fields of interest (see ordering above)
	nbe_cid       = 1 #Netborder Call-id
	call_date     = 2
	number        = 5
	cpe_result    = 6
	detail_result = NF
}
# only comma delimited lines
FNR==NR {

	# copy the title line
	if (NR == 1) { title = $0 }

	# copy the second line
	if (NR == 2) { field_record = $0 }

	#check formatting (put in own routine?)
	#if (NF != 12) {
		# ignore
	#	print "detected non-formatted line!"
	#}else{

		# note: all gawk arrays are associative
		cpe_res_count[$cpe_result]++
		detail-res_count[$detail_result]++

		# sum up all dispositions
		dispsum++

		# remove all lines with "No-Answer"
		if( $cpe_result ~ /No-/) {
			next
			# do other shit like log call id and move files to a new dir for later processing
		}

		# skip entries which are calls to old numbers
		if($number in phonenum) {
			next
		}else{

			# add entries which have not been added yet
			phonenum[$number]++
			lastcall[$number] = $0
			print
		}

	#}
}


END { 

	# random info
	if( rando == 1 ) {
		for( i in phonenum) { 
			print(i " has been called " phonenum[i] " times")
			print("last line is : " lastcall[i])
		}
	}

	# output to file?
	if( output == 1) {
		# print preferred output to a file
		print title > output_file
		print field_record > output_file
		for( i in lastcall) {
			print(lastcall[i]) > output_file
		}
	}
	
	#n = asort(cpe_res_count, sorted_cpe_res, "@val_num_desc")

	# print stats?
	if( stats == 1) {
		# print the results
		print "Summary:"
		for(i in cpe_res_count) {
			percent[i] = 100 * cpe_res_count[i] / dispsum

			# printf fields format: %<sign><zero><width>.<precision>format
			printf("%-6d %-18s  %-5.1f (%)\n", cpe_res_count[i], i, percent[i])
		}
		print "---"
		printf("%-6d total\n", dispsum)
	}
}
