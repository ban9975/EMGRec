import csv
with open('output.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['up', 'down'])

	for i in range(10):
		writer.writerow([i, 2*i])