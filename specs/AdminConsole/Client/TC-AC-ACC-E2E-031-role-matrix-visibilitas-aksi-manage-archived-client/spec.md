---
id: TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client
title: "Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Archived Client (Read, Update, Delete)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-53
  - TC-AC-ACC-583
  - TC-AC-ACC-54
  - TC-AC-ACC-55
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Archived Client (Read, Update, Delete)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-08 | Archived-Read (Manage archived client: Read, exact-match Area Jakarta) | `archivedReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_READ_PASSWORD` |
| A-09 | Archived-Update-Only (Manage archived client: Update + Read, exact-match Area Jakarta) | `archivedUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_UPDATE_PASSWORD` |
| A-10 | Archived-Delete-Only (Manage archived client: Delete + Read, exact-match Area Jakarta) | `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_DELETE_PASSWORD` |

- Login di hook `before` spec ini (Archived-Read, A-08); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-04` `PT Karya Abadi` (Archived, Group `Area Jakarta`) hanya dibaca; Download dan Changelog pada blok Archived-Read hanya dibuka lalu ditutup.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-53: Manage archived client Read-only

1. Lihat sub-tab, buka `⋯` baris pada sub-tab `Archived`
2. Verifikasi hanya sub-tab `Archived` tersedia dan terpilih awal
3. Verifikasi sub-tab `Active` dan `Suspended` Hidden dan badge jumlahnya tidak tampil
4. Verifikasi kolom Checkbox Hidden
5. Verifikasi `[+ New Client]` Hidden
6. Ketik Search `PT Karya Abadi`, tekan Enter
7. Buka `⋯` baris `PT Karya Abadi`
8. Verifikasi menu `⋯` hanya memuat `Detail`
9. Tutup menu `⋯`

### TC-AC-ACC-583: Manage archived client Read-only: Download dan Changelog List tampil, [+ New Client] tidak ada

10. Lihat Table Tools di sub-tab `Archived`
11. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog` tampil
12. Verifikasi `[+ New Client]` tidak ada
13. Klik `Download`
14. Verifikasi overlay Download menampilkan opsi `Download as CSV` dan `Download as XLSX`
15. Tutup overlay Download
16. Klik `Changelog`
17. Verifikasi modal dengan Title `Changelog: Client` terbuka
18. Tutup modal Changelog dan klik `(←)` pada kotak Search
19. Logout dari akun Archived-Read
20. Login sebagai Archived-Update-Only (A-09)

### TC-AC-ACC-54: Manage archived client Update-Only

21. Lihat sub-tab List
22. Verifikasi hanya sub-tab `Archived` tampil dan terpilih awal
23. Verifikasi sub-tab `Active` dan `Suspended` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
24. Ketik Search `PT Karya Abadi`, tekan Enter
25. Buka `⋯` baris `PT Karya Abadi` di sub-tab `Archived`
26. Verifikasi menu `⋯` memuat `Detail` dan `Edit`
27. Verifikasi `Delete`, `Suspend`, dan `Change Partner` Hidden
28. Verifikasi Checkbox dan `[+ New Client]` Hidden
29. Tutup menu `⋯`, klik `(←)` pada kotak Search, lalu Logout dari akun Archived-Update-Only
30. Login sebagai Archived-Delete-Only (A-10)

### TC-AC-ACC-55: Manage archived client Delete-Only

31. Lihat sub-tab List
32. Verifikasi hanya sub-tab `Archived` tampil dan terpilih awal
33. Verifikasi sub-tab `Active` dan `Suspended` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
34. Ketik Search `PT Karya Abadi`, tekan Enter
35. Buka `⋯` baris `PT Karya Abadi` di sub-tab `Archived`
36. Verifikasi menu `⋯` memuat `Detail` dan `Delete`
37. Verifikasi `Edit` Hidden
38. Tutup menu `⋯` dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6, 9, 18 sampai 20, 24, 29, 30, 34, 38. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Spec Role Matrix per blok role (bagian 3a): langkah tiap role berbeda dan ganti akun menuntut Step eksplisit; login akun pertama (Archived-Read, A-08) dilakukan hook `before`.
- Penyimpangan urutan (S-05): TC-AC-ACC-53, 583, 54, 55 (semula 53, 54, 55, 583); TC-AC-ACC-583 memakai akun Archived-Read yang sama dengan TC-AC-ACC-53 sehingga dikelompokkan bersama.
- Pembagian TC lintas spec: role Manage active client di spec 030; akses URL aktor Archived-Read di spec 027.
- Ukuran spec (38 langkah, melewati sekitar 35 langkah): Role Matrix per blok role (tiga role; langkah berbeda) pada satu dataset; tiap blok dimulai dari ganti akun eksplisit dan Search eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-53, 54, 55: Expected tidak menyebut Client pada ⋯; spec memakai `PT Karya Abadi` yang dipakai TC-AC-ACC-54 dan 55.
