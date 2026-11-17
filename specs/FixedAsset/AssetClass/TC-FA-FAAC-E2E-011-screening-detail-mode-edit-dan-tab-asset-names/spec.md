---
id: TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names
title: "Screening Halaman Detail Mode Edit: Badge Status dan Tab Asset Names (Berisi, Search Kosong, dan Genuinely Empty)"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-18
  - TC-FA-FAAC-19
  - TC-FA-FAAC-21
  - TC-FA-FAAC-23
  - TC-FA-FAAC-22
sourceRules: ["§4.2b#p1", "ST-01", "§4.2b#p2", "§9.5#r10", "§4.1.2#r4", "§4.1.2#r5", "§4.1.2#p1", "§4.1.2#p11", "FAAC-LOGIC-07j", "§4.1.3#p1", "§5#b1", "§4.1.3#r1", "§4.1.3#r2", "§4.1.3#r3", "§4.1.3#r4", "§4.1.3#r5", "§4.1.3#r6", "§9.5#r2", "§4.1.3#r9", "§4.1.3#p5", "§4.1.3#r7", "§4.1.3#r8", "ST-24"]
smoke: []
dependsOn: []
trace:
  "§4.2b#p1": [3, 4, 5, 7, 17]
  "ST-01": [6, 16]
  "§4.2b#p2": 8
  "§9.5#r10": 8
  "§4.1.2#r4": 9
  "§4.1.2#r5": 9
  "§4.1.2#p1": 10
  "§4.1.2#p11": [10, 11]
  "FAAC-LOGIC-07j": 12
  "§4.1.3#p1": [22, 23, 41, 47]
  "§5#b1": [22, 47]
  "§4.1.3#r1": [24, 25, 26]
  "§4.1.3#r2": [24, 27, 29]
  "§4.1.3#r3": [24, 30]
  "§4.1.3#r4": [24, 31]
  "§4.1.3#r5": [24, 32]
  "§4.1.3#r6": [24, 33, 35]
  "§9.5#r2": 25
  "§4.1.3#r9": [30, 31, 32, 33]
  "§4.1.3#p5": 37
  "§4.1.3#r7": 37
  "§4.1.3#r8": 37
  "ST-24": [40, 46, 48]
coverage:
  web: automated
---

# Screening Halaman Detail Mode Edit: Badge Status dan Tab Asset Names (Berisi, Search Kosong, dan Genuinely Empty)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): Asset Class Active `B-ANCHOR` dengan Class Name `Anchor Heavy Equipment` tanpa Asset Name ter-assign; Asset Class Inactive `B-INACT`; Asset Class Active `HEAVY-EQ` (Class Name `Heavy Equipment`) dengan tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; kategori Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W, nama lengkap Rina Wulandari), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Seed disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak mengubah data (tidak ada field yang diisi).

## Test Steps

### TC-FA-FAAC-18: Screening Halaman Detail mode Edit Asset Class Active

1. Ketik Search `B-ANCHOR`, tekan Enter
2. Klik link Class Code `B-ANCHOR`
3. Verifikasi breadcrumb `Settings > Accounting > Asset Class > Detail`
4. Verifikasi judul `Edit Asset Class`
5. Verifikasi di bawah judul tampil `B-ANCHOR – Anchor Heavy Equipment`
6. Verifikasi Badge Status `Active` berwarna hijau (success)
7. Verifikasi Badge Status tidak berada di samping judul
8. Verifikasi tab `General` aktif dengan nilai tersimpan Asset Class `B-ANCHOR`
9. Verifikasi Last Posted Period dan Last Exported Period read-only bernilai `—`
10. Verifikasi footer berisi tombol `Clear Field` dan `Save`
11. Verifikasi tombol `Submit` tidak ada
12. Verifikasi tidak ada Alert versi Scheduled

### TC-FA-FAAC-19: Badge Status Inactive pada Halaman Detail mode Edit

13. Klik breadcrumb `Asset Class`
14. Ganti isi kotak search dengan `B-INACT`, tekan Enter
15. Klik link Class Code `B-INACT`
16. Verifikasi Badge Status berbunyi `Inactive` dengan warna merah (danger)
17. Verifikasi judul tetap `Edit Asset Class`

### TC-FA-FAAC-21: Screening tab Asset Names pada Detail Asset Class mode Edit yang sudah memiliki Asset Name

18. Klik breadcrumb `Asset Class`
19. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
20. Klik link Class Code `HEAVY-EQ`
21. Klik tab Asset Names
22. Verifikasi toolbar rata kanan berurutan Search, Filter, tombol `+ Assign Asset Names`
23. Verifikasi toolbar tidak memuat Download maupun Changelog
24. Verifikasi kolom berurutan Asset Name, Category, Label, Assets, Assigned At, Assigned By dengan kolom checkbox di kiri dan Actions ⋯ di kanan
25. Verifikasi baris terurut Asset Name A-Z (default): Crane Rental Unit, Excavator PC200, Wheel Loader
26. Verifikasi Asset Name tampil sebagai link
27. Verifikasi Category tampil sebagai badge berisi leaf saja (`Heavy Equipment`, `Rented`)
28. Arahkan kursor ke badge Category baris Excavator PC200
29. Verifikasi hover badge menampilkan hierarki lengkap `Machinery > Heavy Equipment`
30. Verifikasi Label Excavator PC200 tampil dua badge `Heavy` dan `Insured` tanpa chip `+N more`
31. Verifikasi Assets Excavator PC200 bernilai 8
32. Verifikasi Assigned At Excavator PC200 `02/01/26`
33. Verifikasi tampilan kolom Assigned By Excavator PC200 `Rina W`
34. Arahkan kursor ke teks Assigned By baris Excavator PC200
35. Verifikasi hover Assigned By menampilkan nama lengkap `Rina Wulandari`
36. Klik ikon ⋯ pada baris Crane Rental Unit
37. Verifikasi menu ⋯ baris memuat dua aksi `Move` dan `Unassign`
38. Tutup menu dengan Esc

### TC-FA-FAAC-23: Search tab Asset Names tanpa hasil menampilkan EmptyState No results found

39. Ketik Search `zzzz`, tekan Enter
40. Verifikasi EmptyState menampilkan illustration, title `No results found`, dan description `Try adjusting your search or filter.`
41. Verifikasi toolbar (Search, Filter, `+ Assign Asset Names`) tetap tampil

### TC-FA-FAAC-22: Screening tab Asset Names pada Asset Class yang belum memiliki Asset Name

42. Klik breadcrumb `Asset Class`
43. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
44. Klik link Class Code `B-ANCHOR`
45. Klik tab Asset Names
46. Verifikasi EmptyState menampilkan illustration, title `No asset name yet`, dan description `Assign asset names to apply this asset class to their assets.`
47. Verifikasi tombol `+ Assign Asset Names` tetap tampil di toolbar
48. Verifikasi tombol `+ Assign Asset Names` tidak diduplikasi di EmptyState
49. Klik breadcrumb `Asset Class`
50. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Spec melewati sekitar 35 langkah (50 langkah): kelima blok adalah screening Halaman Detail mode Edit (tab General dan tab Asset Names) tanpa input pada dataset Pre-setup yang sama, tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan navigasi ke Detail. Langkah bertambah karena `Verifikasi` dipecah per klausa (S-01).
- Langkah penghubung (S-03): langkah 1, 14, 19, 43 (Search untuk menemukan baris target karena tabel memiliki lebih dari 10 baris dan baris target tidak diandalkan berada di halaman 1; R-16), langkah 13, 18, 42, dan 49 (kembali ke daftar lewat breadcrumb; kotak Search mempertahankan nilainya sehingga langkah Search berikutnya berbunyi "ganti isi kotak search"), langkah 21, 45 (membuka tab Asset Names), langkah 38 (menutup menu), langkah 50 (mengosongkan Search, S-09).
- Urutan TC dalam spec: 18, 19, 21, 23, 22. TC-FA-FAAC-23 diletakkan sesudah TC-FA-FAAC-21 karena memakai Asset Class dan tab yang sama.
- Nama literal Pre-setup (B-ANCHOR, B-INACT, HEAVY-EQ, nama Asset Name) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, nilai, dan urutan persis dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-FAAC-22 menyebut "Asset Class 'anchor'" tanpa Class Code; spec memakai `B-ANCHOR` (anchor TC-FA-FAAC-18) sebagai Asset Class Active tanpa Asset Name.
  - TC-FA-FAAC-18 butir b menyebut "nilai tersimpan" tanpa daftar nilai; spec mengasersi Class Code dan Class Name dari baris identitas.
  - TC-FA-FAAC-21 butir e menyebut tampilan kolom `Rina W` bersama hover nama lengkap; spec memisahkan keduanya (langkah 33 dan 35).
