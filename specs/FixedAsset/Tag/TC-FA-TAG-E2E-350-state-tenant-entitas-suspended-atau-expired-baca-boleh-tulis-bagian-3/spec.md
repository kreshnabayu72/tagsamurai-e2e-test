---
id: TC-FA-TAG-E2E-350-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-3
title: "State Tenant: Entitas Suspended atau Expired Menolak Report TAG dan Cancel Report dengan Pesan V-22 (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1299
  - TC-FA-TAG-1300
  - TC-FA-TAG-1302
coverage:
  web: automated
---

# State Tenant: Entitas Suspended atau Expired Menolak Report TAG dan Cancel Report dengan Pesan V-22 (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Staff Auditor (tidak memegang Manage asset & TAG) (`staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD`). Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah status entitas Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) perubahan status entitas Client menjadi Suspended lewat fixture backend, dan menjadi Expired atau kembali Suspended oleh pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); hook `before` menyetel Suspended dan hook `after` memulihkan status Active; akun Admin disediakan tim FE; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, task Existence Audit, dan laporan Tag terbuka; (3) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal [RFID] RF-00130 tanpa laporan terbuka saat spec mulai; item In Audit pada task Existence Audit milik spec | `aset20Laporan` |
| Report Type | Damaged | `reportType` |
| Note | Label retak | `noteReport` |
| Reason Cancel Report | Tag ternyata terbaca | `reasonCancel` |

- State yang diubah dan pemulihannya: entitas Client berstatus Suspended dari awal spec (diatur hook `before`), menjadi Expired di langkah 10, dan kembali Suspended di langkah 20; langkah 19 membuat laporan terbuka Damaged untuk `RF-00130` (precondition TC-FA-TAG-1302). Semua commit di spec ini ditolak. Hook `after` memulihkan status entitas Client ke Active dan menghapus laporan serta task Existence Audit walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 19). Aksi tulis pada langkah 5, 14, 24 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 10, 20) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1299: Report TAG saat Suspended

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris 'Excavator 20 Ton - 20'
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Klik tombol [Submit]
6. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
7. Verifikasi dialog tidak menutup sebagai sukses
8. Verifikasi tidak ada toast sukses
9. Muat ulang halaman (F5)

### TC-FA-TAG-1300: Report TAG saat Expired

10. Pelaku kedua (Admin) mengubah status entitas Client menjadi Expired lewat sesi API hingga tersimpan
11. Pilih row action "Report TAG" pada baris 'Excavator 20 Ton - 20'
12. Pilih Report Type "Damaged"
13. Isi Textarea "Note" dengan "Label retak"
14. Klik tombol [Submit]
15. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
16. Verifikasi dialog tidak menutup sebagai sukses
17. Verifikasi tidak ada toast sukses
18. Muat ulang halaman (F5)

### TC-FA-TAG-1302: Cancel Report saat Suspended

19. Buat laporan terbuka Damaged untuk Tag RF-00130 dari Staff Auditor lewat fixture BE hingga tersimpan
20. Pelaku kedua (Admin) mengubah status entitas Client menjadi Suspended lewat sesi API hingga tersimpan
21. Muat ulang halaman (F5)
22. Pilih row action "Cancel Report TAG" pada baris 'Excavator 20 Ton - 20'
23. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
24. Klik tombol [Cancel Report]
25. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
26. Verifikasi dialog tidak menutup sebagai sukses
27. Verifikasi tidak ada toast sukses
28. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1299, 1300, 1302). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-1299 (Suspended), 1300 (Expired), lalu 1302 (Suspended). TC-FA-TAG-1299 dan 1300 mensyaratkan Tag tanpa laporan terbuka, sedangkan TC-FA-TAG-1302 mensyaratkan laporan terbuka, sehingga laporan dibuat sesudah kedua TC pertama (langkah 19).
- Pembagian TC lintas spec: Submit Replace, Pair, dan Batch (TC-FA-TAG-1285 sampai 1288) ada di spec 348 dan 385; Start Print, Receive TAG, dan Receive Manually (TC-FA-TAG-1289, 1296 sampai 1298) ada di spec 349; Decline Report dan halaman baca-saja (TC-FA-TAG-1301, 1317) ada di spec 385.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 18, 21, dan 28 (muat ulang halaman untuk menutup dialog yang berisi isian atau menyegarkan daftar item; dialog `beforeunload` ditangani sesuai Prerequisites), 10 dan 20 (mengubah status entitas, pemicu pelaku kedua lewat sesi API), 19 (membuat laporan terbuka lewat fixture BE hingga tersimpan).
- Pesan pada langkah 6, 15, dan 25 diasersi sebagai teks tampil tanpa menentukan jenis elemen (toast atau pesan inline) karena TC hanya menyebut "Pesan"; langkah 8, 17, dan 27 (tidak ada toast sukses) didahului `Verifikasi` pesan penolakan sebagai anchor positif.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 19). Aksi tulis pada langkah 5, 14, 24 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 10, 20) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1299 dan 1300 ("Tidak ada laporan baru untuk RF-00130; tidak ada entri Event Log, TAG Log, maupun Changelog baru") dan TC-FA-TAG-1302 ("Laporan RF-00130 tetap terbuka; ...") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
