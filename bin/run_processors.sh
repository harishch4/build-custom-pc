cd ../
rm jsonFiles/*_processors.json
scrapy crawl -o jsonFiles/rawdata_processors.json -t jsonlines processor
cd utilityScripts
python3 jsonPrep.py