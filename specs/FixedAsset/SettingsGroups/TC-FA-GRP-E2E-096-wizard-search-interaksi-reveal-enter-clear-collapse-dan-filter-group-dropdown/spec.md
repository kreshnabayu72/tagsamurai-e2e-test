---
id: TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown
title: "Wizard: Interaksi Search (Reveal, Enter, Clear, Collapse) serta Filter Group (Isi Opsi, Dua Opsi OR, Search Dropdown)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1037
  - TC-FA-GRP-1038
  - TC-FA-GRP-1039
  - TC-FA-GRP-1040
coverage:
  web: automated
---

# Wizard: Interaksi Search (Reveal, Enter, Clear, Collapse) serta Filter Group (Isi Opsi, Dua Opsi OR, Search Dropdown)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.

## Test Steps

### TC-FA-GRP-1037: Interaksi Search

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Hover icon Search pada toolbar
3. Verifikasi tooltip Search tampil
4. Klik icon Search
5. Verifikasi input Search melebar dan auto-focus
6. Verifikasi placeholder Search sesuai konvensi platform
7. Ketik keyword 1 karakter `w` tanpa menekan Enter
8. Verifikasi icon `✕` muncul
9. Verifikasi tabel belum tersaring (keenam group masih tampil)
10. Tekan Enter
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi tabel tersaring sesuai keyword
13. Klik icon `✕` di dalam input
14. Verifikasi input kosong, tetap terbuka, dan fokus
15. Verifikasi tabel tetap menampilkan hasil search terakhir
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan semua data
18. Ketik keyword `Ware` dengan dua spasi di awal dan di akhir, tekan Enter
19. Verifikasi sedikitnya satu baris tampil
20. Verifikasi baris yang tampil sama dengan keyword `Ware` tanpa spasi tepi
21. Verifikasi isi input di layar tetap seperti yang diketik
22. Ganti isi kotak search dengan `Ware`, tekan Enter, lalu klik icon `(←)`
23. Verifikasi input Search tertutup dan keyword dikosongkan
24. Verifikasi tabel langsung reset ke semua data

### TC-FA-GRP-1038: Isi opsi dropdown Filter Group

25. Klik icon Filter, lalu buka dropdown Group
26. Verifikasi opsi sama dengan nama group (full path) distinct pada baris tabel step saat ini dan tidak memuat nilai yang tidak dipakai baris mana pun
27. Verifikasi opsi dapat dicentang lebih dari satu (multi-select) dan dropdown memiliki kotak search internal

### TC-FA-GRP-1039: Dua opsi dalam satu field (logika OR)

28. Centang opsi `Warehouse A` dan opsi `Warehouse B` pada Group
29. Klik [Apply]
30. Verifikasi sedikitnya satu baris tampil
31. Verifikasi baris dengan Group `Warehouse A` atau `Warehouse B` tampil
32. Verifikasi baris dengan nilai Group lain tidak tampil

### TC-FA-GRP-1040: Search internal dropdown Filter Group

33. Klik icon Filter, lalu buka dropdown Group
34. Ketik potongan nama opsi huruf kecil `ware` di kotak search dropdown
35. Verifikasi sedikitnya satu opsi tampil
36. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
37. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
38. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 33: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Spec berisi lebih dari 35 langkah. Alasan: empat TC Search dan Filter pada satu surface dan satu dataset, tiap blok berdiri sendiri; TC-1037 memuat sembilan langkah interaksi siklus input yang tiap klausanya punya `Verifikasi` (S-01).
- Verifikasi "sedikitnya satu baris/opsi tampil" (langkah 11, 19, 35) ditambahkan sebagai anchor positif sebelum asersi universal hasil Search dan opsi dropdown (8b butir 2; S-03).
- Langkah penghubung TC-1040: membuka ulang Filter sesudah [Apply] pada TC-1039 (filter yang berlaku tidak memengaruhi opsi dropdown).
- Temuan untuk QA:
  - TC-1037 Expected a menyebut placeholder "sesuai konvensi platform" tanpa teks; spec mengasersi placeholder sesuai konvensi tanpa mengarang teks.
  - TC-1037 Langkah 4 menyebut "keyword 1 karakter lalu lanjutkan tanpa Enter" tanpa nilai; spec memakai `w`.
  - TC-1038 Expected a tidak menyebut jumlah opsi; spec mengasersi kesesuaian dengan baris tabel.
