---
id: TC-GS-POS-E2E-024-selection-limit-bulk
title: "Selection Limit Bulk Position: Checkbox ke-(Limit+1) Disabled dan Select All Dibatasi Limit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-135
  - TC-GS-POS-136
coverage:
  web: automated
---

# Selection Limit Bulk Position: Checkbox ke-(Limit+1) Disabled dan Select All Dibatasi Limit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`), karena spec mengubah state global Selection Limit.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 tidak mengulang pembukaan layar.
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Super Admin Admin Console `superAdminAdminConsole_automated_{namaPrincipal}@qwertysystem.net` (Pre-setup 9) dengan `Spectra.env.AC_TC_PASSWORD`, dipakai hanya di hook `before` dan `after` untuk mengubah dan memulihkan Selection Limit. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 sampai 16 (7 record), yang ikut terhitung dalam jumlah total baris tabel N.
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.selectionLimit024`): 15 Position bersuffix `{runId}-024`: `Account Executive`, `Business Analyst`, `Content Writer`, `Customer Support Agent`, `Facility Manager`, `Graphic Designer`, `Network Engineer`, `Product Designer`, `Project Coordinator`, `Research Analyst`, `Sales Representative`, `Software Tester`, `System Administrator`, `Technical Writer`, dan `UX Researcher`, masing-masing diikuti ` {runId}-024`; tidak dipakai user. N diturunkan dari seeding (7 Pre-setup + 15 seeding = 22, lebih dari 3) dan ditetapkan pada langkah 16, bukan dibaca dari tabel yang hanya menampilkan satu halaman.
- State global dan pemulihannya: hook `before` mencatat nilai awal Selection Limit lalu menurunkannya menjadi 3 di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits memakai akun Super Admin Admin Console; hook `after` memulihkan nilai awal walau spec gagal di tengah. Mekanisme pengubahan (UI Admin Console atau API) disediakan tim FE/BE. Flag Guided Tooltip diatur hook suite (lihat butir Guided Tooltip di bawah).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan Selection Limit; hapus lewat API semua Position bersuffix `{runId}-024` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: hover pada checkbox disabled dan pembacaan tooltip; pembacaan state checkbox, state tombol `Bulk Action` (aktif), teks Bulk Action Bar, dan toast error yang persisten; menunggu waktu nyata sampai lebih dari 4 detik (durasi toast sukses) sejak toast error muncul (langkah 27, jeda pendek).

## Test Steps

### TC-GS-POS-135: Selection Limit, checkbox ke-(limit+1) disabled saat seleksi manual

1. Centang baris `Account Executive {runId}-024`
2. Centang baris `Business Analyst {runId}-024`
3. Centang baris `Content Writer {runId}-024`
4. Verifikasi checkbox baris lain disabled
5. Verifikasi checkbox baris lain tetap tampil
6. Hover checkbox baris ke-4 pada halaman 1
7. Verifikasi tooltip "You've reached the maximum selection of 3 rows."
8. Klik checkbox baris ke-4 pada halaman 1
9. Verifikasi baris `Account Executive {runId}-024`, `Business Analyst {runId}-024`, dan `Content Writer {runId}-024` tetap tercentang
10. Verifikasi Bulk Action Bar tetap tampil
11. Verifikasi tombol `Bulk Action` aktif
12. Klik `Bulk Action`
13. Verifikasi overlay `Bulk Action` memuat aksi `Delete`
14. Klik `Bulk Action` sekali lagi untuk menutup overlay

### TC-GS-POS-136: Selection Limit, Select All dibatasi otomatis ke limit

15. Klik icon `✕` pada Bulk Action Bar
16. Tetapkan N = 22 (7 Position Pre-setup ditambah 15 Position seeding)
17. Centang baris `Account Executive {runId}-024`
18. Klik "Select All (N records)"
19. Verifikasi toast error: "Error, only the first 3 of N rows were selected. Narrow your filter to include the rest."
20. Verifikasi hanya 3 baris pertama tabel yang tercentang
21. Verifikasi counter "3 Positions selected"
22. Verifikasi Bulk Action Bar tetap tampil
23. Verifikasi tombol `Bulk Action` aktif
24. Klik `Bulk Action`
25. Verifikasi overlay `Bulk Action` memuat aksi `Delete`
26. Klik `Bulk Action` sekali lagi untuk menutup overlay
27. Tunggu sampai lebih dari 4 detik berlalu sejak toast error muncul
28. Verifikasi toast error masih tampil melebihi durasi toast sukses (4 detik)
29. Tutup toast error dengan dismiss
30. Klik icon `✕` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 135, 136. Selection Limit diturunkan menjadi 3 sekali di hook `before` (precondition d TC-GS-POS-135 dan 136) dan dipulihkan di hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 dan 26 (menutup overlay), langkah 15 dan 30 (menutup seleksi dengan `✕`), langkah 16 (menetapkan N dari seeding), langkah 27 (menunggu sampai toast error melewati durasi toast sukses 4 detik), dan langkah 29 (dismiss toast).
- Asersi toast pada langkah 19 dan 28 memetakan frasa "tetap tampil melebihi durasi toast sukses (4 detik) sampai di-dismiss" pada TC-GS-POS-136 Expected b: toast diasersi saat muncul, diasersi lagi sesudah langkah-langkah Bulk Action Bar dan jeda lebih dari 4 detik; "sampai di-dismiss" ditulis sebagai aksi dismiss (langkah 29, penghubung).
- Expected c TC-GS-POS-135 dan 136 ("Bulk Action Bar tetap tampil dengan tombol `Bulk Action` aktif; overlay `Bulk Action` memuat `Delete`") diasersi per klausa: bar tampil (langkah 10 dan 22), tombol aktif (langkah 11 dan 23), klik `Bulk Action` (langkah 12 dan 24), overlay memuat `Delete` (langkah 13 dan 25).
- Temuan untuk QA:
  - TC-GS-POS-135 dan 136 mencantumkan dependensi TC-GS-POS-123 (populasi data); spec men-seed 15 Position bersuffix `{runId}-024` lewat API.
  - Precondition d TC-GS-POS-135 dan 136 ("Selection Limit diturunkan menjadi 3") tidak punya langkah di TC; spec menaruhnya di hook `before` dengan kemampuan "disediakan tim FE/BE" tanpa menyebut endpoint, dan memulihkannya di `after`.
  - TC-GS-POS-135 Expected a ("Checkbox baris lain disabled") tidak menyebut apakah checkbox header ikut disabled; spec hanya mengasersi checkbox baris.
  - TC-GS-POS-135 langkah 2 ("Hover dan coba centang baris ke-4") tidak menyebut halaman atau urutan baris; spec memakai baris ke-4 pada halaman 1 urutan default.
  - TC-GS-POS-136 Expected a ("3 baris pertama") tidak menyebut urutan; spec mengasersi 3 baris pertama tabel pada urutan default.
  - TC-GS-POS-136 Expected b menyebut "N" pada teks toast; spec mengisi N dengan angka yang ditetapkan pada langkah 16.
  - Post Condition tidak ada pada TC-GS-POS-135 dan 136.
