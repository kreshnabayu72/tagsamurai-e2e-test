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
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial yang menahan respons Submit Decline Report dan Submit Replace beberapa detik dan menghitung request yang terkirim, lalu melepas tahanan respons (precondition TC-FA-TAG-646 butir c dan TC-FA-TAG-1344 butir f); hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, dan laporan Tag terbuka; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Reason Decline Report | Tag masih terbaca | `reasonDecline` |
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00330` Paired) | `aset220` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: Decline Report di langkah 7 menutup laporan RF-00130 (Declined); langkah 18 mengganti Tag AST-0220 dari `RF-00330` menjadi `RF-00412`. Hook `after` memulihkan laporan, AST-0220 ke `RF-00330` Paired, dan `RF-00412` ke Available lewat fixture backend, serta melepas intercept, walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 18); entri Changelog `Decline Report` per Tag (langkah 7); entri TAG Log Global (langkah 18).

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
9. Verifikasi hanya satu request Submit Decline Report terkirim selama respons ditahan
10. Lepas tahanan respons dan intercept
11. Verifikasi hanya satu Toast sukses tampil
12. Muat ulang halaman (F5)

### TC-FA-TAG-1344: Klik ganda cepat pada Submit Replace

13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Pasang intercept yang menahan respons Submit Replace beberapa detik dan menghitung request
17. Tunggu toast lama hilang otomatis
18. Klik [Submit] dua kali beruntun cepat
19. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading
20. Lepas tahanan respons dan intercept
21. Verifikasi hanya satu request terkirim
22. Verifikasi hanya satu Toast "Success, TAG has been replaced."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-646 dan 1344). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: klik ganda pada Receive, Start Print, dan pindaian beruntun (TC-FA-TAG-257, 494, 566) ada di spec 342; Submit Pair dan Submit & next sesi Batch (TC-FA-TAG-1348, 1349) ada di spec 344; Submit Report TAG dan Cancel Report (TC-FA-TAG-619, 669) ada di spec 351; Submit Receive Manually (TC-FA-TAG-587) ada di spec 383.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 dan 16 (memasang intercept penahan respons), 6 dan 17 (menunggu toast lama hilang otomatis sebelum hitungan toast), 10 dan 20 (melepas tahanan respons dan intercept), 12 (muat ulang halaman untuk menutup Popup Detail dan membersihkan state).
- Langkah 9 (hanya satu request, TC-FA-TAG-646) diasersi selama respons masih ditahan, sebelum langkah 10 melepas tahanan; langkah 21 (hanya satu request, TC-FA-TAG-1344) diasersi sesudah respons dilepas; request yang terhitung tetap satu walau klik dilakukan dua kali.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 18); entri Changelog `Decline Report` per Tag (langkah 7); entri TAG Log Global (langkah 18).
- Temuan untuk QA:
  - Expected TC-FA-TAG-646 butir b ("Toast sukses tampil sekali") tidak menyebut teks toast; spec mengasersi jumlah toast tanpa teks.
  - Post Condition TC-FA-TAG-646 ("Tepat satu penutupan laporan RF-00130 berstatus Declined") dan TC-FA-TAG-1344 ("Hanya satu entri Changelog Replace untuk aset itu; hanya satu entri TAG Log Paired untuk `RF-00412`") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
