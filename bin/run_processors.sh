cd $CUSTOMPC_HOME
rm $CUSTOMPC_HOME/jsonFiles/*_processors.json
scrapy crawl -o $CUSTOMPC_HOME/jsonFiles/rawdata_processors.json -t jsonlines processor
python3 $CUSTOMPC_HOME/utilityScripts/jsonPrep.py