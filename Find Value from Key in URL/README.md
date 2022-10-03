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

<b>Additional possible questions - </b>

1. If the function has an additional parameter <b>returnSourceKey(urlList, parameterKey, utc_device)</b>, let's say utc_device, find which utc_source has the highest frequency. 
2. What if there are more parameters that might need to be extracted from the URL, would another approach work? Like maintaining a JSON object to store all keys and that can be used to run data analytics. 
3. What could be the possible edge cases? One can be what if the parameter we are looking for is not there, or another could be if the parameter key we are looking for exists in the url too - for example - https://geekforgeeksutc_source.com?utc_source=google, and last could be do we need to check validity of URL?
4. What if 2 parameters have the same frequency? Which one to return?


