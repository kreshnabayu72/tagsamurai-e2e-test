---
id: TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia
title: "State Tenant: Baca Tab Asset Class Tetap Tersedia saat Client Suspended atau Expired"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-594
  - TC-FA-FAAC-629
  - TC-FA-FAAC-630
  - TC-FA-FAAC-631
sourceRules: ["§9.3#r1", "§3.9#r1", "§9.4.1#r1", "§4.1.1#r28", "§5#b8"]
smoke: []
dependsOn: []
trace:
  "§9.3#r1": [1, 15, 28]
  "§3.9#r1": [2, 9]
  "§9.4.1#r1": [4, 7, 11, 20, 24, 33]
  "§4.1.1#r28": [13, 26]
  "§5#b8": [18, 31]
coverage:
  web: automated
---

# State Tenant: Baca Tab Asset Class Tetap Tersedia saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: status client (`Active`, `Suspended`, `Expired`). Pelaku perubahan status tidak disebut TC, PRD, atau LLD; fixture BE untuk mengubah status entitas "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Status awal `Active` dicatat di hook `before`; hook `after` memulihkan status ke `Active` walau spec gagal di tengah.
- Data Pre-setup dibaca, tidak diubah: sembilan Asset Class contoh (Tabel Data Uji Pre-setup, nilai mengikuti Example Data PRD §4.1.1): `HEAVY-EQ`, `VEHICLES`, `IT-EQ`, `MACHINERY`, `BLDG`, `STORAGE`, `OFFICE-NEW`, `LAND` (Active) dan `OFFICE-OLD` (Inactive); serta Asset Class `B-ANCHOR` (Active) untuk TC-594. Kode literal dipakai apa adanya karena asersi TC bergantung pada kode itu.
- Kemampuan teknis: membaca berkas unduhan (hanya nama berkas `Asset-Class.csv` yang diasersi, isi berkas tidak); Modal Changelog dibuka lewat UI.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-631: Entitas Active, tab Asset Class dapat dibaca dan tombol aksi tulis tersedia

1. Verifikasi tabel Asset Class tampil
2. Verifikasi Button `[+ Asset Class]` tampil dan Enabled
3. Atur lewat fixture BE status client menjadi `Suspended`, lalu muat ulang halaman

### TC-FA-FAAC-594: Baca tetap tersedia saat entitas Suspended (sisi aksi tulis)

4. Verifikasi tabel Asset Class tampil dengan sedikitnya satu baris
5. Ketik Search `B-ANCHOR`, tekan Enter
6. Klik link Class Code `B-ANCHOR` di tabel
7. Verifikasi Detail `B-ANCHOR` terbuka
8. Klik breadcrumb `Asset Class`
9. Verifikasi Button `[+ Asset Class]` tetap tampil pada toolbar tabel

### TC-FA-FAAC-629: Baca tab Asset Class tetap tersedia saat entitas Suspended

10. Klik tab `Asset Class`
11. Verifikasi tabel Asset Class tampil dengan sedikitnya satu baris
12. Ganti isi kotak search dengan `heavy`, tekan Enter
13. Verifikasi Search menyaring tabel hingga baris `HEAVY-EQ`
14. Klik icon `Changelog`
15. Verifikasi Modal `Changelog: Asset Class` terbuka
16. Tutup Modal Changelog
17. Klik icon `Download`, lalu pilih `Download as CSV`
18. Verifikasi berkas `Asset-Class.csv` terunduh
19. Klik Class Code `HEAVY-EQ` di tabel
20. Verifikasi halaman Detail `HEAVY-EQ` terbuka untuk dilihat
21. Klik breadcrumb `Asset Class`
22. Atur lewat fixture BE status client menjadi `Expired`, lalu muat ulang halaman

### TC-FA-FAAC-630: Baca tab Asset Class tetap tersedia saat entitas Expired

23. Klik tab `Asset Class`
24. Verifikasi tabel Asset Class tampil dengan sedikitnya satu baris
25. Ganti isi kotak search dengan `heavy`, tekan Enter
26. Verifikasi Search menyaring tabel hingga baris `HEAVY-EQ`
27. Klik icon `Changelog`
28. Verifikasi Modal `Changelog: Asset Class` terbuka
29. Tutup Modal Changelog
30. Klik icon `Download`, lalu pilih `Download as CSV`
31. Verifikasi berkas `Asset-Class.csv` terunduh
32. Klik Class Code `HEAVY-EQ` di tabel
33. Verifikasi halaman Detail `HEAVY-EQ` terbuka untuk dilihat
34. Klik breadcrumb `Asset Class`
35. Klik `(←)` pada kotak Search
36. Atur lewat fixture BE status client kembali menjadi `Active`, lalu muat ulang halaman

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor: TC-631 (status Active) lebih dulu, lalu status `Suspended` (TC-594, TC-629), lalu `Expired` (TC-630), supaya status client berganti satu arah (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 3, 22, dan 36 (mengganti status client); langkah 5 (Search untuk menemukan baris target, R-16); langkah 8, 21, dan 34 (kembali ke tabel); langkah 16 dan 29 (menutup Modal Changelog); langkah 35 (mengosongkan Search); langkah 10 dan 23 adalah `Klik tab Asset Class` dari TC dan dicatat sebagai langkah penghubung (S-03).
3. TC-594 Expected b (kontrol tulis tetap tampil) diasersi di spec ini pada langkah 9 (`Verifikasi` Button `[+ Asset Class]` tampil di toolbar tabel saat `Suspended`). Expected c (penolakan aksi tulis) diuji di spec 177 (TC-590 sampai TC-593) dan tidak dirujuk di sini sebagai pemenuhan Expected b; yang diasersi di spec ini hanya tabel, Detail, dan kontrol tulis tampil.
4. Langkah 11 dan 24 memuat `Verifikasi` tambahan (tabel tampil dengan sedikitnya satu baris) sebagai pembanding asersi universal "Search menyaring tabel" (8b butir 2); asersi tambahan ini dicatat sesuai S-03.
5. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `HEAVY-EQ` dan `B-ANCHOR`; dipakai apa adanya tanpa suffix `{runId}`. Spec hanya membaca data tersebut.
6. Alasan melebihi sekitar 35 langkah (36 langkah): blok TC-629 dan TC-630 identik (satu kelas harness h, tiap blok mengganti status client dan berdiri sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah 10 sampai 21 dan langkah 23 sampai 34 adalah langkah yang sama dengan status client berbeda.
7. Temuan untuk QA: TC-631 mengasumsikan sembilan Asset Class contoh pada client yang sama dengan TC-629 dan TC-630; spec memakai client dan seed yang sama dan hanya mengubah status client. TC-594 tidak menyebut keadaan kotak Search saat kembali dari Detail; spec menulis langkah 12 dan 25 sebagai "ganti isi kotak search" dengan mengandalkan hasil Search sebelumnya dipertahankan.
