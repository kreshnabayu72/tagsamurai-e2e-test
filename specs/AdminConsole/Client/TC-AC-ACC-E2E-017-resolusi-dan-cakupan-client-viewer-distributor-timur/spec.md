---
id: TC-AC-ACC-E2E-017-resolusi-dan-cakupan-client-viewer-distributor-timur
title: "Anchor, Group, dan Cakupan Client untuk Viewer Distributor PT Distribusi Timur"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-567
  - TC-AC-ACC-928
  - TC-AC-ACC-573
coverage:
  web: automated
---

# Anchor, Group, dan Cakupan Client untuk Viewer Distributor PT Distribusi Timur

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-ROL-1 | Distributor Total Control (PT Distribusi Timur) | `totalControlDistributorTimur_automated_ptDistribusiTimur@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TIMUR_TC_PASSWORD` |

- Login di hook `before` spec ini (Distributor Total Control, A-ROL-1); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-10` `PT Lintas Jaringan` (relasi CV Mitra Sejati dari jaringan PT Distribusi Nusantara lebih awal dari CV Mitra Timur jaringan PT Distribusi Timur; Group Partner CV Mitra Timur `Cabang Rungkut`) dan fixture A3 residen `C-ROL-13` `PT Direct Jakarta` hanya dibaca.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-567: Anchor per viewer: Distributor jaringan lain melihat Anchor miliknya sendiri

1. Ketik Search `PT Lintas Jaringan`, tekan Enter
2. Lihat sel Managed By dan Group baris `PT Lintas Jaringan`
3. Verifikasi Managed By `PT Lintas Jaringan` diawali `CV Mitra Timur`
4. Verifikasi Managed By `PT Lintas Jaringan` tidak memuat `CV Mitra Sejati`
5. Verifikasi Group `PT Lintas Jaringan` adalah `Cabang Rungkut` (Group Partner CV Mitra Timur)

### TC-AC-ACC-928: Managed By per viewer: Distributor lain melihat Anchor dalam jaringannya sendiri tanpa +N more

6. Ganti isi kotak Search dengan `PT Lintas Jaringan`, tekan Enter
7. Lihat sel Managed By baris `PT Lintas Jaringan`
8. Verifikasi sel Managed By `PT Lintas Jaringan` adalah `CV Mitra Timur` tanpa teks `+N more`
9. Verifikasi teks `CV Mitra Sejati` tidak tampil pada sel Managed By baris `PT Lintas Jaringan`

### TC-AC-ACC-573: Distributor lain tidak melihat Client Direct yang Group-nya milik Distributor berbeda

10. Ganti isi kotak Search dengan `PT Timur Perkasa`, tekan Enter
11. Verifikasi baris `PT Timur Perkasa` tampil
12. Ganti isi kotak Search dengan `PT Direct Jakarta`, tekan Enter
13. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
14. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 14. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-567, 928, 573 (semula 567, 573, 928); asersi positif atas Managed By dikelompokkan sebelum asersi cakupan.
- Pembagian TC lintas spec: viewer Principal, Distributor PT Distribusi Nusantara, dan Partner ada di spec 013, 015, 016, 018, dan 019.
- Temuan untuk QA:
  - TC-AC-ACC-567 dan 928 menguji skenario yang sama (viewer Distributor PT Distribusi Timur atas `PT Lintas Jaringan`) dengan Expected yang saling melengkapi; QA dapat mempertimbangkan penggabungan.
