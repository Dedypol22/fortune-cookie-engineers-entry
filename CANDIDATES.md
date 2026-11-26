# Kandidat baris — Fortune Cookie Funnies for Engineers

Dinilai terhadap judge brief kit (urutan kriteria: 1. fortune untuk engineer;
2. lucu saat pertama dibaca; 3. bunyi seperti fortune cookie; 4. segar; 5. rapat,
kata terlucu di akhir) + pola rank-1 dari `~/workspace/makefun/rank1-lessons.md`:
satu adegan konkret yang bisa dibayangkan; anekdot mikro + nada datar;
sudut segar mengalahkan poles baris lama; pemenang seri fortune bertema
identitas/penggantian; hindari klise mug (Friday deploy, "works on my machine",
angka keberuntungan — baris angka keberuntungan kita di fortune suroso hanya
mid-field).

| # | Baris (karakter) | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|
| 1 | Beware the pull request approved at 11:58 p.m. by a reviewer who only read the title. (89) | 5 | 4 | 5 | 4 | 4 | 22 |
| 2 | The deploy you call 'a tiny change' will be the one they write the postmortem about. (84) | 5 | 5 | 4 | 4 | 5 | **23** |
| 3 | A quiet week is coming. Your pager knows otherwise, and it is already charging. (78) | 5 | 4 | 5 | 5 | 4 | **23** |
| 4 | The bug you cannot reproduce will reproduce itself in front of your manager at 9 a.m. sharp. (94) | 5 | 4 | 4 | 3 | 4 | 20 |
| 5 | Your replacement has already started. It never sleeps, and it has already reviewed your code. (91) | 4 | 4 | 3 | 3 | 4 | 18 |
| 6 | The feature you ship on Friday will be opened exactly once, by the person who asked for it. (93) | 5 | 4 | 4 | 4 | 4 | 21 |
| 7 | Good fortune: the production bug is not yours. It belongs to the engineer who quit last month. (99) | 5 | 4 | 5 | 4 | 4 | 22 |
| 8 | You will find the bug at 2 a.m., in the file you skipped because its name looked boring. (86) | 5 | 4 | 5 | 5 | 4 | **23** |
| 9 | The intern will fix in one afternoon the bug you chased for a week, by deleting your code. (89) | 4 | 5 | 3 | 4 | 5 | 21 |
| 10 | You will write 'temporary fix' in the code today. In three years it will still be there, and it will be load-bearing. (112) | 5 | 5 | 4 | 4 | 5 | **23** |
| 11 | You will deploy on Friday at 4:59 p.m. It will work. No one will ever know why. (75) | 5 | 3 | 4 | 2 | 4 | 18 |
| 12 | A stranger will inherit your code next week. It is you, and you will not remember writing any of it. (102) | 5 | 4 | 4 | 3 | 3 | 19 |

Catatan penolakan:
- #5 terlalu dekat dengan mekanisme pemenang fortune suroso ("Your replacement
  arrives Tuesday") — risiko kesegaran.
- #10 memakai "temporary fix jadi permanen", lelucon dev yang paling sering
  diceritakan; "load-bearing" memang kata pemenang (cat review #1) tapi
  mekanismenya sudah dikenal.
- #11 Friday deploy = klise mug; #4 efek-demo = trope dikenal; #12 future-you
  = lelucon lama.

Tie-break 23 (empat baris): kriteria 2 juri — seberapa keras lelucon mendarat
di bacaan pertama dengan punchline nyata. #2 menang: "postmortem" adalah kata
tertawa yang duduk di akhir, tanpa bacaan kedua; #3 dan #8 mendarat sebagai
senyum (pager mengisi daya / nama file membosankan), #10 kalah di kriteria 4.
#2 juga menerapkan pola pemenang developer-excuses yang terbukti:
"[tindakan kecil] — [konsekuensi absurd yang terukur]" ("tiny change" →
postmortem).

## Pemenang

**"The deploy you call 'a tiny change' will be the one they write the postmortem about."**
— 84 karakter, satu baris, tanpa newline akhir.
