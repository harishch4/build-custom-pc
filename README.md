# build-custom-pc
## _Comparing prices across webstores._

### Initial setup:
```sh
pip3 install -r requirements.txt
export CUSTOMPC_HOME="path_to_root_dir"
```

### Run Steps:
```sh
cd bin
./run_processors.sh
```

### output file:
```sh
jsonFiles/final_processors.json
```

### _Currently scraping processor prices from :_
- [MDComputers](https://mdcomputers.in/)
- [PCShop](https://www.pcshop.in//)
- [ThinkPC](https://www.thinkpc.in/)
- [VedantComputers](https://www.vedantcomputers.com/)
- [TPSTech](https://www.tpstech.in/)


```sh
Processor                     	MDComputers	    PCShop	   ThinkPC	    Vedant	   TPSTech
AMD RYZEN 5-5600X             	         0	    21,999	     42000	₹22,250.00	Rs. 22,299
AMD RYZEN 5-3600              	         0	    16,999	     24000	₹16,750.00	Rs. 16,799
AMD RYZEN 9-5900X             	         0	    43,500	     78000	₹42,000.00	Rs. 42,249
AMD RYZEN 7-5800X             	         0	    33,999	     62000	₹33,400.00	Rs. 33,490
AMD RYZEN 7-3700X             	         0	    26,999	         0	₹24,650.00	Rs. 25,999
AMD RYZEN 9-3900X             	         0	    45,250	         0	         0	Rs. 37,890
AMD RYZEN 9-5950X             	         0	         0	    114000	₹57,700.00	Rs. 57,899
AMD RYZEN 5-5600G             	         0	         0	         0	₹22,280.00	Rs. 22,280
AMD RYZEN 5-3500X             	         0	    14,765	         0	         0	Rs. 14,700
AMD RYZEN 7-5700G             	         0	         0	         0	₹28,250.00	Rs. 28,380
Intel Core I3-10100F          	   ₹6,855 	         0	         0	         0	 Rs. 6,859
AMD RYZEN 7-3800X             	         0	         0	         0	         0	Rs. 25,900
Intel Core I5-10400           	         0	         0	     18000	         0	Rs. 13,910
Intel Core I5-9600K           	         0	         0	         0	         0	Rs. 14,990
Intel Core I3-10100           	         0	    11,999	         0	         0	 Rs. 9,399
Intel Core I5-12400F          	  ₹15,515 	         0	     25000	         0	Rs. 15,820
Intel Core I7-10700F          	  ₹23,579 	         0	         0	         0	Rs. 23,700
Intel Core I5-10500           	         0	    17,200	         0	         0	Rs. 17,499
Intel Core I3-12100F          	   ₹9,395 	         0	     15000	         0	 Rs. 9,450
Intel Core I5-11400           	  ₹15,120 	         0	     21500	         0	Rs. 15,260
Intel Core I9-11900           	  ₹38,975 	         0	         0	         0	Rs. 38,999
Intel Core I7-12700K          	  ₹37,375 	         0	         0	         0	Rs. 37,900
Intel Core I3-10105F          	   ₹6,830 	     7,800	         0	         0	 Rs. 7,120
Intel Core I9-11900KF         	         0	         0	         0	         0	Rs. 36,690
```

# TODO:
1. Add all components required for custom pc build.
2. Add more webstores to compare prices.
3. A clean WebUI.

