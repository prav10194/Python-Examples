## Find value from key in URL

Given a URL, extract the value of a given key from list of parameters. 

Example URLS - 

[
"https://leetcode.com?utc_device=mobile&utc_source=google",
"https://hackerrank.com?utc_device=desktop&utc_source=facebook",
"https://hackerrank.com?utc_device=mobile",
"https://geekforgeeks.com?utc_source=google"
]

given <b>returnSourceKey(urlList, parameterKey)</b> return the value with the highest frequency. In above example, if parameterKey = utc_source then return google as frequency is 2. If parameterKey = utc_device then return mobile as frequency is 2. 

<b>Solution: </b>
