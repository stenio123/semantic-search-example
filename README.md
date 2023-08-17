# Semantic Search Example

## Overview

This example uses 1000 pdfs offered by the [US Library of Congress](https://www.loc.gov/item/2020445568/). The code will do the following:

### generateDataset.py

- Extracts the text from the pdfs
- Uses 'all-MiniLM-L6-v2' to encode the vector representation
- Stores generated dataset as a local file

### uploadDatasetToHuggingFace.py

- Uploads a local file to a HuggingFace Dataset repository

### uploadToPinecone.py

- Retrieves a dataset from HuggingFace
- Transforms it to match Pinecone requirements
- Creates an index and upserts the dataset to Pinecone

### queryExample.py

- Given a query, fetches closely matching documents
- Generates a summary of the text to improve readability

## Notes

Out of the 1000 pdfs available, 19 have errors and were not included in the dataset:

```
Total PDFs processed: 1000
Number of successful PDFs: 981
Number of PDFs with errors: 19
Files with errors:
ILRVVACIV2JDSO4LHLATCOCKSEQYZCMZ.pdf
W432ODS2OFAWYUFA5RQ3B7OWKDQWFXCD.pdf
RUL7FW772XCJNPOZ34TKKQD3THLBCHH7.pdf
SW62D5RJMAPDJWHDMA5DLJWWLMSYZE26.pdf
6HTC5FVAQW3DVHYRD7PVJGBBQS7GRZTL.pdf
YFPURNDOL6TDJBBMD6FIMGPZ64OBYAQ6.pdf
EKYCT6JDYSVHCFQPJSCTM7VEB5GEUPWR.pdf
3P5D3UKXU2R6I2TK4OJSLL6LGIQJ4NY5.pdf
DEAHZFTA4CQDFDYMRX2NPJCKEHYPIK2Z.pdf
QBU5BZSBYX6YRLYVHQU4VCFMBYAHDHLU.pdf
6F47YISD72RZCG6OYZQCQLCYJX5E7MBK.pdf
LPA7M5D76YBCPXXCRVU7ZYECI6ODH24E.pdf
MDQ4BAARW6OTVBNBQE7BACYBNCCTWQDO.pdf
4GJGAIUVBMLM3W7O5SV4EKDNKC4DVOCL.pdf
R7YJNQZ3EFASORAHOJYEDNW3ZDWBNO4K.pdf
P7MWMCFFFSYYNCKYBTUACYK2SLL32AB5.pdf
WCILDJ3BDTTDKHJ3HGRQD2SF45E55AXN.pdf
BCUX3MK6IP7A6DWNH2ORKIO2PECOXJDO.pdf
3RCHLDD2YCPDNLHEV4AVKEPBYJP5UBZB.pdf
```

The query results would be better if the input data was cleaned up. Current result:

Query: "Foreign trade sanctions"

Result:
```
0.4 Match - id: 359, pdf_file: STG36KDTBPEJTVEWCY734EISHQ5ZUVWF.pdf, text summary: Summarize: Table 1267. U.S. Exports and Imports for Consumption of Merchandise. By Customs District: 2000 to 2008. In billions of dollars (780.0 represents $780,000,000,.000).

0.39 Match - id: 246, pdf_file: DQSGXNBZHHZWC6653JA34RT56TTUZ6W5.pdf, text summary: summarize: Summary US vs. Foreign by Program and Vessel Type for 11/20/2007 12:16:51 PM. 10/1/2002 9/30/2003 throughBULK/TUG/BARGEProg. Total                  Metric TonsUS                 Metric TonsForeign                  Metric TONS %US %FR /Country Total OFR US OFR Foreign OFR %US%FR / country Total of the US Navy’s ships and submarines.

0.38 Match - id: 276, pdf_file: GOCYUTJWJZBXHIUSFYG3LVX5SG6HPEVV.pdf, text summary: USTDA's program inChina focuses onadvancing U.S. trade and commercial interests in transportation, energy, agriculture, and healthcare sectors. USTDA conducted 9 reverse trade missions to introduce Chinese officials to U.s. best practices.

0.37 Match - id: 286, pdf_file: WYIDAT7X2DXYMKGRFAXDEAA2EJF23GRQ.pdf, text summary: The Credit Union National Association (CUNA) appreciates the opportunity to  criticize the proposed rule. CUNA represents more than 90 percent of our nation's 10,500 state and federal credit unions. We have always been concerned that the ever-increasing complexity of the OFAC sanctions programs raises the risk that entities may  mistakenlymistakenly violate the requirment.

0.36 Match - id: 874, pdf_file: YVM7OB53IEXWGJUUIKINFKKEDK23PC5K.pdf, text summary: Report setting forth in full the cir-centriccumstances relating to such transfer promptly upon discovery that: Such transfer was in violation of provisions of this part or any regu-lation, ruling, instruction, direction, or license issued pursuant to this part; or such transfer was not licensed or authorized by the Director of the Office of Foreign Assets Control; or if a license did purport to cover the transfer, such license had been ob-tained by misrepresentation of a third party or withholding of material facts.
```