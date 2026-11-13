---
id: TC-FA-FAREG-UI-002-draft-tampilan-kolom-toolbar
title: "Sub tab Draft: kolom, format sel, nilai kosong, dan toolbar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r2", "§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§4.1#p8", "§5#r1", "EB-TBL-2@kolom-origin", "EB-TBL-4@kolom-requested-by", "EB-TBL-8@tabel-draft", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "§4.1#r2": 2
  "§4.1#r22": [4, 6, 7]
  "§4.1#r23": [9, 10]
  "§4.1#r24": [11, 12]
  "§4.1#r25": [13, 14, 15]
  "§4.1#r26": [17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34]
  "§4.1#r27": [36, 37, 39, 40, 60, 61, 63, 64, 66]
  "§4.1#p8": [45, 46, 47, 49, 50, 51, 53, 54, 55, 56, 58]
  "§5#r1": [45, 46, 47, 50, 51]
  EB-TBL-2@kolom-origin: 10
  EB-TBL-4@kolom-requested-by: [17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34]
  EB-TBL-8@tabel-draft: 42
  EB-XM-1: [36, 37, 39, 40, 60, 61, 63, 64, 66]
coverage:
  web: automated
---

# Sub tab Draft: kolom, format sel, nilai kosong, dan toolbar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-002-1: batch Draft Group `Gudang 1` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`), Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Budi`, Last Updated `2026-03-25T09:15:00Z`.
  - DU-002-2: batch Draft Group `Gudang 2` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 2`), Origin `REG-20261105-00007`, Total Asset `5`, Progress `60%`, Requested By `Siti Nurbaya`, Last Updated `2026-03-24T23:30:00Z`.
  - DU-002-3: batch Draft Group `Kantor Pusat` (path penuh `PT Sejahtera Abadi > Kantor Pusat`), Origin `—`, Total Asset `30`, Progress `100%`, Requested By `Alexander Graham Bell`, Last Updated `2026-03-23T09:05:00Z`.
  - DU-002-4: batch Draft yang Group-nya belum dipilih, Origin `—`, Total Asset `0`, Progress `0%`, Requested By `Buzzlightyear Sumardi`, Last Updated `2026-03-22T13:10:00Z`.
  - DU-002-5: batch Draft Group `Gudang 4` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 4`), Origin `—`, Total Asset `8`, Progress `25%`, Requested By `Dewi Anggraini`, Last Updated `2026-03-21T10:00:00Z`.
  - DU-002-6: batch Draft Group `Gudang 5` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 5`), Origin `—`, Total Asset `6`, Progress `50%`, Requested By `Dewi Anggreni`, Last Updated `2026-03-20T11:30:00Z`.
  - DU-002-7: batch Draft Group `<b>Gudang 3</b>` (path penuh `PT Sejahtera Abadi > Cabang A > <b>Gudang 3</b>`), Origin `—`, Total Asset `4`, Progress `75%`, Requested By `Hadi Kusuma`, Last Updated `2026-03-19T14:45:00Z`.
  - Requested By yang diharapkan: `Budi` dari `Budi`; `Siti N` dari `Siti Nurbaya`; `Alexander G` dari `Alexander Graham Bell`; `Buzzlightyear S` dari `Buzzlightyear Sumardi`; `Dewi A` dari `Dewi Anggraini`; `Dewi A` dari `Dewi Anggreni`. Nama tanpa last name (`Budi`) tidak memuat inisial.
  - Last Updated yang diharapkan dengan Date Format `dd/MM/yy`: `25/03/26, 09:15` dari `2026-03-25T09:15:00Z`; `24/03/26, 23:30` dari `2026-03-24T23:30:00Z`.
  - Last Updated yang diharapkan dengan Date Format `M/d/yy`: `3/25/26, 09:15` dari `2026-03-25T09:15:00Z`; `3/24/26, 23:30` dari `2026-03-24T23:30:00Z`.
  - Last Updated yang diharapkan dengan Date Format `dd/MM/yy`, Time Format `12h`, dan Time Zone UTC: `25/03/26, 09:15 AM` dari `2026-03-25T09:15:00Z`; `24/03/26, 11:30 PM` dari `2026-03-24T23:30:00Z`.
  - Last Updated yang diharapkan dengan Date Format `dd/MM/yy`, Time Format `24h`, dan Time Zone Asia/Jakarta (UTC+7): `25/03/26, 16:15` dari `2026-03-25T09:15:00Z`; `25/03/26, 06:30` dari `2026-03-24T23:30:00Z`.
- Kondisi:
  - K1: tabel berisi DU-002-1 sampai DU-002-7; Date Format General Settings `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - K2: sama dengan K1 kecuali Date Format General Settings `M/d/yy`.
  - K3: sama dengan K1 kecuali Time Format General Settings `12h`.
  - K4: sama dengan K1 kecuali Time Zone General Settings `Asia/Jakarta`.

## Test Steps

### Tabel Draft memuat kolom batch registrasi
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Verifikasi header kolom `Group`, `Origin`, `Total Asset`, `Progress`, `Requested By`, dan `Last Updated` tampil

### Group: badge, path penuh saat hover, dan nilai kosong
3. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
4. Verifikasi sel Group pada baris `Gudang 1` menampilkan badge `Gudang 1`
5. Arahkan kursor ke badge Group `Gudang 1`
6. Verifikasi tooltip menampilkan path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`
7. Verifikasi sel Group pada baris batch tanpa Group (DU-002-4) menampilkan `No group yet`

### Origin, Total Asset, dan Progress
8. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
9. Verifikasi sel Origin pada baris `Gudang 2` menampilkan `REG-20261105-00007`
10. Verifikasi sel Origin pada baris `Gudang 1` menampilkan `—`
11. Verifikasi sel Total Asset pada baris `Gudang 1` menampilkan `12`
12. Verifikasi sel Total Asset pada baris batch tanpa Group (DU-002-4) menampilkan `0`
13. Verifikasi sel Progress pada baris `Gudang 2` menampilkan `60%` dengan `severity="primary"`
14. Verifikasi sel Progress pada baris `Kantor Pusat` menampilkan `100%` dengan `severity="success"`
15. Verifikasi sel Progress pada baris `Gudang 1` menampilkan `0%`

### Requested By tampil sebagai nama singkat dan nama lengkap saat hover
16. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
17. Verifikasi sel Requested By pada baris `Gudang 1` menampilkan `Budi`
18. Arahkan kursor ke sel Requested By pada baris `Gudang 1`
19. Verifikasi tooltip menampilkan nama lengkap `Budi`
20. Verifikasi sel Requested By pada baris `Gudang 2` menampilkan `Siti N`
21. Arahkan kursor ke sel Requested By pada baris `Gudang 2`
22. Verifikasi tooltip menampilkan nama lengkap `Siti Nurbaya`
23. Verifikasi sel Requested By pada baris `Kantor Pusat` menampilkan `Alexander G`
24. Arahkan kursor ke sel Requested By pada baris `Kantor Pusat`
25. Verifikasi tooltip menampilkan nama lengkap `Alexander Graham Bell`
26. Verifikasi sel Requested By pada baris batch tanpa Group (DU-002-4) menampilkan `Buzzlightyear S`
27. Arahkan kursor ke sel Requested By pada baris batch tanpa Group (DU-002-4)
28. Verifikasi tooltip menampilkan nama lengkap `Buzzlightyear Sumardi`
29. Verifikasi sel Requested By pada baris `Gudang 4` menampilkan `Dewi A`
30. Arahkan kursor ke sel Requested By pada baris `Gudang 4`
31. Verifikasi tooltip menampilkan nama lengkap `Dewi Anggraini`
32. Verifikasi sel Requested By pada baris `Gudang 5` menampilkan `Dewi A`
33. Arahkan kursor ke sel Requested By pada baris `Gudang 5`
34. Verifikasi tooltip menampilkan nama lengkap `Dewi Anggreni`

### Last Updated mengikuti Date Format dan Time Format General Settings
35. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
36. Verifikasi sel Last Updated pada baris `Gudang 1` menampilkan `25/03/26, 09:15`
37. Verifikasi sel Last Updated pada baris `Gudang 2` menampilkan `24/03/26, 23:30`

### Last Updated mengikuti Date Format yang diganti
38. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
39. Verifikasi sel Last Updated pada baris `Gudang 1` menampilkan `3/25/26, 09:15`
40. Verifikasi sel Last Updated pada baris `Gudang 2` menampilkan `3/24/26, 23:30`

### Teks yang memuat markup tampil apa adanya
41. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
42. Verifikasi sel Group pada baris DU-002-7 menampilkan teks `<b>Gudang 3</b>` apa adanya

### Toolbar sub tab Draft
43. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
44. Klik ikon Search pada toolbar
45. Verifikasi placeholder kotak Search adalah `Search group, origin...`
46. Verifikasi toolbar memuat `Filter`
47. Verifikasi toolbar memuat `Download`
48. Klik `Download`
49. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
50. Verifikasi toolbar memuat `[+ Register Asset]`
51. Verifikasi toolbar tidak memuat tombol `Changelog`

### Aksi baris memakai ikon dan Bulk Action Delete
52. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
53. Verifikasi baris `Gudang 1` menampilkan aksi `Edit` dengan ikon `Edit2Line`
54. Verifikasi baris `Gudang 1` menampilkan aksi `Registration Log` dengan ikon `Note`
55. Verifikasi baris `Gudang 1` menampilkan aksi `Delete` dengan ikon `DeleteBin6Line`
56. Verifikasi baris `Gudang 1` tidak menampilkan aksi `Submit`
57. Centang baris `Gudang 1`
58. Verifikasi Bulk Action `Delete` tampil dengan ikon `DeleteBin6Line`

### Last Updated mengikuti Time Format 12 jam
59. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
60. Verifikasi sel Last Updated pada baris `Gudang 1` menampilkan `25/03/26, 09:15 AM`
61. Verifikasi sel Last Updated pada baris `Gudang 2` menampilkan `24/03/26, 11:30 PM`

### Last Updated mengikuti Time Zone General Settings
62. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K4
63. Verifikasi sel Last Updated pada baris `Gudang 1` menampilkan `25/03/26, 16:15`
64. Verifikasi sel Last Updated pada baris `Gudang 2` menampilkan `25/03/26, 06:30`

### Kolom Actions tepat sesudah Last Updated
65. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
66. Verifikasi header kolom `Actions` tampil tepat sesudah header kolom `Last Updated`
