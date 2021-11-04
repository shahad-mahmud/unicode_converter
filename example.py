from unicodeconverter import converter
from unicodeconverter.converter import UnicodeConverter

bijoy_text = 'aviv 2 G ‡NvlYvh় D‡jøwLZ ¯^vaxbZv Ges AwaKvimg~‡n ‡MvÎ, ag©, eY©, wk¶v, fvlv, ivR‰bwZK ev Ab¨wea gZvgZ, RvZxh় ev mvgvwRK DZ&‍cwË, Rb¥, m¤úwË ev Ab¨ ‡Kvb gh©v`v wbwe©‡k‡l c«‡Z¨‡Ki‌B mgvb AwaKvi _vK‡e| ‡Kvb ‡`k ev f~L‡Êi ivR‰bwZK, mxgvbvMZ ev Avš—R©vwZK gh©v`vi wfwË‡Z Zvi ‡Kvb Awaevmxi c«wZ ‡Kvbiƒc ‰elg¨ Kiv n‡ebv; ‡m ‡`k ev f~LÊ ¯^vaxb‌B ‡nvK, ‡nvK AwQf~³, A¯^vh়Z¡kvwmZ wKsev mve©‡fŠg‡Z¡i Ab¨ ‡Kvb mxgve×Zvh় weivRgvb|'
unicode_text = UnicodeConverter.from_bijoy(bijoy_text)

print(unicode_text)