---
id: TC-FA-SU-E2E-108-label-role-count-modified-by-dan-last-updated-mengikuti-aksi-dan-temporary-until-non
title: "Label Role Count pada User List: Dihitung per Assignment dan Mengikuti Assignment Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-369
  - TC-FA-SU-370
coverage:
  web: automated
---

# Label Role Count pada User List: Dihitung per Assignment dan Mengikuti Assignment Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Data Pre-setup tambahan: pohon grup (#21), penugasan peran (#23), Transaction Role (#39), dan atribut User List (#43). Pengguna yang dibaca tanpa diubah: Wawan Setiawan, Yuda Pratama, dan Oscar Pranata (Data TC-FA-SU-369; Oscar Pranata memegang baris pola Group Manager pada IT Infrastructure dan Accounts Payable).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; S-06): `Gita Permata {runId}-108`, email `gita.permata+{runId}-108@qwertysystem.net`, Active, tanpa Group Role. Grup yang ditambahkan: `Fixture.fa-settings-user.grupTambahan` (node pohon Pre-setup #21).

## Test Steps

### TC-FA-SU-369: Label jumlah Role dihitung per assignment

1. Ketik Search `Wawan`, tekan Enter
2. Verifikasi kolom Role baris Wawan Setiawan menampilkan `7 roles`
3. Klik label `7 roles` pada baris Wawan Setiawan
4. Verifikasi popup Role Count memuat Manage files 2 grup, Manage purchase 2 grup, dan Manage group 3 grup
5. Tutup popup dengan Esc
6. Ganti isi kotak search dengan `Yuda`, tekan Enter
7. Verifikasi label jumlah Role baris Yuda Pratama dihitung per assignment (Jenis Transaksi × Group × Role)
8. Verifikasi Global Role OFF milik Yuda Pratama tidak dihitung pada label jumlah Role
9. Ganti isi kotak search dengan `Oscar`, tekan Enter
10. Verifikasi kolom Role baris Oscar Pranata menampilkan `48 roles`: status Group Manager tidak dihitung sebagai peran, sedangkan baris pola Group Manager (Group Role dan Transaction Role) dihitung per assignment seperti baris biasa
11. Klik `(←)` pada kotak Search

### TC-FA-SU-370: Role Count bertambah dan berkurang mengikuti assignment

12. Ketik Search `Gita Permata {runId}-108`, tekan Enter
13. Catat label jumlah Role baris `Gita Permata {runId}-108` sebagai baseline
14. Klik ⋯ pada baris `Gita Permata {runId}-108`, klik `Detail`
15. Buka Tab Role, Sub-tab Group Role
16. Tambahkan grup `Fixture.fa-settings-user.grupTambahan` ke Group Role `Manage files` lewat popup `Assign Group Role` hingga tersimpan
17. Klik breadcrumb `User`
18. Klik menu Settings > User pada sidebar
19. Ketik Search `Gita Permata {runId}-108`, tekan Enter
20. Verifikasi label jumlah Role baris `Gita Permata {runId}-108` bertambah satu dari baseline
21. Klik label jumlah Role pada baris tersebut
22. Verifikasi header popup Role Count `Active Roles (N)` sama dengan label jumlah Role
23. Tutup popup dengan Esc
24. Klik ⋯ pada baris `Gita Permata {runId}-108`, klik `Detail`
25. Buka Tab Role, Sub-tab Group Role
26. Cabut grup `Fixture.fa-settings-user.grupTambahan` dari Group Role `Manage files` hingga tersimpan
27. Klik breadcrumb `User`
28. Klik menu Settings > User pada sidebar
29. Ketik Search `Gita Permata {runId}-108`, tekan Enter
30. Verifikasi label jumlah Role baris `Gita Permata {runId}-108` turun satu dan sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 11, 12, 18, 19, 28, 29 (Search untuk menemukan baris target, R-16, dan menu sidebar yang mereset Search).
- TC-FA-SU-371 dan TC-FA-SU-372, ada di spec 129.
- Temuan untuk QA (S-15): (1) TC-FA-SU-369 tidak menyebut jumlah label Role Yuda Pratama; spec mengasersi aturan hitung (per assignment, Global Role OFF tidak dihitung) tanpa angka. Angka `48 roles` Oscar Pranata (Expected c) diturunkan dari baris pola Group Manager (6 Group Role katalog × 2 grup + 2 Transaction Role × 9 Jenis Transaksi × 2 grup, lihat TC-FA-SU-1096), bukan dari data seeding spec ini, dan perilaku hitung belum diputuskan PM (Open Item 3 PRD settings-user); spec mengasersi sesuai TC. Klausa "status Group Manager tidak dihitung sebagai peran" tidak teramati terpisah dari angka `48 roles` sehingga ditulis satu `Verifikasi` (S-03). (2) Langkah 3 TC-FA-SU-369 tidak punya Expected eksplisit untuk isi popup; rincian grup per Group Role pada Expected a diasersi di popup Role Count. (3) TC-FA-SU-370 tidak menyebut Group Role dan grup yang ditambahkan; spec memakai `Manage files` dan grup fixture. Post Condition TC-FA-SU-370 (entri `Assign` Object `Group Role` pada Tab Changelog target, Tab System Log aktor, dan Activity Log) tidak punya langkah observasi sehingga tidak diasersi.
