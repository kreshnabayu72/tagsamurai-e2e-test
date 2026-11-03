---
id: TC-FA-TAG-E2E-319-replace-tag-saat-transaksi-berjalan-diizinkan-dan-disposal-bagian-1
title: "Replace TAG saat Transaksi Berjalan: Aset Assigned, Menunggu Serah Terima, In Transfer Process, dan Under Maintenance"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1224
  - TC-FA-TAG-1226
  - TC-FA-TAG-1227
  - TC-FA-TAG-1229
coverage:
  web: automated
---

# Replace TAG saat Transaksi Berjalan: Aset Assigned, Menunggu Serah Terima, In Transfer Process, dan Under Maintenance

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dengan satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin; seed dan pemulihan idempotent aset, Tag per status registri (Paired, Available), transaksi, dan sesi opname lewat fixture backend; pembacaan state backend (status aset dan data transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0020` ('Excavator 20 Ton - 20', Group Plant B) dengan Tag RFID `RF-00130` berstatus Paired; Tag RFID `RF-00500` berstatus Available di registri Global. Keadaan awal di hook `before`: aset berstatus Assigned (TC pertama di spec ini). Tiap TC memakai status aset yang berbeda sehingga keadaan aset disiapkan ulang lewat fixture BE sebelum TC berikutnya (langkah penghubung).
- Nama dan kode literal TC (aset `AST-0020` dan Tag `RF-00130`, `RF-00500`) tidak diberi suffix `{runId}` karena precondition dan asersi TC bergantung pada kode persis. Lampiran A belum memuat butir modul ini; seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE dicatat sebagai kebutuhan, dan suite berjalan serial.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0020`, Tag `RF-00130` dan `RF-00500` (status registri Global), transaksi, dan status reader simulator ke keadaan awal.
- State global: stok Tag RFID di registri Global dan status Tag pengganti diubah spec ini dan dipulihkan di hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1224: Replace TAG pada aset berstatus Assigned diizinkan

1. Buka Popup Assets group Plant B
2. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
3. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
4. Klik `[Submit]`
5. Verifikasi toast "Success, TAG has been replaced." tampil
6. Verifikasi status aset tetap Assigned (dibaca lewat kemampuan baca state backend)
7. Verifikasi transaksi berjalan tidak berubah (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1226: Replace TAG pada aset berstatus Menunggu serah terima atau approval transaksi diizinkan

8. Tutup Popup Assets
9. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus Menunggu serah terima atau approval transaksi; Tag `RF-00500` Available di Global
10. Buka Popup Assets group Plant B
11. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
12. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
13. Klik `[Submit]`
14. Verifikasi toast "Success, TAG has been replaced." tampil
15. Buka layar serah terima transaksi untuk aset `AST-0020`
16. Pindai Tag baru `RF-00500` dengan simulator reader
17. Verifikasi serah terima memindai Tag baru `RF-00500`

### TC-FA-TAG-1227: Replace TAG pada aset berstatus In Transfer Process diizinkan

18. Buka menu Fixed Asset > TAG lewat sidebar, tab Paired
19. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus In Transfer Process; Tag `RF-00500` Available di Global
20. Buka Popup Assets group Plant B
21. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
22. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
23. Klik `[Submit]`
24. Verifikasi toast "Success, TAG has been replaced." tampil
25. Buka layar Receive di tujuan untuk aset `AST-0020`
26. Jalankan langkah "Receive di tujuan" dengan Tag yang tidak terbaca
27. Verifikasi Receive di tujuan memakai identifikasi manual: tombol `[I can't scan the TAG]` tersedia

### TC-FA-TAG-1229: Replace TAG pada aset berstatus Under Maintenance diizinkan

28. Buka menu Fixed Asset > TAG lewat sidebar, tab Paired
29. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus Under Maintenance; Tag `RF-00500` Available di Global
30. Buka Popup Assets group Plant B
31. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
32. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
33. Klik `[Submit]`
34. Verifikasi toast "Success, TAG has been replaced." tampil

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1225 dan 1228 ada di spec 322. TC-FA-TAG-1230 sampai 1232 ada di spec 320.
- Langkah penghubung (tanpa awalan `Verifikasi`): 8, 9, 18, 19, 28, 29 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Temuan untuk QA:
  - TC-FA-TAG-1224 Expected b ("transaksi berjalan tidak berubah") dan TC-FA-TAG-1226/1227 Expected b tidak menyebut tempat teramatinya; spec membaca status aset dan data transaksi lewat kemampuan baca state backend (disediakan tim FE/BE).
  - TC-FA-TAG-1227 Expected b ("Receive di tujuan memakai identifikasi manual bila Tag tidak terbaca") bersyarat dan tidak menyebut hasil yang diamati; spec mengasersi bahwa tombol `[I can't scan the TAG]` tersedia saat Tag tidak terbaca.
  - TC-FA-TAG-1224 sampai 1229 menyebut status aset "Menunggu serah terima atau approval transaksi" dan "Sesi opname berjalan" sebagai status; TC tidak menjabarkan keadaan konkretnya, sehingga cara menyiapkannya diserahkan ke fixture BE (disediakan tim FE/BE).
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
