# covclass (Covid Classifier)
A covid death classifier.
- Data from [Govt website](https://covid19.karnataka.gov.in/english)
- Grabs the PDF, extracts the data using Py2PDF
- Raw Data is cleaned using various methods including regex, identifying valid readable data pages
- Data is stored in localdb.txt
- This data is used to plot visualizations using [Plotly](https://plotly.com/)

Note : Readable data available from 21-07-2020. Data before this date is not included as it does not follow the conventions for clean data.

**(PR's welcome on branch:release)**
***
##Help me on/TO-DO

- [x] Inital release with basic visualizations
- [ ] Add more informative metrics
- [ ] Serve collected data via a REST API
***
##Changelog

| Releases      | What changed?                   |
| ------------- |:-------------------------------:|
| 1.0           |  Uploaded root directory        |
|               |  Static html file delivery      |
| 2.0           |  Moved to Flask framework       |
|               |  Improved CSS                   |
