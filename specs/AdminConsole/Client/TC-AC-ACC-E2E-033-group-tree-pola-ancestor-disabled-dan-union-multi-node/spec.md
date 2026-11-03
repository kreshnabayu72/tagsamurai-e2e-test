---
id: TC-AC-ACC-E2E-033-group-tree-pola-ancestor-disabled-dan-union-multi-node
title: "Sidebar Group Tree: Pola Ancestor-disabled dan All Groups sebagai Union Node Assignment"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-62
  - TC-AC-ACC-63
coverage:
  web: automated
---

# Sidebar Group Tree: Pola Ancestor-disabled dan All Groups sebagai Union Node Assignment

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-04 | Active-Read (Manage active client: Read, exact-match Area Jakarta) | `activeReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_READ_PASSWORD` |
| A-GRP-2 | Active-Read Multi-node (Manage active client: Read, exact-match Cabang Menteng dan Area Surabaya) | `activeReadMultiNode_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GRP2_PASSWORD` |

- Login di hook `before` spec ini (Active-Read, A-04); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-ROL-7` `PT Regional Barat` (Direct, Group `Regional Barat`) dan Pre-setup `C-01`, `C-09`, `C-12` hanya dibaca. Assignment A-04 hanya pada `Area Jakarta` (3 level: `Regional Barat` > `Area Jakarta` > `Cabang Menteng`); assignment A-GRP-2 pada `Cabang Menteng` dan `Area Surabaya`.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-62: Pola ancestor-disabled: ancestor greyed out, descendant hidden untuk Group Role exact-match

1. Klik ikon hierarchy toggle (expand all), lalu lihat Sidebar Group Tree
2. Verifikasi `Regional Barat` greyed out (tidak bisa diklik)
3. Verifikasi `Area Jakarta` aktif
4. Verifikasi `Cabang Menteng`, `Cabang Bekasi`, `Cabang Kemang`, `Regional Timur`, `Area Surabaya`, dan `Cabang Rungkut` tidak muncul
5. Klik node `Regional Barat`
6. Verifikasi klik `Regional Barat` tidak mengubah filter: `[All Groups]` tetap aktif
7. Ketik Search `PT Sejahtera Abadi`, tekan Enter
8. Verifikasi baris `PT Sejahtera Abadi` (Group `Area Jakarta`) tampil
9. Ganti isi kotak Search dengan `PT Baru Daftar`, tekan Enter
10. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Baru Daftar`, Group `Cabang Menteng`, descendant, tidak tampil)
11. Ganti isi kotak Search dengan `PT Regional Barat`, tekan Enter
12. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Regional Barat`, Group `Regional Barat`, ancestor, tidak tampil)
13. Klik `(←)` pada kotak Search
14. Logout dari akun Active-Read
15. Login sebagai Active-Read Multi-node (A-GRP-2)

### TC-AC-ACC-63: [All Groups] = union node yang di-assign tanpa ancestor greyed out

16. Lihat Sidebar Group Tree dengan `[All Groups]` terpilih
17. Verifikasi `[All Groups]` aktif
18. Ketik Search `PT Baru Daftar`, tekan Enter
19. Verifikasi baris `PT Baru Daftar` (Group `Cabang Menteng`) tampil
20. Ganti isi kotak Search dengan `PT Timur Perkasa`, tekan Enter
21. Verifikasi baris `PT Timur Perkasa` (Group `Area Surabaya`) tampil
22. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
23. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Sejahtera Abadi`, Group `Area Jakarta`, ancestor `Cabang Menteng`, tidak tampil)
24. Ganti isi kotak Search dengan `PT Regional Barat`, tekan Enter
25. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Regional Barat`, Group `Regional Barat`, ancestor, tidak tampil)
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 13 sampai 15, 26. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Spec Role Matrix per blok role (bagian 3a): ganti akun menuntut Step eksplisit; login akun pertama (Active-Read, A-04) dilakukan hook `before`.
- TC-AC-ACC-62 langkah 1 menyebut membuka seluruh level tree; TC-AC-ACC-63 langkah 1 hanya "Lihat Sidebar Group Tree" sehingga tree tidak di-expand.
- Pembagian TC lintas spec: tree per sub-tab (TC-AC-ACC-33, 34, 557) ada di spec 011; Group Manager (scope descendant) di spec 032.
- Temuan untuk QA:
  - TC-AC-ACC-63 Expected butir a ("[All Groups] aktif") dan butir b sampai e memakai Client A3 `PT Regional Barat` pada precondition e; tidak ada temuan sumber lain.
