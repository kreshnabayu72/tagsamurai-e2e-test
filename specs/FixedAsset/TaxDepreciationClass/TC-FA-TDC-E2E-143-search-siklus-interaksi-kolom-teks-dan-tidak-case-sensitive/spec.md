---
id: TC-FA-TDC-E2E-143-search-siklus-interaksi-kolom-teks-dan-tidak-case-sensitive
title: "Search: Siklus Interaksi, Kolom Teks, dan Tidak Case-Sensitive"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-489
  - TC-FA-TDC-490
  - TC-FA-TDC-491
  - TC-FA-TDC-492
sourceRules: ["§4.1.1#p5", "§5#b2", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r8", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r9"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p5": 4
  "§5#b2": [9, 15, 17]
  "§4.1.1#r2": [11, 24]
  "§4.1.1#r3": 26
  "§4.1.1#r4": 28
  "§4.1.1#r8": 30
  "§4.1.1#r5": 32
  "§4.1.1#r6": 34
  "§4.1.1#r7": 36
  "§4.1.1#r9": 38
anchor: [2, 3, 6, 8, 13, 14, 20, 21, 22]
coverage:
  web: automated
---

# Search: Siklus Interaksi, Kolom Teks, dan Tidak Case-Sensitive

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Nilai yang dicari: Class Name BLD-NP `Bangunan tidak permanen`; Asset Type LAND `Land`; Allowed Methods `Straight Line · Declining Balance` pada NB-1, NB-2, NB-4, dan NB-KHS; Useful Life NB-SL `16`; Straight Line Rate NB-2 `12.5%`; Declining Balance Rate NB-1 `50%`; Used By NB-2 `3`. Pada tiap nilai Search, sedikitnya dua nilai berbeda ada pada kolom yang dicari (S-11).
- Data uji (keyword Search, literal TC): `NB-1`, `NB-2`, `nb-kh`, `tidak permanen`, `land`, `declining`, `16`, `12.5`, `50`, `3`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); mengarahkan kursor (hover) untuk tooltip; membaca fokus input.
- State global yang diubah: Search pada tabel (dikosongkan oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Siklus interaksi Search box (TC-FA-TDC-489)

1. Klik icon Search
2. Verifikasi Search bar melebar
3. Verifikasi kursor fokus di input Search
4. Verifikasi placeholder `Search class code, name, or regulation`
5. Arahkan kursor ke icon Search
6. Verifikasi tooltip `Search` tampil
7. Ketik `NB-1`
8. Verifikasi icon `(✕)` muncul di sisi kanan input
9. Verifikasi tabel belum tersaring dan masih menampilkan 9 baris
10. Tekan Enter
11. Verifikasi tabel tersaring menjadi satu baris NB-1
12. Klik icon `(✕)` pada input Search
13. Verifikasi input Search kosong
14. Verifikasi search bar tetap terbuka dengan kursor fokus di input
15. Verifikasi tabel tetap menampilkan hasil NB-1 (satu baris)
16. Tekan Enter pada input yang kosong
17. Verifikasi tabel reset menampilkan 9 baris
18. Ketik `NB-2`
19. Klik icon panah `(←)` di kiri input
20. Verifikasi Search bar menutup menjadi icon Search
21. Verifikasi keyword Search dikosongkan
22. Verifikasi tabel langsung menampilkan 9 baris

### Search kolom Class Code dan Class Name (TC-FA-TDC-490)

23. Ketik Search `nb-kh`, tekan Enter
24. Verifikasi (Class Code) tabel hanya menampilkan baris NB-KHS
25. Ganti isi kotak search dengan `tidak permanen`, tekan Enter
26. Verifikasi (Class Name) tabel hanya menampilkan baris BLD-NP (`Bangunan tidak permanen`)

### Search kolom Asset Type dan Allowed Methods (TC-FA-TDC-491)

27. Ganti isi kotak search dengan `land`, tekan Enter
28. Verifikasi (Asset Type) tabel hanya menampilkan baris LAND
29. Ganti isi kotak search dengan `declining`, tekan Enter
30. Verifikasi (Allowed Methods) tabel menampilkan tepat empat baris: NB-1, NB-2, NB-4, dan NB-KHS

### Search kolom Useful Life, Straight Line Rate, Declining Balance Rate, dan Used By (TC-FA-TDC-492)

31. Ganti isi kotak search dengan `16`, tekan Enter
32. Verifikasi (Useful Life (years)) tabel hanya menampilkan baris NB-SL
33. Ganti isi kotak search dengan `12.5`, tekan Enter
34. Verifikasi (Straight Line Rate) tabel hanya menampilkan baris NB-2
35. Ganti isi kotak search dengan `50`, tekan Enter
36. Verifikasi (Declining Balance Rate) tabel hanya menampilkan baris NB-1
37. Ganti isi kotak search dengan `3`, tekan Enter
38. Verifikasi (Used By) tabel hanya menampilkan baris NB-2
39. Klik `(←)` pada kotak Search

## Notes

- Urutan TC dalam spec: TC-FA-TDC-489, 490, 491, 492 (siklus interaksi Search box di awal, lalu variasi kolom yang dicari).
- Langkah penghubung (S-03): langkah 5 (hover icon Search; TC-FA-TDC-489 Expected a menyebut tooltip tanpa langkah hover, dan hover dilakukan segera sesudah klik supaya tooltip diasersi sebelum state berubah, 8b.5), langkah 39 (menutup kotak Search dan mereset tabel sebelum akhir spec; S-09). Pergantian isi kotak Search pada langkah 25, 27, 29, 31, 33, 35, 37 mengikuti butir "ganti isi kotak search" (8b.9) untuk langkah TC "Kosongkan Search, ketik X".
- Asersi "hanya menampilkan baris X" mengasersi X tampil; baris lain Example Data yang dijamin ada tidak tampil karena hasil Search menyempit dari 9 baris (langkah 9 dan 17 membuktikan 9 baris tampil sebelum Search).
- Spec ini sekitar 39 langkah, di atas ~35 langkah. Alasan: satu topik (Search kolom tabel utama) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri dan tidak butuh blok sebelumnya, dan S-01 mengharuskan satu `Verifikasi` per klausa (TC-FA-TDC-489 punya enam butir Expected, TC-FA-TDC-492 empat). Tidak ada alasan lain.
- Temuan untuk QA:
  - TC-FA-TDC-489 Expected a (tooltip `Search` saat hover) tanpa langkah hover di TC; spec menambah satu langkah hover.
  - TC-FA-TDC-489 Expected f "keyword dikosongkan" tidak menyebut cara mengamatinya sesudah Search bar menutup; spec mengasersinya apa adanya.
  - TC-FA-TDC-490 sampai 492: langkah "Kosongkan Search, ketik X" tidak menyebut cara mengosongkan; spec memakai "ganti isi kotak search".
  - Email akun Total Control tidak tertulis di TC.
