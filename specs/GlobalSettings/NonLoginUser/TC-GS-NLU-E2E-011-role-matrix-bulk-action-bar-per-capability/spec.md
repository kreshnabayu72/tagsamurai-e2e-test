---
id: TC-GS-NLU-E2E-011-role-matrix-bulk-action-bar-per-capability
title: "Role Matrix: Bulk Action Bar per capability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-41
  - TC-GS-NLU-42
  - TC-GS-NLU-46
coverage:
  web: automated
---

# Role Matrix: Bulk Action Bar per capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-41 | Total Control | Siti Nurhaliza | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-NLU-42 | Manage user and role (Update-Only: R+U) | Bayu Saputra | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-NLU-46 | Manage user and role (Full CRUD) | Fajar Nugroho | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FULLCRUD_PASSWORD` |
- Login akun aktor pertama (Total Control) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By) hanya dibaca.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE): Non-Login User `Tono Wijaya {runId}-011` (Active, Division Operations, Represented By Ahmad Fauzi, Email `tonowijaya+{runId}-011@qwertysystem.net`) dan `Rani Lestari {runId}-011` (Inactive, Division Operations, Represented By Ahmad Fauzi, Email `ranilestari+{runId}-011@qwertysystem.net`). Keduanya dipakai oleh ketiga TC; Search `{runId}-011` menyaring tepat dua baris ini (2 record dari seeding).
- Pemulihan: TC-GS-NLU-46 meng-Convert kedua user menjadi Login User; hook `after` menghapus kedua user dan Login User hasil Convert (bila ada) lewat API, tanpa mengasumsikan seeding berhasil penuh.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-41: Bulk Action Bar tampil untuk Total Control dengan aksi Activate, Deactivate, Convert to Login User

1. Ketik Search `{runId}-011`, tekan Enter
2. Centang baris `Tono Wijaya {runId}-011` (Active)
3. Centang baris `Rani Lestari {runId}-011` (Inactive)
4. Verifikasi Bulk Action Bar muncul berisi: button `Bulk Action`, teks `"2 Non-Login Users selected"`, button `Select All (2 records)`, icon `(X)`
5. Klik button `Bulk Action`
6. Verifikasi Overlay `Bulk Action` memuat: `Activate`, `Deactivate`, `Convert to Login User`
7. Verifikasi Overlay `Bulk Action` tidak memuat `Delete`
8. Klik icon `(X)` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-NLU-42: Bulk Action Bar tampil untuk Update-Only dan tidak ada Delete

9. Logout dari akun Total Control, lalu login sebagai Manage user and role (Update-Only: R+U) (Bayu Saputra, `manageUserUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_UPDATE_PASSWORD`)
10. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `{runId}-011`, tekan Enter
11. Centang baris `Tono Wijaya {runId}-011` (Active)
12. Verifikasi Bulk Action Bar muncul
13. Klik button `Bulk Action`
14. Verifikasi Overlay memuat `Deactivate` (sesuai seleksi Active) dan `Convert to Login User`
15. Verifikasi Overlay tidak memuat `Delete`
16. Klik icon `(X)` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-NLU-46: Tombol bulk Convert tersedia dan berhasil untuk Full CRUD pada seleksi campuran Active dan Inactive

17. Logout dari akun Manage user and role (Update-Only: R+U), lalu login sebagai Manage user and role (Full CRUD) (Fajar Nugroho, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_FULLCRUD_PASSWORD`)
18. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `{runId}-011`, tekan Enter
19. Centang baris `Tono Wijaya {runId}-011` dan `Rani Lestari {runId}-011`
20. Pilih `Bulk Action`
21. Verifikasi opsi `Convert to Login User` tersedia walau seleksi campuran Active dan Inactive
22. Pilih `Convert to Login User`, lalu klik `[Convert]`
23. Verifikasi Toast sukses `"Success, non-login user has been converted."`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 1, 8, 9, 10, 16, 17, 18 (Search data uji, membuka halaman sesudah ganti akun, dan membatalkan seleksi).
- Spec Role Matrix (bagian 3a konvensi): topik Bulk Action Bar per capability. Ditulis per blok role karena langkah tiap role tidak identik dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07). TC-GS-NLU-46 (aksi Convert) di akhir karena menghapus kedua baris dari tabel (S-10).
- Pelaku seeding adalah API; tidak ada konteks kedua UI (tidak memakai P-2).
- Temuan untuk QA:
  - TC-GS-NLU-41 dan TC-GS-NLU-46 memakai Budi Kurniawan/Joko Susilo dan Tono Wijaya/Rani Lestari dari Pre-setup. Spec memakai satu pasangan data milik spec (`Tono Wijaya {runId}-011` Active dan `Rani Lestari {runId}-011` Inactive) untuk ketiga TC agar Search `{runId}-011` memuat kedua baris sekaligus tanpa bergantung pada persistensi seleksi lintas Search, dan agar target Convert bukan data Pre-setup (S-06).
  - TC-GS-NLU-41 Expected a menyebut `Select All ({N} records)` tanpa menyebut apakah N menghitung hasil Search; spec mengasumsikan N = 2 (hasil Search `{runId}-011`).
  - TC-GS-NLU-42 "Centang satu baris" tidak menyebut baris dan status; Expected "Activate/Deactivate sesuai seleksi" tidak menyebut hasil untuk seleksi Active. Spec mencentang baris Active dan mengasersi `Deactivate`.
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_UPDATE_PASSWORD` mencantumkan email lain; tim FE perlu memastikan satu nama env satu akun (R-07).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
