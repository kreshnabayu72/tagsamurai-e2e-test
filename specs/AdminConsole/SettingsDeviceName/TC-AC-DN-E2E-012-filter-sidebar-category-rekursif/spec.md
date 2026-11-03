---
id: TC-AC-DN-E2E-012-filter-sidebar-category-rekursif
title: "Filter Category Sidebar: Leaf, Parent, Multi-pilih, Hapus Pilihan, dan Filter Panel Tanpa Field Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-35
  - TC-AC-DN-36
  - TC-AC-DN-37
  - TC-AC-DN-38
  - TC-AC-DN-39
  - TC-AC-DN-40
  - TC-AC-DN-41
coverage:
  web: automated
---

# Filter Category Sidebar: Leaf, Parent, Multi-pilih, Hapus Pilihan, dan Filter Panel Tanpa Field Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14: `Hardware` > `Handheld Reader` > `UHF Handheld`, `Smart Fixed Reader` > `Antenna`; `TAG` > `NFC` > `Tag`), Device Name inti (#16), dan seed 120 Device Name (#17); baca-saja. Tidak ada data Dinamis.
- State global: pilihan node Category Sidebar dibersihkan di akhir tiap TC; tidak ada state tersimpan yang diubah.

## Test Steps

### TC-AC-DN-35: Pilih leaf Category Antenna menyaring List ke Device Name berkategori Antenna

1. Expand `Hardware`, `Smart Fixed Reader`, `Handheld Reader`, `TAG`, dan `NFC` pada Category Sidebar
2. Pilih node leaf `Antenna` pada Category Sidebar
3. Verifikasi List memuat dua baris berurutan: Door Antenna, Gate Antenna
4. Verifikasi Device Name berkategori lain (Cable Tester, Legacy Scanner, NFC Tag, RFID Reader) tidak tampil
5. Hapus pilihan node `Antenna`

### TC-AC-DN-36: Pilih leaf Category UHF Handheld menyaring List ke Device Name berkategori itu

6. Pilih node leaf `UHF Handheld` pada Category Sidebar
7. Verifikasi List memuat dua baris berurutan: Legacy Scanner, RFID Reader
8. Verifikasi Gate Antenna, Door Antenna, NFC Tag, dan Cable Tester tidak tampil
9. Hapus pilihan node `UHF Handheld`

### TC-AC-DN-37: Pilih parent Hardware menyaring List ke Device Name berkategori turunan di tiga level

10. Pilih node `Hardware` pada Category Sidebar
11. Verifikasi List memuat empat baris berurutan: Door Antenna, Gate Antenna, Legacy Scanner, RFID Reader
12. Verifikasi Door Antenna dan Gate Antenna (kategori Antenna, level 3) serta Legacy Scanner dan RFID Reader (kategori UHF Handheld, level 3) tampil sebagai turunan Hardware
13. Verifikasi Cable Tester, NFC Tag, Field Radio, Tag Reel, dan Barcode Station tidak tampil
14. Hapus pilihan node `Hardware`

### TC-AC-DN-38: Pilih parent Handheld Reader menyaring List ke Device Name berkategori turunan Handheld Reader

15. Pilih node `Handheld Reader` pada Category Sidebar
16. Verifikasi List memuat dua baris berurutan: Legacy Scanner, RFID Reader
17. Verifikasi Door Antenna dan Gate Antenna (kategori Antenna, bukan turunan Handheld Reader) tidak tampil
18. Hapus pilihan node `Handheld Reader`

### TC-AC-DN-39: Pilih dua node Sidebar menampilkan gabungan Device Name kedua kategori

19. Pilih node `Antenna` pada Category Sidebar
20. Pilih node `Tag` pada Category Sidebar
21. Verifikasi List memuat empat baris berurutan: Door Antenna, Gate Antenna, NFC Tag, Tag Reel
22. Verifikasi kedua node `Antenna` dan `Tag` tampil terpilih
23. Hapus pilihan node `Antenna`
24. Hapus pilihan node `Tag`

### TC-AC-DN-40: Menghapus pilihan node Sidebar mengembalikan List ke seluruh Device Name

25. Pilih node `Antenna` pada Category Sidebar
26. Hapus pilihan node `Antenna`
27. Verifikasi List kembali memuat sepuluh baris halaman 1 mulai dari Barcode Station
28. Verifikasi tidak ada node yang tampil terpilih di Category Sidebar

### TC-AC-DN-41: Filter Panel tidak memuat field Category karena Category hanya dikelola Sidebar

29. Klik ikon Filter
30. Verifikasi Filter Panel memuat field berurutan `Brand | Model/Type | Measurement | Last Modified`
31. Verifikasi tidak ada field `Category` di Filter Panel
32. Tekan Esc untuk menutup Filter Panel

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 1 membuka semua cabang pohon Sidebar sekali di awal (menggantikan frasa "expand bila belum terbuka" pada TC); langkah "Hapus pilihan node" di akhir tiap TC membersihkan filter Sidebar sebelum TC berikutnya; langkah 32 menutup Filter Panel.
- Urutan: leaf, parent, multi-pilih, hapus pilihan, dan Filter Panel; TC-AC-DN-40 mengasersi penghapusan pilihan secara eksplisit sehingga tidak bergantung pada langkah pembersih TC lain.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
