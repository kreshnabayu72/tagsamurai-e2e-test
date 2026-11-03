---
id: TC-AC-DN-E2E-118-kombinasi-seleksi-baris-baru-dan-edit
title: "Kombinasi: Seleksi Bertahan, Logika AND Sidebar, Baris Baru Tidak Cocok Filter, dan Edit Hilang dari Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-350
  - TC-AC-DN-354
  - TC-AC-DN-351
  - TC-AC-DN-352
coverage:
  web: automated
---

# Kombinasi: Seleksi Bertahan, Logika AND Sidebar, Baris Baru Tidak Cocok Filter, dan Edit Hilang dari Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `TAG` > `NFC` > `Accessory`); #16 Device Name inti (`Barcode Station`, `Cable Tester`, `Door Antenna` ber-Category `Antenna` dan Measurement `Unit`, `Tag Reel` ber-Measurement `Meter`); #17 seed 120 baris.
- Data Dinamis (milik spec, dibuat lewat API di langkah yang menyebutnya dan dihapus lewat API; kemampuan seeding dan penghapusan Device Name disediakan tim FE/BE): `Filter Probe {runId}-118` (dibuat lewat form Create pada TC-AC-DN-351, Measurement `Unit`, Category `Accessory`, tanpa SKU) dan `Door Antenna Uji {runId}-118` (Measurement `Unit`, Category `Antenna`, tanpa SKU; diubah namanya pada TC-AC-DN-352). `{runId}` hanya digit. Hook `after` menghapus kedua record sebagai cadangan.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Seleksi, Search, Filter, dan pilihan Sidebar dikembalikan ke awal di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-350: Centang baris bertahan saat Search dan Filter diubah

1. Centang checkbox baris Barcode Station dan Cable Tester
2. Verifikasi bulk action bar menampilkan `2 Device Names selected`
3. Ketik Search `zzzxyz`, tekan Enter
4. Verifikasi bulk action bar tetap menampilkan `2 Device Names selected` setelah Search tanpa hasil
5. Klik `✕` pada Search, tekan Enter
6. Verifikasi checkbox Barcode Station dan Cable Tester masih tercentang
7. Hapus centang checkbox baris Barcode Station dan Cable Tester

### TC-AC-DN-354: Category Sidebar, Search, dan Filter Panel dengan logika AND

8. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
9. Pilih node `Antenna` pada Category Sidebar
10. Ketik Search `Door`, tekan Enter
11. Klik ikon Filter, klik field `Measurement`, centang `Unit`, lalu klik `[Apply]`
12. Verifikasi tabel menampilkan 1 baris: Door Antenna (kategori Antenna, cocok keyword `Door`, Measurement Unit)
13. Verifikasi Sidebar tetap memilih `Antenna`
14. Verifikasi keyword `Door` tetap terisi di kolom pencarian
15. Klik ikon Filter
16. Verifikasi chip `Unit` tetap aktif di Filter Panel
17. Klik `[Clear Field]`, lalu klik `[Apply]`
18. Klik `(←)` pada kotak Search
19. Hapus pilihan node `Antenna`

### TC-AC-DN-351: Device Name baru yang tidak cocok filter aktif tidak muncul

20. Klik ikon Filter, klik field `Measurement`, centang `Meter`, lalu klik `[Apply]`
21. Klik `+ Device Name`
22. Ketik `Filter Probe {runId}-118` pada field Device Name
23. Klik field Measurement lalu pilih `Unit`
24. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Accessory`
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, device name has been created."
27. Verifikasi tabel tetap menampilkan 1 baris Tag Reel
28. Verifikasi `Filter Probe {runId}-118` tidak tampil karena Measurement `Unit` tidak cocok filter `Meter`
29. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
30. Hapus `Filter Probe {runId}-118` lewat API hingga terhapus

### TC-AC-DN-352: Edit nama yang membuat baris tidak cocok Search

31. Buat `Door Antenna Uji {runId}-118` (Measurement `Unit`, Category `Antenna`) lewat API hingga tersimpan
32. Ketik Search `Door Antenna Uji {runId}-118`, tekan Enter
33. Buka menu aksi pada baris `Door Antenna Uji {runId}-118`, klik `Edit`
34. Kosongkan field Device Name lalu ketik `Entry Antenna Uji {runId}-118`
35. Klik `[Save]`
36. Verifikasi toast sukses: "Success, device name has been updated."
37. Verifikasi baris `Entry Antenna Uji {runId}-118` hilang dari tabel karena tidak cocok keyword
38. Verifikasi tabel menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
39. Klik `(←)` pada kotak Search
40. Hapus `Entry Antenna Uji {runId}-118` lewat API hingga terhapus

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09, R-16): langkah 7, 17 sampai 19, 29, 39 mengembalikan seleksi, Filter, Search, dan Sidebar; langkah 30, 31, dan 40 menyiapkan dan menghapus record milik spec lewat API; langkah 32 (Search record target) dan langkah 33 menemukan baris target.
- Record milik spec (S-06, S-12, R-13): TC-AC-DN-352 mengubah `Door Antenna` Pre-setup; spec memakai record milik spec `Door Antenna Uji {runId}-118` dengan Search memakai nama lengkap itu (bukan `Door`), supaya `Door Antenna` Pre-setup tidak ikut cocok dan empty state tetap teramati. Data Pre-setup #16 tidak berubah.
- Urutan: TC-AC-DN-354 dijalankan sebelum TC-AC-DN-351 dan TC-AC-DN-352 (berbeda dari urutan sourceTc di indeks TC) supaya asersi baca-saja mendahului aksi Create dan Edit (S-10).
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (kombinasi kontrol List), satu dataset, satu kelas harness; tiap blok memulai dari kontrol yang dikembalikan ke awal dan record milik sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-351 dan TC-AC-DN-352 menyatakan hasil dipulihkan automation baseline sebagai Post Condition tanpa langkah observasi; tidak diasersi.
