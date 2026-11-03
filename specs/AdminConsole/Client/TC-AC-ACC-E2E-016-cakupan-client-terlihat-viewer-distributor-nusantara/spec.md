---
id: TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara
title: "Cakupan Client yang Terlihat Distributor PT Distribusi Nusantara pada List dan Detail"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-58
  - TC-AC-ACC-574
  - TC-AC-ACC-575
  - TC-AC-ACC-576
  - TC-AC-ACC-950
  - TC-AC-ACC-451
coverage:
  web: automated
---

# Cakupan Client yang Terlihat Distributor PT Distribusi Nusantara pada List dan Detail

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-13 | Distributor Total Control (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |

- Login di hook `before` spec ini (Distributor Total Control, A-13); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen: `C-ROL-10` `PT Hanya Relasi Beku` (satu-satunya relasi Partner CV Mitra Beku, Suspended), `C-ROL-14` `PT Mitra Pindah` (relasi CV Mitra Sejati Transferred, CV Mitra Mandiri aktif; dipakai sebagai Client dengan relasi Transferred untuk TC-AC-ACC-58 karena precondition d tidak menyebut Client-nya), `C-ROL-13` `PT Direct Jakarta`, `C-ROL-5` `PT Suspend Menteng`, `C-ROL-6` `PT Arsip Menteng`, dan Pre-setup `C-14` `PT Uji Halaman 01…30` (Direct, Group Regional Timur) hanya dibaca.
- ID Client `PT Timur Perkasa` (C-12) untuk URL Detail (UUID opaque) diambil dari keluaran skrip seed atau respons API; kemampuan itu disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-58: Distributor melihat Client sesuai jaringannya; relasi Transferred tidak tampil

1. Lihat daftar Client sub-tab `Active`
2. Ketik Search `PT Sejahtera Abadi`, tekan Enter
3. Verifikasi Client Partner P1 `PT Sejahtera Abadi` tampil
4. Ganti isi kotak Search dengan `PT Teknologi Maju`, tekan Enter
5. Verifikasi Client Partner P1/P2 `PT Teknologi Maju` tampil
6. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
7. Verifikasi `PT Sinar Distributor` (relasi langsung) tampil
8. Ganti isi kotak Search dengan `PT Timur Perkasa`, tekan Enter
9. Verifikasi `PT Timur Perkasa` (jaringan lain) tidak tampil: empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`
10. Ganti isi kotak Search dengan `PT Mitra Pindah`, tekan Enter
11. Verifikasi Client dengan relasi Transferred `PT Mitra Pindah` tidak tampil: empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`

### TC-AC-ACC-576: Distributor tidak melihat Client yang hanya memiliki relasi Transferred di jaringannya

12. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
13. Verifikasi baris `PT Sejahtera Abadi` tampil
14. Ganti isi kotak Search dengan `PT Mitra Pindah`, tekan Enter
15. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`

### TC-AC-ACC-574: Distributor tidak melihat Client Direct dengan Group di luar tree Distributor

16. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
17. Verifikasi baris `PT Sejahtera Abadi` tampil
18. Ganti isi kotak Search dengan `PT Uji Halaman`, tekan Enter
19. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (Client Direct `PT Uji Halaman` ber-Group `Regional Timur`)

### TC-AC-ACC-575: Distributor tetap melihat Client dengan relasi berstatus Suspended

20. Ganti isi kotak Search dengan `PT Hanya Relasi Beku`, tekan Enter
21. Lihat baris `PT Hanya Relasi Beku` di sub-tab `Active`
22. Verifikasi baris `PT Hanya Relasi Beku` tampil di sub-tab `Active`
23. Verifikasi Managed By `PT Hanya Relasi Beku` adalah `CV Mitra Beku`
24. Verifikasi Group `PT Hanya Relasi Beku` adalah `Cabang Kemang`

### TC-AC-ACC-950: Distributor tidak melihat Client Direct yang Group-nya descendant dari Group Distributor (exact-match, bukan subtree)

25. Ganti isi kotak Search dengan `PT Direct Jakarta`, tekan Enter
26. Verifikasi baris `PT Direct Jakarta` (Group `Area Jakarta`, node Group Distributor) tampil di sub-tab `Active`
27. Klik sub-tab `Suspended`, ketik Search `PT Wahana Nusantara`, tekan Enter
28. Verifikasi baris `PT Wahana Nusantara` tampil di sub-tab `Suspended`
29. Ganti isi kotak Search dengan `PT Suspend Menteng`, tekan Enter
30. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Suspend Menteng` ber-Group `Cabang Menteng`, descendant Group Distributor)
31. Klik sub-tab `Archived`, ketik Search `PT Karya Abadi`, tekan Enter
32. Verifikasi baris `PT Karya Abadi` tampil di sub-tab `Archived`
33. Ganti isi kotak Search dengan `PT Arsip Menteng`, tekan Enter
34. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Arsip Menteng` ber-Group `Cabang Menteng`, descendant Group Distributor)
35. Klik `(←)` pada kotak Search dan klik sub-tab `Active`

### TC-AC-ACC-451: Distributor membuka Detail Client di luar jaringannya: diperlakukan seperti tidak ada

36. Buka URL Detail dengan ID Client `PT Timur Perkasa` (jaringan PT Distribusi Timur) langsung
37. Verifikasi toast netral `This client is no longer available.`
38. Verifikasi halaman kembali ke List
39. Verifikasi data `PT Timur Perkasa` tidak tampil dan tidak ada petunjuk bahwa Client berada di luar jaringan

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 4, 6, 12, 16, 20, 25, 35. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: TC-AC-ACC-58 dan 576 mengasersi hal yang sama untuk `PT Mitra Pindah` (relasi Transferred); keduanya ditulis lengkap karena tiap TC tepat satu spec dan langkah dependensi disalin utuh (S-04).
- Asersi absence di empty state `No results found` memakai baris yang tampil pada `Verifikasi` sebelumnya di sub-tab dan akun yang sama sebagai anchor positif (bagian 8b butir 2); khusus TC-AC-ACC-58 anchor ada pada tiga baris `PT Sejahtera Abadi`, `PT Teknologi Maju`, dan `PT Sinar Distributor`.
- Dua verifikasi empty state memakai Search sebagai cara mengamati "tidak tampil" (TC-AC-ACC-58 langkah 2 hanya berbunyi "Cari 'PT Timur Perkasa' dan Client Transferred").
- Ukuran spec (39 langkah, melewati sekitar 35 langkah): satu akun (Distributor PT Distribusi Nusantara), satu dataset (cakupan List), tanpa aksi tulis, dan tiap blok TC memulai dari Search eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap pasangan anchor dan absence menjadi dua `Verifikasi` (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACC-58: precondition d ("Satu Client dengan relasi Partner berstatus Transferred pada jaringan Distributor") tidak menyebut nama Client; spec memakai `C-ROL-14` `PT Mitra Pindah` (satu-satunya Client A3 dengan relasi Transferred di jaringan D1) dan menandai asumsi ini ke QA.
  - TC-AC-ACC-58 dan 576 menguji skenario yang sama (relasi Transferred tidak tampil) dengan Client yang sama; QA dapat mempertimbangkan penggabungan.
  - TC-AC-ACC-451: Expected "lalu kembali ke List" tidak menyebut sub-tab yang dituju; spec hanya mengasersi halaman List tampil.
