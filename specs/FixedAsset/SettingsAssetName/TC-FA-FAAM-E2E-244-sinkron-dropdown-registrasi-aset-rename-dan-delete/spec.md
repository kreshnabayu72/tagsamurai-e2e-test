---
id: TC-FA-FAAM-E2E-244-sinkron-dropdown-registrasi-aset-rename-dan-delete
title: "Sinkron Registrasi Aset: Rename Asset Name Terlihat di Dropdown dan Policy, Asset Name Dihapus Hilang dari Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-739
  - TC-FA-FAAM-740
coverage:
  web: automated
---

# Sinkron Registrasi Aset: Rename Asset Name Terlihat di Dropdown dan Policy, Asset Name Dihapus Hilang dari Dropdown

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor kedua (ganti akun eksplisit di langkah 6 dan 13): Manage Asset & TAG `manageAssetTag_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 9b; `Spectra.env.FA_MAT_PASSWORD`, nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo). TC-FA-FAAM-740 butir d menyebut akun ini sebagai akun penguji dropdown Registrasi Aset.
- Env var: `FA_TC_PASSWORD`, `FA_MAT_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 10 (`Dell Latitude`, dipakai sebagai opsi pembanding di dropdown), No. 9b.
- Data Dinamis, di-seed lewat API di hook `before` sebagai salinan fixture 13 (Total Asset 0), nama bersuffix `{runId}-244`:
  - `Warehouse Pallet 740 {runId}-244` (Code `PLT-WH740`; Tabel Data Uji Dinamis No. 101); diubah nama menjadi `Warehouse Pallet 740 {runId}-244 Baru` oleh TC-FA-FAAM-740.
  - `Warehouse Pallet 739 {runId}-244` (Code `PLT-WH739`; Tabel Dinamis No. 100); dihapus oleh TC-FA-FAAM-739.
- Kemampuan teknis: pembukaan Registrasi Aset (dropdown Asset Name, `[+ Quick Register]`) dan FAMS > Settings > Asset Transactional Policy.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Warehouse Pallet 740 {runId}-244 Baru` dan sisa seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-739 dan 740: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-740: Rename Asset Name langsung terlihat di dropdown dan kolom Asset Name Asset Transactional Policy

1. Ketik Search `Warehouse Pallet 740 {runId}-244`, tekan Enter
2. Klik `⋯` baris `Warehouse Pallet 740 {runId}-244` lalu `Edit`
3. Ubah Asset Name menjadi `Warehouse Pallet 740 {runId}-244 Baru`
4. Klik `[Save]`
5. Tunggu aksi selesai
6. Logout lalu login sebagai Manage Asset & TAG
7. Buka Fixed Asset > Assets > Registration
8. Klik `[+ Quick Register]`
9. Buka dropdown Asset Name
10. Ketik di kotak dropdown `Warehouse Pallet 740 {runId}-244`
11. Verifikasi dropdown memuat `Warehouse Pallet 740 {runId}-244 Baru`
12. Verifikasi dropdown tidak memuat `Warehouse Pallet 740 {runId}-244` dengan nama lama
13. Logout lalu login sebagai Total Control
14. Buka FAMS > Settings > Asset Transactional Policy
15. Ketik Search `Warehouse Pallet 740 {runId}-244`, tekan Enter
16. Verifikasi tabel memuat baris `Warehouse Pallet 740 {runId}-244 Baru`
17. Verifikasi tabel tidak memuat baris `Warehouse Pallet 740 {runId}-244` dengan nama lama

### TC-FA-FAAM-739: Asset Name yang dihapus hilang dari dropdown Asset Name Registrasi Aset

18. Buka Fixed Asset > Settings > Asset Master > Asset Name
19. Buka Registrasi Aset
20. Buka dropdown Asset Name
21. Ketik di kotak dropdown `Warehouse Pallet 739 {runId}-244`
22. Verifikasi `Warehouse Pallet 739 {runId}-244` ada di dropdown
23. Buka Fixed Asset > Settings > Asset Master > Asset Name
24. Ketik Search `Warehouse Pallet 739 {runId}-244`, tekan Enter
25. Klik `⋯` baris `Warehouse Pallet 739 {runId}-244` lalu `Delete`
26. Klik `[Delete]`
27. Buka Registrasi Aset
28. Buka dropdown Asset Name
29. Verifikasi opsi `Dell Latitude` tampil di dropdown
30. Ketik di kotak dropdown `Warehouse Pallet 739 {runId}-244`
31. Verifikasi `Warehouse Pallet 739 {runId}-244` tidak ada di dropdown

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 15, 24 (Search tabel), langkah 5 (menunggu Save selesai sebelum ganti akun), langkah 7, 14, 18, 19, 23, 27 (navigasi), langkah 10, 21, 30 (mengetik di kotak pencarian dropdown), dan langkah 8, 9, 20, 28 (membuka dropdown).
- Ganti akun eksplisit di langkah 6 dan 13 (S-07); sesi dikembalikan ke akun default suite di hook `after`.
- Urutan TC: TC-FA-FAAM-740 sebelum TC-FA-FAAM-739 (aksi menghapus data di akhir; S-10).
- Langkah 12, 17, 31 adalah asersi absence atas opsi dropdown atau baris tabel dengan anchor positif langkah 11, 16, 29 pada surface yang sama (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-FAAM-598 dan 599 ada di spec 222; TC-FA-FAAM-675 di spec 243.
- Temuan untuk QA:
  - TC-FA-FAAM-740 menyebut `#9` dan `#9b` tidak jelas pada kolom ACC indeks (`#9` adalah Import Data); spec memakai `#9b` (Manage Asset & TAG) sesuai langkah TC.
  - TC-FA-FAAM-740 menulis `Warehouse Pallet 740` sebagai kata pencarian nama lama; hasil pencarian juga mencocokkan nama baru karena nama lama adalah awalan nama baru, sehingga asersi nama lama memeriksa kecocokan persis.
