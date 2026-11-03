---
id: TC-AC-DN-E2E-078-bulk-selection-limit
title: "Bulk Delete: Selection Limit (Checkbox Disabled dan Select All Dipotong)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-537
  - TC-AC-DN-217
  - TC-AC-DN-218
coverage:
  web: automated
---

# Bulk Delete: Selection Limit (Checkbox Disabled dan Select All Dipotong)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control; berhak mengubah Lifecycle Settings), password `Spectra.env.AC_DN_TC2_PASSWORD` (disediakan tim FE). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan Selection Limit; tidak ada sesi UI kedua.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester`; #17 seed `Seed Device 001` sampai `Seed Device 120` (total baris 130); #21 Selection Limit entitas uji bernilai awal 1000.
- State global: Selection Limit di Lifecycle Settings > System Limits diubah ke 100 oleh langkah 1 dan dipulihkan ke 1000 oleh langkah 27; fixture BE (disediakan tim FE/BE) memastikan nilai awal 1000 di hook `before` dan memulihkannya di hook `after`. Efek pada Last Modified dan audit trail Lifecycle Settings dicatat di sini. - Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` dan `AC_DN_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-537: Selection Limit dari System Limits dibaca pada Bulk Delete setelah nilainya diubah

1. Maya Putri (sesi API) mengisi Selection Limit pada Lifecycle Settings > System Limits dengan 100 hingga tersimpan
2. Buka halaman `Settings > Device > Device Name`
3. Pilih page size 100 pada Overlay Page Size
4. Klik checkbox header kolom
5. Verifikasi Bulk Action Bar menampilkan "100 Device Names selected"
6. Klik tombol navigasi halaman berikutnya
7. Hover checkbox baris pertama halaman 2
8. Verifikasi checkbox baris pertama halaman 2 tetap tampil namun berstatus disabled
9. Verifikasi tooltip pada checkbox disabled berbunyi "You've reached the maximum selection of 100 rows."

### TC-AC-DN-217: Checkbox melewati Selection Limit menjadi disabled dengan tooltip

10. Verifikasi teks counter `100 Device Names selected`
11. Verifikasi Bulk Action Bar tetap aktif
12. Verifikasi checkbox baris `Seed Device 093` tetap tampil dalam keadaan disabled
13. Pindahkan kursor ke area lain halaman, lalu arahkan kursor ke checkbox baris `Seed Device 093`
14. Verifikasi tooltip pada checkbox: "You've reached the maximum selection of 100 rows."

### TC-AC-DN-218: Select All melebihi Selection Limit memotong seleksi ke batas dengan toast error

15. Klik ikon `(X)` pada Bulk Action Bar
16. Klik tombol pagination ke halaman 1
17. Centang baris `Cable Tester`
18. Klik `Select All (130 records)`
19. Verifikasi toast error persisten: "Error, only the first 100 of 130 rows were selected. Narrow your filter to include the rest."
20. Verifikasi teks counter `100 Device Names selected`
21. Verifikasi Bulk Action Bar tetap tampil dan dapat dipakai
22. Klik tombol pagination ke halaman 2
23. Verifikasi baris halaman 2 tidak tercentang
24. Tutup toast error persisten
25. Klik ikon `(X)` pada Bulk Action Bar
26. Ubah Page Size kembali ke 10 lewat Overlay Page Size
27. Pulihkan Selection Limit ke 1000 lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Kelas e menurut dataset dan state global (Selection Limit, Pre-setup #21); suite berjalan serial dan spec memulihkan nilai di langkah 27 serta hook `after`.
- Urutan TC berbeda dari urutan nomor TC; spec ini menjalankan TC-AC-DN-537, 217, 218: TC-AC-DN-537 menetapkan Selection Limit 100 lewat pelaku kedua, dan TC-AC-DN-217 serta TC-AC-DN-218 mensyaratkan nilai itu (halaman yang sama dipakai berulang). TC-AC-DN-217 melanjutkan kondisi halaman 2 dengan 100 baris tercentang dari TC-AC-DN-537.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah 1 ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (S-03, S-09): langkah 15 dan 25 (membersihkan seleksi); langkah 24 (menutup toast persisten); langkah 26 (mengembalikan Page Size); langkah 27 (pemulihan state global).
- Temuan untuk QA:
  - TC-AC-DN-218 Expected butir d "Baris halaman 2 tidak tercentang" hanya benar pada Page Size 100 (pada Page Size 10 baris halaman 2 termasuk 100 baris pertama); spec memakai Page Size 100 hasil TC-AC-DN-537 dan TC tidak menyebut Page Size.
  - TC-AC-DN-537 Langkah Uji mengubah Selection Limit lewat UI Lifecycle Settings oleh Total Control (sesi kedua); spec memakai sesi API sesuai keputusan pelaku kedua. Post Condition "Selection Limit entitas tersimpan 100" tidak punya langkah observasi di TC dan tidak diasersi.
