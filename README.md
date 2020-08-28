# covclass (Covid Classifier)
A covid death classifier.
- Data from https://covid19.karnataka.gov.in/english
- Grabs the PDF, extracts the data using Py2PDF
- Raw Data is cleaned using various methods including regex, identifying valid readable data pages
- Data is stored in localdb.txt
- This data is used to plot visualizations using https://plotly.com/

Note : Readable data available from 21-07-2020. Data before this date is not included as it does not follow the conventions for clean data.

(PR's welcome on branch:release)
