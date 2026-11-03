---
id: TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati
title: "Resolusi Group dan Cakupan Client untuk Viewer Partner CV Mitra Sejati"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-37
  - TC-AC-ACC-560
  - TC-AC-ACC-59
  - TC-AC-ACC-909
coverage:
  web: automated
---

# Resolusi Group dan Cakupan Client untuk Viewer Partner CV Mitra Sejati

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-14 | Partner Total Control (CV Mitra Sejati) | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |

- Login di hook `before` spec ini (Partner Total Control, A-14); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen: `C-ROL-15` `PT Dibuat Mitra` (dibuat CV Mitra Sejati dengan Group `Cabang Menteng` dipilih Partner), `C-ROL-8` `PT Ubah Mitra 01` (dibuat Principal dengan CV Mitra Sejati terpilih, Group tidak di-assign Partner), Pre-setup `C-13` `PT Ganti Mitra`, dan `C-ROL-4` `PT Mandiri Jaya` hanya dibaca.
- ID Client `PT Timur Perkasa` (C-12) untuk URL Detail (UUID opaque) diambil dari keluaran skrip seed atau respons API; kemampuan itu disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-37: Partner: Group tampil bila di-assign Partner sendiri, "—" bila Group tidak di-assign Partner itu

1. Ketik Search `PT Dibuat Mitra`, tekan Enter
2. Lihat sel Group baris `PT Dibuat Mitra`
3. Verifikasi Group `PT Dibuat Mitra` adalah `Cabang Menteng` (Group yang di-assign Partner itu sendiri)
4. Ganti isi kotak Search dengan `PT Ganti Mitra`, tekan Enter
5. Lihat sel Group baris `PT Ganti Mitra`
6. Verifikasi Group `PT Ganti Mitra` adalah `—` (Group tidak di-assign Partner itu)
7. Klik `(←)` pada kotak Search

### TC-AC-ACC-560: Klik node Group memfilter Client yang Group-nya di-assign Partner itu sendiri

8. Klik node `Cabang Menteng` pada Sidebar Group Tree
9. Lihat baris tabel sub-tab `Active`
10. Verifikasi node `Cabang Menteng` aktif
11. Verifikasi `[All Groups]` tidak aktif
12. Verifikasi tabel memuat `PT Dibuat Mitra` dengan Group `Cabang Menteng`
13. Verifikasi `PT Ubah Mitra 01` tidak tampil di tabel
14. Klik `[All Groups]`

### TC-AC-ACC-59: Partner hanya melihat Client yang berelasi langsung dengannya

15. Lihat daftar Client sub-tab `Active`
16. Ketik Search `PT Sejahtera Abadi`, tekan Enter
17. Verifikasi Client berelasi CV Mitra Sejati `PT Sejahtera Abadi` tampil
18. Ganti isi kotak Search dengan `PT Mandiri Jaya`, tekan Enter
19. Verifikasi Client Partner lain `PT Mandiri Jaya` tidak tampil: empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`
20. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
21. Verifikasi `PT Sinar Distributor` tidak tampil: empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`
22. Klik `(←)` pada kotak Search

### TC-AC-ACC-909: Partner membuka Detail Client di luar relasinya: diperlakukan seperti tidak ada

23. Buka URL Detail dengan ID Client `PT Timur Perkasa` (relasi Partner CV Mitra Timur) langsung
24. Verifikasi toast netral `This client is no longer available.`
25. Verifikasi halaman kembali ke List
26. Verifikasi data `PT Timur Perkasa` tidak tampil dan tidak ada petunjuk bahwa Client berada di luar relasi Partner

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 4, 7, 14, 16, 22. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-37, 560, 59, 909 (semula 37, 59, 560, 909); TC-AC-ACC-560 mengubah pilihan node dan dipulihkan sebelum 59.
- TC-AC-ACC-59 langkah 1 hanya berbunyi "Lihat daftar Client sub-tab Active"; cara mengamati "Client Partner lain dan PT Sinar Distributor tidak tampil" memakai Search nama (langkah penghubung) dengan baris `PT Sejahtera Abadi` sebagai anchor positif.
- Pembagian TC lintas spec: viewer Principal, Distributor, dan Partner CV Mitra Timur ada di spec 013, 015, 016, 017, dan 019.
- Temuan untuk QA:
  - TC-AC-ACC-59: Expected "Client Partner lain ... tidak tampil" tidak menyebut Client Partner lain yang dipakai; spec memakai `PT Mandiri Jaya` (Partner CV Mitra Mandiri) dan `PT Sinar Distributor`.
