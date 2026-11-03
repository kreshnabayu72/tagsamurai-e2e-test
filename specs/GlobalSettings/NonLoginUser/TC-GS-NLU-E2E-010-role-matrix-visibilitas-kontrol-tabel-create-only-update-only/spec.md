---
id: TC-GS-NLU-E2E-010-role-matrix-visibilitas-kontrol-tabel-create-only-update-only
title: "Role Matrix: visibilitas kontrol tabel (Create-Only, Update-Only)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-37
  - TC-GS-NLU-38
coverage:
  web: automated
---

# Role Matrix: visibilitas kontrol tabel (Create-Only, Update-Only)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-37 | Manage user and role (Create-Only: C+R) | Lestari Ayu | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-NLU-38 | Manage user and role (Update-Only: R+U) | Bayu Saputra | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13: Non-Login User Budi Kurniawan (Active) hanya dibaca. Spec hanya membaca; tidak membuat data dan tidak mengubah state global. Search yang dipakai dipulihkan oleh pembukaan ulang halaman.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-37: Visibilitas kontrol tabel Non-Login User oleh Manage user and role (Create-Only: C+R)

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
3. Verifikasi `[+ Non-Login User]`: Show
4. Verifikasi kolom checkbox seleksi baris: Hidden
5. Hover switch Active baris Budi Kurniawan
6. Verifikasi switch Active baris Budi Kurniawan tampil Disabled
7. Verifikasi Tooltip `"You don't have permission to edit."`
8. Klik ikon `⋯` pada baris Budi Kurniawan
9. Verifikasi Overlay row action berisi: hanya `Detail`
10. Tutup Overlay row action

### TC-GS-NLU-38: Visibilitas kontrol tabel Non-Login User oleh Manage user and role (Update-Only: R+U)

11. Logout dari akun Manage user and role (Create-Only: C+R), lalu login sebagai Manage user and role (Update-Only: R+U) (Bayu Saputra, `manageUserUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_UPDATE_PASSWORD`)
12. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `Budi Kurniawan`, tekan Enter
13. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
14. Verifikasi `[+ Non-Login User]`: Hidden
15. Verifikasi kolom checkbox seleksi baris: Show
16. Verifikasi switch Active baris Budi Kurniawan: Show dan enabled
17. Klik ikon `⋯` pada baris Budi Kurniawan
18. Verifikasi Overlay row action berisi: `Detail`, `Edit`, `Convert to Login User`
19. Verifikasi opsi `Delete` pada Overlay row action Hidden
20. Tutup Overlay row action

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 11, 12, 20 (Search baris target, membuka halaman sesudah ganti akun, dan menutup overlay).
- Spec Role Matrix visibilitas (bagian 3a konvensi): satu daftar kontrol tabel, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur. Ditulis per blok role karena langkah tiap role tidak identik (hover switch hanya untuk role dengan switch Disabled) dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07).
- Urutan Verifikasi tiap blok disusun mengikuti state (Table Tools dan kolom diamati sebelum overlay row action dibuka, 8b butir 5); Table Tools Show dan aktif diasersi lebih dulu sebagai anchor permukaan untuk asersi Hidden (8b butir 2). Baris Budi Kurniawan dicari lewat Search karena Pre-setup berisi lebih dari 10 baris (R-16).
- Temuan untuk QA:
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, dan `GS_DELETE_PASSWORD` mencantumkan email lain (`..._automated_qaTeam1`). Spec memakai email TC dan nama env yang sudah terdaftar; tim FE perlu memastikan satu nama env satu akun (R-07).
- Pembagian TC lintas spec: TC-GS-NLU-39 (Delete-Only) dan TC-GS-NLU-40 (Read-Only role) ada di spec 126; keduanya satu matriks dengan spec ini.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
