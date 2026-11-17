---
id: TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended
title: "Kasus Tepi: Destination Move Hanya Asset Class Active, Satu Class per Asset Name, dan Duplicate Tidak Mengubah Data atau Menyalin Asset Name"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-634
  - TC-FA-FAAC-635
  - TC-FA-FAAC-637
  - TC-FA-FAAC-643
sourceRules: ["§[F-FAAC-09] Move Asset Names#b1", "§[F-FAAC-04] Deactivate Asset Class#b4", "F-FAAC-09.k1", "§4.2f#b2", "§[F-FAAC-06] Duplicate Asset Class#b3", "§4.1.3#p1", "ST-05", "§[F-FAAC-01] Create Asset Class#b5", "§[F-FAAC-01] Create Asset Class#b3", "§[F-FAAC-06] Duplicate Asset Class#b2", "§[F-FAAC-09] Move Asset Names#b5"]
smoke: []
dependsOn: []
trace:
  "§[F-FAAC-09] Move Asset Names#b1": 4
  "§[F-FAAC-04] Deactivate Asset Class#b4": 5
  "F-FAAC-09.k1": 6
  "§4.2f#b2": 13
  "§[F-FAAC-06] Duplicate Asset Class#b3": [15, 16]
  "§4.1.3#p1": 21
  "ST-05": 22
  "§[F-FAAC-01] Create Asset Class#b5": 29
  "§[F-FAAC-01] Create Asset Class#b3": 30
  "§[F-FAAC-06] Duplicate Asset Class#b2": [34, 38]
  "§[F-FAAC-09] Move Asset Names#b5": [39, 43]
coverage:
  web: automated
---

# Kasus Tepi: Destination Move Hanya Asset Class Active, Satu Class per Asset Name, dan Duplicate Tidak Mengubah Data atau Menyalin Asset Name

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (kode dan nama literal TC, disediakan fixture BE): Asset Class `B-NAMES` (Active, dengan Asset Name ter-assign) dan Asset Class Inactive `B-INACT` (TC-634); Asset Class `B-ANCHOR` (Active; sumber Duplicate TC-635, hanya dibaca); Asset Class `Heavy Equipment` (`HEAVY-EQ`, Active) dengan tiga Asset Name ter-assign `Excavator PC200` (8 aset aktif; Machinery > Heavy Equipment; Label Heavy, Insured), `Wheel Loader` (4 aset aktif; Label Heavy), `Crane Rental Unit` (0 aset aktif; Machinery > Rented; Label Rented) dan Asset Name `Welding Rod Cart` (0 aset aktif) ter-assign ke `Heavy Equipment` (TC-637 dan TC-643); Asset Class `Machinery` (`MACHINERY`, Active). Spec memindahkan `Welding Rod Cart` ke `MACHINERY` (TC-637); fixture BE memulihkan keanggotaannya di hook `after` (efek Last Updated dan entri Changelog dicatat di sini).
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` menurut precondition TC-643; fixture BE menyetelnya pada langkah 17 sebelum blok TC-643 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Data Dinamis milik spec: Asset Class hasil Duplicate Class Code literal `B-HEQ2` dan Class Name `Heavy Equipment {runId}-190` (TC-643; nilai Data Uji TC "HEAVY-EQ-2" diganti kode literal 15 karakter atau kurang dan `{runId}-190` dipindah ke Class Name agar unik per run; field wajib lain mengikuti pre-fill), sisa run sebelumnya dihapus fixture BE di hook `before` dan hasil Duplicate dihapus di hook `after`.
- Kemampuan teknis: pembacaan jumlah Asset Class dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (disediakan tim FE/BE; audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-634: Asset Class Inactive tidak muncul pada pilihan Destination Asset Class di dialog Move

1. Ketik Search `B-NAMES`, tekan Enter
2. Buka Detail `B-NAMES`, klik tab `Asset Names`, lalu klik ikon `⋯` pada baris pertama dan pilih `Move`
3. Buka daftar `Destination Asset Class`
4. Verifikasi daftar `Destination Asset Class` memuat sedikitnya satu Asset Class Active selain `B-NAMES`
5. Verifikasi `B-INACT` tidak ada di daftar tujuan
6. Verifikasi daftar tujuan hanya memuat Asset Class Active selain asal
7. Klik `[Cancel]` pada dialog Move

### TC-FA-FAAC-635: Duplicate tidak mengubah data sebelum Submit

8. Catat baseline lewat kemampuan baca BE: jumlah Asset Class dan jumlah entri Changelog Asset Class, System Log, dan Activity Log
9. Klik breadcrumb `Asset Class`
10. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
11. Klik ikon `⋯` pada baris `B-ANCHOR`, lalu pilih `Duplicate`
12. Klik breadcrumb `Asset Class`
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Verifikasi tidak ada Asset Class baru: jumlah Asset Class sama dengan baseline
16. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)

### TC-FA-FAAC-643: Duplicate Asset Class tidak menyalin Asset Name

17. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-643)
18. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
19. Pilih row action `Duplicate` pada baris `HEAVY-EQ`
20. Klik tab `Asset Names` pada halaman Add Asset Class
21. Verifikasi tab `Asset Names` pada halaman Add Asset Class tampil dengan tombol `+ Assign Asset Names`
22. Verifikasi daftar draft tab `Asset Names` kosong (tanpa `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit`)
23. Isi Class Code `B-HEQ2` dan Class Name `Heavy Equipment {runId}-190`, dan field wajib lain mengikuti pre-fill
24. Klik `[Submit]`
25. Tunggu aksi selesai
26. Klik breadcrumb `Asset Class`
27. Ganti isi kotak search dengan `B-HEQ2`, tekan Enter
28. Buka Detail `B-HEQ2`, lalu klik tab `Asset Names`
29. Verifikasi Detail Asset Class baru terbuka dengan tab `Asset Names`
30. Verifikasi Asset Class baru tidak memiliki Asset Name
31. Klik breadcrumb `Asset Class`
32. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
33. Buka Detail `HEAVY-EQ`, lalu klik tab `Asset Names`
34. Verifikasi `Heavy Equipment` tetap memiliki `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit`

### TC-FA-FAAC-637: Asset Name yang dipindah hanya berada di satu Asset Class

35. Klik ikon `⋯` pada baris `Welding Rod Cart`, lalu pilih `Move`
36. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, lalu klik `[Move]`
37. Tunggu aksi selesai (dialog Move menutup)
38. Verifikasi `Excavator PC200` tetap tampil di tab `Asset Names` Heavy Equipment
39. Verifikasi `Welding Rod Cart` tidak tampil di tab `Asset Names` Heavy Equipment
40. Klik breadcrumb `Asset Class`
41. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
42. Buka Detail `MACHINERY`, lalu klik tab `Asset Names`
43. Verifikasi `Welding Rod Cart` tampil di tab `Asset Names` Machinery

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor TC: TC-643 sebelum TC-637 supaya halaman Detail `HEAVY-EQ` yang sudah terbuka (langkah 33) langsung dipakai TC-637, dan TC-637 (yang mengubah keanggotaan Asset Name) berada di akhir (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 10, 18, 27, 32, dan 41 memakai Search untuk menemukan baris target (R-16); langkah 7 menutup dialog Move dengan `[Cancel]`, yang tidak memunculkan dialog `Unsaved Changes` menurut Catatan Cakupan TC-698 dan TC-699; langkah 9, 26, 31, dan 40 kembali ke tabel; langkah 12 sampai 14 menutup form Duplicate yang dirty lewat breadcrumb sesuai langkah TC (S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08); langkah 25 dan 37 (menunggu aksi selesai, 8b butir 8); langkah 17 (fixture BE menyetel keadaan awal dinamis TC-643, S-14, bukan bagian TC).
3. Prinsip 13g dan S-12: klausa "tidak ada log" pada TC-635 adalah asersi jumlah pada TC fungsional (aksi UI Duplicate yang ditutup tanpa Submit) sehingga diasersi di spec ini dengan `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log), sesudah `Verifikasi` dialog `Unsaved Changes` sebagai anchor positif; baseline dicatat sebelum pemicu.
4. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `B-NAMES`, `B-INACT`, `B-ANCHOR`, `HEAVY-EQ`, `MACHINERY`, dan nama Asset Name literal; dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nilai itu. TC-637 memindahkan `Welding Rod Cart` (seed, dipulihkan fixture BE di hook `after`).
5. Alasan di atas sekitar 35 langkah: keempat TC satu topik (aturan Asset Class tujuan dan keanggotaan Asset Name pada Move dan Duplicate); tiap blok berdiri sendiri dengan data dan baseline sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain (konvensi bagian 3 prinsip 13).
6. Temuan untuk QA: TC-634 menyebut "Asset Name Asset Class lain" tanpa menyebut baris atau Asset Class tujuan buka dialog; spec memakai baris pertama Asset Name `B-NAMES`. TC-634 menyebut `B-INACT` tanpa menyebut statusnya di Precondition; spec memakai seed Inactive. TC-635 tidak menyebut apakah form Duplicate yang belum diubah memunculkan dialog `Unsaved Changes`; spec mengikuti langkah TC ("tutup lewat breadcrumb dan Leave") dengan `Verifikasi` dialog yang diwajibkan S-08. TC-637 tidak menyebut Effective From untuk Move Asset Name tanpa aset aktif. TC-643 memakai Data Uji Class Code `HEAVY-EQ-2`; spec memakai kode literal `B-HEQ2` dengan `{runId}-190` di Class Name (batas 15 karakter Class Code; S-12; pola spec 066 sampai 069).
7. Setelah `[Submit]` pada Duplicate halaman tetap di Detail mode Edit (PRD asset-class.md; TC-75, TC-259 b), sehingga langkah 26 kembali ke tabel lewat breadcrumb `Asset Class` sebelum Search `B-HEQ2`.
