---
id: TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by
title: "Isi Sel Kolom List Client: Company Name, Managed By, Modified By, dan Kolom Opsional"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-9
  - TC-AC-ACC-10
  - TC-AC-ACC-16
  - TC-AC-ACC-17
  - TC-AC-ACC-929
coverage:
  web: automated
---

# Isi Sel Kolom List Client: Company Name, Managed By, Modified By, dan Kolom Opsional

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-W3LST-1` `PT Arsip Sistem Uji` (Modified By `System`, Last Updated 08 Jul 2026), `C-W3LST-2` `PT Arsip Manusia Uji` (Modified By `Citra Dewi`, Last Updated 02 Jul 2026), dan `C-W3LST-3` `PT Tiga Mitra Uji` (relasi CV Mitra Sejati 2026-01-05, CV Mitra Mandiri 2026-02-10, CV Mitra Lestari 2026-03-15) hanya dibaca.
- Modified By `PT Sejahtera Abadi` = `Andi Wijaya` (aktor terakhir pada seed Pre-setup).
- General Settings tenant: format tanggal-waktu mengikuti nilai General Settings (Date Format, Time Format, Time Zone) yang berlaku; spec tidak mengubahnya.
- State Column Visibility yang dicentang spec dipulihkan dalam spec; tidak ada Setup Column yang disimpan.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-9: Kolom Company Name berupa link dan badge Derived

1. Ketik Search `PT Maju Bersama`, tekan Enter
2. Verifikasi baris `PT Maju Bersama` menampilkan badge `Derived` (outlined, severity primary)
3. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
4. Verifikasi baris `PT Sejahtera Abadi` tanpa badge `Derived`
5. Verifikasi link Company Name `PT Sejahtera Abadi` berwarna default netral
6. Arahkan kursor ke link Company Name `PT Sejahtera Abadi`
7. Verifikasi link berwarna primary saat hover
8. Verifikasi teks nama tidak dipotong
9. Verifikasi tidak ada tooltip pada nama
10. Klik Company Name `PT Sejahtera Abadi`
11. Verifikasi Admin Console > Client > Detail milik `PT Sejahtera Abadi` terbuka
12. Kembali ke List dengan tombol Back browser

### TC-AC-ACC-10: Kolom Managed By: Anchor pertama, +N more, hover daftar manager, suffix (Direct), dan Direct

13. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
14. Lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
15. Verifikasi sel Managed By `PT Sejahtera Abadi` menampilkan `CV Mitra Sejati` tanpa teks `+N more`
16. Verifikasi hover pada sel tidak menampilkan daftar manager
17. Ganti isi kotak Search dengan `PT Teknologi Maju`, tekan Enter
18. Lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
19. Verifikasi sel Managed By `PT Teknologi Maju` menampilkan `CV Mitra Sejati` diikuti `+1 more`
20. Verifikasi hover menampilkan daftar manager berurutan: `CV Mitra Sejati` (Anchor), lalu `CV Mitra Lestari`
21. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
22. Lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
23. Verifikasi sel Managed By `PT Sinar Distributor` menampilkan `PT Distribusi Nusantara (Direct)`
24. Verifikasi hover pada sel tidak menampilkan daftar manager
25. Ganti isi kotak Search dengan `PT Baru Daftar`, tekan Enter
26. Lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
27. Verifikasi sel Managed By `PT Baru Daftar` menampilkan `Direct`
28. Verifikasi hover pada sel tidak menampilkan daftar manager
29. Ganti isi kotak Search dengan `PT Tiga Mitra Uji`, tekan Enter
30. Lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
31. Verifikasi sel Managed By `PT Tiga Mitra Uji` menampilkan `CV Mitra Sejati` diikuti `+2 more`
32. Verifikasi hover menampilkan daftar manager berurutan: `CV Mitra Sejati` (Anchor), lalu `CV Mitra Lestari` dan `CV Mitra Mandiri` (sisanya A-Z, bukan urutan penetapan relasi)
33. Klik `(←)` pada kotak Search

### TC-AC-ACC-16: Kolom Modified By dan Last Updated

34. Ketik Search `PT Sejahtera Abadi`, tekan Enter
35. Lihat sel Modified By dan Last Updated pada baris `PT Sejahtera Abadi`
36. Verifikasi Modified By berupa teks biasa (bukan badge) `Andi W`
37. Arahkan kursor ke nama Modified By
38. Verifikasi hover menampilkan `Andi Wijaya`
39. Verifikasi Last Updated berupa tanggal-waktu mengikuti format General Settings

### TC-AC-ACC-17: Kolom Hidden opsional menampilkan "—" bila kosong, kolom wajib tidak pernah kosong

40. Klik Column Visibility `(⋯)`, centang `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City`
41. Verifikasi kolom `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City` tampil di tabel
42. Ganti isi kotak Search dengan `PT Baru Daftar`, tekan Enter
43. Lihat baris `PT Baru Daftar`
44. Verifikasi sel opsional `Company Email`, `PIC Phone`, dan `Industry` yang tanpa nilai pada baris `PT Baru Daftar` menampilkan `—`
45. Verifikasi kolom wajib `PIC Email`, `Country`, `State`, dan `City` pada baris `PT Baru Daftar` berisi nilai dan tidak menampilkan `—`
46. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
47. Verifikasi kolom wajib `PIC Email`, `Country`, `State`, dan `City` pada baris `PT Sejahtera Abadi` berisi nilai dan tidak menampilkan `—`
48. Verifikasi sel opsional yang berisi pada baris `PT Sejahtera Abadi` menampilkan nilainya
49. Klik Column Visibility `(⋯)`, hapus centang `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City`, lalu tutup overlay
50. Klik `(←)` pada kotak Search

### TC-AC-ACC-929: Modified By aktor sistem tampil System dan Last Updated sesuai seed

51. Klik sub-tab `Archived`
52. Klik ikon Search, ketik Search `PT Arsip Sistem Uji`, tekan Enter
53. Lihat sel Modified By dan Last Updated
54. Verifikasi Modified By `PT Arsip Sistem Uji` berupa teks biasa `System` (bukan format nama orang)
55. Verifikasi Last Updated memuat tanggal 08 Jul 2026
56. Ganti isi kotak Search dengan `PT Arsip Manusia Uji`, tekan Enter
57. Lihat sel Modified By dan Last Updated
58. Verifikasi Modified By `PT Arsip Manusia Uji` adalah `Citra D`
59. Verifikasi Last Updated memuat tanggal 02 Jul 2026
60. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 3, 12, 33, 34, 42, 46, 49, 50, 60. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: badge produk (FAMS, SAMS, SIEM) ada di spec 004 dan 005; Group di spec 006 (badge Group dan truncate) dan 013, 015, 018 (resolusi per viewer); PIC Name panjang di spec 007.
- TC-AC-ACC-10 diulang per baris Client: langkah 'Ganti isi kotak Search' dan 'Lihat sel Managed By' memakai Search nama sebagai satu-satunya cara memilih baris target karena populasi List berpaginasi.
- Ukuran spec (60 langkah, melewati sekitar 35 langkah): satu dataset (kolom List Client), tanpa aksi tulis; langkah TC-AC-ACC-10 mengulang pola Search, amati sel, hover untuk lima Client dengan parameter tertera tiap langkah, dan tiap blok TC berdiri sendiri (Search diganti di awal blok) sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-AC-ACC-16: format tanggal-waktu "mengikuti format General Settings" tidak menyebut nilai Date Format, Time Format, dan Time Zone yang diharapkan; spec mengasersi kesesuaian dengan General Settings tenant tanpa menebak nilainya.
  - TC-AC-ACC-17: Expected "sel berisi tampil nilainya" tidak menyebut nilai Company Email, PIC Phone, atau Industry Client mana pun pada Tabel A2; spec hanya mengasersi sel yang berisi menampilkan nilai (tidak kosong) pada baris `PT Sejahtera Abadi`. Client `PT Baru Daftar` diasumsikan tanpa Company Email, PIC Phone, dan Industry sesuai precondition d.
  - TC-AC-ACC-9: Expected butir b (link default netral, hover primary) tidak menyebut token warna; spec mengasersi state netral dan primary saja.
