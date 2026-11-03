---
id: TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover
title: "Modal Changelog: Sort Kolom Date, Action, Old Value, New Value, Modified By dan Hover Modified By"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-306
  - TC-AC-RP-307
  - TC-AC-RP-308
  - TC-AC-RP-309
  - TC-AC-RP-310
  - TC-AC-RP-311
coverage:
  web: automated
---

# Modal Changelog: Sort Kolom Date, Action, Old Value, New Value, Modified By dan Hover Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed). Seed Changelog Tab Total Control (Pre-setup #18) bertanggal 05 Jun 2026 sampai 16 Jun 2026; urutan default Date Newest First, sehingga entri seed terbaru (16 Jun 2026) berada di awal dan entri 05 Jun 2026 di akhir. Dua nilai berbeda per kolom pada seed: Action `Assign` dan `Remove`; Old Value `Total Control` dan "—"; New Value `Total Control` dan "—"; Modified By "Bambang H" dan "Siti N". Karena audit trail permanen terus bertambah dan Pagination default 10 baris, spec membatasi tampilan ke rentang tanggal seed lewat Filter Date dan 100 baris per halaman sebagai langkah penghubung (S-14); seluruh entri seed dalam rentang itu berada di satu halaman dan jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Klik ikon Changelog
2. Klik Filter, pilih Date 05 Jun 2026 sampai 16 Jun 2026, lalu klik `[Apply]`
3. Pilih 100 baris per halaman

### TC-AC-RP-306: Sort Changelog kolom Date

4. Klik header Date
5. Verifikasi urutan Date Oldest First
6. Klik header Date
7. Verifikasi urutan Date Newest First
8. Klik header Date
9. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-RP-307: Sort Changelog kolom Action

10. Klik header Action
11. Verifikasi kolom Action terurut A-Z
12. Klik header Action
13. Verifikasi kolom Action terurut Z-A
14. Klik header Action
15. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-RP-308: Sort Changelog kolom Old Value

16. Klik header Old Value
17. Verifikasi nilai kosong "—" kolom Old Value berada di akhir pada urutan ascending
18. Klik header Old Value
19. Verifikasi nilai kosong "—" kolom Old Value berada di awal pada urutan descending
20. Klik header Old Value
21. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-RP-309: Sort Changelog kolom New Value

22. Klik header New Value
23. Verifikasi nilai kosong "—" kolom New Value berada di akhir pada urutan ascending
24. Klik header New Value
25. Verifikasi nilai kosong "—" kolom New Value berada di awal pada urutan descending
26. Klik header New Value
27. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-RP-310: Sort Changelog kolom Modified By

28. Klik header Modified By
29. Verifikasi kolom Modified By terurut A-Z berdasarkan nama tampil `[First Name] [Last Initial]`
30. Klik header Modified By
31. Verifikasi kolom Modified By terurut Z-A berdasarkan nama tampil `[First Name] [Last Initial]`
32. Klik header Modified By
33. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-RP-311: Hover Modified By Changelog menampilkan nama lengkap

34. Hover nilai Modified By "Siti N"
35. Verifikasi tooltip "Siti Nurhaliza"
36. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09, S-14): langkah 2 dan 3 (Filter Date rentang seed dan 100 baris per halaman, pola langkah 2 dan 3 pada spec 090), langkah 36 (tutup modal Changelog).
- Pada TC-AC-RP-308 dan 309, nilai kosong "—" di akhir (ascending) atau di awal (descending) urutan diamati pada satu halaman yang memuat seluruh entri seed dalam rentang Filter (langkah 2 dan 3), tanpa pindah halaman (S-14).
- Hover Modified By (TC-AC-RP-311) diasersi segera setelah hover (bagian 8b butir 5).
- Alasan sekitar 35 langkah (36 langkah): enam blok sort dan hover satu kelas fungsional pada modal Changelog dan dataset yang sama; tiap blok hanya membaca urutan sehingga tidak mengubah data, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-RP-308 dan 309 menyebut nilai kosong "—" di akhir saat ascending tanpa menyatakan halaman yang diamati; spec membatasi data dengan Filter Date rentang seed dan 100 baris per halaman supaya seluruh entri seed berada di satu halaman, dengan asumsi Filter dan jumlah baris per halaman tidak direset oleh sort.
  - TC-AC-RP-310 Expected menyatakan A-Z berdasarkan nama lengkap sedangkan kolom menampilkan format "[First Name] [Last Initial]" (R-14); urutan nama lengkap hanya teramati lewat singkatan nama, sehingga langkah 29 dan 31 mengasersi urutan berdasarkan nama tampil.
  - TC-AC-RP-306 hingga 310 menyebut klik ketiga "kembali ke default Date Newest First" tanpa langkah observasi pada TC-AC-RP-307, 308, 309, 310 selain Expected; spec mengasersi sesuai Expected.
