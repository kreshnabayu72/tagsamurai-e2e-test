---
id: TC-AC-DN-E2E-014-sidebar-persistensi-state
title: "Pilihan Node Sidebar: Refresh, Sub-tab, dan Setelah Edit"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-44
  - TC-AC-DN-45
  - TC-AC-DN-629
coverage:
  web: automated
---

# Pilihan Node Sidebar: Refresh, Sub-tab, dan Setelah Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Device Name inti (#16: `Door Antenna`, `Gate Antenna`), dan seed 120 Device Name (#17); baca-saja.
- Data Dinamis (milik spec ini): Device Name `Pindai Antena {runId}-014` (Measurement `Unit`, Category `Antenna`, tanpa SKU dan tanpa unit BYO), dibuat lewat API (disediakan tim FE/BE) pada langkah penghubung sebelum TC-AC-DN-629 dan dihapus di hook `after` (cleanup tidak berasumsi setup berhasil). TC-AC-DN-629 mengubah namanya menjadi `Pindai Antena Edit {runId}-014`; Device Name Pre-setup `Door Antenna` tidak diubah (S-06).
- Efek pada Pre-setup bersama: tidak ada. Pilihan node Sidebar dibersihkan di akhir tiap TC.

## Test Steps

### TC-AC-DN-44: Pilihan node Sidebar dipertahankan dan state expand pohon kembali ke kondisi awal setelah refresh halaman

1. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
2. Pilih node `Antenna` pada Category Sidebar
3. Refresh halaman dengan F5
4. Verifikasi halaman `Settings > Device > Device Name` tampil kembali dengan Category Sidebar terbuka
5. Verifikasi tidak ada error
6. Verifikasi state expand pohon Category kembali ke state awal: `Hardware` dan `Smart Fixed Reader` tertutup
7. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
8. Verifikasi node `Antenna` tetap terpilih di Category Sidebar (terlihat tercentang)
9. Verifikasi List tetap memuat dua baris berurutan: Door Antenna, Gate Antenna
10. Hapus pilihan node `Antenna`

### TC-AC-DN-45: Pilihan node Sidebar dipertahankan dan state expand pohon kembali ke kondisi awal setelah pindah ke sub-tab Device SKU lalu kembali

11. Pilih node `Antenna` pada Category Sidebar
12. Klik sub-tab `Device SKU`
13. Klik sub-tab `Device Name`
14. Verifikasi sub-tab `Device Name (aktif) | Device SKU`
15. Verifikasi Category Sidebar terbuka tanpa error
16. Verifikasi state expand pohon Category kembali ke state awal: `Hardware` dan `Smart Fixed Reader` tertutup
17. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
18. Verifikasi node `Antenna` tetap terpilih (terlihat tercentang)
19. Verifikasi List tetap memuat dua baris berurutan: Door Antenna, Gate Antenna
20. Hapus pilihan node `Antenna`

### TC-AC-DN-629: Pilihan node Category Sidebar dipertahankan setelah Edit Device Name

21. Buat Device Name `Pindai Antena {runId}-014` (Measurement `Unit`, Category `Antenna`) lewat API hingga tersimpan
22. Muat ulang halaman dengan F5
23. Pilih node `Antenna` pada Category Sidebar
24. Klik ikon `⋯` pada baris `Pindai Antena {runId}-014` lalu klik `Edit`
25. Kosongkan field Device Name lalu ketik "Pindai Antena Edit {runId}-014"
26. Klik `[Save]`
27. Verifikasi toast sukses: "Success, device name has been updated."
28. Verifikasi popup form tertutup
29. Verifikasi node `Antenna` tetap terpilih pada Category Sidebar
30. Verifikasi List tetap difilter dan memuat tiga baris berurutan: Door Antenna, Gate Antenna, Pindai Antena Edit {runId}-014
31. Verifikasi halaman aktif pada pagination tetap halaman 1
32. Hapus pilihan node `Antenna`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 10, 20, dan 32 melepas pilihan Sidebar antar-TC; langkah 21 membuat Device Name milik spec lewat API (pemicu data, bukan objek uji) dan langkah sesudahnya memuat ulang halaman supaya List memuatnya.
- TC-AC-DN-629 mengubah `Door Antenna` Pre-setup menjadi `Door Antenna Edit`; spec memakai Device Name milik spec `Pindai Antena {runId}-014` (kategori Antenna) sebagai target Edit supaya Pre-setup tidak berubah (S-06). Record itu dibuat setelah TC-AC-DN-44 dan TC-AC-DN-45 supaya Expected dua baris pada kedua TC itu tetap utuh; akibatnya Expected TC-AC-DN-629 "dua baris: Door Antenna Edit, Gate Antenna" ditulis tiga baris: Door Antenna, Gate Antenna, Pindai Antena Edit {runId}-014 (lihat Temuan untuk QA).
- Asersi "state expand kembali ke awal" ditulis sebelum langkah expand (bagian 8b butir 5), sesuai klausa TC "sebelum langkah 4 ... tertutup".
- TC-AC-DN-626 (reset oleh klik ulang menu, tab baru, dan login ulang) berada di spec 022 karena objek asersinya tab kedua.
- Temuan untuk QA:
  - TC-AC-DN-629 mengubah record Pre-setup `Door Antenna` (data inti bersama); spec memakai record milik spec sehingga jumlah baris Expected berbeda dari TC.
