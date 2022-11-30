with open(newfile.txt,'r') as fp:
    total_lines=fp.readlines()

with open(final_ans.txt,'w') as fp:
    count=0
    for line in total_lines:
        if count==4:    
            count=count+1
            continue
        else:
            fp.write(lines)
        count += 1