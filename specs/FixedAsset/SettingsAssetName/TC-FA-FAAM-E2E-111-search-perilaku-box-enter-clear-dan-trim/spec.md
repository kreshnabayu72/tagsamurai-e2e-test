---
id: TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim
title: "Search: Reveal Box, Mengetik Belum Menyaring, Enter, Clear, Collapse, dan Trim"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-352
  - TC-FA-FAAM-353
  - TC-FA-FAAM-354
  - TC-FA-FAAM-355
  - TC-FA-FAAM-356
  - TC-FA-FAAM-357
coverage:
  web: automated
---

# Search: Reveal Box, Mengetik Belum Menyaring, Enter, Clear, Collapse, dan Trim

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10) dan `Ergonomic Chair` (Pre-setup #11).
- Kemampuan teknis: hover dan fokus input.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-352: Search box reveal, auto-focus, placeholder, dan tooltip
1. Arahkan kursor ke icon Search
2. Verifikasi tooltip `Search` tampil
3. Klik icon Search
4. Verifikasi search bar melebar
5. Verifikasi kursor fokus di input Search
6. Verifikasi placeholder input Search `Search asset name, code, category...`
### TC-FA-FAAM-353: Mengetik belum menyaring tabel dan icon clear muncul
7. Ketik `Dell` pada input Search tanpa menekan Enter
8. Verifikasi icon `(✕)` muncul di kanan input
9. Verifikasi tabel belum tersaring: baris `Ergonomic Chair` (tidak cocok dengan `Dell`) tetap tampil di tabel
### TC-FA-FAAM-354: Enter menjalankan pencarian
10. Pindah ke halaman 2 tabel
11. Tekan Enter pada input Search yang berisi `Dell`
12. Verifikasi sedikitnya satu baris tampil di tabel
13. Verifikasi tabel hanya menampilkan baris yang cocok dengan `Dell` (`Dell Latitude`)
14. Verifikasi halaman tabel reset ke halaman 1
### TC-FA-FAAM-355: Klik clear tidak mereset tabel sampai Enter pada input kosong
15. Klik `(✕)` pada input Search
16. Verifikasi input Search kosong
17. Verifikasi search bar tetap terbuka
18. Verifikasi input Search tetap fokus
19. Verifikasi tabel masih menampilkan hasil `Dell` (`Dell Latitude`)
20. Tekan Enter pada input Search yang kosong
21. Verifikasi tabel kembali menampilkan semua data: baris `Dell Latitude` dan `Ergonomic Chair` tampil
### TC-FA-FAAM-356: Collapse lewat panah kiri mengosongkan keyword dan langsung mereset tabel
22. Ketik Search `Dell`, tekan Enter
23. Klik icon panah `(←)` di kiri toolbar
24. Verifikasi search bar menutup menjadi icon Search
25. Verifikasi tabel langsung menampilkan semua data: baris `Dell Latitude` dan `Ergonomic Chair` tampil
26. Klik icon Search
27. Verifikasi keyword pada input Search kosong
### TC-FA-FAAM-357: Query di-trim saat Enter dan query hanya spasi mereset
28. Ganti isi kotak search dengan `  Dell  ` (spasi di awal dan akhir), tekan Enter
29. Verifikasi hasil sama dengan pencarian `Dell`: baris `Dell Latitude` tampil
30. Verifikasi isi search box tetap `  Dell  ` seperti yang diketik
31. Ganti isi kotak search dengan tiga spasi, tekan Enter
32. Verifikasi query hanya spasi diperlakukan kosong: tabel menampilkan semua data (baris `Dell Latitude` dan `Ergonomic Chair` tampil)
33. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Pindah ke halaman 2 tabel" sebelum Enter pada TC-FA-FAAM-354 agar reset ke halaman 1 pada TC-FA-FAAM-354 dapat teramati (S-14), langkah klik icon Search sebelum asersi keyword kosong pada TC-FA-FAAM-356, dan langkah klik `(←)` terakhir yang menutup Search.
- Verifikasi "baris `Ergonomic Chair` tetap tampil" pada TC-FA-FAAM-353 adalah cara spec mengamati Expected "tabel belum tersaring" (baris yang tidak cocok dengan `Dell` masih ada); `Ergonomic Chair` tampil di halaman 1 menurut urutan default Asset Name A-Z.
- Search diketik dan dikosongkan sesuai bagian 8b butir 9; urutan blok mengikuti urutan TC karena state Search satu blok menjadi precondition blok berikutnya (hasil `Dell` pada TC-FA-FAAM-354 dipakai TC-FA-FAAM-355).
- Temuan untuk QA: Expected TC-FA-FAAM-354 "halaman reset ke 1" tidak punya langkah menuju halaman lain di TC; spec menambah langkah pindah ke halaman 2 sebelum Enter sebagai penghubung.
