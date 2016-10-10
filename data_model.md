# Moody's Data Model

- days
	- { day }
		- { unique key }
			- timestamp
			- value


# Example
{
	days : {
		"2016-10-06" : {
			"UNIQUE_KEY" : {
				"day": ""2016-10-06",
				"ts" : "2016-10-06T17:29:45Z,
				"value" : "HAPPY"
			},
			UNIQUE_KEY" : {
				"day": ""2016-10-06",
				"ts" : "2016-10-06T17:27:37Z,
				"value" : "MEDIUM"
			}
		},
		"2016-10-05" : {
			"UNIQUE_KEY" : {
				"day": ""2016-10-05",
				"ts" : "2016-10-05T16:12:32Z,
				"value" : "SAD"
			},
			"UNIQUE_KEY" : {
				"day": ""2016-10-05",
				"ts" : "2016-10-05T17:04:10Z,
				"value" : "SAD"
			},
			"UNIQUE_KEY" : {
				"day": ""2016-10-05",
				"ts" : "2016-10-05T17:08:36Z,
				"value" : "HAPPY"
			}
		}
	}
}