#!/bin/gawk -f

# Fields of the csv in order are:
# Netborder Call-id,Call Date,Reference ID,Campaign Name,Phone Number,
# NCA Engine Result,Time Dialing,Time Connected,Time NCA Engine Completed,
# Time Queued,Time Connected to Agent,Detailed Cpd Result
BEGIN { 

	FS="," 

	# hard code the fields of interest (see ordering above)
	nbe_cid       = 1 #Netborder Call-id
	call_date     = 2
	number        = 5
	cpe_result    = 6;
	detail_result = NF
}
# only comma delimited lines
/\,/ {
	# skip the second line
	if (NR == 2) { next }

	#check formatting (put in own routine?)
	if (NF != 12) {
		# ignore
		print "detected non-formatted line!"
	}else{

		# note: all gawk arrays are associative
		cpe_res_count[$cpe_result]++
		detail-res_count[$detail_result]++

		# sum up all dispositions
		dispsum++

		# for later logs processing/organization
		if( cpe_result ~ /No-Answer/) {
			# do other shit like log call id and move files to a new dir for later processing
		}
	}
}
END { 

	#n = asort(cpe_res_count, sorted_cpe_res, "@val_num_desc")

	# print the results
	print "Summary:"
	for(i in cpe_res_count) {
		percent[i] = 100 * cpe_res_count[i] / dispsum

		# printf fields format: %<sign><zero><width>.<precision>format
		printf("%-6d are %-11s  %-4.1f (%)\n", cpe_res_count[i], i, percent[i])
	}
	printf("\n%-6d are %-11s  %-4.1f (%)\n", dispsum, "total", "100")
}
