---
id: TC-FA-TDC-E2E-279-screening-field-declining-balance-rate-dan-end-of-life-treatment-di-create-dan-nilai-seed-di-edit
title: "Screening Field End-of-Life Treatment di Drawer Create (Wajib, Tiga Opsi, Tidak Dapat Dikosongkan, Reset) dan Nilai Declining Balance Rate serta End-of-Life Treatment Tiap Class Seed"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-935
  - TC-FA-TDC-943
  - TC-FA-TDC-952
sourceRules: ["FLD-19", "ST-10", "FATDC-LOGIC-03g.1", "FATDC-LOGIC-03g.5", "FI-03", "FATDC-LOGIC-03f.3", "FATDC-LOGIC-03f.4", "FATDC-LOGIC-03f.2", "§4.1.5"]
smoke: []
dependsOn: []
trace:
  "FLD-19": [7, 8, 9, 11]
  "ST-10": [7, 9, 25]
  "FATDC-LOGIC-03g.1": [11, 13, 15, 16, 17]
  "FATDC-LOGIC-03g.5": [3, 22, 25, 51, 55, 59]
  "FI-03": [21, 22, 24, 25]
  "FATDC-LOGIC-03f.3": [21, 22]
  "FATDC-LOGIC-03f.4": [24, 25]
  "FATDC-LOGIC-03f.2": [30, 35, 40, 45]
  "§4.1.5": [30, 32, 35, 37, 40, 42, 45, 47, 51, 55, 58, 59]
coverage:
  web: automated
---

# Screening Field End-of-Life Treatment di Drawer Create (Wajib, Tiga Opsi, Tidak Dapat Dikosongkan, Reset) dan Nilai Declining Balance Rate serta End-of-Life Treatment Tiap Class Seed

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Pre-setup (hanya dibaca, tidak diubah; Last Updated tidak berubah, S-06): tujuh class seed bawaan hasil aktivasi pertama modul akuntansi, belum diubah, dengan nilai seed berikut (Precondition c TC-FA-TDC-952).

| Class Code | Declining Balance Rate | End-of-Life Treatment |
|---|---|---|
| `NB-1` | 50 | Charge in final period |
| `NB-2` | 25 | Charge in final period |
| `NB-3` | 12.5 | Charge in final period |
| `NB-4` | 10 | Charge in final period |
| `BLD-P` | tidak tampil | tidak tampil |
| `BLD-NP` | tidak tampil | tidak tampil |
| `LAND` | Disabled tanpa nilai | tidak tampil |

- Master Data Count Limit belum tercapai (Precondition c TC-FA-TDC-935 dan TC-FA-TDC-943); kemampuan mengatur kuota disediakan tim FE/BE.
- Tabel memuat tujuh class seed bawaan (7 baris dalam satu halaman) sehingga baris target dibuka tanpa Search (8b.13, R-23). Spec tidak membuat data dan tidak mengubah state global.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-935: Create: End-of-Life Treatment berlabel wajib, tiga opsi, bernilai awal, dan tidak dapat dikosongkan

1. Klik `+ Class` di toolbar
2. Verifikasi Drawer Add Tax Depreciation Class tampil dengan field Allowed Methods
3. Verifikasi field End-of-Life Treatment tidak tampil
4. Pilih Asset Type `Non-building`
5. Isi Useful Life `8`
6. Pilih Allowed Methods `Declining Balance`
7. Verifikasi End-of-Life Treatment * — Select single tampil di bawah Declining Balance Rate (%)
8. Verifikasi label End-of-Life Treatment berpenanda wajib (`*`)
9. Verifikasi nilai awal End-of-Life Treatment adalah "Charge in final period"
10. Buka dropdown End-of-Life Treatment
11. Verifikasi dropdown memuat tepat tiga opsi: "Charge in final period", "Switch to straight-line", "Keep depreciating"
12. Klik opsi "Charge in final period" yang sedang terpilih
13. Verifikasi klik opsi yang sedang terpilih tidak menghapus pilihan
14. Fokuskan Select End-of-Life Treatment, tekan `Backspace`, lalu tekan `Delete`
15. Verifikasi `Backspace` dan `Delete` tidak mengosongkan Select
16. Verifikasi tidak ada ikon atau opsi clear pada Select End-of-Life Treatment
17. Verifikasi nilai End-of-Life Treatment tetap "Charge in final period"

### TC-FA-TDC-943: Create: Declining Balance dilepas lalu dipilih lagi mengosongkan Declining Balance Rate dan mengembalikan End-of-Life Treatment ke nilai awal

18. Isi Declining Balance Rate `25`
19. Pilih End-of-Life Treatment `Keep depreciating`
20. Lepas `Declining Balance` dan pilih `Straight Line`
21. Verifikasi Straight Line Rate (%) "12.5" tampil
22. Verifikasi input Declining Balance Rate dan Select End-of-Life Treatment tidak tampil
23. Pilih kembali `Declining Balance`
24. Verifikasi Declining Balance Rate (%) tampil kosong
25. Verifikasi End-of-Life Treatment kembali "Charge in final period" (bukan `Keep depreciating`)
26. Klik `[×]` pada Drawer Create
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`

### TC-FA-TDC-952: Seed: Declining Balance Rate dan End-of-Life Treatment tiap class seed

29. Klik link Class Code `NB-1` pada tabel
30. Verifikasi Declining Balance Rate "50"
31. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
32. Verifikasi End-of-Life Treatment "Charge in final period"
33. Klik `[×]` pada Drawer Edit
34. Klik link Class Code `NB-2` pada tabel
35. Verifikasi Declining Balance Rate "25"
36. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
37. Verifikasi End-of-Life Treatment "Charge in final period"
38. Klik `[×]` pada Drawer Edit
39. Klik link Class Code `NB-3` pada tabel
40. Verifikasi Declining Balance Rate "12.5"
41. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
42. Verifikasi End-of-Life Treatment "Charge in final period"
43. Klik `[×]` pada Drawer Edit
44. Klik link Class Code `NB-4` pada tabel
45. Verifikasi Declining Balance Rate "10"
46. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
47. Verifikasi End-of-Life Treatment "Charge in final period"
48. Klik `[×]` pada Drawer Edit
49. Klik link Class Code `BLD-P` pada tabel
50. Verifikasi field Class Name tampil pada Drawer Edit
51. Verifikasi Declining Balance Rate dan End-of-Life Treatment tidak tampil
52. Klik `[×]` pada Drawer Edit
53. Klik link Class Code `BLD-NP` pada tabel
54. Verifikasi field Class Name tampil pada Drawer Edit
55. Verifikasi Declining Balance Rate dan End-of-Life Treatment tidak tampil
56. Klik `[×]` pada Drawer Edit
57. Klik link Class Code `LAND` pada tabel
58. Verifikasi Declining Balance Rate Disabled tanpa nilai
59. Verifikasi End-of-Life Treatment tidak tampil
60. Klik `[×]` pada Drawer Edit

## Notes

- Alasan melewati sekitar 35 langkah (60 langkah): ketiga TC satu topik layar (field Declining Balance Rate dan End-of-Life Treatment), semuanya tanpa membuat atau mengubah data, dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna). Blok TC-FA-TDC-952 berulang per class seed (langkah 29 sampai 60) karena nilai tiap class berbeda.
- Urutan dan form: screening di awal (prinsip 2). TC-FA-TDC-943 melanjutkan form Create TC-FA-TDC-935 (prinsip 3.6: kasus yang menguji pengosongan atau revert boleh melanjutkan form yang sama): langkah 1 dan 2 TC-FA-TDC-943 (membuka Drawer, memilih Non-building, Useful Life 8, dan `Declining Balance`) dipenuhi oleh keadaan form akhir TC-FA-TDC-935 dan tidak diulang, karena memilih lagi `Declining Balance` akan melepasnya. Form ditutup di langkah 26 sampai 28 (S-08).
- Langkah penghubung (S-03): langkah 12 (mengklik opsi terpilih, bagian langkah TC-FA-TDC-935), langkah 26 sampai 28 (menutup form dirty), langkah 33, 38, 43, 48, 52, 56, 60 (menutup Drawer Edit tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 adalah anchor positif untuk asersi absence langkah 3 ("End-of-Life Treatment tidak tampil", 8b.2); langkah 21 adalah anchor untuk langkah 22 (Expected a TC-FA-TDC-943 menyebut keduanya); langkah 50, 54, dan 58 adalah anchor untuk asersi absence langkah 51, 55, dan 59 pada Drawer Edit (field lain pada surface yang sama tampil, 8b.2).
- Langkah 14 menggabungkan `Backspace` dan `Delete` sesuai langkah 7 TC-FA-TDC-935; langkah 15 sampai 17 memecah Expected d (klik opsi, `Backspace` dan `Delete`, ikon clear, nilai tetap) per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-TDC-935 langkah 2 dan 4 serta Expected a hanya menyebut End-of-Life Treatment; spec menambah `Verifikasi` Drawer tampil (anchor, langkah 2).
  - TC-FA-TDC-935 tidak menyebut apakah dropdown tertutup setelah langkah 12; spec melanjutkan ke langkah 14 tanpa langkah penutup dropdown. Perlu konfirmasi FE.
  - TC-FA-TDC-943 mensyaratkan form baru (langkah 1 dan 2) tetapi spec melanjutkan form TC-FA-TDC-935 (lihat Notes di atas).
  - TC-FA-TDC-943 Expected a menyebut "input Declining Balance Rate dan Select End-of-Life Treatment tidak tampil" tanpa menyebut cara menyatakan helper bawaan; spec hanya mengasersi dua elemen itu.
  - TC-FA-TDC-952 menulis nilai seed `NB-1` sampai `NB-4` sebagai angka tanpa satuan ("50", "25", "12.5", "10"); spec memakainya persis, sedangkan tabel menampilkan satuan `%` (TC-FA-TDC-937).
  - TC-FA-TDC-952 tidak menyebut kondisi Drawer Edit `LAND` selain Declining Balance Rate "Disabled tanpa nilai"; spec tidak mengasersi field lain.
  - TC-FA-TDC-935 dan TC-FA-TDC-943 Post Condition "Tidak ada data berubah" tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
