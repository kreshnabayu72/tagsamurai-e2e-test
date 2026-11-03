---
id: TC-GS-NLU-E2E-013-role-matrix-aksi-halaman-detail-per-capability-dan-aksi
title: "Role Matrix: aksi halaman Detail per capability (Total Control, Update-Only, Delete-Only, Read Only)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-47
  - TC-GS-NLU-48
  - TC-GS-NLU-49
  - TC-GS-NLU-50
coverage:
  web: automated
---

# Role Matrix: aksi halaman Detail per capability (Total Control, Update-Only, Delete-Only, Read Only)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-47 | Total Control | Siti Nurhaliza | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-NLU-48 | Manage user and role (Update-Only: R+U) | Bayu Saputra | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-NLU-49 | Manage user and role (Delete-Only: R+D) | Citra Melati | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-NLU-50 | Read Only | Yudi Pratomo | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
- Login akun aktor pertama (Total Control) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13: Non-Login User Budi Kurniawan (Employee ID `FT-0231`, Active) hanya dibaca. Spec hanya membaca; tidak membuat data dan tidak mengubah state global.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-47: Aksi halaman Detail untuk Total Control: switch Active dan menu `⋯` berisi Edit, Convert to Login User, Delete

1. Buka Detail Non-Login User Budi Kurniawan: ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
2. Verifikasi header Detail menampilkan `[Avatar] Budi Kurniawan`
3. Verifikasi switch Active di header enabled
4. Verifikasi subtitle Employee ID `FT-0231`
5. Klik `⋯` di header
6. Verifikasi menu `⋯` berisi `Edit`, `Convert to Login User`, `Delete` (danger)
7. Tutup menu `⋯`

### TC-GS-NLU-48: Aksi halaman Detail untuk Update-Only: Delete Hidden

8. Logout dari akun Total Control, lalu login sebagai Manage user and role (Update-Only: R+U) (Bayu Saputra, `manageUserUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_UPDATE_PASSWORD`)
9. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
10. Verifikasi switch Active enabled
11. Klik `⋯` di header
12. Verifikasi menu `⋯` berisi `Edit` dan `Convert to Login User`
13. Verifikasi `Delete` Hidden di menu `⋯`
14. Tutup menu `⋯`

### TC-GS-NLU-49: Aksi halaman Detail untuk Delete-Only: hanya Delete di menu

15. Logout dari akun Manage user and role (Update-Only: R+U), lalu login sebagai Manage user and role (Delete-Only: R+D) (Citra Melati, `manageUserDelete_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_DELETE_PASSWORD`)
16. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
17. Hover switch Active
18. Verifikasi switch Active tampil Disabled
19. Verifikasi Tooltip `"You don't have permission to edit."`
20. Klik `⋯` di header
21. Verifikasi menu `⋯` berisi `Delete` saja
22. Tutup menu `⋯`

### TC-GS-NLU-50: Aksi halaman Detail untuk Read Only: switch Active Disabled dan menu `⋯` tidak dirender

23. Logout dari akun Manage user and role (Delete-Only: R+D), lalu login sebagai Read Only (Yudi Pratomo, `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_RO_PASSWORD`)
24. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
25. Hover switch Active
26. Verifikasi switch Active tampil Disabled
27. Verifikasi Tooltip `"You don't have permission to edit."`
28. Verifikasi ikon menu `⋯` di header tidak dirender sama sekali

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 8, 9, 14, 15, 16, 22, 23, 24 (membuka Detail Budi Kurniawan lewat Search dan klik Name, dan menutup menu `⋯`).
- Spec Role Matrix (bagian 3a konvensi): aksi header halaman Detail per capability. Ditulis per blok role karena langkah tiap role berbeda (hover switch hanya untuk role dengan switch Disabled) dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07). Search baris target dicatat sebagai langkah penghubung (R-16).
- Pembagian TC lintas spec: TC-GS-NLU-51 dan TC-GS-NLU-52 ada di spec 125.
- Temuan untuk QA:
  - TC-GS-NLU-47 sampai 50 menyebut precondition "berada di Detail Non-Login User Budi Kurniawan" tanpa menyebut cara membukanya; spec membuka lewat Search dan klik Name.
  - TC-GS-NLU-48 dan TC-GS-NLU-49 "Amati switch Active" tidak menyebut hover untuk tooltip pada switch Disabled; hover ditambahkan untuk mengamati tooltip yang diminta Expected.
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk env role (`GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`) mencantumkan email lain; tim FE perlu memastikan satu nama env satu akun (R-07).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
