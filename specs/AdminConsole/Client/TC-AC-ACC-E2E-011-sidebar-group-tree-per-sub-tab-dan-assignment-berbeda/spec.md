---
id: TC-AC-ACC-E2E-011-sidebar-group-tree-per-sub-tab-dan-assignment-berbeda
title: "Sidebar Group Tree per Sub-tab bila Assignment Group Role Berbeda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-34
  - TC-AC-ACC-557
  - TC-AC-ACC-33
coverage:
  web: automated
---

# Sidebar Group Tree per Sub-tab bila Assignment Group Role Berbeda

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-GRP-1 | Active-Full + Archived-Read (Manage active client: C/R/U/D, exact-match Area Jakarta; Manage archived client: Read, exact-match Area Surabaya) | `activeFullJakartaArchivedReadSurabaya_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GRP1_PASSWORD` |

- Login di hook `before` spec ini (Active-Full + Archived-Read, A-GRP-1); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Assignment aktor A-GRP-1: Manage active client pada Area Jakarta (C/R/U/D) dan Manage archived client pada Area Surabaya (Read), berbeda per sub-tab (Tabel A3).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-34: Isi Sidebar dihitung ulang per sub-tab bila assignment Group Role berbeda

1. Klik ikon hierarchy toggle (expand all) di sub-tab `Active`, lalu amati tree
2. Verifikasi sub-tab `Active`: `Area Jakarta` aktif
3. Verifikasi sub-tab `Active`: `Regional Barat` greyed out (ancestor)
4. Verifikasi sub-tab `Active`: `Cabang Menteng`, `Cabang Bekasi`, `Cabang Kemang`, `Regional Timur`, `Area Surabaya`, dan `Cabang Rungkut` tidak muncul (hidden total)
5. Klik sub-tab `Archived`
6. Klik ikon hierarchy toggle (expand all) di sub-tab `Archived`, lalu amati tree
7. Verifikasi sub-tab `Archived`: `Area Surabaya` aktif
8. Verifikasi sub-tab `Archived`: `Regional Timur` greyed out (ancestor)
9. Verifikasi sub-tab `Archived`: `Regional Barat`, `Area Jakarta`, `Cabang Menteng`, `Cabang Bekasi`, `Cabang Kemang`, dan `Cabang Rungkut` tidak muncul (hidden total)

### TC-AC-ACC-557: Sidebar Group Tree sub-tab Suspended memakai scope Manage active client

10. Klik sub-tab `Active`
11. Amati tree Sidebar di sub-tab `Active`
12. Verifikasi node `Area Jakarta` aktif dan dapat diklik
13. Verifikasi `Regional Barat` greyed out
14. Verifikasi `Cabang Menteng`, `Regional Timur`, dan `Area Surabaya` tidak tampil
15. Klik sub-tab `Suspended`
16. Amati tree Sidebar
17. Verifikasi tree sama dengan sub-tab `Active`: `Area Jakarta` aktif, `Regional Barat` greyed out
18. Verifikasi `Area Surabaya` tidak tampil walau aktor memegang Read "Manage archived client" pada Area Surabaya
19. Ketik Search `PT Wahana Nusantara`, tekan Enter
20. Lihat baris tabel
21. Verifikasi baris `PT Wahana Nusantara` (Group `Area Jakarta`) tampil
22. Klik `(←)` pada kotak Search

### TC-AC-ACC-33: Pilihan node reset ke All Groups saat tidak valid di scope sub-tab baru

23. Klik sub-tab `Active`
24. Klik node `Area Jakarta`
25. Verifikasi node `Area Jakarta` aktif (highlight + teks bold)
26. Verifikasi `[All Groups]` tidak aktif
27. Klik sub-tab `Archived`
28. Verifikasi filter reset otomatis ke `[All Groups]` versi sub-tab `Archived` karena `Area Jakarta` tidak valid di scope `Archived`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 19, 22. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-34, 557, 33 (semula 33, 34, 557); TC-AC-ACC-33 di akhir karena mengubah pilihan node, sedangkan 34 dan 557 membaca tree saja.
- Pembagian TC lintas spec: screening tree Total Control dan interaksi dasar ada di spec 010; pola ancestor-disabled aktor Active-Read dan union multi-node di spec 033.
- Temuan untuk QA:
  - TC-AC-ACC-557: Expected butir a mengasersi tree sub-tab `Active` sebelum klik apa pun, tetapi langkah TC tidak membuka seluruh level tree (expand all); spec tidak meng-expand dan mengasersi node yang terlihat pada level awal sesuai langkah TC. `Cabang Menteng` bisa tersembunyi hanya karena collapse; asersi "tidak tampil" pada level collapse tidak membuktikan hidden total (penekanan perlu dari QA).
