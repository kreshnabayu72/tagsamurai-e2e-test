---
id: TC-AC-LCS-E2E-166-konsumen-selection-limit-seleksi-dan-select-all
title: "Konsumen Selection Limit: Seleksi Manual, Select All pada 150 Baris, dan Pembacaan Live"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-582
  - TC-AC-LCS-583
  - TC-AC-LCS-584
coverage:
  web: automated
---

# Konsumen Selection Limit: Seleksi Manual, Select All pada 150 Baris, dan Pembacaan Live

## Prerequisites

- Mode: FE+BE. Kelas harness e (volume data: 150 Group level 1 pada tabel Settings > Group dengan Bulk Action Bar).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: 150 Group level 1 pada Settings > Group diatur lewat Fixture BE (seeding minimal 150 baris; disediakan tim FE/BE) dan dibuang di hook `after` suite; nilai Selection Limit awal `1000` (default). TC 583 memakai Selection Limit tersimpan `100` yang diatur lewat Fixture BE sebagai precondition TC.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): Fixture BE untuk membangun 150 Group, mengisi tab System Limits dengan nilai tertentu, dan memulihkan ketujuh tab ke nilai default.
- State global: konfigurasi tab System Limits dan 150 Group diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-582: Selection Limit diturunkan ke 100, seleksi manual ke-101 diblok live dengan tooltip

1. Atur lewat Fixture BE: Settings > Group memuat 150 Group level 1 pada tabel dengan Bulk Action Bar
2. Klik tab System Limits
3. Ubah Selection Limit dari `1000` menjadi `100` lalu klik `[Save]`
4. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
5. Buka Settings > Group tanpa logout
6. Centang baris ke-1 sampai ke-100 satu per satu (satu klik checkbox per baris, berurutan dari atas)
7. Verifikasi 100 baris tercentang dan Bulk Action Bar menampilkan "100 Groups selected"
8. Arahkan kursor ke checkbox baris ke-101
9. Verifikasi checkbox baris ke-101 tampil namun berstatus disabled dengan tooltip "You've reached the maximum selection of 100 rows."

### TC-AC-LCS-583: Selection Limit 100, Select All pada 150 baris di-cap ke 100 baris pertama dengan Toast Error

10. Kosongkan seleksi: klik `Unselect All` pada Bulk Action Bar
11. Atur lewat Fixture BE: Selection Limit tersimpan `100`; Settings > Group tetap memuat 150 Group level 1; muat ulang Settings > Group
12. Centang satu baris lalu klik "Select All (150 records)"
13. Verifikasi seleksi di-cap ke 100 baris pertama dan Bulk Action Bar menampilkan "100 Groups selected"
14. Verifikasi toast error yang bertahan sampai di-dismiss: "Error, only the first 100 of 150 rows were selected. Narrow your filter to include the rest."
15. Dismiss toast error

### TC-AC-LCS-584: Selection Limit dinaikkan ke 120 dibaca live, seleksi manual baru berhenti pada baris ke-121

16. Kosongkan seleksi: klik `Unselect All` pada Bulk Action Bar
17. Buka Plans & Licensing > Lifecycle Settings > System Limits
18. Ubah Selection Limit dari `100` menjadi `120` lalu klik `[Save]`
19. Tunggu aksi `[Save]` selesai (tombol `[Save]` tidak lagi dalam state loading)
20. Buka Settings > Group tanpa logout
21. Centang baris ke-1 sampai ke-120 satu per satu (satu klik checkbox per baris, berurutan dari atas)
22. Verifikasi 120 baris tercentang
23. Arahkan kursor ke checkbox baris ke-121
24. Verifikasi checkbox baris ke-121 disabled dengan tooltip "You've reached the maximum selection of 120 rows."
25. Kosongkan seleksi: klik `Unselect All` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness e.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Seleksi dibersihkan (`Unselect All`) sebelum TC berikutnya (S-09).
- Langkah 6 dan 21 mengulang klik checkbox masing-masing 100 dan 120 kali tanpa langkah bersyarat; pengulangan ini adalah isi TC ("centang 100 baris satu per satu"), sehingga ambang langkah dihitung dengan ekspansi (bagian 8b butir 7).
- Alasan jumlah langkah: dengan ekspansi langkah 6 dan 21 spec ini melewati sekitar 35 langkah; ketiga blok satu kelas harness (e) dan berbagi seeding 150 baris, sehingga memecahnya hanya menggandakan seeding yang sama dan tiap blok tetap bermakna walau blok lain gagal.
- Temuan untuk QA:
  - TC 583 langkah 1 "Buka Settings > Group, centang satu baris lalu klik Select All (150 records)" tidak menyebut lokasi tautan "Select All" selain Bulk Action Bar; spec mengikuti teks TC.
  - TC 584 menyebut "seleksi manual baru berhenti pada baris ke-121" pada judul dan Expected menyebut checkbox baris ke-121 disabled; spec mengikuti Expected.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 4-5, 10-11, 15-17, 19-20, 25.
