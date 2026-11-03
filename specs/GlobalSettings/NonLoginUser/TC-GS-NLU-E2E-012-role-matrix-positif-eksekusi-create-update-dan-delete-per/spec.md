---
id: TC-GS-NLU-E2E-012-role-matrix-positif-eksekusi-create-update-dan-delete-per
title: "Role Matrix positif: eksekusi Create, Update, dan Delete per capability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-43
  - TC-GS-NLU-44
  - TC-GS-NLU-45
coverage:
  web: automated
---

# Role Matrix positif: eksekusi Create, Update, dan Delete per capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-43 | Manage user and role (Create-Only: C+R) | Lestari Ayu | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-NLU-44 | Manage user and role (Update-Only: R+U) | Bayu Saputra | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-NLU-45 | Manage user and role (Delete-Only: R+D) | Citra Melati | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
- Login akun aktor pertama (Create-Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE): Non-Login User `Tono Wijaya {runId}-012` (Active, Position `Driver`, Division Operations, Represented By Ahmad Fauzi, Email `tonowijaya+{runId}-012@qwertysystem.net`), `Rani Lestari {runId}-012` (Inactive, Division Operations, Represented By Ahmad Fauzi, Email `ranilestari+{runId}-012@qwertysystem.net`), dan `Hendra Wijaya {runId}-012` (Active, Division Operations, Represented By Ahmad Fauzi, Email `hendrawijaya+{runId}-012@qwertysystem.net`).
- Data yang dibuat TC-GS-NLU-43 lewat UI: Non-Login User First Name `Wulan`, Last Name `Sari {runId}-012`, Division `Logistics`, Email `wulansari+{runId}-012@qwertysystem.net`, Represented By `Ahmad Fauzi`. Master data Position `Driver` dan `Manager`, Division `Logistics` dan `Operations`, dan Login User Ahmad Fauzi (Pre-setup No. 9 dan 10) hanya dibaca.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-012` yang tersisa (Wulan Sari, Tono Wijaya, Hendra Wijaya bila belum terhapus, dan Login User hasil Convert Rani Lestari), tanpa mengasumsikan seeding berhasil penuh.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-43: Create-Only berhasil membuat Non-Login User sampai selesai

1. Klik `[+ Non-Login User]`
2. Isi First Name `Wulan`, Last Name `Sari {runId}-012`, Division `Logistics`, Email `wulansari+{runId}-012@qwertysystem.net`
3. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
4. Klik `[Submit]`
5. Verifikasi popup menutup
6. Verifikasi Toast sukses `"Success, non-login user has been created."`
7. Ketik Search `Wulan Sari {runId}-012`, tekan Enter
8. Verifikasi baris Wulan Sari `{runId}-012` muncul di tabel
9. Verifikasi switch Active baris Wulan Sari `{runId}-012` ON

### TC-GS-NLU-44: Update-Only berhasil Edit, Activate/Deactivate, dan Convert to Login User sampai selesai

10. Logout dari akun Manage user and role (Create-Only: C+R), lalu login sebagai Manage user and role (Update-Only: R+U) (Bayu Saputra, `manageUserUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_UPDATE_PASSWORD`)
11. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `{runId}-012`, tekan Enter
12. Klik `⋯` baris Tono Wijaya `{runId}-012` > `Edit`
13. Ubah Position menjadi `Manager`, lalu klik `[Save]`
14. Verifikasi Toast sukses `"Success, non-login user has been updated."`
15. Klik switch Active baris Tono Wijaya `{runId}-012`, lalu konfirmasi dialog dengan `[Deactivate]`
16. Verifikasi Toast sukses `"Success, non-login user has been deactivated."`
17. Verifikasi switch Active baris Tono Wijaya `{runId}-012` OFF
18. Klik `⋯` baris Rani Lestari `{runId}-012` > `Convert to Login User`
19. Konfirmasi dengan `[Convert]`
20. Verifikasi Toast sukses `"Success, Rani Lestari {runId}-012 has been converted to a login user."`
21. Verifikasi baris Rani Lestari `{runId}-012` hilang dari tabel

### TC-GS-NLU-45: Delete-Only berhasil menghapus Non-Login User sampai selesai

22. Logout dari akun Manage user and role (Update-Only: R+U), lalu login sebagai Manage user and role (Delete-Only: R+D) (Citra Melati, `manageUserDelete_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_DELETE_PASSWORD`)
23. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `{runId}-012`, tekan Enter
24. Klik `⋯` baris Hendra Wijaya `{runId}-012` > `Delete`
25. Verifikasi Dialog `"Delete Non-Login User"` tampil
26. Klik `[Delete]` pada dialog konfirmasi
27. Verifikasi Toast sukses `"Success, non-login user has been deleted."`
28. Verifikasi baris Hendra Wijaya `{runId}-012` hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 7, 10, 11, 22, 23 (Search data uji yang dicari lewat Search, dan membuka halaman sesudah ganti akun).
- Spec Role Matrix positif per capability (bagian 3a konvensi): Create-Only (C+R), Update-Only (R+U), Delete-Only (R+D) berhasil mengeksekusi aksinya. Ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07). Target aksi tulis dan hapus selalu data milik spec (S-06).
- Search `{runId}-012` menemukan baris data milik spec; baris dicari lewat Search karena tabel berisi lebih dari 10 baris (R-16).
- Temuan untuk QA:
  - TC-GS-NLU-43 sampai 45 memakai nama literal (`Wulan Sari`, `Tono Wijaya`, `Rani Lestari`, `Hendra Wijaya`) dari Pre-setup dan Dinamis. Spec memakai nama bersuffix `{runId}-012` pada Last Name dan email (S-12, S-06). Aturan karakter Last Name tidak disebut TC, sehingga suffix berupa digit dan tanda hubung diasumsikan lolos validasi.
  - TC-GS-NLU-44 langkah 1 "ubah Position" tidak menyebut nilai baru; spec memakai `Manager` dari Pre-setup No. 9 untuk user dengan Position awal `Driver`.
  - TC-GS-NLU-43 langkah 3 tidak merinci aksi di popup Select User (Search, pilih, konfirmasi); spec menulis satu langkah sesuai TC dan rincian mengikuti spec popup Select User.
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, dan `GS_DELETE_PASSWORD` mencantumkan email lain; tim FE perlu memastikan satu nama env satu akun (R-07).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
