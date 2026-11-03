---
id: TC-AC-DN-E2E-013-sidebar-irisan-dengan-search-filter
title: "Category Sidebar sebagai Irisan dengan Search dan Filter Panel, Reset Halaman, dan Konsistensi Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-42
  - TC-AC-DN-43
  - TC-AC-DN-46
  - TC-AC-DN-598
coverage:
  web: automated
---

# Category Sidebar sebagai Irisan dengan Search dan Filter Panel, Reset Halaman, dan Konsistensi Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Master Brand (#15: `Brand A`), Device Name inti (#16), dan seed 120 Device Name (#17); baca-saja. Tidak ada data Dinamis. Form Create pada TC-AC-DN-598 dibuka hanya untuk membaca pohon Category dan ditutup tanpa menyimpan.
- State global: Search, Filter, halaman aktif, dan pilihan Sidebar dibersihkan di akhir tiap TC.

## Test Steps

### TC-AC-DN-42: Sidebar Category dan Search bekerja sebagai irisan

1. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
2. Pilih node `Antenna` pada Category Sidebar
3. Ketik Search `Gate`, tekan Enter
4. Verifikasi List memuat satu baris: Gate Antenna
5. Verifikasi node `Antenna` tetap terpilih dan tidak direset oleh Search
6. Klik `(←)` pada kotak Search
7. Hapus pilihan node `Antenna`

### TC-AC-DN-43: Sidebar Category dan Filter Panel bekerja sebagai irisan

8. Expand `Handheld Reader` pada Category Sidebar
9. Pilih node `UHF Handheld` pada Category Sidebar
10. Klik ikon Filter
11. Pilih Brand `Brand A` pada field `Brand` (placeholder "All brands")
12. Klik `[Apply]`
13. Verifikasi List memuat satu baris: RFID Reader
14. Verifikasi Legacy Scanner tidak tampil karena tidak ber-Brand `Brand A`
15. Verifikasi node `UHF Handheld` tetap terpilih
16. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
17. Hapus pilihan node `UHF Handheld`

### TC-AC-DN-46: Pilihan node Sidebar dari halaman 2 mereset halaman aktif ke halaman 1

18. Klik navigasi halaman berikutnya pada Pagination
19. Pilih node `Antenna` pada Category Sidebar
20. Verifikasi halaman aktif pada pagination kembali ke halaman 1
21. Verifikasi List memuat dua baris berurutan: Door Antenna, Gate Antenna
22. Verifikasi tidak ada kondisi halaman kosong
23. Verifikasi node `Antenna` tetap terpilih
24. Hapus pilihan node `Antenna`

### TC-AC-DN-598: Node Category pada Sidebar dan pada dropdown Category popup Create sama

25. Expand `TAG` lalu `NFC` pada Category Sidebar
26. Verifikasi Category Sidebar memuat leaf `BLE Gateway`, `UHF Handheld`, `Antenna`, `BLE`, `GPS`, `RFID`, `Accessory`, `Tag`, dan `Perangkat Pemindai Kode Batang Industri`
27. Verifikasi Category Sidebar memuat node `Hardware`, `Handheld Reader`, `Smart Fixed Reader`, `TAG`, dan `NFC` sebagai node yang punya anak
28. Klik tombol `+ Device Name`
29. Klik field Category
30. Expand `Hardware`, `Handheld Reader`, `Smart Fixed Reader`, `TAG`, dan `NFC` pada pohon TreeSelect
31. Verifikasi TreeSelect memuat leaf yang sama: `BLE Gateway`, `UHF Handheld`, `Antenna`, `BLE`, `GPS`, `RFID`, `Accessory`, `Tag`, dan `Perangkat Pemindai Kode Batang Industri`
32. Verifikasi TreeSelect memuat node `Hardware`, `Handheld Reader`, `Smart Fixed Reader`, `TAG`, dan `NFC` sebagai node yang punya anak
33. Tekan Esc untuk menutup dropdown Category, lalu klik ikon silang `[✕]` pada header popup Create

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09, R-16): langkah 1, 8, dan 25 membuka cabang pohon Sidebar yang dibutuhkan tiap TC (cabang yang sudah terbuka dari TC sebelumnya tidak dibuka ulang; TC-AC-DN-598 membuka `TAG` dan `NFC`, sedangkan `Hardware`, `Handheld Reader`, dan `Smart Fixed Reader` sudah terbuka sejak langkah 1 dan 8); langkah 6 dan 16 mengosongkan Search dan Filter Panel; langkah 7, 17, dan 24 melepas pilihan Sidebar; langkah 33 menutup popup Create yang tidak diubah.
- TC-AC-DN-598: langkah "catat node tanpa anak" pada TC dijalankan sebagai `Verifikasi` daftar leaf dan node bercabang pada Sidebar sebelum popup Create dibuka.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
