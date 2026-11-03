---
id: TC-FA-CF-E2E-177-row-action-tanpa-detail-dan-tab-accounting-berlisensi
title: "Row Action Tanpa Detail dan Tab Accounting Berlisensi FA-7"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-448
  - TC-FA-CF-449
coverage:
  web: automated
---

# Row Action Tanpa Detail dan Tab Accounting Berlisensi FA-7

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11, lisensi FA-7 Single Depreciation aktif) dengan baseline tab General delapan field (Pre-setup #12), tab Purchasing empat field (Pre-setup #13), dan tab Accounting dua field (Pre-setup #13: `Cost Center` Text General Active Required Yes dan `Asset Tag Class` Text General), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral`, `Fixture.faCustomFields.baselinePurchasing`, dan `Fixture.faCustomFields.baselineAccounting` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat spec ini lewat UI pada langkah 8 sampai 11, dibersihkan hook `after` lewat seed reset Company dan penghapusan field via API yang disediakan tim FE/BE): field `Group Bound Accounting {runId}-177` (Text, tab Accounting).
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi menu row action dan status tautan pada sel Field Name.
- State global: tidak ada yang diubah selain data Dinamis di atas.

## Test Steps

### TC-FA-CF-448: Modul tidak memiliki halaman Detail sehingga tidak ada navigasi Back dari Detail

1. Klik row action `⋯` pada baris `Legacy Tag`
2. Verifikasi menu row action memuat `Edit` dan `Delete`
3. Verifikasi menu row action tidak memuat aksi lain termasuk `Detail`
4. Verifikasi `Field Name` pada baris `Legacy Tag` berupa teks tanpa tautan
5. Tutup menu row action dengan `Esc`

### TC-FA-CF-449: Tab Accounting berlisensi FA-7 dapat dibuka dan menampilkan tabel grup Accounting

6. Klik tab `Accounting`
7. Verifikasi tabel grup Accounting tampil memuat field `Cost Center` dan `Asset Tag Class`
8. Klik `[+ Custom Field]`
9. Isi Field Name `Group Bound Accounting {runId}-177`
10. Pilih Data Type `Text`
11. Klik `[Submit]`
12. Verifikasi baris `Group Bound Accounting {runId}-177` tampil pada tabel tab Accounting
13. Klik tab `General`
14. Verifikasi baris `Asset Serial Tag` tampil pada tabel tab General
15. Verifikasi baris `Group Bound Accounting {runId}-177` tidak tampil pada tabel tab General
16. Klik tab `Purchasing`
17. Verifikasi baris `Vendor Code` tampil pada tabel tab Purchasing
18. Verifikasi baris `Group Bound Accounting {runId}-177` tidak tampil pada tabel tab Purchasing

## Notes

- Spec memuat 18 langkah, di bawah ambang sekitar 35 langkah. Dua topik tabel utama (menu row action dan tab Accounting), satu akun, satu dataset (Company Alpha).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (menutup menu), langkah 13 dan 16 (pindah tab untuk memeriksa pengikatan grup). Langkah 14 dan 17 adalah anchor positif untuk absence langkah 15 dan 18 (bagian 8b butir 2).
- Langkah 8 sampai 12 menjalankan klausa Expected TC-FA-CF-449 "Create dari tab ini mengikat grup Accounting"; TC-FA-CF-449 tidak memiliki langkah Create sendiri, sehingga langkah itu mengikuti pola langkah uji TC-FA-CF-56. Langkah 13 sampai 18 memeriksa bahwa field baru terikat hanya pada grup Accounting.
- Urutan TC di spec: 448 lalu 449; TC-FA-CF-449 berisi aksi yang menambah data sehingga berada di akhir (S-10). TC-FA-CF-443 sampai 447 ada di spec 116.
- Temuan untuk QA:
  - TC-FA-CF-449 Expected b ("Create dari tab ini mengikat grup Accounting") tidak memiliki langkah uji dan tidak menyebut data uji; spec melengkapinya dari pola TC-FA-CF-56 (Field Name bersuffix, Data Type `Text`).
  - TC-FA-CF-449 Data Uji hanya menyebut `Cost Center`; `Asset Tag Class` dari Pre-setup #13 ikut diasersi karena Expected menyebut tabel "memuat field grup Accounting".
  - TC-FA-CF-448 Langkah Uji ("Periksa row action dan tautan identifier") tidak menyebut baris; spec memakai baris `Legacy Tag`.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
