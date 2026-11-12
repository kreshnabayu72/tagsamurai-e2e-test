---
id: TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran
title: "Bulk Status: Activate Berhasil, Deactivate Campuran Lolos dan Diblokir, serta Seleksi Campuran"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-243
  - TC-FA-FAAC-244
  - TC-FA-FAAC-245
  - TC-FA-FAAC-249
coverage:
  web: automated
---

# Bulk Status: Activate Berhasil, Deactivate Campuran Lolos dan Diblokir, serta Seleksi Campuran

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): `B-IN1` "Inactive One" dan `B-IN2` "Inactive Two" Inactive; `B-FREE1` "Free One" dan `B-FREE2` "Free Two" Active tanpa Asset Name; `B-FREE3` "Free Three" Active tanpa Asset Name; `B-NAMES` "Names Fixture" dengan 2 Asset Name; `B-FREE5` Active tanpa Asset Name; `B-IN4` "Inactive Four" Inactive.
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE: jumlah entri dicatat sebelum aksi dan asersi memakai selisih (audit trail permanen, N tidak diturunkan dari seeding, bagian 8b butir 10 dan S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: `B-IN1`, `B-IN2`, `B-IN4` kembali Inactive dan `B-FREE1`, `B-FREE2`, `B-FREE3` kembali Active.
- Seluruh baris target terlihat bersama di tabel (seed menempatkan baris `B-*` pada halaman yang tampil atau tim FE/BE menyediakan ukuran halaman yang memuatnya); lihat Temuan untuk QA di Notes.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode, nama, dan jumlah Asset Name itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-249: Seleksi campuran Active dan Inactive menampilkan kedua aksi dan memproses sesuai status

1. Catat jumlah entri Changelog sebagai baseline N
2. Centang baris `B-FREE5` (Active) dan `B-IN4` (Inactive) di tabel
3. Verifikasi Bulk Action Bar menampilkan `Activate` dan `Deactivate`
4. Klik `Activate`
5. Verifikasi Dialog `Activate Asset Class` berbentuk single, hanya memuat bullet `• B-IN4 – Inactive Four` (`B-FREE5` yang sudah Active tidak ditampilkan)
6. Klik `Activate`
7. Verifikasi toast sukses `Success, asset class has been activated.` yang hanya menghitung `B-IN4`
8. Buka Changelog
9. Verifikasi jumlah entri Changelog bertambah 1 dari N dan entri itu hanya untuk `B-IN4` (Edit Field `Status` Old `Inactive` New `Active`), tanpa entri untuk `B-FREE5`
10. Tutup modal Changelog

### TC-FA-FAAC-245: Bulk Deactivate campuran lolos dan diblokir

11. Catat jumlah entri Changelog sebagai baseline N
12. Centang baris `B-FREE3` dan `B-NAMES` di tabel
13. Klik Bulk Action `Deactivate`
14. Verifikasi Dialog `Deactivate Asset Classes` berisi `The following will be deactivated:` dengan bullet `• B-FREE3 – Free Three`, `The following cannot be deactivated and will be skipped:` dengan bullet `• B-NAMES – Names Fixture — has asset names`, dan `Are you sure you want to continue?` dengan tombol `Cancel` dan `Continue`
15. Klik `Continue`
16. Verifikasi toast sukses `Success, asset class has been deactivated. Some items were skipped (still has asset names).`
17. Verifikasi `B-FREE3` menjadi Inactive dan `B-NAMES` tetap Active
18. Buka Changelog
19. Verifikasi jumlah entri Changelog bertambah 1 dari N dan entri itu hanya untuk `B-FREE3`, tanpa entri untuk `B-NAMES`
20. Tutup modal Changelog
21. Klik `Unselect All`

### TC-FA-FAAC-243: Bulk Activate dua Asset Class Inactive

22. Catat jumlah entri Changelog sebagai baseline N
23. Centang baris `B-IN1` dan `B-IN2` di tabel
24. Verifikasi Bulk Action Bar hanya menyediakan aksi `Activate` karena semua baris terpilih Inactive
25. Klik tombol Bulk Action `Activate`
26. Verifikasi Dialog `Activate Asset Classes` berisi `• B-IN1 – Inactive One`, `• B-IN2 – Inactive Two`, dan `Are you sure you want to activate them?` dengan tombol `Cancel` dan `Activate`
27. Klik `Activate`
28. Verifikasi toast sukses `Success, asset class has been activated.`
29. Verifikasi toggle Active kedua baris On dan seleksi direset
30. Buka Changelog
31. Verifikasi jumlah entri Changelog bertambah 2 dari N, satu kejadian Edit Field `Status` Old `Inactive` New `Active` per Asset Class (`B-IN1` dan `B-IN2`)
32. Tutup modal Changelog

### TC-FA-FAAC-244: Bulk Deactivate semua lolos guard

33. Centang baris `B-FREE1` dan `B-FREE2` di tabel
34. Klik Bulk Action `Deactivate`
35. Verifikasi Dialog `Deactivate Asset Classes` berisi `• B-FREE1 – Free One`, `• B-FREE2 – Free Two`, dan `Are you sure you want to deactivate them?` dengan tombol `Cancel` dan `Deactivate` (merah)
36. Klik `Deactivate`
37. Verifikasi toast sukses `Success, asset class has been deactivated.`
38. Verifikasi toggle Active pada baris `B-FREE1` dan `B-FREE2` Off dan seleksi direset

## Notes

1. Urutan dalam spec: seleksi campuran (TC-249), lalu Deactivate campuran (TC-245), Activate dua baris (TC-243), dan Deactivate semua lolos (TC-244); semuanya mengubah status dan TC yang meninggalkan seleksi (TC-245) dibersihkan di langkah 21 sebelum TC berikutnya (S-09).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 11, dan 22 (pencatatan baseline Changelog, S-12), langkah 10, 20, dan 32 (menutup modal Changelog), dan langkah 21 (membersihkan seleksi). Langkah 8, 18, dan 30 membuka Changelog sebagai langkah observasi karena langkah TC tidak menuliskannya padahal Expected memuat isi log.
3. Baris Changelog baru dibaca sebagai himpunan baris teratas sebanyak selisih dari baseline tanpa mengandalkan urutan di antaranya, karena beberapa entri dapat jatuh dalam menit yang sama (S-14).
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Pembagian TC: dialog Bulk yang diblokir, batal, dan collapse ke dialog single ada di spec 094.
6. Temuan untuk QA: langkah TC "Centang baris X, Y di tabel" tidak menyebut cara menemukan baris pada tabel berhalaman dan tidak menyebut Search; spec mengikuti TC dan mengandalkan seed yang menampilkan baris target pada halaman yang tampil. TC-243 Expected d menyebut Changelog tetapi langkah TC tidak membuka Changelog.
7. Alasan melebihi sekitar 35 langkah (38 langkah): spec berisi empat blok Bulk Status yang masing-masing berdiri sendiri dengan baris Asset Class berbeda dan satu topik aksi; tiga dari empat blok membaca Changelog dengan baseline sendiri (S-12) sehingga tidak dapat digabung; kegagalan satu blok tidak membuat blok lain kehilangan makna.
