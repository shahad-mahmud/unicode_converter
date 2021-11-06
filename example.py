import unicodeconverter
from bijoytounicode import bijoy2unicode

# bijoy_text = 'aviv 2 G ‡NvlYvh় D‡jøwLZ ¯^vaxbZv Ges AwaKvimg~‡n ‡MvÎ, ag©, eY©, wk¶v, fvlv, ivR‰bwZK ev Ab¨wea gZvgZ, RvZxh় ev mvgvwRK DZ&‍cwË, Rb¥, m¤úwË ev Ab¨ ‡Kvb gh©v`v wbwe©‡k‡l c«‡Z¨‡Ki‌B mgvb AwaKvi _vK‡e| ‡Kvb ‡`k ev f~L‡Êi ivR‰bwZK, mxgvbvMZ ev Avš—R©vwZK gh©v`vi wfwË‡Z Zvi ‡Kvb Awaevmxi c«wZ ‡Kvbiƒc ‰elg¨ Kiv n‡ebv; ‡m ‡`k ev f~LÊ ¯^vaxb‌B ‡nvK, ‡nvK AwQf~³, A¯^vh়Z¡kvwmZ wKsev mve©‡fŠg‡Z¡i Ab¨ ‡Kvb mxgve×Zvh় weivRgvb|'
# bijoy_text = 'বাণিজ্য  মন্ত্রী মহোদয় অনুগ্রহ করিয়া বলিবেন কি'
bijoy_text = 'A‡_©i'
# bijoy_text = '‡nj‡g‡Ui wb‡P mvbM­vm| c¨vU KvwgÝ‡K RvqMv ‡_‡K `vuwo‡q ‡Lj‡Z wM‡q ejUv ÷v‡¤ú ‡W‡K Avb‡jb| ‡divi c‡_ ‡nj‡gUUv Ly‡j e¨vUUv DuwP‡q ai‡jb M¨vjvwii w`‡K| evDÛvwii Icv‡k Zvu‡K Rwo‡q ai‡jb mZx_©iv| Aveyavwei ‡W«wmsi“‡gi Uv‡b‡j ‡XvKvi ci ‡cQb ‡_‡K R¡jR¡j KiwQj Rvwm©i 45 b¤^i| `ª“ZB wgwj‡q ‡Mj ‡mUv| nq‡Zv wµ‡÷vdvi ‡nbwi ‡MBj‡K ‡klev‡ii g‡Zv ‡`Lv ‡Mj Avš—R©vwZK wµ‡K‡U e¨vwUs Ki‡Z| AvbyôvwbK ‡Kv‡bv ‡NvlYv Av‡mwb, Z‡e A‡÷«wjqvi wec‡¶ I‡q÷ BwÛ‡Ri g¨v‡P ‡MBj‡K wN‡i ‰Zwi nIqv AvenUv Bw½Z w`‡q‡Q AgbB|'

unicode_text = unicodeconverter.convert_bijoy_to_unicode(bijoy_text)
# unicode_text2 = bijoy2unicode(bijoy_text)

# print(unicode_text2)
print(unicode_text)


# ‡KŠwk‡Ki nv‡Z A‡bK K‡ivbv -- i = 0
# K‡Šwk‡Ki nv‡Z A‡bK K‡ivbv -- i = 2