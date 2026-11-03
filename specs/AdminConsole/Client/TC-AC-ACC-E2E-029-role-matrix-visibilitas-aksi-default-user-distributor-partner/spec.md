---
id: TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner
title: "Role Matrix: Visibilitas Elemen dan Aksi List untuk Default User, Distributor, dan Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-578
  - TC-AC-ACC-579
  - TC-AC-ACC-580
  - TC-AC-ACC-56
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen dan Aksi List untuk Default User, Distributor, dan Partner

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-ROL-3 | Default User (Principal) | `defaultUserPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_DU_PRINCIPAL_PASSWORD` |
| A-ROL-4 | Default User (Partner CV Mitra Sejati) | `defaultUserPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_DU_PARTNER_PASSWORD` |
| A-13 | Distributor Total Control (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |
| A-14 | Partner Total Control (CV Mitra Sejati) | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |

- Login di hook `before` spec ini (Default User, A-ROL-3); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-01` `PT Sejahtera Abadi`, `C-09` `PT Baru Daftar` (tanpa riwayat subscription), dan `C-04` `PT Karya Abadi` (Archived) hanya dibaca. Pilihan baris Bulk Action pada blok Distributor dibatalkan dalam spec.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-578: Default User entitas Principal: tiga sub-tab dan elemen aksi tulis tampil

1. Lihat sub-tab, Table Tools, dan kolom Checkbox di sub-tab `Active`
2. Verifikasi sub-tab `Active`, `Suspended`, dan `Archived` tampil
3. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]` tampil
4. Verifikasi kolom Checkbox tampil
5. Ketik Search `PT Baru Daftar`, tekan Enter
6. Buka `⋯` baris `PT Baru Daftar`
7. Verifikasi menu `⋯` `PT Baru Daftar` memuat `Detail`, `Edit`, `Change Partner`, `Suspend`, dan `Delete`
8. Tutup menu `⋯` dan klik `(←)` pada kotak Search
9. Klik sub-tab `Suspended` dan lihat kolom Checkbox
10. Verifikasi sub-tab `Suspended`: kolom Checkbox tampil
11. Klik sub-tab `Archived`
12. Ketik Search `PT Karya Abadi`, tekan Enter
13. Buka `⋯` baris `PT Karya Abadi`
14. Verifikasi sub-tab `Archived`: kolom Checkbox tidak tersedia
15. Verifikasi menu `⋯` `PT Karya Abadi` memuat `Detail`, `Edit`, dan `Delete`
16. Tutup menu `⋯`, klik `(←)` pada kotak Search, klik sub-tab `Active`, lalu Logout dari akun Default User (Principal)
17. Login sebagai Default User (Partner CV Mitra Sejati) (A-ROL-4)

### TC-AC-ACC-579: Default User entitas Partner: Change Partner tidak ada, aksi lain sesuai gate entitas

18. Lihat Table Tools di sub-tab `Active`
19. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]` tampil
20. Ketik Search `PT Sejahtera Abadi`, tekan Enter
21. Buka `⋯` baris `PT Sejahtera Abadi`
22. Verifikasi menu `⋯` `PT Sejahtera Abadi` memuat `Detail`, `Edit`, dan `Suspend`
23. Verifikasi `Change Partner` tidak ada karena gate entitas
24. Verifikasi `Delete` tidak ada karena sudah pernah memiliki subscription
25. Tutup menu `⋯`, klik `(←)` pada kotak Search, lalu Logout dari akun Default User (Partner)
26. Login sebagai Distributor Total Control (PT Distribusi Nusantara) (A-13)

### TC-AC-ACC-580: Distributor Total Control: elemen tulis dan menu ⋯ Client dalam jaringannya

27. Lihat Table Tools dan kolom Checkbox di sub-tab `Active`
28. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]` tampil
29. Verifikasi kolom Checkbox tampil
30. Ketik Search `PT Sejahtera Abadi`, tekan Enter
31. Buka `⋯` baris `PT Sejahtera Abadi`
32. Verifikasi menu `⋯` `PT Sejahtera Abadi` memuat `Detail`, `Edit`, `Change Partner`, dan `Suspend`
33. Verifikasi `Delete` tidak ada karena sudah pernah memiliki subscription
34. Tutup menu `⋯`
35. Centang baris `PT Sejahtera Abadi`, lalu klik Bulk Action
36. Verifikasi menu Bulk Action hanya memuat `Suspend`
37. Tutup menu Bulk Action, hapus centang baris `PT Sejahtera Abadi`, klik `(←)` pada kotak Search, lalu Logout dari akun Distributor
38. Login sebagai Partner Total Control (CV Mitra Sejati) (A-14)

### TC-AC-ACC-56: Partner tidak melihat aksi Change Partner di menu ⋯ Client

39. Ketik Search `PT Sejahtera Abadi`, tekan Enter
40. Buka `⋯` baris `PT Sejahtera Abadi` di sub-tab `Active`
41. Verifikasi menu `⋯` `PT Sejahtera Abadi` memuat `Detail`, `Edit`, dan `Suspend`
42. Verifikasi aksi `Change Partner` tidak ada (gate entitas, Partner tidak diizinkan)
43. Verifikasi `Delete` tidak ada karena sudah pernah memiliki subscription
44. Tutup menu `⋯` dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 8, 12, 16, 17, 20, 25, 26, 30, 34, 37 sampai 39, 44. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-578, 579, 580, 56 (semula 56, 578, 579, 580); dikelompokkan per akun supaya ganti akun minimal.
- Spec Role Matrix per blok role (bagian 3a): langkah tiap role berbeda dan ganti akun menuntut Step eksplisit; login akun pertama (Default User Principal, A-ROL-3) dilakukan hook `before`; bagian sesudah tiap ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Pembagian TC lintas spec: Total Control dan Read Only ada di spec 028; role Manage active client di spec 030.
- Ukuran spec (44 langkah, melewati sekitar 35 langkah): Role Matrix per blok role (empat role; langkah berbeda) pada satu dataset; tiap blok dimulai dari ganti akun eksplisit dan Search eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-578, 579, 580, 56: Expected `Table Tools` atau menu ⋯ ditulis sebagai satu butir daftar; spec memecahnya menjadi `Verifikasi` per butir sesuai Expected TC.
  - TC-AC-ACC-578: Expected butir a memuat sub-tab, Table Tools, dan kolom Checkbox sebagai satu butir; spec memecahnya menjadi tiga `Verifikasi`.
