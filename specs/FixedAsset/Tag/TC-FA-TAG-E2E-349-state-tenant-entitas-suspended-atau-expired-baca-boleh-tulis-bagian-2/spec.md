---
id: TC-FA-TAG-E2E-349-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-2
title: "State Tenant: Entitas Suspended atau Expired Menolak Start Print, Receive TAG, dan Receive Manually dengan Pesan V-22 (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1289
  - TC-FA-TAG-1296
  - TC-FA-TAG-1297
  - TC-FA-TAG-1298
coverage:
  web: automated
---

# State Tenant: Entitas Suspended atau Expired Menolak Start Print, Receive TAG, dan Receive Manually dengan Pesan V-22 (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah status entitas Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di dialog Receive TAG; (2) perubahan status entitas Client menjadi Suspended lewat fixture backend, dan menjadi Expired oleh pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); hook `before` menyetel Suspended dan hook `after` memulihkan status Active; akun Admin disediakan tim FE; (3) pengamatan dialog cetak browser (untuk memastikan dialog tidak terbuka); (4) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Quantity Print QR | 2 | `qtyPrint` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |

- State yang diubah dan pemulihannya: entitas Client berstatus Suspended dari awal spec (diatur hook `before`) dan menjadi Expired di langkah 22; semua commit ditolak sehingga Tag tidak berubah status. Hook `after` memulihkan status entitas Client ke Active walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-1289: Start Print saat Suspended

1. Klik tombol `Print QR`
2. Isi `Quantity` dengan 2
3. Klik [Start Print]
4. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
5. Verifikasi dialog cetak browser tidak terbuka
6. Verifikasi dialog Print QR tetap terbuka
7. Muat ulang halaman (F5)

### TC-FA-TAG-1296: Receive TAG saat Suspended

8. Buka tab To Be Returned lalu klik tombol "Receive TAG"
9. Pindai Tag RF-00071
10. Klik tombol [Receive]
11. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
12. Verifikasi dialog tidak menutup sebagai sukses
13. Verifikasi tidak ada toast sukses
14. Muat ulang halaman (F5)

### TC-FA-TAG-1298: Receive Manually saat Suspended

15. Buka tab To Be Returned lalu buka menu aksi baris RF-00071 dan klik "Receive Manually"
16. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
17. Klik tombol [Submit]
18. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
19. Verifikasi dialog tidak menutup sebagai sukses
20. Verifikasi tidak ada toast sukses
21. Muat ulang halaman (F5)

### TC-FA-TAG-1297: Receive TAG saat Expired

22. Pelaku kedua (Admin) mengubah status entitas Client menjadi Expired lewat sesi API hingga tersimpan
23. Buka tab To Be Returned lalu klik tombol "Receive TAG"
24. Pindai Tag RF-00071
25. Klik tombol [Receive]
26. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
27. Verifikasi dialog tidak menutup sebagai sukses
28. Verifikasi tidak ada toast sukses
29. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1289, 1296, 1297, 1298). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-1289, 1296, 1298 (Suspended), lalu 1297 (Expired), supaya status entitas hanya berubah satu kali.
- Pembagian TC lintas spec: Submit Replace, Pair, dan Batch saat Suspended atau Expired (TC-FA-TAG-1285 sampai 1288) ada di spec 348 dan 385; Report TAG dan Cancel Report (TC-FA-TAG-1299, 1300, 1302) ada di spec 350; Decline Report dan halaman baca-saja (TC-FA-TAG-1301, 1317) ada di spec 385.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7, 14, 21, dan 29 (muat ulang halaman untuk menutup dialog; dialog `beforeunload` ditangani sesuai Prerequisites), 8, 15, dan 23 (membuka tab To Be Returned sesudah muat ulang halaman), 22 (mengubah status entitas, pemicu pelaku kedua lewat sesi API).
- Pesan pada langkah 4, 11, 18, dan 26 diasersi sebagai teks tampil tanpa menentukan jenis elemen (toast atau pesan inline) karena TC hanya menyebut "Pesan"; langkah 13, 20, dan 28 (tidak ada toast sukses) didahului `Verifikasi` pesan penolakan sebagai anchor positif.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1289 ("Tidak ada kode QR yang dibuat") dan TC-FA-TAG-1296 sampai 1298 ("Tag RF-00071 tetap To Be Returned; tidak ada entri Event Log, TAG Log, maupun Changelog baru") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1289 menyebut reader tersambung sebagai precondition padahal Print QR tidak memindai Tag; spec tidak memakainya.
  - Nama dan kode literal Pre-setup (kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
