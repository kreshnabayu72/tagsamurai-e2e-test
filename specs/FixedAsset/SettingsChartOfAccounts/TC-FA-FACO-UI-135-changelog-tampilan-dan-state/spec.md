---
id: TC-FA-FACO-UI-135-changelog-tampilan-dan-state
title: "Modal Changelog: kolom, format sel, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["ST-20", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "EB-TBL-1@tabel-changelog", "EB-TBL-2@kolom-old-value", "EB-TBL-2@kolom-new-value", "EB-TBL-4@kolom-modified-by-changelog", "EB-TBL-8@tabel-changelog", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "ST-20": [50, 51, 55, 56]
  "§4.1.1#r21": [4, 11, 27, 28, 29]
  "§4.1.1#r22": [5, 11, 14, 18, 22]
  "§4.1.1#r23": [6, 11, 15]
  "§4.1.1#r24": [7, 11, 21]
  "§4.1.1#r25": [8, 11, 16, 19, 21, 23]
  "§4.1.1#r26": [9, 11, 17, 20, 21, 24]
  "§4.1.1#r27": [10, 11, 35, 37, 38, 40, 41, 43]
  "EB-TBL-1@tabel-changelog": [50, 51, 55, 56, 59, 60, 61]
  "EB-TBL-2@kolom-old-value": 16
  "EB-TBL-2@kolom-new-value": 24
  "EB-TBL-4@kolom-modified-by-changelog": [35, 37, 38, 40, 41, 43]
  "EB-TBL-8@tabel-changelog": [46, 47]
  "EB-XM-1": [27, 28, 29, 32]
anchor: [3]
coverage:
  web: automated
---

# Modal Changelog: kolom, format sel, dan state data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Changelog
- Data:
  - DU-135-1: entri Create, Date `2026-03-25T09:15:00Z`, Account Code `1-1001`, Field `Account Code`, Old Value kosong, New Value `1-1001`, Modified By `Rina Pratiwi`. Date tampil `25/03/26, 09:15`, dari `2026-03-25T09:15:00Z`. Modified By tampil `Rina P`, dari `Rina Pratiwi`. Pada Date Format `dd MMM yy`, Date tampil `25 Mar 26, 09:15`.
  - DU-135-2: entri Edit, Date `2026-03-26T10:30:00Z`, Account Code `1-1001`, Field `Account Name`, Old Value `Fixed Asset Equipment`, New Value `Fixed Assets – Equipment`, Modified By `Rina Pratiwi`. Date tampil `26/03/26, 10:30`, dari `2026-03-26T10:30:00Z`.
  - DU-135-3: entri Edit, Date `2026-03-27T23:30:00Z`, Account Code `1-1001`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Budi`. Date tampil `27/03/26, 23:30`, dari `2026-03-27T23:30:00Z`. Modified By tampil `Budi`, dari `Budi`.
  - DU-135-4: entri Delete, Date `2026-03-28T08:05:00Z`, Account Code `4-7001`, Field `Account Code`, Old Value `4-7001`, New Value kosong, Modified By `Alexander Graham Bell`. Modified By tampil `Alexander G`, dari `Alexander Graham Bell`.
  - DU-135-5: entri Edit, Date `2026-03-29T07:45:00Z`, Account Code `9-0001`, Field `Account Name`, Old Value `<b>Kas</b>`, New Value `<b>Kas Besar</b>`, Modified By `Rina Pratiwi`.
  - DU-135-6: daftar entri Changelog kosong, jumlah entri `0`.
  - DU-135-7: kata kunci Search `Zxqv Tidak Ada`, tidak cocok dengan entri mana pun.
- Kondisi:
  - K1: modal Changelog berisi DU-135-1 sampai DU-135-5; Date Format bernilai `dd/MM/yy`, Time Format bernilai `24h`, dan Time Zone bernilai `UTC`.
  - K2: seperti K1, dengan Date Format bernilai `dd MMM yy`.
  - K3: daftar entri kosong menurut DU-135-6.
  - K4: modal Changelog berisi DU-135-1; kata kunci Search `Zxqv Tidak Ada` menghasilkan daftar kosong.
  - K5: memuat entri Changelog gagal karena error server.

## Test Steps

### Kolom default modal Changelog
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik ikon Changelog
3. Verifikasi modal `Changelog: Chart of Accounts` tampil
4. Verifikasi header kolom `Date` tampil
5. Verifikasi header kolom `Action` tampil
6. Verifikasi header kolom `Account Code` tampil
7. Verifikasi header kolom `Field` tampil
8. Verifikasi header kolom `Old Value` tampil
9. Verifikasi header kolom `New Value` tampil
10. Verifikasi header kolom `Modified By` tampil
11. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Date`, `Action`, `Account Code`, `Field`, `Old Value`, `New Value`, `Modified By`

### Isi sel entri Create, Edit, dan Delete
12. Tampilkan Tab Chart of Accounts dengan kondisi K1
13. Klik ikon Changelog
14. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Action `Create`
15. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Account Code `1-1001`
16. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Old Value `—`
17. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan New Value `1-1001`
18. Verifikasi entri `1-1001` dengan Field `Account Name` menampilkan Action `Edit`
19. Verifikasi entri `1-1001` dengan Field `Account Name` menampilkan Old Value `Fixed Asset Equipment`
20. Verifikasi entri `1-1001` dengan Field `Account Name` menampilkan New Value `Fixed Assets – Equipment`
21. Verifikasi entri `1-1001` dengan Field `Status` menampilkan Old Value `Active` dan New Value `Inactive`
22. Verifikasi entri `4-7001` menampilkan Action `Delete`
23. Verifikasi entri `4-7001` menampilkan Old Value `4-7001`
24. Verifikasi entri `4-7001` menampilkan New Value `—`

### Format Date mengikuti General Settings
25. Tampilkan Tab Chart of Accounts dengan kondisi K1
26. Klik ikon Changelog
27. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Date `25/03/26, 09:15`, dari `2026-03-25T09:15:00Z`
28. Verifikasi entri `1-1001` dengan Field `Account Name` menampilkan Date `26/03/26, 10:30`, dari `2026-03-26T10:30:00Z`
29. Verifikasi entri `1-1001` dengan Field `Status` menampilkan Date `27/03/26, 23:30`, dari `2026-03-27T23:30:00Z`

### Format Date mengikuti Date Format yang diubah
30. Tampilkan Tab Chart of Accounts dengan kondisi K2
31. Klik ikon Changelog
32. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Date `25 Mar 26, 09:15`, dari `2026-03-25T09:15:00Z`

### Modified By singkat dan nama lengkap saat hover
33. Tampilkan Tab Chart of Accounts dengan kondisi K1
34. Klik ikon Changelog
35. Verifikasi entri `1-1001` dengan Field `Account Code` menampilkan Modified By `Rina P`, dari `Rina Pratiwi`
36. Arahkan kursor ke sel Modified By entri `1-1001` dengan Field `Account Code`
37. Verifikasi nama lengkap `Rina Pratiwi` tersampaikan pada sel Modified By entri `1-1001` dengan Field `Account Code`
38. Verifikasi entri `1-1001` dengan Field `Status` menampilkan Modified By `Budi`, dari `Budi`
39. Arahkan kursor ke sel Modified By entri `1-1001` dengan Field `Status`
40. Verifikasi nama lengkap `Budi` tersampaikan pada sel Modified By entri `1-1001` dengan Field `Status`
41. Verifikasi entri `4-7001` menampilkan Modified By `Alexander G`, dari `Alexander Graham Bell`
42. Arahkan kursor ke sel Modified By entri `4-7001`
43. Verifikasi nama lengkap `Alexander Graham Bell` tersampaikan pada sel Modified By entri `4-7001`

### Markup tampil apa adanya
44. Tampilkan Tab Chart of Accounts dengan kondisi K1
45. Klik ikon Changelog
46. Verifikasi entri `9-0001` menampilkan Old Value `<b>Kas</b>` apa adanya sebagai teks
47. Verifikasi entri `9-0001` menampilkan New Value `<b>Kas Besar</b>` apa adanya sebagai teks

### Changelog belum berisi entri
48. Tampilkan Tab Chart of Accounts dengan kondisi K3
49. Klik ikon Changelog
50. Verifikasi judul `No changelog yet` tampil
51. Verifikasi deskripsi `Activities and changes will appear here.` tampil

### Changelog kosong karena Search
52. Tampilkan Tab Chart of Accounts dengan kondisi K4
53. Klik ikon Changelog
54. Ketik Search `Zxqv Tidak Ada`, tekan Enter
55. Verifikasi judul `No results found` tampil
56. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Gagal memuat Changelog
57. Tampilkan Tab Chart of Accounts dengan kondisi K5
58. Klik ikon Changelog
59. Verifikasi pesan `Unable to load this data.` tampil
60. Verifikasi tombol `[Try Again]` tampil
61. Verifikasi judul `No changelog yet` tidak tampil
