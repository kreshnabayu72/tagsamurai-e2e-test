---
id: TC-FA-TAG-E2E-385-state-tenant-entitas-suspended-decline-report-baca-saja-dan-replace-expired
title: "State Tenant: Decline Report Ditolak saat Suspended, Halaman TAG Tetap Dapat Dibaca, dan Submit Replace Ditolak saat Expired (Bagian 4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1286
  - TC-FA-TAG-1301
  - TC-FA-TAG-1317
coverage:
  web: automated
---

# State Tenant: Decline Report Ditolak saat Suspended, Halaman TAG Tetap Dapat Dibaca, dan Submit Replace Ditolak saat Expired (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah status entitas Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) perubahan status entitas Client menjadi Suspended lewat fixture backend, dan menjadi Expired oleh pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); hook `before` menyetel Suspended dan hook `after` memulihkan status Active; akun Admin disediakan tim FE; (3) pembacaan state data lewat fixture backend (Tag Paired, jumlah entri Changelog; baseline Changelog dicatat di hook `before` karena audit trail permanen, sehingga asersi memakai selisih terhadap baseline); (4) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, stok Tag, dan laporan Tag terbuka; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Reason Decline Report | Tag masih terbaca | `reasonDecline` |
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00130` Paired) | `aset220` |
| Stok Global Available | Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |

- State yang diubah dan pemulihannya: entitas Client berstatus Suspended dari awal spec (diatur hook `before`) dan menjadi Expired di langkah 24; semua commit ditolak sehingga laporan dan Tag tidak berubah. Hook `after` memulihkan status entitas Client ke Active walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-1301: Decline Report saat Suspended

1. Klik Asset Name 'Excavator 20 Ton' pada baris group Plant B (Popup Assets)
2. Buka menu aksi baris 'Excavator 20 Ton - 20'
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik tombol [Submit]
6. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
7. Verifikasi dialog tidak menutup sebagai sukses
8. Verifikasi tidak ada toast sukses
9. Muat ulang halaman (F5)

### TC-FA-TAG-1317: Halaman TAG hanya dapat dibaca

10. Klik menu `TAG` pada sidebar Fixed Asset
11. Verifikasi halaman TAG terbuka penuh dan tabel grup memuat keempat grup Pre-setup
12. Klik Asset Name 'Excavator 20 Ton' / Plant B
13. Verifikasi Popup Detail 'Excavator 20 Ton' / Plant B terbuka dan memuat baris detail
14. Tutup Popup Detail dengan ikon close
15. Klik tombol `Changelog` pada Table Tools
16. Verifikasi Modal Changelog Paired TAG terbuka
17. Tutup Modal Changelog
18. Buka tab To Be Returned
19. Klik tombol "Event Log"
20. Verifikasi Modal Event Log To Be Returned terbuka
21. Verifikasi tidak ada pesan V-22 pada aksi baca
22. Tutup Modal Event Log
23. Buka tab Paired

### TC-FA-TAG-1286: Submit Replace saat Expired

24. Pelaku kedua (Admin) mengubah status entitas Client menjadi Expired lewat sesi API hingga tersimpan
25. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
26. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
27. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
28. Klik [Submit]
29. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
30. Verifikasi (lewat fixture BE) Tag `RF-00130` tetap Paired
31. Muat ulang halaman (F5)
32. Klik tombol `Changelog`
33. Verifikasi Modal Changelog Paired TAG terbuka
34. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada entri baru)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1286, 1301, 1317). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-1301 dan 1317 (Suspended), lalu 1286 (Expired), supaya status entitas hanya berubah satu kali.
- Pembagian TC lintas spec: Submit Replace, Pair, dan Batch saat Suspended (TC-FA-TAG-1285, 1287, 1288) ada di spec 348; Start Print, Receive TAG, dan Receive Manually (TC-FA-TAG-1289, 1296 sampai 1298) ada di spec 349; Report TAG dan Cancel Report (TC-FA-TAG-1299, 1300, 1302) ada di spec 350.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 dan 31 (muat ulang halaman untuk menutup dialog yang berisi isian; dialog `beforeunload` ditangani sesuai Prerequisites), 17, 22 (menutup modal), 23 (membuka kembali tab Paired sesudah Event Log), 24 (mengubah status entitas, pemicu pelaku kedua lewat sesi API).
- Pesan pada langkah 6 dan 29 diasersi sebagai teks tampil tanpa menentukan jenis elemen (toast atau pesan inline) karena TC hanya menyebut "Pesan"; langkah 8 (tidak ada toast sukses) dan langkah 21 (tidak ada pesan V-22) didahului `Verifikasi` pesan penolakan atau elemen halaman yang tampil (langkah 6, 11, 13, 16, 20) sebagai anchor positif.
- Temuan untuk QA:
  - Expected TC-FA-TAG-1286 butir b ("Tag `RF-00130` tetap Paired") tidak punya langkah observasi di UI pada TC; spec mengasersinya lewat pembacaan state data fixture BE (S-11).
  - Changelog tidak memuat entri baru (TC-FA-TAG-1286 butir c): Changelog adalah audit trail permanen sehingga spec memakai baseline jumlah entri yang dicatat di hook `before` (S-12).
  - Post Condition TC-FA-TAG-1286 ("Tidak ada perubahan data dan tidak ada log"), TC-FA-TAG-1301 ("Laporan RF-00130 tetap terbuka; tidak ada entri ...") dan TC-FA-TAG-1317 tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
