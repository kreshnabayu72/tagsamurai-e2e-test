---
id: TC-AC-RP-E2E-090-modal-changelog-isi-per-varian
title: "Modal Changelog: Isi Entri Tab Total Control, GM, System, dan Detail Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-298
  - TC-AC-RP-299
  - TC-AC-RP-300
  - TC-AC-RP-301
coverage:
  web: automated
---

# Modal Changelog: Isi Entri Tab Total Control, GM, System, dan Detail Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed). Seed Changelog Pre-setup #18 bertanggal 05 Jun 2026 sampai 16 Jun 2026 untuk Tab Total Control, Read Only, Group Manager, System, dan Detail Role; nilai Action, Old Value, dan New Value pada seed memuat sedikitnya dua nilai berbeda. Karena audit trail permanen terus bertambah, spec membatasi tampilan ke rentang tanggal seed lewat Filter Date dan 100 baris per halaman sebagai langkah penghubung (S-14); jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-298: Isi Changelog Tab Total Control

1. Klik ikon Changelog
2. Klik Filter, pilih Date 05 Jun 2026 sampai 16 Jun 2026, lalu klik `[Apply]`
3. Pilih 100 baris per halaman
4. Verifikasi ada entri Action `Assign` dengan Old Value "—" atau `Read Only`, New Value `Total Control`, dan Field `Access Level`
5. Verifikasi ada entri Action `Remove` dan `Auto-Revert` dengan Old Value `Total Control`, New Value "—", dan Field `Access Level`
6. Verifikasi Action tampil sebagai teks polos (bukan badge)
7. Tutup modal Changelog

### TC-AC-RP-299: Isi Changelog Tab Group Manager memuat Remove (Group Deleted)

8. Klik tab `Group Manager`
9. Klik ikon Changelog
10. Klik Filter, pilih Date 05 Jun 2026 sampai 16 Jun 2026, lalu klik `[Apply]`
11. Pilih 100 baris per halaman
12. Verifikasi ada entri Action `Assign`, `Remove`, `Auto-Revert`, dan `Remove (Group Deleted)`
13. Verifikasi entri tersebut ber-Field `Group Manager` dan Object "[User Name] — [Group Name]"
14. Tutup modal Changelog

### TC-AC-RP-300: Isi Changelog Tab System superset seluruh role

15. Klik tab `System`
16. Klik ikon Changelog
17. Klik Filter, pilih Date 05 Jun 2026 sampai 16 Jun 2026, lalu klik `[Apply]`
18. Pilih 100 baris per halaman
19. Verifikasi ada entri lintas role dengan Action `Assign`, `Remove`, `Edit`, `Assign (via Total Control)`, `Assign (via Read Only)`, `Remove (via Total Control)`, `Remove (via Read Only)`, dan `Add`
20. Verifikasi Field CRUD bernilai `Inactive` atau `Active` (bukan boolean)
21. Tutup modal Changelog

### TC-AC-RP-301: Changelog Detail Role hanya berisi entri role yang dibuka

22. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
23. Klik ikon Changelog
24. Klik Filter, pilih Date 05 Jun 2026 sampai 16 Jun 2026, lalu klik `[Apply]`
25. Pilih 100 baris per halaman
26. Verifikasi sedikitnya satu entri tampil
27. Verifikasi seluruh entri pada halaman memiliki Object berawalan "Manage device master data — "
28. Verifikasi tidak ada entri role lain (mis. Object berawalan "Manage language — ") pada halaman

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 2, 3, 7, 10, 11, 14, 17, 18, 21, 24, 25.
- Langkah Filter Date (05 Jun 2026 sampai 16 Jun 2026) dan 100 baris per halaman adalah langkah penghubung yang membatasi tampilan ke baris seed (S-14); tidak ada di TC sumber.
- Expected TC-AC-RP-298, 299, dan 300 "entri memuat ..." ditulis sebagai keberadaan entri tiap jenis pada halaman terbatas seed; jumlah entri tidak diasersi.
- Asersi universal "seluruh entri" pada TC-AC-RP-301 didahului Verifikasi sedikitnya satu entri tampil (bagian 8b butir 2); absence entri role lain berpembanding entri role yang dibuka pada halaman yang sama.
- Alasan sekitar 35 langkah (28 langkah): blok TC-AC-RP-298 sampai 301 satu kelas fungsional pada modal Changelog yang sama, hanya membaca, dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-RP-298 sampai 301 menyebut "Riwayat Changelog seed" tanpa daftar baris dan jumlah per varian; spec hanya mengasersi keberadaan jenis entri dan bergantung pada seed Pre-setup #18 yang disediakan tim FE/BE.
  - TC-AC-RP-299 Expected memakai "Remove (Group Deleted)" pada Changelog Tab Group Manager; seed Pre-setup #18 harus memuatnya.
