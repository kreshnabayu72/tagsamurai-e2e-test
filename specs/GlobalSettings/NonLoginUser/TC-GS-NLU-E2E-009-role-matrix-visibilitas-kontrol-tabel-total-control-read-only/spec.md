---
id: TC-GS-NLU-E2E-009-role-matrix-visibilitas-kontrol-tabel-total-control-read-only
title: "Role Matrix: visibilitas kontrol tabel (Total Control, Read Only, Full CRUD)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-34
  - TC-GS-NLU-35
  - TC-GS-NLU-36
coverage:
  web: automated
---

# Role Matrix: visibilitas kontrol tabel (Total Control, Read Only, Full CRUD)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-34 | Total Control | Siti Nurhaliza | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-NLU-35 | Read Only | Yudi Pratomo | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-NLU-36 | Manage user and role (Full CRUD) | Fajar Nugroho | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FULLCRUD_PASSWORD` |
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13: Non-Login User Budi Kurniawan (Active) hanya dibaca. Spec hanya membaca; tidak membuat data dan tidak mengubah state global. Search yang dipakai dipulihkan oleh pembukaan ulang halaman.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-34: Visibilitas kontrol tabel Non-Login User oleh Total Control

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
3. Verifikasi `[+ Non-Login User]`: Show
4. Verifikasi kolom checkbox seleksi baris: Show
5. Verifikasi switch Active baris Budi Kurniawan: Show dan enabled
6. Klik ikon `⋯` pada baris Budi Kurniawan
7. Verifikasi Overlay row action berisi: `Detail`, `Edit`, `Convert to Login User`, `Delete`
8. Tutup Overlay row action

### TC-GS-NLU-35: Visibilitas kontrol tabel Non-Login User oleh Read Only

9. Logout dari akun Total Control, lalu login sebagai Read Only (Yudi Pratomo, `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_RO_PASSWORD`)
10. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `Budi Kurniawan`, tekan Enter
11. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
12. Verifikasi `[+ Non-Login User]`: Hidden
13. Verifikasi kolom checkbox seleksi baris: Hidden
14. Hover switch Active baris Budi Kurniawan
15. Verifikasi switch Active baris Budi Kurniawan tampil Disabled
16. Verifikasi Tooltip `"You don't have permission to edit."`
17. Klik ikon `⋯` pada baris Budi Kurniawan
18. Verifikasi Overlay row action berisi: hanya `Detail`
19. Tutup Overlay row action

### TC-GS-NLU-36: Visibilitas kontrol tabel Non-Login User oleh Manage user and role (Full CRUD)

20. Logout dari akun Read Only, lalu login sebagai Manage user and role (Full CRUD) (Fajar Nugroho, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_FULLCRUD_PASSWORD`)
21. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `Budi Kurniawan`, tekan Enter
22. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
23. Verifikasi `[+ Non-Login User]`: Show
24. Verifikasi kolom checkbox seleksi baris: Show
25. Verifikasi switch Active baris Budi Kurniawan: Show dan enabled
26. Klik ikon `⋯` pada baris Budi Kurniawan
27. Verifikasi Overlay row action berisi: `Detail`, `Edit`, `Convert to Login User`, `Delete`
28. Tutup Overlay row action

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 9, 10, 19, 20, 21, 28 (Search baris target, membuka halaman sesudah ganti akun, dan menutup overlay).
- Spec Role Matrix visibilitas (bagian 3a konvensi): satu daftar kontrol tabel, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur. Ditulis per blok role karena langkah tiap role tidak identik (hover switch hanya untuk role dengan switch Disabled) dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07).
- Urutan Verifikasi tiap blok disusun mengikuti state (Table Tools dan kolom diamati sebelum overlay row action dibuka, 8b butir 5); Table Tools Show dan aktif diasersi lebih dulu sebagai anchor permukaan untuk asersi Hidden (8b butir 2). Baris Budi Kurniawan dicari lewat Search karena Pre-setup berisi lebih dari 10 baris (R-16).
- Temuan untuk QA:
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, dan `GS_DELETE_PASSWORD` mencantumkan email lain (`..._automated_qaTeam1`). Spec memakai email TC dan nama env yang sudah terdaftar; tim FE perlu memastikan satu nama env satu akun (R-07).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
