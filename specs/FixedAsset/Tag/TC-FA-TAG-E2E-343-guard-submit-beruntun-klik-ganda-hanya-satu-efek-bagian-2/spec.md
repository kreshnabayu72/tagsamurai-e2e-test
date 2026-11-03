---
id: TC-FA-TAG-E2E-343-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-2
title: "Guard Klik Ganda: Submit Decline Report dan Submit Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-646
  - TC-FA-TAG-1344
coverage:
  web: automated
---

# Guard Klik Ganda: Submit Decline Report dan Submit Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 2)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial yang menahan respons Submit Decline Report dan Submit Replace beberapa detik dan menghitung request yang terkirim, lalu melepas tahanan respons (precondition TC-FA-TAG-1344; TC-FA-TAG-646 tidak menyebutnya, spec memakai kemampuan yang sama agar state loading teramati); hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, dan laporan Tag terbuka; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Reason Decline Report | Tag masih terbaca | `reasonDecline` |
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00130` Paired) | `aset220` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: Decline Report di langkah 7 menutup laporan RF-00130 (Declined); langkah 17 mengganti Tag AST-0220 dari `RF-00130` menjadi `RF-00412`. Hook `after` memulihkan laporan, AST-0220 ke `RF-00130` Paired, dan `RF-00412` ke Available lewat fixture backend, serta melepas intercept, walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-646: Submit Decline Report ditekan beruntun

1. Klik Asset Name 'Excavator 20 Ton' pada baris group Plant B (Popup Assets)
2. Buka menu aksi baris 'Excavator 20 Ton - 20'
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Pasang intercept yang menahan respons Decline Report beberapa detik dan menghitung request
6. Tunggu toast lama hilang otomatis
7. Klik tombol [Submit] dua kali beruntun dengan cepat
8. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading
9. Lepas tahanan respons dan intercept
10. Verifikasi hanya satu Toast sukses tampil
11. Muat ulang halaman (F5)

### TC-FA-TAG-1344: Klik ganda cepat pada Submit Replace

12. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Pasang intercept yang menahan respons Submit Replace beberapa detik dan menghitung request
16. Tunggu toast lama hilang otomatis
17. Klik [Submit] dua kali beruntun cepat
18. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading
19. Lepas tahanan respons dan intercept
20. Verifikasi hanya satu request terkirim
21. Verifikasi hanya satu Toast "Success, TAG has been replaced."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-646 dan 1344). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: klik ganda pada Receive, Start Print, dan pindaian beruntun (TC-FA-TAG-257, 494, 566) ada di spec 342; Submit Pair dan Submit & next sesi Batch (TC-FA-TAG-1348, 1349) ada di spec 344; Submit Report TAG dan Cancel Report (TC-FA-TAG-619, 669) ada di spec 351; Submit Receive Manually (TC-FA-TAG-587) ada di spec 383.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 dan 15 (memasang intercept penahan respons), 6 dan 16 (menunggu toast lama hilang otomatis sebelum hitungan toast), 9 dan 19 (melepas tahanan respons dan intercept), 11 (muat ulang halaman untuk menutup Popup Detail dan membersihkan state).
- Langkah 20 (hanya satu request) diasersi sesudah respons dilepas; request yang terhitung tetap satu walau klik dilakukan dua kali.
- Temuan untuk QA:
  - TC-FA-TAG-646 tidak menyebut respons Submit ditahan, padahal Expected butir a (Disabled dengan state loading) hanya teramati saat respons masih tertahan; spec menahan respons seperti TC-FA-TAG-1344.
  - Expected TC-FA-TAG-646 butir b ("Toast sukses tampil sekali") tidak menyebut teks toast; spec mengasersi jumlah toast tanpa teks.
  - Post Condition TC-FA-TAG-646 ("Tepat satu penutupan laporan RF-00130 berstatus Declined") dan TC-FA-TAG-1344 ("Hanya satu entri Changelog Replace untuk aset itu; hanya satu entri TAG Log Paired untuk `RF-00412`") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
