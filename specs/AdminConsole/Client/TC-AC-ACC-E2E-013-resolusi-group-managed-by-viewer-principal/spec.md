---
id: TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal
title: "Resolusi Group dan Managed By pada List Client untuk Viewer Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-35
  - TC-AC-ACC-566
  - TC-AC-ACC-571
  - TC-AC-ACC-558
coverage:
  web: automated
---

# Resolusi Group dan Managed By pada List Client untuk Viewer Principal

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-ROL-4` `PT Mandiri Jaya` (Partner CV Mitra Mandiri tanpa Distributor induk, Group Partner `Cabang Bekasi`) dan Pre-setup `C-10` `PT Lintas Jaringan` (relasi CV Mitra Sejati ditetapkan lebih awal; CV Mitra Timur ditambahkan Principal via Change Partner setelahnya) hanya dibaca.
- Populasi node `Cabang Bekasi` tertutup (Active 2: `PT Mandiri Jaya`, `PT Mitra Pindah`; Tabel A3).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-35: Principal: Group Client mengikuti Group Distributor ancestor, Distributor-langsung ke Group Distributor, Direct ke Group Client

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Lihat kolom Group baris `PT Sejahtera Abadi`
3. Verifikasi Group `PT Sejahtera Abadi` (Partner CV Mitra Sejati) adalah `Area Jakarta` (Group Distributor induk)
4. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
5. Lihat kolom Group baris `PT Sinar Distributor`
6. Verifikasi Group `PT Sinar Distributor` (Distributor langsung) adalah `Area Jakarta` (Group Distributor)
7. Ganti isi kotak Search dengan `PT Baru Daftar`, tekan Enter
8. Lihat kolom Group baris `PT Baru Daftar`
9. Verifikasi Group `PT Baru Daftar` (Direct) adalah `Cabang Menteng` (Group Client langsung)

### TC-AC-ACC-566: Anchor global pada Client lintas jaringan: Principal melihat Anchor ter-awal dengan +1 more

10. Ganti isi kotak Search dengan `PT Lintas Jaringan`, tekan Enter
11. Lihat sel Managed By dan Group baris `PT Lintas Jaringan`
12. Verifikasi Managed By `PT Lintas Jaringan` adalah `CV Mitra Sejati` diikuti `+1 more`
13. Verifikasi Group `PT Lintas Jaringan` adalah `Area Jakarta`

### TC-AC-ACC-571: Principal: Group Client dengan Anchor Partner tanpa Distributor induk mengikuti Group Partner itu langsung

14. Ganti isi kotak Search dengan `PT Mandiri Jaya`, tekan Enter
15. Lihat sel Managed By dan Group baris `PT Mandiri Jaya`
16. Verifikasi Managed By `PT Mandiri Jaya` adalah `CV Mitra Mandiri`
17. Verifikasi Group `PT Mandiri Jaya` adalah `Cabang Bekasi`
18. Klik `(←)` pada kotak Search

### TC-AC-ACC-558: Klik node Group Partner tanpa Distributor induk memfilter Client Partner tersebut oleh Principal

19. Klik node `Cabang Bekasi` pada Sidebar Group Tree
20. Lihat baris tabel sub-tab `Active`
21. Verifikasi node `Cabang Bekasi` aktif (highlight + teks bold)
22. Verifikasi `[All Groups]` tidak aktif
23. Verifikasi tabel memuat `PT Mandiri Jaya` dengan Group `Cabang Bekasi`
24. Verifikasi `PT Sejahtera Abadi` dan `PT Baru Daftar` tidak tampil di tabel
25. Klik `[All Groups]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 4, 7, 10, 14, 18, 25. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Asersi absence TC-AC-ACC-558 memakai baris `PT Mandiri Jaya` yang tampil pada `Verifikasi` tepat sebelumnya sebagai anchor positif pada surface yang sama (bagian 8b butir 2).
- Pembagian TC lintas spec: resolusi untuk viewer Distributor di spec 015 dan 017, viewer Partner di spec 018 dan 019; perpindahan Group Distributor (TC-AC-ACC-38) di spec 014.
- Temuan untuk QA:
  - TC-AC-ACC-566: Expected tidak menyebut isi hover `+1 more`; spec mengasersi teks sel saja sesuai Expected.
  - TC-AC-ACC-558: klik node Group dan tabel `Active` memakai populasi node yang tertutup (Tabel A3); tidak ada temuan sumber lain.
