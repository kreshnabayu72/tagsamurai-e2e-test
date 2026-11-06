---
id: TC-FA-TAG-E2E-327-defense-in-depth-izin-dicabut-saat-dialog-atau-halaman-terbuka-bagian-1
title: "Defense-in-Depth: Izin Update atau Scope Group Dicabut saat Dialog Replace atau Pair Terbuka, Submit Ditolak Server (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1281
  - TC-FA-TAG-1282
  - TC-FA-TAG-1283
coverage:
  web: automated
---

# Defense-in-Depth: Izin Update atau Scope Group Dicabut saat Dialog Replace atau Pair Terbuka, Submit Ditolak Server (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (`manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TAG_MU_UPA_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`) yang mencabut dan memulihkan akses Update serta assign group pengguna di Settings > Role & Permission, tanpa asersi di sesinya; akun Admin disediakan tim FE; (3) pembacaan state data lewat fixture backend (status aset dan Tag, jumlah entri Changelog; baseline dicatat di hook `before`); (4) seed dan pemulihan idempotent lewat fixture backend; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired | `aset220` |
| Aset Pair | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: akses Update dan assign group Plant A pengguna dicabut di langkah 4, 14, dan 24 dan dipulihkan di langkah 9, 18, dan 28; hook `after` memulihkan capability dan assign group pengguna walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 15, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 4, 9, 14, 18, 24, 28) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1281: Role Update dicabut saat Dialog Replace TAG terbuka

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Pelaku kedua (Admin) mencabut akses Update pengguna di Settings > Role & Permission lewat sesi API hingga tersimpan
5. Klik [Submit]
6. Verifikasi server menolak penggantian
7. Verifikasi Tag `RF-00330` tetap Paired pada 'Excavator 20 Ton - 220'
8. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
9. Pelaku kedua memulihkan akses Update pengguna lewat sesi API hingga tersimpan
10. Muat ulang halaman (F5)

### TC-FA-TAG-1282: Scope group dicabut saat Dialog Replace TAG terbuka

11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Pelaku kedua (Admin) mencabut assign Group Plant A dari pengguna lewat sesi API hingga tersimpan
15. Klik [Submit]
16. Verifikasi server menolak penggantian
17. Verifikasi Tag `RF-00330` tetap Paired
18. Pelaku kedua memulihkan assign Group Plant A pengguna lewat sesi API hingga tersimpan
19. Muat ulang halaman (F5)

### TC-FA-TAG-1283: Role Update dicabut saat Dialog Pair TAG terbuka

20. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
21. Klik `Show` di samping `Not Paired Yet`
22. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
24. Pelaku kedua (Admin) mencabut akses Update pengguna lewat sesi API hingga tersimpan
25. Klik [Submit]
26. Verifikasi server menolak pairing
27. Verifikasi AST-0051 tetap Not Paired Yet
28. Pelaku kedua memulihkan akses Update pengguna lewat sesi API hingga tersimpan
29. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1281 s.d. 1283). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1284 dan TC-FA-TAG-1313 ada di spec 352 (izin dicabut saat dialog Print QR dan halaman terbuka); TC-FA-TAG-1303 s.d. 1305 ada di spec 328 (izin dicabut saat dialog Receive, Receive Manually, dan Decline Report terbuka).
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 4, 9, 14, 18, 24, 28). Langkah 5, 15, dan 25 memicu penolakan sesudah pencabutan tersimpan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 18, dan 28 (memulihkan capability atau assign group), 10, 19, dan 29 (muat ulang halaman untuk menutup dialog dirty dan menyegarkan capability di UI; dialog `beforeunload` ditangani sesuai Prerequisites).
- Asersi "jumlah entri Changelog tidak bertambah" (langkah 8) ditulis di spec ini dengan baseline (S-12) dan didahului `Verifikasi` respons penolakan dan state Tag sebagai anchor; spec absence kelas g milik modul ini tidak memuat TC-FA-TAG-1281.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 15, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Aksi lain lewat sesi API (langkah 4, 9, 14, 18, 24, 28) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1281 s.d. 1283 tidak menyebut perilaku UI sesudah penolakan (dialog tetap terbuka atau menutup, ada toast atau tidak); spec hanya mengasersi "server menolak" tanpa teks pesan.
  - Post Condition TC-FA-TAG-1283 ("Tag `RF-00412` tetap Available") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1282 mensyaratkan pencabutan assign group tanpa menyebut menu admin; spec menulis aksi seperti di TC lewat sesi API.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
