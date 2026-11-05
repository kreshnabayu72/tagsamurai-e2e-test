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
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00330` Paired) | `aset220` |
| Stok Global Available | Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |

- State yang diubah dan pemulihannya: entitas Client berstatus Suspended dari awal spec (diatur hook `before`) dan menjadi Expired di langkah 27; semua commit ditolak sehingga laporan dan Tag tidak berubah. Hook `after` memulihkan status entitas Client ke Active walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 31 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan. Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.

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
12. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil
13. Klik Asset Name 'Excavator 20 Ton' / Plant B
14. Verifikasi Popup Detail 'Excavator 20 Ton' / Plant B terbuka dan memuat baris detail
15. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil
16. Tutup Popup Detail dengan ikon close
17. Klik tombol `Changelog` pada Table Tools
18. Verifikasi Modal Changelog Paired TAG terbuka
19. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil
20. Tutup Modal Changelog
21. Buka tab To Be Returned
22. Klik tombol "Event Log"
23. Verifikasi Modal Event Log To Be Returned terbuka
24. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil (aksi baca tidak memicu V-22)
25. Tutup Modal Event Log
26. Buka tab Paired

### TC-FA-TAG-1286: Submit Replace saat Expired

27. Pelaku kedua (Admin) mengubah status entitas Client menjadi Expired lewat sesi API hingga tersimpan
28. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
29. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
30. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
31. Klik [Submit]
32. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
33. Verifikasi (lewat fixture BE) Tag `RF-00330` tetap Paired
34. Muat ulang halaman (F5)
35. Klik tombol `Changelog`
36. Verifikasi Modal Changelog Paired TAG terbuka
37. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada entri baru)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1286, 1301, 1317). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-1301 dan 1317 (Suspended), lalu 1286 (Expired), supaya status entitas hanya berubah satu kali.
- Pembagian TC lintas spec: Submit Replace, Pair, dan Batch saat Suspended (TC-FA-TAG-1285, 1287, 1288) ada di spec 348; Start Print, Receive TAG, dan Receive Manually (TC-FA-TAG-1289, 1296 sampai 1298) ada di spec 349; Report TAG dan Cancel Report (TC-FA-TAG-1299, 1300, 1302) ada di spec 350.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 dan 34 (muat ulang halaman untuk menutup dialog yang berisi isian; dialog `beforeunload` ditangani sesuai Prerequisites), 20, 25 (menutup modal), 26 (membuka kembali tab Paired sesudah Event Log), 27 (mengubah status entitas, pemicu pelaku kedua lewat sesi API).
- Pesan pada langkah 6 dan 32 diasersi sebagai teks tampil tanpa menentukan jenis elemen (toast atau pesan inline) karena TC hanya menyebut "Pesan"; langkah 8 (tidak ada toast sukses) didahului `Verifikasi` pesan penolakan (langkah 6) sebagai anchor positif. Toast error V-22 pada TC-FA-TAG-1317 butir e diasersi tidak tampil segera setelah tiap aksi baca TC (langkah 12, 15, 19, dan 24 untuk langkah TC 1, 2, 4, dan 5; bagian 8b butir 11), masing-masing didahului `Verifikasi` elemen halaman yang tampil (langkah 11, 14, 18, dan 23) sebagai anchor positif.
- Asersi tidak ada entri log baru (langkah 37, TC-FA-TAG-1286 butir c) memakai pengecualian kelas h (S-05, prinsip 13g): objek uji TC state tenant ini adalah penolakan aksi tulis, sehingga asersi berada di spec ini sendiri dengan `Verifikasi` selisih jumlah entri Changelog Paired TAG terhadap baseline yang dicatat di hook `before` (S-12, satu surface log).
- Alasan spec ini 37 langkah (di atas ambang sekitar 35 langkah): ketiga blok memakai satu kelas harness (FE+BE dengan perubahan status entitas Client) dan berdiri sendiri, dan memecahnya memaksa status entitas Client diubah lebih dari sekali (lihat urutan TC di atas); tiga langkah tambahan berasal dari butir e TC-FA-TAG-1317 yang meminta absence toast V-22 segera setelah tiap aksi baca.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 31 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Expected TC-FA-TAG-1286 butir b ("Tag `RF-00330` tetap Paired") tidak punya langkah observasi di UI pada TC; spec mengasersinya lewat pembacaan state data fixture BE (S-11).
  - Changelog tidak memuat entri baru (TC-FA-TAG-1286 butir c): Changelog adalah audit trail permanen sehingga spec memakai baseline jumlah entri yang dicatat di hook `before` (S-12).
  - Post Condition TC-FA-TAG-1286 ("Tidak ada perubahan data dan tidak ada log"), TC-FA-TAG-1301 ("Laporan RF-00130 tetap terbuka; tidak ada entri ...") dan TC-FA-TAG-1317 tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
