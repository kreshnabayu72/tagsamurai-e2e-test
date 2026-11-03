---
id: TC-FA-SU-E2E-120-tabel-user-list-filter-dan-kontrol-filter-bagian-1
title: "Tabel User List: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-340
  - TC-FA-SU-341
  - TC-FA-SU-342
coverage:
  web: automated
---

# Tabel User List: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Data Pre-setup tambahan: atribut User List (#43) untuk Transaction Role pada filter Role.
- Tabel `Filter Enum`:

| Field | Nilai | Opsi | Hasil |
|---|---|---|---|
| Status | `Active` | `Active`, `Inactive` | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma` (21 baris) |
| Activation Status | `Activated` | `Activated`, `Pending Activation`, `Pending Email Confirmation` | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`, `Fajar Nugroho` (21 baris) |
| Temporary User | `No` | `No`, `Yes` | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`, `Gita Permata` (24 baris) |


## Test Steps

### TC-FA-SU-340: Screening Filter Panel

1. Klik icon Filter
2. Verifikasi panel Filter terbuka di bawah Table Tools
3. Verifikasi ikon Filter menjadi gelap
4. Hover icon Filter
5. Verifikasi tooltip `Filter` tampil
6. Verifikasi field berurutan: Status (multi-select searchable, placeholder `All statuses`), Role (`All roles`), Home Group (`All home groups`), Position (`All positions`), Division (`All divisions`), Modified By (`All users`), Last Updated (date range picker, placeholder `Select date`), Activation Status (`All statuses`), Temporary User (`All options`), Temporary Until (date range picker, `Select date`), Shift (`All shifts`)
7. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
8. Verifikasi ikon Filter tanpa badge titik selama belum ada filter ter-Apply

### TC-FA-SU-341: Filter kelas enum

9. Untuk setiap baris tabel `Filter Enum` di Prerequisites (langkah 10 sampai 16):
10. Buka dropdown <Field>
11. Verifikasi opsi dropdown <Field> = DISTINCT data tabel (<Opsi>)
12. Centang <Nilai>
13. Klik `[Apply]`
14. Verifikasi memilih <Nilai> menyisakan <Hasil>
15. Verifikasi chip <Nilai> tampil di dalam field <Field>
16. Klik `[Clear Field]` pada field <Field> lalu `[Apply]`

### TC-FA-SU-342: Filter kelas role

17. Buka dropdown Role
18. Verifikasi opsi dropdown Role = DISTINCT data tabel berupa nama peran aktif yang ditugaskan eksplisit (nama Global Role, nama Group Role, nama Transaction Role `Asset Admin`, `Monitoring & Report`, `Staff`, `Approver` tanpa Jenis Transaksi) dan label tier `Total Control` serta `Read Only`
19. Verifikasi label jumlah seperti `3 roles` tidak muncul sebagai opsi dropdown Role
20. Centang `Approver`
21. Klik `[Apply]`
22. Verifikasi memilih `Approver` menyisakan pemegang Transaction Role Approver (Pre-setup #43): `Eka Wulandari`, `Lukman Hakim`, `Mira Anggraini`, `Yuda Pratama` (4 baris)
23. Verifikasi chip `Approver` tampil di dalam field Role
24. Klik `[Clear Field]` pada field Role lalu `[Apply]`
25. Buka dropdown Role, centang `Total Control`
26. Klik `[Apply]`
27. Verifikasi memilih `Total Control` menyisakan `Ahmad Dahlan`, `Lina Marlina` (2 baris; pengguna bertier hanya cocok lewat label tier)
28. Verifikasi chip `Total Control` tampil di dalam field Role
29. Klik `[Clear Field]` pada field Role lalu `[Apply]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah yang diulang: langkah 10 sampai 16 (tiga field enum), parameter pada tabel Prerequisites. Panel Filter tetap terbuka antar blok (langkah `[Clear Field]` lalu `[Apply]` tidak menutup panel).
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 10 sampai 16) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman.
