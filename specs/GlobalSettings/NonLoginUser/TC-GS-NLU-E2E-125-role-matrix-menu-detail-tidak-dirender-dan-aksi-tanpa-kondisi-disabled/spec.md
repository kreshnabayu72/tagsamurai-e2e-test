---
id: TC-GS-NLU-E2E-125-role-matrix-menu-detail-tidak-dirender-dan-aksi-tanpa-kondisi-disabled
title: "Role Matrix: menu `⋯` Detail tidak dirender (Create-Only, Read-Only role) dan aksi tanpa kondisi Disabled"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-51
  - TC-GS-NLU-52
coverage:
  web: automated
---

# Role Matrix: menu `⋯` Detail tidak dirender (Create-Only, Read-Only role) dan aksi tanpa kondisi Disabled

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-51 | Manage user and role (Create-Only: C+R) | Lestari Ayu | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-NLU-51 | Manage user and role (Read-Only role: R saja) | Eko Prasetyo | `manageUserRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-NLU-52 | Manage user and role (Full CRUD) | Fajar Nugroho | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FULLCRUD_PASSWORD` |
- Login akun aktor pertama (Create-Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13: Non-Login User Budi Kurniawan (Active), Joko Susilo (Inactive manual), dan Agus Salim (Temporary-expired) (No. 11) hanya dibaca. Spec hanya membaca; tidak membuat data dan tidak mengubah state global.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-51: Menu `⋯` header Detail tidak dirender bagi pemegang Create-Only dan Read-Only role

1. Buka Detail Non-Login User Budi Kurniawan: ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
2. Hover switch Active
3. Verifikasi switch Active tampil Disabled (Create-Only)
4. Verifikasi Tooltip `"You don't have permission to edit."` (Create-Only)
5. Verifikasi ikon menu `⋯` di header tidak dirender (Create-Only)
6. Logout dari akun Manage user and role (Create-Only: C+R), lalu login sebagai Manage user and role (Read-Only role: R saja) (Eko Prasetyo, `manageUserRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_READ_PASSWORD`)
7. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, ketik Search `Budi Kurniawan`, tekan Enter, lalu klik Name Budi Kurniawan
8. Hover switch Active
9. Verifikasi switch Active tampil Disabled (Read-Only role)
10. Verifikasi Tooltip `"You don't have permission to edit."` (Read-Only role)
11. Verifikasi ikon menu `⋯` di header tidak dirender (Read-Only role)

### TC-GS-NLU-52: Aksi tulis identik untuk semua baris tanpa kondisi Disabled berdasarkan target

12. Logout dari akun Manage user and role (Read-Only role: R saja), lalu login sebagai Manage user and role (Full CRUD) (Fajar Nugroho, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_FULLCRUD_PASSWORD`)
13. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `Budi Kurniawan`, tekan Enter
14. Klik `⋯` pada baris Budi Kurniawan (Active)
15. Verifikasi overlay baris Budi Kurniawan berisi `Detail`, `Edit`, `Convert to Login User`, `Delete`
16. Verifikasi tidak ada opsi Disabled pada overlay baris Budi Kurniawan
17. Tutup overlay row action
18. Ganti isi kotak search dengan `Joko Susilo`, tekan Enter
19. Klik `⋯` pada baris Joko Susilo (Inactive)
20. Verifikasi overlay baris Joko Susilo berisi `Detail`, `Edit`, `Convert to Login User`, `Delete` (identik dengan baris Budi Kurniawan)
21. Verifikasi tidak ada opsi Disabled pada overlay baris Joko Susilo
22. Tutup overlay row action
23. Ganti isi kotak search dengan `Agus Salim`, tekan Enter
24. Klik `⋯` pada baris Agus Salim (Temporary-expired)
25. Verifikasi overlay baris Agus Salim berisi `Detail`, `Edit`, `Convert to Login User`, `Delete` (identik dengan kedua baris sebelumnya)
26. Verifikasi tidak ada opsi Disabled pada overlay baris Agus Salim berdasarkan relasi aktor dengan target

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 7, 12, 13, 17, 18, 22, 23 (membuka Detail atau List lewat Search, dan menutup overlay).
- Spec Role Matrix (bagian 3a konvensi): menu `⋯` header Detail tidak dirender bagi dua role (TC-GS-NLU-51) dan aksi tulis tanpa kondisi Disabled (TC-GS-NLU-52). TC-GS-NLU-51 ditulis per blok role karena ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07).
- Pembagian TC lintas spec: TC-GS-NLU-47 sampai 50 ada di spec 013.
- Temuan untuk QA:
  - TC-GS-NLU-51 langkah 1 menyebut precondition "berada di Detail Non-Login User Budi Kurniawan" tanpa cara membukanya; spec membuka lewat Search dan klik Name. Hover switch ditambahkan untuk mengamati tooltip yang diminta Expected b.
  - TC-GS-NLU-52 Expected a ("overlay identik") diasersi dengan isi overlay yang sama pada tiap baris, dan Expected b ("tidak ada opsi Disabled") diasersi per baris; hasil identik antar baris tidak dibandingkan lewat satu langkah gabungan.
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk env role (`GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`) mencantumkan email lain; tim FE perlu memastikan satu nama env satu akun (R-07).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
