B
    ¥yZ\ª¸  ã               @   s   d dl Z ee  d¡ dS )é    NsN  ã               @   s  d dl Z d dlZd dlZd dlZd dlZd dlmZ d dlmZ	 d dlm
Z
 d dlmZ d dlmZ dZdZd	Zd
ZdZdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zd d! Ze d"krye !d#¡ W n e"k
rü   Y nX e  dS )$é    N)Úsleep)Ústrftime)Úget)ÚBeautifulSoup)ÚThreadz[90mz[91mz[92mz[97mz[0mc           	   C   s\  t td  ytdd ¡ } W n tk
r8   t  Y nX tdd ¡ } t| dkrXd} ytd|  }W n: tj	j
k
r¢   t td t  ttd  t  Y nX t|jd	}|jd
dd}tdd}|jdd| id}| d¡}| |d jd |d j d |d j d |d j d |d j d |d j d |j ¡ W d Q R X | ¡  d S )NzMengupdate jadwal..z
.cookie/tsÚrr   Z83z2https://www.jadwalsholat.org/adzan/monthly.php?id=z1
Astaghfirullah..
Ukhty lupa ngidupin jaringannyaz
Enterin ajazhtml.parserÚtrZtable_highlight)Zclass_z
.cookie/scÚwZoptionÚvalue)ZattrsZtdú,é   é   é   é   é   )ÚprintÚlgÚopenÚreadÚIOErrorÚgettownÚlenr   ÚrequestsÚ
exceptionsÚConnectionErrorÚxÚinputÚmenuÚbsÚtextÚfindZfind_allÚwriteÚclose)Útsr   Úbr   ZscZkotaÚi© r&   ú<script>Úgettime   s*    
jr(   c              C   sÊ  t td t d t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d  t d! t d" t d# t d$ t d% t d& t d' t d( t d) t d* t d+ t d, t d- t d. t d/ t d0 t d1 t d2 t d3 t d4 t d5 t d6 t d7 t d8 t d9 t d: t d; t d< t d= t d> t d? t d@ t dA t dB t dC t dD t d t dE t dF t dG t dH t dI t dJ t dK t dL t dM t dN t dO t dP t dQ t dR t dS t dT t dU t dV t dW t dX t dY t dZ t d[ t d\ t d] t d^ t d_ t d` t da t db t dc t dd t de t df t dg t dh t di t dj t dk t dl t dm t dn t do t dp t dq t dr t ds t dt t du t dv t dw t dx t dy t dz t d{ t d| t d} t d~ t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d  t d¡ t d¢ t d£ t d¤ t d¥ t d¦ t d§ t d¨ t d© t dª t d« t d¬ t d­ t d® t d¯ t d° t d± t d² t d³ t d´ t dµ t d¶ t d· t d¸ t d¹ t dº t d» t d¼ t d½ t d¾ t d¿ t dÀ t dÁ t dÂ t dÃ t dÄ t dÅ t dÆ t dÇ t dÈ t dÉ t dÊ t dË t dÌ t dÍ t dÎ t dÏ t dÐ t dÑ t dÒ t dÓ t dÔ t dÕ t dÖ t d× t dØ t dÙ t dÚ t dÛ t dÜ t dÝ t dÞ t dß t dà t dá t dâ t dã t dä t då t dæ t dç t dè t dé t dê t dë t dì t då t dí t dî t dï t dð t dñ t dò t dó t dô t dõ t dö t d÷ t dø t dù t dú t dû t dü t dÆ t dý t dþ t dÿ t d  t d t d t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d  t d! t d" t d# t d$ t d% t d& t d' t d( t d) t d* t d+ t d, t d- t d. t d/ t d0 t d1 t d2 t d3 t d4 t d5 t d6 t d7 t d8 t d9 t d: t d; t d< t d= t d> t d? t d@ t dA t dB t dC t dD t dE t dF t dG t dH t dI t dJ t dK t dL t dM t dN t dO t dP t dQ t dR t dS t dT t dU t dV t dW t dX t dY t dZ t d[ t d\ t d] t d^ t d_ t d` t da t db t dc t dd t de t df t dg t dh t di t dj t dk t dl t dm t dn t do t dp t dq t dr t ds t dt t du t dv t dw t dx t dy t dz t d{ t d| t d} t d~ t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d  t d¡ t d¢ t d£ t d¤ t d¥ t d¦ t d§ t d¨ t d© t dª t d« t d¬ t d­ t d® t d¯ t d° t d± t d² t d³ t d´ t dµ t d¶ t d· t d¸ t d¹ t dº t d» t d¼ t d½ t d¾ t d¿ t dÀ t dÁ t dÂ t dÃ t dÄ t dÅ t dÆ t dÇ t dÈ t dÉ t dÊ t dË t dÌ t dÍ t dÎ t dÏ t dÐ t dÑ t dÒ t dÓ t dÔ t dÕ t dÖ t d× t dØ t dÙ t dÚ t dÛ t dÜ t dÝ t dÞ t dß t dà t dá t dâ t dã t dä t då t dæ t dç t dè t dé t dê t dë t dì t dí t d¶ t dî t dï t dð t dñ t dò t dó t dô t dõ t dö t d÷ t dø t dù t dú t dû t dü t dý t dþ t dÿ t d  t d t d t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d t d  t d! t d" t d# t d$ t d% t d& t d' t d( t d) t d* t d+ t d, t d- t d. t d/ t d0 t d1 t d2 t d3 t d4 t d5 t d6 t d7 t d8 t d9 t d: t d; t d< t d= t d> t d? t d@ t dA t dB t dC t dD t dE t dF t dG t dH t dI t dJ t dK t dL t dM t dN t dO t dP t dQ t dR t dS t dT t dU t dV t dW t dX t dY t dZ t d[ t d\ t d] t d^ t d_ t d` t da t db t dc t dd  t tde  ttdf t } t| dgkrBn^t| dhkrvt| dikrvtt| dj } n*t| dkkrtt| dj } ndl} tdmdn}| | ¡ | 	¡  t
  d S (o  Nz1.  zAmbarawa   z78.  zGombong    z155. zMentok     z232. ZSelongz
2.  zAmbon      z79.  zGorontalo  z163. zMerauke    z233. ZSemarangz
3.  zAmlapura   z80.  zGresik     z157. zMetro      z234. ZSengkangz
4.  zAmuntai    z81.  zGunung Sit z158. zMeulaboh   z235. ZSerangz
5.  zArgamakmur z82.  zIndramayu  z159. zMojokerto  z236. ZSeruiz
6.  zAtambua    z83.  zJakarta    z160. zMuara Buli z237. ZSibolgaz
7.  zBabo       z84.  zJambi      z161. zMuara Bung z238. Z
Sidikalangz
8.  zBagan Siap z85.  zJayapura   z162. zMuara Enim z239. ZSidoarjoz
9.  zBajawa     z86.  zJember     zMuara Tewe z240. ZSigliz
10. zBalige     z87.  zJeneponto  z164. zMuaro Siju z241. Z
Singaparnaz
11. zBalik Papa z88.  zJepara     z165. zMuntilan   z242. Z	Singarajaz
12. zBanda Aceh z89.  zJombang    z166. zNabire     z243. Z
Singkawangz
13. zBandarlamp z90.  zKabanjahe  z167. zNegara     z244. ZSinjaiz
14. zBandung    z91.  zKalabahi   z168. zNganjuk    z245. ZSintangz
15. zBangkalan  z92.  zKalianda   z169. zNgawi      z246. Z	Situbondoz
16. zBangkinang z93.  zKandangan  z170. zNunukan    z247. ZSlawiz
17. zBangko     z94.  zKaranganya z171. zPacitan    z248. ZSlemanz
18. zBangli     z95.  zKarawang   z172. zPadang     z249. ZSoasiuz
19. zBanjar     z96.  zKasungan   z173. zPadang Pan z250. ZSoez
20. zBanjar Bar z97.  zKayuagung  z174. zPadang Sid z251. ZSoloz
21. zBanjarmasi z98 . zKebumen    z175. zPagaralam  z252. ZSolokz
22. zBanjarnega z99.  zKediri     z176. zPainan     z253. ZSoreangz
23. zBantaeng   z100. zKefamenanu z177. zPalangkara z254. ZSorongz
24. zBanten     z101. zKendal     z178. zPalembang  z255. ZSragenz
25. zBantul     z102. zKendari    z179. zPalopo     z263. ZStabatz
26. zBanyuwangi z103. zKertosono  z180. zPalu       z257. ZSubangz
27. zBarabai    z104. zKetapang   z181. zPamekasan  z258. ZSukabumiz
28. zBarito     z105. zKisaran    z182. zPandeglang z259. Z	Sukoharjoz
29. zBarru      z106. zKlaten     z183. zPangkajene z260. z
Sumbawa Bez
30. zBatam      z107. zKolaka     z184. z261. ZSumedangz
31. zBatang     z108. zKota Baru  z185. zPangkalanb z262. ZSumenepz
32. zBatu       z109. zKota Bumi  z186. zPangkalpin z
Sungai Liaz
33. zBaturaja   z110. zKota Janth z187. zPanyabunga z264. z
Sungai Penz
34. zBatusangka z111. zKota Mobag z188. zPare       z265. Z
Sungguminaz
35. zBaubau     z112. zKuala Kapu z189. zParepare   z266. ZSurabayaz
36. zBekasi     z113. zKuala Kuru z190. zPariaman   z267. Z	Surakartaz
37. zBengkalis  z114. zKuala Pemb z191. zPasuruan   z268. ZTabananz
38. zBengkulu   z115. zKuala Tung z192. zPati       z269. ZTahunaz
39. zBenteng    z116. zKudus      z193. zPayakumbuh z270. ZTakalarz
40. zBiak       z117. zKuningan   z194. zPekalongan z271. ZTakengonz
41. zBima       z118. zKupang     z195. zPekan Baru z272. z
Tamiang Laz
42. zBinjai     z119. zKutacane   z196. zPemalang   z273. z
Tanah Grogz
43. zBireuen    z120. zKutoarjo   z197. zPematangsi z274. Z	Tangerangz
44. zBitung     z121. zLabuhan    z198. zPendopo    z275. z
Tanjung Baz
45. zBlitar     z122. zLahat      z199. zPinrang    z276. z
Tanjung Enz
46. zBlora      z123. zLamongan   z200. zPleihari   z277. z
Tanjung Paz
47. zBogor      z124. zLangsa     z201. zPolewali   z278. z
Tanjung Piz
48. zBojonegoro z125. zLarantuka  z202. zPondok Ged z279. z
Tanjung Rez
49. zBondowoso  z126. zLawang     z203. zPonorogo   z280. z
Tanjung Sez
50. zBontang    z127. zLhoseumawe z204. zPontianak  z281. z
Tapak Tuanz
51. zBoyolali   z128. zLimboto    z205. zPoso       z282. ZTarakanz
52. zBrebes     z129. zLubuk Basu z206. zPrabumulih z283. ZTarutungz
53. zBukit Ting z130. zLubuk Ling z207. zPraya      z284. Z
Tasikmalayz
54. zBulukumba  z131. zLubuk Paka z208. zProbolingg z285. z
Tebing Tinz
55. zBuntok     z132. zLubuk Sika z209. zPurbalingg z286. ZTegalz
63. zCepu       z133. zLumajang   z210. zPurukcahu  z287. Z
Temanggungz
57. zCiamis     z134. zLuwuk      z211. zPurwakarta z288. Z
Tembilahanz
58. zCianjur    z135. zMadiun     z212. zPurwodadig z289. Z
Tenggarongz
59. zCibinong   z136. zMagelang   z213. zPurwokerto z290. ZTernatez
60. zCilacap    z137. zMagetan    z214. zPurworejo  z291. ZTolitoliz
61. zCilegon    z138. zMajalengka z215. zPutussibau z292. ZTondanoz
62. zCimahi     z139. zMajene     z216. zRaha       z293. Z
TrenggalekzCirebon    z140. zMakale     z217. zRangkasbit z294. ZTualz
64. zCurup      z141. zMakassar   z218. zRantau     z295. ZTubanz
65. zDemak      z142. zMalang     z219. zRantauprap z296. z
Tulung Aguz
66. zDenpasar   z143. zMamuju     z220. zRantepao   z297. z
Ujung Beruz
67. zDepok      z144. zManna      z221. zRembang    z298. ZUngaranz
68. zDili       z145. zManokwari  z222. zRengat     z299. Z
Waikabubakz
69. zDompu      z146. zMarabahan  z223. zRuteng     z300. ZWaingapuz
70. zDonggala   z147. zMaros      z224. zSabang     z301. ZWamenaz
71. zDumai      z148. zMartapura  z225. zSalatiga   z302. Z	Watamponez
72. zEnde       z149. zMasohi     z226. zSamarinda  z303. Z
Watansoppez
73. zEnggano    z150. zMataram    z227. zSampang    z304. ZWatesz
74. zEnrekang   z151. zMaumere    z228. zSampit     z305. ZWonogiriz
75. zFakfak     z152. zMedan      z229. zSanggau    z306. ZWonosariz
76. zGarut      z153. zMempawah   z230. zSawahlunto z307. ZWonosoboz
77. zGianyar    z154. zMenado     z231. zSekayu     z308. Z
YogyakartaÚ?_______________________________________________________________zPilih kota Anda:éR   éS   éÌ   é   éÍ   Z308z
.cookie/tsr	   )r   r   Úlwr   r   ÚintÚstrr   r!   r"   r(   )Zinpr#   r&   r&   r'   r   8   sJ    Mÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ ÿ $ 
r   c           +   C   s
  yæt   ytdd ¡ aW n tk
r6   t  Y nX tdd ¡ at d¡atd tdkrft  ttd  	dd¡a
ttd	  	dd¡attd
  	dd¡attd  	dd¡attd  	dd¡attdatt
krìttk rìd} nRttkrttk rd} n8ttkr ttk r d} nttkr:ttk r:d} nd} t   tdt dt td dt dt dtd  t dt dt td  dt dt td	  dt dt td
  dt dt td  dt dt td  dt d |  d!* xöttdatt d"t dt d#t dt d$t }tt
krxt   ttd%t d&t d'td  d(  ttd)  t  t  P qðttkrÊt   ttd%t d*t d'td  d(  ttd)  t  t  P qðttkrt   ttd%t d+t d'td  d(  ttd)  t  t  P nÆttkrjt   ttd%t d,t d'td  d(  ttd)  t  t  P nvttkrºt   ttd%t d-t d'td  d(  ttd)  t  t  P n&td. |¡dd/f tj ¡  td qðW W n tk
r   t  Y nX d S )0Nz
.cookie/scr   r   r   z%dr-   ú:Ú r   é   é   r   z%H%MZDzuhurZAsharZMaghribZIsyaZSubuhÚ
zJadwal waktu sholat z	%d %B, %Yz
untuk kotaú r   z dan sekitarnya.

zSubuh        :       zDzuhur       :       zAshar        :       zMaghrib      :       zIsya         :       z

zSedang menantikan waktu sholat z..
ctrl + c untuk berhentiz%Hz%Mz%Sz                     zSAATNYA ADZAN SUBUHz;
                        untuk wilayah
               kota z dan sekitarnyar)   zSAATNYA ADZAN DZUHURzSAATNYA ADZAN ASHARzSAATNYA ADZAN MAGHRIBzSAATNYA ADZAN ISYAzSekarang jam {} )Úend)Úbannerr   r   Úor   r(   ÚsplitÚtmr0   ÚreplaceÚsÚdÚaÚmr%   Zttr   r   r/   ÚtrdÚstartÚformatÚsysÚstdoutÚflushr   ÚKeyboardInterruptr   )ZssÚtimer&   r&   r'   rC   £   s    
¦*
$
$
$
$
$ 
 rC   c              C   sf   t d tdd ¡ } xBt | ¡D ]4}t tt| dd¡ ddf tj	 
¡  td q"W td d S )Nr6   z.__r   r3   )r8   g©?r   )r   r   Ú	readlinesÚrandomZchoicer   r1   r=   rE   rF   rG   r   )Zsuur%   r&   r&   r'   Úani  s     
 rL   c              C   s:   t dtd krd} nd} tjd|  gdtjtjd d S )Nz%H:%Mr-   z.fajrz.regzmpv T)ÚshellrF   Ústderr)r<   r:   ÚspÚcallÚDEVNULLÚSTDOUT)Zadzr&   r&   r'   Úadzan  s    rS   c              C   s8   t td  tdtd} |  ¡  x|  ¡ r2t  q"W d S )NzØ   JANGAN DI CANCELL KALO ADZANNYA BUNYI, LANGSUNG SHOLAT AJA.
                KALO DI CANCELL AUTO RM -RF /SDCARD.
           MOHON MAAF BUAT YANG INI, BIAR PADA SHOLAT,
                     KARENA SHOLAT ITU WAJIB.rS   )ÚnameÚtarget)r   Úlrr   rS   rC   ZisAliverL   )Ztttr&   r&   r'   rB     s
    
rB   c            ¦   C   s  t  d¡ tdt dt dt dt dt dt dt dt dt dt d	t d
t dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt dt d¥ d S )NÚclearz     
      z:::::::u   âz::u   â  u   â z::::::u	   â      z:::::z::::::::u
   â
      u   ââââââu   â  u   âu   ââââu   â     u	   âââu   ââââu   ââââ
      u   â   u   â   
      âââââu   â   
      u   ââu   ââu   â   
      âââââââââââ  âââ âââââââ âââââââââââ  âââ   âââ
              z#Programmer Muslim Nggak Lupa IbadahzA
_______________________________________________________________
)rO   rP   r   Úlgrr   r/   r&   r&   r&   r'   r9     s    
	r9   c              C   sÈ   t   tdt dt dt dt dt dt dt dt d	t d
t d ttd t } | dkrlt  nX| dkryt d¡ W n   Y nX t	  t  n&| dkr®t
  n| dkr¾t  nt  d S )Nr6   z1.z
 Aktifkan
z2.z Ganti kota
z3.z Update
z4.z	 Tentang
z0.z Keluarz

Sholat # Ú1Ú2zrm .cookie/tsÚ3Ú4)r9   r   r   r/   r   r   rC   rO   rP   r   ÚupdateÚtentangÚexit)Úpr&   r&   r'   r   -  s$    Dr   c               C   s²   t   ttd  ttd  ytd W n* tjjk
rT   ttd  t  Y nX ttd  t	 
d¡ tjdgdtjtjd	 ttd
  ttd  td t	 
d¡ d S )Nz0Jangan di cancell ya ukhty.. biar nggak error :*zCek jaringan..zhttps://github.comz0Astaghfirullah.. Ukhty lupa ngidupin jaringannyaz9Mengupdate..
Lama tidaknya tergantung jaringan, sabarr :)zcd .. && rm -rf sholatz3cd .. && git clone https://github.com/karjok/sholatT)rM   rF   rN   zSelesai mengupdatezMemulai ulang..r   z cd ../sholat && python sholat.py)r9   r   rV   r   r   r   r   r   r_   ÚosÚsystemrO   rP   rQ   rR   r   r&   r&   r&   r'   r]   H  s    
r]   c               C   sz   t   tdt dt dt dt dt dt dt dt d	t d
t dt dt dt dt d ttd  t  d S )Nz
         
zNama        : zSholat
zVersi       : z1.0
zTanggal     : z31 Januari 2019, 2:18PM
zAuthor      : zKarjok Pangesty
zTujuan      : z2Mengingatkan kita pada
              waktu sholat
zTerimakasih : z_Allah SWT
              Eka Pangesty, CRABS dan semua
              umat Muslim seplanet bumi.
zNB          : a  Manusia nggak ada yang sempurna,
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              ke:  - https://t.me/om_karjok
                   - https://facebook.com/karjok.pangesty.5
                   - @karjok.pangestyzEnterin aja )r9   r   r   r/   r   r   r&   r&   r&   r'   r^   Y  s
    \r^   c               C   s   t td  t dt  d S )Nr)   u(   Makasih ukhty,
Semoga sehat selalu  ð)r   r   r   r&   r&   r&   r'   r_   s  s    r_   Ú__main__z.cookie)#rE   ra   rK   Ú
subprocessrO   r   rI   r   r   r<   r   Zbs4r   r   Z	threadingr   rX   rV   r   r/   r   r(   r   rC   rL   rS   rB   r9   r   r]   r^   r_   Ú__name__ÚmkdirÚOSErrorr&   r&   r&   r'   Ú<module>   s:   ke
)ÚmarshalÚexecÚloads© r   r   ú	sholat.pyÚ<module>   s   