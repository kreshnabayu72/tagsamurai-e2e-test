---
id: TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action
title: "Setup Column Sub-tab Global Role dan Group Role, Sort Role, serta Tools Sub-tab Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-376
  - TC-FA-SU-379
  - TC-FA-SU-380
  - TC-FA-SU-381
coverage:
  web: automated
---

# Setup Column Sub-tab Global Role dan Group Role, Sort Role, serta Tools Sub-tab Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Data Pre-setup tambahan: penugasan peran (#23). Pengguna yang dibuka: Wawan Setiawan (nama Group Role: Manage user & role, Manage purchase, Manage files, Manage group, Manage asset & TAG). TC tidak menyebut pengguna target untuk TC-FA-SU-376, 379, 380, dan 381; spec memakai Wawan Setiawan (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Klik ⋯ pada baris Wawan Setiawan, klik `Detail`
3. Buka Tab Role, Sub-tab Global Role

### TC-FA-SU-376: Setup Column Sub-tab Global Role

4. Klik header kolom Actions (⋯)
5. Verifikasi overlay Column Visibility memuat `Active`, `Role Name`, `Create`, `Read`, `Update`, dan `Delete` seluruhnya tercentang dan Enabled
6. Hapus centang `Update`
7. Verifikasi kolom `Update` hilang dari tabel
8. Centang kembali `Update`
9. Verifikasi kolom `Update` tampil kembali di tabel
10. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-380 dan TC-FA-SU-381: Sort dan tools Sub-tab Global Role

11. Klik header kolom `Active`, `Role Name`, `Create`, `Read`, `Update`, dan `Delete` satu per satu
12. Verifikasi tidak ada sort pada header mana pun di Sub-tab Global Role
13. Verifikasi TableTools hanya berisi ikon Changelog, tanpa Search, Filter, dan Download

### TC-FA-SU-379, TC-FA-SU-380, dan TC-FA-SU-381: Sub-tab Group Role

14. Buka Sub-tab Group Role
15. Verifikasi TableTools hanya berisi ikon Changelog, tanpa Search, Filter, dan Download
16. Klik header kolom Actions (⋯)
17. Verifikasi overlay Column Visibility memuat `Role Name` dan `Group` Hideable (tercentang)
18. Hapus centang `Group`
19. Centang kembali `Group`
20. Tutup overlay Column Visibility dengan Esc
21. Verifikasi `Role Name` berurutan default A-Z tanpa panah sort aktif
22. Klik header `Role Name` satu kali
23. Verifikasi `Role Name` ascending: `Manage asset & TAG`, `Manage files`, `Manage group`, `Manage purchase`, `Manage user & role`
24. Klik header `Role Name` kedua kali
25. Verifikasi `Role Name` descending: `Manage user & role`, `Manage purchase`, `Manage group`, `Manage files`, `Manage asset & TAG`
26. Klik header `Role Name` ketiga kali
27. Verifikasi `Role Name` kembali ke default A-Z
28. Klik header `Group` satu kali
29. Verifikasi kolom `Group` dapat di-sort (panah sort aktif pada header `Group`)
30. Klik header `Group` dua kali lagi hingga sort netral
31. Klik header kolom `Actions`
32. Verifikasi kolom `Actions` tidak dapat di-sort

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), 2 dan 3 (membuka Detail dan Sub-tab Global Role), 10, 20 (menutup overlay), 14 (berpindah sub-tab), dan 30 (mengembalikan sort netral, S-09).
- Urutan TC diubah: seluruh blok Sub-tab Global Role (TC-FA-SU-376, bagian TC-FA-SU-380 dan 381) dikerjakan lebih dulu agar sub-tab hanya dibuka sekali, lalu Sub-tab Group Role (S-10).
- Temuan untuk QA (S-15): (1) TC-FA-SU-376, 379, 380, dan 381 tidak menyebut pengguna target; Wawan Setiawan dipakai karena daftar Group Role-nya dirinci di TC-FA-SU-377. (2) Expected b TC-FA-SU-381 ("Hasil kosong dari Search tidak berlaku karena daftar tetap dari katalog") tidak punya langkah observasi dan tidak diasersi. (3) TC-FA-SU-379 dan 380 tidak merinci daftar Role Name Sub-tab Group Role; urutan A-Z diasersi atas lima nama Group Role Wawan Setiawan dari TC-FA-SU-377.
