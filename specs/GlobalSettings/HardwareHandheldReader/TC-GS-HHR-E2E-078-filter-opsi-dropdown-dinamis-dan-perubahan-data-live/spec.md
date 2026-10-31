---
id: TC-GS-HHR-E2E-078-filter-opsi-dropdown-dinamis-dan-perubahan-data-live
title: "Filter Daftar Reader Handheld Reader: Opsi Dropdown Device Name Bertambah Setelah Aktivasi, Opsi Aktif Dibersihkan Setelah Reader Dihapus Admin Lain, dan Loading serta No options available pada Client Tanpa Reader"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-255
  - TC-GS-HHR-256
  - TC-GS-HHR-456
coverage:
  web: automated
---

# Filter Daftar Reader Handheld Reader: Opsi Dropdown Device Name Bertambah Setelah Aktivasi, Opsi Aktif Dibersihkan Setelah Reader Dihapus Admin Lain, dan Loading serta No options available pada Client Tanpa Reader

## Prerequisites

- Mode: FE+BE (backend nyata). Intercept respons dipakai pada TC-GS-HHR-255 untuk menahan respons request pemuat opsi filter.
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Admin B (langkah 20, TC-GS-HHR-256): Total Control Client A kedua, `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Nadia Pratama), `Spectra.env.GS_TC2_PASSWORD`. Admin B hanya memakai sesi API yang menghapus reader DD-08 (kemampuan sesi API aktor dinyatakan di `suite.md`); tidak ada sesi UI kedua.
- Akun kedua (langkah 27 dan 28, TC-GS-HHR-255): Total Control Client E, `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client E (Client E belum memiliki reader, entri Changelog, maupun Event Log; alokasi `Short Range` 2 dan `Long Range` 2), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps` kecuali setelah ganti akun.
- Client A: plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, alokasi `Short Range` 8 dan `Long Range` 6, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini). Kuota `Long Range` Client A 5 dari 6 sehingga satu aktivasi `Long Range` masih diizinkan.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): 10 reader DD-01 sampai DD-10, dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dan dipulihkan antar TC oleh fixture backend. Pengecualian S-12 Population Seed Reader A HHR: nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, opsi dropdown DISTINCT, dan jumlah opsi. Baris dikenali lewat Serial Number:

| ID | Device Name | Serial Number | Range Type | Status |
|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | SN-HHR-00101 | Long Range | Available |
| DD-02 | Gudang Reader - 1 | SN-HHR-00102 | Short Range | Available |
| DD-03 | Zebra Mobile Reader - 1 | SN-HHR-00103 | Long Range | Damaged |
| DD-04 | Gudang Reader - 2 | SN-HHR-00104 | Short Range | Missing |
| DD-05 | Chainway C72 - 1 | SN-HHR-00105 | Long Range | Waiting for Approval |
| DD-06 | Zebra RFID Reader - 1 | SN-HHR-00107 | Short Range | Available |
| DD-07 | Honeywell CK65 - 1 | SN-HHR-00108 | Long Range | Available |
| DD-08 | Unitech EA520 - 1 | SN-HHR-00109 | Short Range | Available |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | SN-HHR-00110 | Long Range | Available |
| DD-10 | Gudang Reader - 4 | SN-HHR-00205 | Short Range | Waiting for Approval |

- Tabel "Opsi Device Name awal" (9 opsi, hasil DISTINCT dari Seed Reader A; DD-01 dan DD-06 memakai nama yang sama dan tampil satu kali): `Chainway C72 - 1`, `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`, `Honeywell CK65 - 1`, `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1`, `Unitech EA520 - 1`, `Zebra Mobile Reader - 1`, `Zebra RFID Reader - 1`.
- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap blok TC membuka panel sendiri dan menutupnya di akhir blok.
- TC-GS-HHR-456 (langkah 1 sampai 15): simulator reader USB dengan Serial Number SN-HHR-00201 (HS-01: SKU-HHR-01 Zebra RFID Reader, Long Range, Zebra / RFD40, Current Power 22 dBm, stok Hardware Stock Principal berstatus `Available`) tersambung ke komputer desktop dan driver lokal terpasang; kemampuan simulator dan driver disediakan tim FE (mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; lihat "Temuan untuk QA"). Reader baru `Zebra RFID Reader - 2` yang dibuat spec dan pemulihan stok SN-HHR-00201 ke `Available` dibersihkan hook `after` (disediakan tim FE/BE; tidak berasumsi aktivasi berhasil penuh).
- TC-GS-HHR-256 (langkah 16 sampai 26): penghapusan reader DD-08 oleh Admin B lewat sesi API; DD-08 dipulihkan oleh fixture backend sesudah spec.
- TC-GS-HHR-255 (langkah 27 sampai 39): kemampuan teknis menahan respons request pemuat opsi dropdown filter (intercept respons tertunda) lalu melepasnya; endpoint request opsi filter tidak tertulis di TC, PRD, atau LLD yang dirujuk spec ini sehingga tidak ditulis di sini (lihat "Temuan untuk QA"). Intercept dilepas pada langkah 35 sebelum asersi akhir.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control Client A dan hook `after` memulihkannya (lihat `suite.md`); untuk akun Client E flag diatur hook yang sama (disediakan tim FE).
- Suite serial (`parallel: false`): spec mengubah data (aktivasi reader baru pada TC-GS-HHR-456, penghapusan DD-08 pada TC-GS-HHR-256), dipulihkan seperti dinyatakan di atas.

## Test Steps

### TC-GS-HHR-456: Opsi Device Name bertambah setelah aktivasi tanpa reload

1. Klik ikon Filter untuk membuka panel
2. Buka dropdown `Device Name`
3. Verifikasi dropdown `Device Name` memuat 9 opsi sesuai tabel "Opsi Device Name awal"
4. Verifikasi opsi `Zebra RFID Reader - 2` tidak ada
5. Klik ikon Filter untuk menutup panel
6. Klik `[+ Activate Reader]`
7. Klik `Long Range` pada Overlay `Select Range Type`
8. Klik `[Sync]` (reader USB SN-HHR-00201)
9. Klik `[Submit]`
10. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
11. Klik ikon Filter untuk membuka panel
12. Buka dropdown `Device Name`
13. Verifikasi dropdown `Device Name` memuat 10 opsi tanpa reload halaman
14. Verifikasi opsi `Zebra RFID Reader - 2` ada di dropdown
15. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-256: Opsi filter aktif yang recordnya dihapus admin lain dibersihkan

16. Klik ikon Filter untuk membuka panel
17. Pilih `Unitech EA520 - 1` pada field `Device Name`
18. Klik `[Apply]`
19. Tunggu aksi selesai (permintaan `[Apply]` selesai dan tabel menampilkan hasil filter)
20. Pada sesi API Admin B hapus reader DD-08 (`Unitech EA520 - 1`) hingga tersimpan
21. Pada sesi pertama klik `[Apply]` lagi
22. Verifikasi tidak ada crash atau pesan error pada halaman
23. Verifikasi nilai `Unitech EA520 - 1` dibersihkan dari kriteria (field `Device Name` tanpa chip)
24. Verifikasi sedikitnya satu baris reader tampil pada tabel
25. Verifikasi baris `Unitech EA520 - 1` tidak ada di tabel
26. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-255: Dropdown filter menampilkan loading dan No options available (Client E)

27. Logout dari akun Total Control Client A (ganti akun)
28. Login sebagai Total Control Client E (`Spectra.env.GS_CLIENTE_TC_PASSWORD`)
29. Buka Global Settings > Hardware > Handheld Reader
30. Tahan respons request pemuat opsi filter (penundaan respons)
31. Klik ikon Filter untuk membuka panel
32. Buka dropdown `Status` selama request tertunda
33. Verifikasi dropdown `Status` menampilkan skeleton atau spinner
34. Tutup dropdown `Status`
35. Lepas penundaan respons
36. Buka dropdown `Status`
37. Verifikasi teks `No options available` tampil di dropdown `Status`
38. Verifikasi tidak ada pesan error
39. Klik ikon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 456, 256, lalu 255 (urutan TC sumber: 255, 256, 456). TC-GS-HHR-456 menambah satu reader dan TC-GS-HHR-256 menghapus DD-08 (aksi yang mengubah data); 456 sebelum 256 supaya baseline 9 opsi pada 456 belum terpengaruh penghapusan DD-08. TC-GS-HHR-255 memakai akun Client E dan ditaruh paling akhir karena ada langkah ganti akun eksplisit (langkah 27 dan 28); bagian itu tetap bermakna walau dua blok sebelumnya gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, tutup dropdown, langkah 10 ("Tunggu aksi selesai" sesudah `[Submit]` aktivasi; TC tidak menyebut hasil `[Submit]`) dan langkah 19 ("Tunggu aksi selesai" sesudah `[Apply]` sebelum aktor berpindah ke sesi API Admin B).
- Kelas harness: spec ini satu kelas harness (kelas d). TC-GS-HHR-456 satu-satunya yang memakai harness eksternal (simulator reader USB untuk `[Sync]`). TC-GS-HHR-256 memakai sesi API Admin B sebagai pelaku kedua yang hanya memicu penghapusan DD-08 sementara asersi dilakukan di sesi pertama; pelaku kedua lewat sesi API bukan konteks kedua kelas c. TC-GS-HHR-255 menahan respons hanya untuk mengamati state loading (bukan kelas b) dan penahanan dilepas pada langkah 35.
- Anchor absence: langkah 4 (opsi `Zebra RFID Reader - 2` tidak ada) didahului `Verifikasi` 9 opsi lain yang tampil di dropdown yang sama; langkah 25 didahului `Verifikasi` sedikitnya satu baris reader tampil (langkah 24); langkah 38 (tidak ada pesan error) didahului `Verifikasi` teks `No options available` (langkah 37).
- Tidak ada asersi tambahan di luar Expected TC selain `Verifikasi` "sedikitnya satu baris reader tampil" (langkah 24, anchor). Pembagian TC lintas spec: Screening, DISTINCT, kombinasi, chip, dan indikator Filter Panel (TC-GS-HHR-239 sampai 259) ada di spec 051; Filter rentang ada di spec 052.
- Pengecualian S-12 Population Seed Reader A HHR dipakai untuk Seed Reader A (nama literal tanpa suffix `{runId}`); suite berjalan serial dan pemulihan lewat fixture backend dinyatakan di Prerequisites dan `suite.md`.
- Spec memuat 39 langkah nominal (tanpa blok ulang; sedikit di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik (opsi dropdown Filter Panel yang berubah mengikuti data live dan state loading) pada satu permukaan, tanpa blok ulang; tiga blok TC berdiri sendiri dan tiap blok menutup Filter Panel sebelum blok berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok ganti akun (255) di akhir tetap bermakna walau blok sebelumnya gagal.
- Temuan untuk QA:
  - TC-GS-HHR-255: endpoint request opsi filter dan mekanisme "penundaan respons" tidak didefinisikan di TC, PRD, atau LLD yang dirujuk; kebutuhan ditulis sebagai kemampuan teknis tanpa mengarang endpoint (S-13). Akun Total Control Client E mengikuti pola email fixture `totalControl_automated_{namaClient}@qwertysystem.net`; nilai persis tidak tertulis di Pre-setup TC.
  - TC-GS-HHR-456: mekanisme simulasi reader USB (Sync) dan pembersihan reader hasil aktivasi tidak didefinisikan di TC, PRD, atau LLD; TC berlabel Manual Only (membaca reader USB fisik). TC tidak menyebut hasil `[Submit]` (toast atau tabel) sehingga tidak diasersi; Expected b "tanpa reload halaman" diasersi pada langkah 14 dengan tidak melakukan reload di antara langkah.
  - TC-GS-HHR-256: berlabel Manual Only karena dua sesi paralel; spec memicu penghapusan DD-08 lewat sesi API Admin B. Expected b "hasil tabel mengikuti kriteria yang tersisa" tidak menyebut jumlah baris; spec mengasersi baris `Unitech EA520 - 1` tidak ada dengan anchor sedikitnya satu baris reader.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.
