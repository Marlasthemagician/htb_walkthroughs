#!/usr/bin/python3

users = ["Jane","Mike","John","Tim","James","Elisa","Roy"]

companies = ["qconsultingltd","qconsulting","qconsultingpvtltd","darkwingsolutions","winkmedia","lazycoopltd","lazycooppvtltd","lazycoop","wink","darkwing","scoobydoo","penguincrop","penguincorp","quick","penguin","dws","qcl","lcl"]

exts = [".htb",".com",".org",".net",".uk",".de",".eu",".cn",".fr",".it",".us",".au",".ca",".ltd",".co.uk"]


for user in users:
	for ext in exts:
		for company in companies:
			print(user + "@" + company + ext)
