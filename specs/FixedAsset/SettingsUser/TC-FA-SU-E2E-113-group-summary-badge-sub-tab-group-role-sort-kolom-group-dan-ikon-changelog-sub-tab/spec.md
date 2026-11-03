---
id: TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab
title: "Group Summary Badge Sub-tab Group Role, Sort Kolom Group, Ikon Changelog Sub-tab Role, dan Ikon Row Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-377
  - TC-FA-SU-378
  - TC-FA-SU-382
  - TC-FA-SU-1044
coverage:
  web: automated
---

# Group Summary Badge Sub-tab Group Role, Sort Kolom Group, Ikon Changelog Sub-tab Role, dan Ikon Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Data Pre-setup tambahan: pohon grup (#21), penugasan peran (#23), Changelog (#27), dan Group Role (#45). Pengguna yang dibuka: Wawan Setiawan dengan Group Role Manage user & role (0 grup), Manage purchase (1 grup), Manage files (2 grup), Manage group (3 grup), dan Manage asset & TAG (All Groups).

## Test Steps

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Klik ⋯ pada baris Wawan Setiawan, klik `Detail`
3. Buka Tab Role, Sub-tab Group Role

### TC-FA-SU-377: Group Summary Badge

4. Verifikasi kolom Group baris `Manage user & role` (0 grup) menampilkan `—`
5. Verifikasi kolom Group baris `Manage purchase` (1 grup) menampilkan 1 badge nama grup
6. Verifikasi kolom Group baris `Manage files` (2 grup) menampilkan 2 badge nama grup berurut A-Z
7. Verifikasi kolom Group baris `Manage group` (3 grup) menampilkan 2 badge ditambah chip `+1 more`
8. Klik chip `+1 more` pada baris `Manage group`
9. Verifikasi popover daftar semua grup yang scrollable tampil
10. Tutup popover dengan Esc
11. Verifikasi kolom Group baris `Manage asset & TAG` menampilkan badge tunggal `All Groups`
12. Hover satu badge grup pada baris `Manage group`
13. Verifikasi tooltip menampilkan hierarki lengkap grup `[Parent] > [Child]`

### TC-FA-SU-378: Sort kolom Group

14. Klik header kolom Group satu kali
15. Verifikasi ascending: baris `Manage purchase` (1 grup) di atas `Manage files` (2 grup) di atas `Manage group` (3 grup), dan `Manage user & role` (tanpa grup, `—`) di akhir
16. Klik header kolom Group kedua kali
17. Verifikasi descending: baris `Manage group` (3 grup) di atas `Manage files` (2 grup) di atas `Manage purchase` (1 grup), dan `Manage user & role` (tanpa grup) di awal
18. Klik header kolom Group ketiga kali
19. Verifikasi default sort Role Name A-Z dipulihkan

### TC-FA-SU-1044: Ikon dan severity row action Sub-tab Group Role

20. Klik ⋯ pada baris `Manage files`
21. Verifikasi aksi baris `Detail` berikon `FileInfoLine` dan `Assign Group` berikon `UserReceived2Line`, keduanya severity dark
22. Verifikasi header kolom Actions (⋯) menjadi pintu Column Visibility
23. Tutup menu row action dengan Esc

### TC-FA-SU-382: Ikon Changelog di Sub-tab Role

24. Buka Sub-tab Global Role
25. Klik ikon Changelog
26. Verifikasi modal `Changelog: User > Global Role` tampil
27. Klik backdrop modal
28. Verifikasi modal `Changelog: User > Global Role` tidak tertutup
29. Tekan Esc
30. Verifikasi modal Changelog tertutup
31. Buka Sub-tab Group Role, klik ikon Changelog
32. Verifikasi modal Changelog Group Role tampil
33. Klik `[✕]` pada modal
34. Verifikasi modal Changelog tertutup
35. Buka Sub-tab Transaction Role, klik ikon Changelog
36. Verifikasi modal Changelog Transaction Role tampil
37. Klik `[✕]` pada modal
38. Verifikasi modal Changelog tertutup

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), 2 dan 3 (membuka Detail dan Sub-tab Group Role), 10 dan 23 (menutup popover dan menu).
- Urutan TC diubah: TC-FA-SU-1044 sebelum TC-FA-SU-382 agar perpindahan sub-tab hanya sekali; TC-FA-SU-382 menutup spec karena memuat tiga sub-tab.
- Langkah TC-FA-SU-382 "Close `[✕]` atau Esc" dipetakan: Esc pada modal Global Role, `[✕]` pada modal Group Role dan Transaction Role.
- Temuan untuk QA (S-15): (1) TC-FA-SU-378 menyebut pengurutan "jumlah sama" secara alfabetis, tetapi data Wawan Setiawan tidak memuat dua Group Role dengan jumlah grup sama; aturan itu tidak diasersi dan posisi `Manage asset & TAG` (All Groups) tidak ditentukan TC. (2) TC-FA-SU-382 tidak menyebut judul modal Changelog Group Role dan Transaction Role; spec mengasersi modal sesuai sub-tab tanpa mengarang judul. (3) TC-FA-SU-377 Expected d tidak menyebut grup tertentu untuk hierarki hover; spec mengasersi format `[Parent] > [Child]`.
- Alasan di atas sekitar 35 langkah: keempat TC berkelas fungsional yang sama, read-only, pada Detail Wawan Setiawan dan Tab Role yang sama; satu pembukaan Detail melayani semuanya, dan kegagalan satu blok tidak membuat blok lain kehilangan makna, sedangkan pemecahan menambah pencarian, pembukaan Detail, dan pindah sub-tab tanpa nilai tambah (bagian 3).
