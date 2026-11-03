---
id: TC-FA-CAT-E2E-161-tabel-step-interaksi-search-dan-search-vs-visibilitas-kolom
title: "Tabel Step Category Consolidation: Interaksi Search (Reveal, Enter, Clear, Panah Tutup) dan Search Terikat Visibilitas Kolom sedangkan Filter Independen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-595
  - TC-FA-CAT-596
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Interaksi Search (Reveal, Enter, Clear, Panah Tutup) dan Search Terikat Visibilitas Kolom sedangkan Filter Independen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech` (Code `AT`), `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle` (Code `ZV`), `Eta Furniture`, `Theta Heavy`, dengan Modified By bergantian `Jane Smith`, `Alex Brown`, dan `System`. Daftar nama kategori ber-Modified By `Jane Smith` (langkah 34) dibaca lewat kemampuan baca state BE yang disediakan tim FE/BE tanpa endpoint karangan.
- Keyword yang dipakai: `Alpha`, `Beta`, `ZV`; Filter Modified By: `Jane S`.
- State yang diubah spec: visibilitas kolom `Code` dan `Modified By` serta Filter tabel Step (langkah 23 sampai 35). Dipulihkan pada langkah 35 dan di hook `after` suite dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`); kemampuan disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-595: Interaksi Search tabel Step, reveal, Enter, (✕), dan panah tutup

2. Hover icon Search di toolbar tabel Step
3. Verifikasi tooltip icon `Search`
4. Klik icon Search
5. Verifikasi input Search melebar (reveal)
6. Verifikasi kursor langsung fokus pada input
7. Verifikasi placeholder `Search category name, code, status...`
8. Ketik `Alpha` tanpa menekan `Enter`
9. Verifikasi icon (✕) muncul pada input
10. Verifikasi tabel belum tersaring (tidak live-as-you-type)
11. Tekan `Enter`
12. Verifikasi tabel hanya memuat `Alpha Tech`
13. Klik icon (✕) pada input
14. Verifikasi input kosong
15. Verifikasi tabel mempertahankan hasil terakhir (hanya `Alpha Tech`)
16. Tekan `Enter` pada input kosong
17. Verifikasi tabel kembali memuat semua kategori
18. Ketik Search `Beta`, tekan `Enter`
19. Verifikasi tabel hanya memuat `Beta Tools`
20. Klik icon panah (←) di kiri toolbar
21. Verifikasi kotak pencarian menjadi icon Search biasa dengan keyword kosong
22. Verifikasi tabel langsung memuat seluruh kategori tanpa `Enter`

### TC-FA-CAT-596: Search terikat visibilitas kolom, sedangkan Filter independen dari visibilitas kolom

23. Klik header Actions (⋯) > `Setup Column...`, hilangkan centang kolom `Code`, lalu klik `[Save]`
24. Ketik Search `ZV`, tekan `Enter`
25. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil (keyword `ZV` tidak mencocokkan baris saat `Code` di-hide)
26. Klik header Actions (⋯) > `Setup Column...`, centang kembali kolom `Code`, lalu klik `[Save]`
27. Ganti isi kotak search dengan `ZV`, tekan `Enter`
28. Verifikasi tabel memuat `Zeta Vehicle` (keyword `ZV` mencocokkan setelah `Code` di-unhide)
29. Klik icon panah (←) di kiri toolbar untuk mengosongkan Search
30. Klik header Actions (⋯) > `Setup Column...`, hilangkan centang kolom `Modified By`, lalu klik `[Save]`
31. Klik icon Filter, pilih Modified By `Jane S`, lalu klik `[Apply]`
32. Klik icon Filter untuk membuka kembali Filter Panel
33. Verifikasi field Filter `Modified By` tetap ada di Filter Panel dengan nilai `Jane S` tetap ter-Apply walau kolomnya disembunyikan
34. Verifikasi tabel tersaring hanya pada kategori hasil ubahan `Jane Smith`
35. Klik `[Clear Field]`, klik `[Apply]`, lalu pulihkan visibilitas kolom `Code` dan `Modified By` dengan menghapus preferensi kolom di browser

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 (membuka wizard), langkah 29 (mengosongkan Search lewat panah), langkah 32 (membuka kembali Filter Panel), langkah 35 (membersihkan Filter dan memulihkan kolom, sesuai Post Condition TC-FA-CAT-596).
- Langkah 18 dan Verifikasi langkah 19 mengikuti langkah 6 TC-FA-CAT-595 ("Ketik `Beta`, tekan Enter"); Expected TC tidak menyebut hasilnya. Verifikasi langkah 19 ditambahkan agar asersi langkah 22 (tabel kembali memuat seluruh kategori) bermakna dari keadaan tersaring.
- Asersi empty state pada langkah 25 menjadi anchor positif untuk absence hasil Search (bagian 8b butir 2).
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-595 Expected d ("tabel kembali memuat semua kategori baru saat `Enter` pada input kosong") ditulis sebagai Verifikasi langkah 17 setelah langkah 16.
  - TC-FA-CAT-596 Expected c menyebut "hanya kategori hasil ubahan `Jane Smith`" tanpa nama kategorinya; kolom Modified By disembunyikan sehingga hasilnya tidak teramati dari tabel, dan spec membandingkannya dengan data seed yang dibaca BE.
  - TC-FA-CAT-596 Post Condition ("Kolom `Code` dan `Modified By` dikembalikan ke Visible") dipenuhi dengan menghapus preferensi kolom di browser sesuai konvensi bagian 4.
