<h1>The Poor Man's All Weather Strategy</h1>

Standard disclaimer: This code is developed for academic and illustrative purposes only and shall not be construed as financial, tax or legal advice or recommendations. The accuracy of the data on this site cannot be guaranteed. Users should use the information provided at their own risk and should always do their own due diligence before any investment decision. The information on this site does not constitute a solicitation for the purchase or sale of securities. No representation or implication is being made that using the information provided here will generate profits or ensure freedom from losses. All ideas and material presented are entirely those of the author and do not necessarily reflect those of the publisher. 

CFTC RULE 4.41 – HYPOTHETICAL OR SIMULATED PERFORMANCE RESULTS HAVE CERTAIN LIMITATIONS. UNLIKE AN ACTUAL PERFORMANCE RECORD, SIMULATED RESULTS DO NOT REPRESENT ACTUAL TRADING. ALSO, SINCE THE TRADES HAVE NOT BEEN EXECUTED, THE RESULTS MAY HAVE UNDER-OR-OVER COMPENSATED FOR THE IMPACT, IF ANY, OF CERTAIN MARKET FACTORS, SUCH AS LACK OF LIQUIDITY. SIMULATED TRADING PROGRAMS IN GENERAL ARE ALSO SUBJECT TO THE FACT THAT THEY ARE DESIGNED WITH THE BENEFIT OF HINDSIGHT. NO REPRESENTATION IS BEING MADE THAT ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFIT OR LOSSES SIMILAR TO THOSE SHOWN.

<h2> Why All Weather? </h2>

Gonna fill out this section at some point

<h2> Assumptions </h2>

In no particular order and subject to revision:

<ul>
	<li> Equalized variance within boxes before equalizing variance between boxes </li>
	<li> Didn't sum variances the statistically correct way because "correlation doesn't exist" </li>
	<li> Used four ETFs -- GLD (gold), DBC (commodities), TLT (long-term treasuries), and VTI (American stock market) </li>
	<li> The point of using these ETFs is that they all have roughly similar volatilities (as measured by standard deviation). I didn't double check to make sure that they have the same returns (and thus the same risk/return profiles) since I only have data going back  </li>
	<li> I did not include an IL bond asset because there were no IL ETFs that were volatile enough or levered to work out. Gold is an (imperfect) substitute for this. </li>
</ul>

The All Weather configuration was as such (and also subject to revision):

<ul> 
	<li>Growth Rising: VTI, DBC (may also want to add EMB for EM debt and HYG for corporate debt)</li>
	<li>Growth Falling: TLT, GLD</li>
	<li>Inflation Rising: GLD, DBC, (may also want to add EMB for EM debt)</li>
	<li>Inflation Falling: VTI, TLT</li>
</ul>

Since I don't have access to leverage, I can only choose relevant ETFs with similar volatility (and hopefully return) profiles. Below are the volatilities of different ETFs. 

HYG 0.0177601625748 (only goes back to 2008)
EMB 0.0192013473106 (only goes back to 2008)
TLT 0.0185163656414

VTI 0.0254056851964
EEM 0.0380752440487
VGK 0.0323986392606

DBC 0.0283440488481
GLD 0.0272751538992

<h2> Navigating the Files </h2>

The workflow is something like this: 

<ol>
	<li> Use series_getter.py to download price data for ETFs from Yahoo! Finance. This will output them to CSV, which I copied and pasted over to data/all-weather.xlsx</li>
	<li> Do whatever analysis in all-weather.xlsx. Use the "Simulated Returns" column to weight each asset however you'd like in a back-of-the-envelope manner. </li>
	<li> Copy and paste this column over to backtest/aw-simulated-returns.csv </li>
	<li> Use comparison.py to get the SP500's price data and remove #N/As from aw-simulated returns. Output these to two new files. </li>
	<li> Plot them in aw-simulated-returns.xlsx. </li>
</ol>

This is all completely separate from all-weather.py in the main folder, which takes the results of all the above research and systematizes it to spit out weights for the future, based on the last X days' volatilities for each ETF.