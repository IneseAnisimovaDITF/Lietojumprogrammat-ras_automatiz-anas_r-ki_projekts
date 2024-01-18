# Noslēguma projekts - jauniegūtās prasmju pielietojums ikdienas uzdevumu veikšanā.
&nbsp;_Darba tēma :_ Noslēguma projekts - jauniegūtās prasmju pielietojums ikdienas uzdevumu veikšanā.

&nbsp;_Priekšmetā :_ Lietojumprogrammatūras automatizēšanas rīki.

&nbsp;_Darba autors :_ Inese Aņisimova. 231RDB004. Grupa  Nr. 11.

&nbsp;_Darba mērķis :_ Pielietot jauniegūtās prasmes un izstrādāt programmu, kas atvieglo ikdienas uzdevumus.

&nbsp;_Darba uzdevumi :_ 
1. analizēt ikdienas dzīves laikietilpīgus procesus, kurus var automatizēt ar Python valodu un jauniegūtajām prasmēm;
1. izstrādāt README.md datni kurā detalizēti jāapraksta projektu;
1. analizēt Python bibliotēkas, kuras tiks izmantotas projekta izstrādes laikā, aprakstīt tās;
1. izstrādāt Python valodā programmu izmantojot GitHub;
1. ierakstīt video, kurā tiks attēlots programmatūras darbība un rezultāts.

## Detalizēts apraksts par projektu.
&nbsp;&nbsp;&nbsp;&nbsp; Analizējot ikdienas dzīves laikietilpīgus procesus, esmu pamanījusi, ka vairākas reizes dienā ir nepieciešams ieiet Ortus sistēmā un pārbaudīt infopaneli, kur tiek attēlots kādi uzdevumi uzdoti un kad to ir jānodot, kā arī tur attēlojas eksāmeni izpildes lapas, gadijumā ja eksāmenu raksta caur Ortus sistēmu.

&nbsp;&nbsp;&nbsp;&nbsp; Lai automatizētu šo laikietilpīgu procesu tika pieņemts lēmums iztrādāt programmu, kas izvadīs datus no Ortus sistēmas un nosūtīs to E-pastā, lai ērtāk būtu analizēt dienas uzdevumus un plānot ikdienu. E-pasta tiks atsutīts kad, cikos un kurā priekšmetā jāizpilda darbu. Man paliks ātri apskatīt E-pastu un izplānot rītdienu.

&nbsp;_Projekta izstrādes laikā izmantotās bibliotēkas :_ 

* Selenium - ir atvērta pirmskoda rīku komplekts, kas ļauj automatomatizēt jebkuras tīmekļa pārlūkprogrammas darbību savā projektā. Izstrādātā projektā tika pieslēgta Selenium bibliotēka, lai strādātu ar chrome pārlūkprogrammu
* Time - Tā ir iebuvēta jeb standarta Python bibliotēka, kas tiek izmantota, nodrošinot automatizāciju, jo ir nepieciešams iepauzēt programmas izpildi, lai programma nenolasa saturu no neielādētās mājaslapas, tāpēc ka griežoties pie mājaslapām saturs netiek uzreiz ielādēts un ir nepieciešams laiks, lai mājaslapa ielādētu savu saturu.Noslēguma projektā tā tika izmantota, lai ievietotu pauzes time.sleep() (iekavās var ievietot skaitli piemēram 3, kas paradīs uz cik sekundēm programma iepauzēs)
* Smtplib - 

&nbsp;_Darbības process :_ 
2. No sākuma tika importētas nepieciešamās bibliotēkas;
2. Izveidojam webdriver Chrome objektu izmantojot Selenium bibliotēku;
2. Atveram tīmekļa vietni un ar funkciju time.sleep(2) uzgaidam divas sekundes kamēr ielādēsies mājaslapa;
2. Vēlāk mēs mājaslapas kodā meklējam nepieciešamo kodu CLASS,CLASS_NAME,NAME,ID un ja neatrodam klases, vārdus un id tad izmantojam XPATH metodi. Tādā veidā mēs nospiežam mums nepieciešamos objektus, ievadam paroli, lietotājvārdu un izvadam nepieciešamo informāciju no mājaslapas;
2. Kad nepiecišamā informācija tika atrasta, informāciju izvadam un pierakstam izveidota teksta datne, no kuras vēlāk tiks nosūtīts E-pasts.
2. E-pasta parametru rakstīšana, kur mēs ievadam paroli, E-pastu, serveri, portu kuru izmantojam, ielogojamies E-pastā;
2. Tika izveidots rindu skaitītājs ar kura palīdzību programma izvada tikai nepieciešamo informāciju;
2. Formatējam E-pastu un nosūtam to;
2. Aizstaisam ciet E-pastu;
2. Programma pabeidz savu darbību.
## 
Kad projekts tika izstrādāts, pienācis laiks parādit, kas tad sanāca!

_*Pārnesot failu no Visual Studio Code radās problēmas ka tas never vaļā chrome tīmekļa vietni, tāpec video tiek parādits, kā darbojas programma no Visual Studio Code*_

## 
&nbsp;_Projekta izstrādes laikā izmantotie resursi :_ 
* YouTube, The Digital Skill Hub, 5 lekcijas ieraksts. Selenium izmantošana pārlūkprogrammas vadībai Python valodā [https://www.youtube.com/watch?v=t0PBBPuPgaw].

* Pieraksti, kas tika veidoti 7. lekcijas laikā - E-pasta apstrāde izmantojot Python.

* Selenium bibliotēkas aprakstam tika izmantota tīmekļa vietne : [https://www.selenium.dev/documentation/].

* Time bibliotēkas aprakstam tika izmantota tīmekļa vietne : [https://docs.python.org/3/library/time.html].

* Smptlib bibliotēkas aprakstam tika izmantota tīmekļa vietne : [].

* Markdown sintakses pielitošanai tika izmantotas timekļa vietne : [https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls][https://www.markdownguide.org/hacks/#indent-tab].

* E-pasta sagatavošanai, lai izmantotu Python programmas izstrāde, tika izmantota tīmekļa vietne : [https://www.sitepoint.com/quick-tip-sending-email-via-gmail-with-python/].

* Izmantojot XPATH, lai izprastu kā to lietot, tika izmantota tīmekļa vietne [https://habr.com/ru/articles/250975/].

* Izmantojot Utf-8, lai iedarbinātu projektu (,jo bez Utf-8, programma nedarbojās), tika izmantota tīmekļa vietne [https://blog.hubspot.com/website/what-is-utf-8].

###
_*Projekts netika izstrādāts vienas dienas laikā, projekta izstrādes izmaiņas daļēji tika uzglabātas GitHub krātuvē, kas ļautu izsekot projekta izstrādes gaitu, jo sākumā projekts tika izstrādāts Visual Studio Code un tad ar nelielām izmaiņām tika pievienots GitHub krātuvē*_

_*Gmail konts tika izveidots mācibu projektam, tāpēc parole un pats gmail konts tika atstāts projektā*_

_*Parole no Ortus sistēmas netiek uzglabāta šajā projekta, jo tā ir sensitīvie dati*_