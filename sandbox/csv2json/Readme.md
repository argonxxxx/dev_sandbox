# csv2json

#### usage linux

	cat sample.csv | python csv2json.py

#### usage windows

	type sample.csv | csv2json.py

#### sample.csv

	1,2,3,4,5
	a,aa,aaa,aaaa,aaaaa
	b,bb,bbb,bbbb,bbbbb
	c,cc,ccc,cccc,ccccc
	d,dd,ddd,dddd,ddddd


#### output sample


	{
	    "1" : "a",
	    "2" : "aa",
	    "3" : "aaa",
	    "4" : "aaaa",
	    "5" : "aaaaa"
	}
	{
	    "1" : "b",
	    "2" : "bb",
	    "3" : "bbb",
	    "4" : "bbbb",
	    "5" : "bbbbb"
	}
	{
	    "1" : "c",
	    "2" : "cc",
	    "3" : "ccc",
	    "4" : "cccc",
	    "5" : "ccccc"
	}
	{
	    "1" : "d",
	    "2" : "dd",
	    "3" : "ddd",
	    "4" : "dddd",
	    "5" : "ddddd"
	}
