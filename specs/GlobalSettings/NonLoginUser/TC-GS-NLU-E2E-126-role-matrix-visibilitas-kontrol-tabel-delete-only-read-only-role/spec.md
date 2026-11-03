---
id: TC-GS-NLU-E2E-126-role-matrix-visibilitas-kontrol-tabel-delete-only-read-only-role
title: "Role Matrix: visibilitas kontrol tabel (Delete-Only, Read-Only role)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-39
  - TC-GS-NLU-40
coverage:
  web: automated
---

# Role Matrix: visibilitas kontrol tabel (Delete-Only, Read-Only role)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-39 | Manage user and role (Delete-Only: R+D) | Citra Melati | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-NLU-40 | Manage user and role (Read-Only role: R saja) | Eko Prasetyo | `manageUserRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13: Non-Login User Budi Kurniawan (Active) hanya dibaca. Spec hanya membaca; tidak membuat data dan tidak mengubah state global. Search yang dipakai dipulihkan oleh pembukaan ulang halaman.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-39: Visibilitas kontrol tabel Non-Login User oleh Manage user and role (Delete-Only: R+D)

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
3. Verifikasi `[+ Non-Login User]`: Hidden
4. Verifikasi kolom checkbox seleksi baris: Hidden
5. Hover switch Active baris Budi Kurniawan
6. Verifikasi switch Active baris Budi Kurniawan tampil Disabled
7. Verifikasi Tooltip `"You don't have permission to edit."`
8. Klik ikon `⋯` pada baris Budi Kurniawan
9. Verifikasi Overlay row action berisi: `Detail`, `Delete`
10. Verifikasi opsi `Edit` dan `Convert to Login User` pada Overlay row action Hidden
11. Tutup Overlay row action

### TC-GS-NLU-40: Visibilitas kontrol tabel Non-Login User oleh Manage user and role (Read-Only role: R saja)

12. Logout dari akun Manage user and role (Delete-Only: R+D), lalu login sebagai Manage user and role (Read-Only role: R saja) (Eko Prasetyo, `manageUserRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_READ_PASSWORD`)
13. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, lalu ketik Search `Budi Kurniawan`, tekan Enter
14. Verifikasi Search, Filter, Download, dan Changelog di Table Tools Show dan aktif
15. Verifikasi `[+ Non-Login User]`: Hidden
16. Verifikasi kolom checkbox seleksi baris: Hidden
17. Hover switch Active baris Budi Kurniawan
18. Verifikasi switch Active baris Budi Kurniawan tampil Disabled
19. Verifikasi Tooltip `"You don't have permission to edit."`
20. Klik ikon `⋯` pada baris Budi Kurniawan
21. Verifikasi Overlay row action berisi: hanya `Detail`
22. Tutup Overlay row action

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 12, 13, 22 (Search baris target, membuka halaman sesudah ganti akun, dan menutup overlay).
- Spec Role Matrix visibilitas (bagian 3a konvensi): satu daftar kontrol tabel, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur. Ditulis per blok role karena langkah tiap role tidak identik (hover switch hanya untuk role dengan switch Disabled) dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07).
- Urutan Verifikasi tiap blok disusun mengikuti state (Table Tools dan kolom diamati sebelum overlay row action dibuka, 8b butir 5); Table Tools Show dan aktif diasersi lebih dulu sebagai anchor permukaan untuk asersi Hidden (8b butir 2). Baris Budi Kurniawan dicari lewat Search karena Pre-setup berisi lebih dari 10 baris (R-16).
- Temuan untuk QA:
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, dan `GS_DELETE_PASSWORD` mencantumkan email lain (`..._automated_qaTeam1`). Spec memakai email TC dan nama env yang sudah terdaftar; tim FE perlu memastikan satu nama env satu akun (R-07).
- Pembagian TC lintas spec: TC-GS-NLU-37 (Create-Only) dan TC-GS-NLU-38 (Update-Only) ada di spec 010; keduanya satu matriks dengan spec ini.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
