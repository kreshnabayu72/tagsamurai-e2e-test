---
id: TC-FA-TAG-E2E-351-guard-submit-report-tag-dan-cancel-report-ditekan-beruntun-hanya-satu-laporan
title: "Guard Klik Ganda: Submit Report TAG dan Cancel Report Ditekan Beruntun Hanya Membuat dan Menutup Satu Laporan (Bagian 4)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-619
  - TC-FA-TAG-669
coverage:
  web: automated
---

# Guard Klik Ganda: Submit Report TAG dan Cancel Report Ditekan Beruntun Hanya Membuat dan Menutup Satu Laporan (Bagian 4)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Staff Auditor (tidak memegang Manage asset & TAG) (`staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD`). Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial yang menahan respons Submit Report TAG dan Cancel Report beberapa detik dan menghitung request yang terkirim, lalu melepas tahanan respons (precondition TC-FA-TAG-619 butir c; TC-FA-TAG-669 tidak menyebutnya, spec memakai kemampuan yang sama agar jumlah request teramati); hook `after` melepas semua intercept; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, task Existence Audit, dan laporan Tag; (3) halaman Audit > Task Detail dapat dibuka akun Staff Auditor. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal [RFID] RF-00130 tanpa laporan terbuka saat spec mulai; item In Audit pada task Existence Audit milik spec | `aset20Laporan` |
| Report Type | Damaged | `reportType` |
| Note | Label retak | `noteReport` |
| Reason Cancel Report | Tag ternyata terbaca | `reasonCancel` |

- State yang diubah dan pemulihannya: langkah 7 membuat satu laporan terbuka Damaged untuk `RF-00130`; laporan itu menjadi precondition TC-FA-TAG-669 (laporan terbuka Damaged dari Staff Auditor) dan ditutup (Canceled) di langkah 17. Hook `after` menghapus laporan, task Existence Audit, dan melepas intercept walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 7); entri Changelog `Cancel Report` per Tag (langkah 17).

## Test Steps

### TC-FA-TAG-619: Submit Report TAG ditekan beruntun

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris 'Excavator 20 Ton - 20'
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Pasang intercept yang menahan respons Report TAG beberapa detik dan menghitung request
6. Tunggu toast lama hilang otomatis
7. Klik tombol [Submit] dua kali beruntun dengan cepat
8. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading
9. Verifikasi hanya satu request Submit Report TAG terkirim selama respons ditahan
10. Lepas tahanan respons dan intercept
11. Verifikasi hanya satu Toast sukses tampil
12. Muat ulang halaman (F5)

### TC-FA-TAG-669: Cancel Report ditekan beruntun

13. Pilih row action "Cancel Report TAG" pada baris 'Excavator 20 Ton - 20'
14. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
15. Pasang intercept yang menahan respons Cancel Report beberapa detik dan menghitung request
16. Tunggu toast lama hilang otomatis
17. Klik tombol [Cancel Report] dua kali beruntun dengan cepat
18. Verifikasi hanya satu request Cancel Report terkirim (penekanan ulang diabaikan)
19. Lepas tahanan respons dan intercept
20. Verifikasi hanya satu Toast sukses tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-619 dan 669). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: klik ganda pada pindaian, Start Print, dan Receive (TC-FA-TAG-257, 494, 566) ada di spec 342; Submit Decline Report dan Submit Replace (TC-FA-TAG-646, 1344) ada di spec 343; Submit Pair dan Submit & next sesi Batch (TC-FA-TAG-1348, 1349) ada di spec 344; Submit Receive Manually (TC-FA-TAG-587) ada di spec 383.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 dan 15 (memasang intercept penahan respons), 6 dan 16 (menunggu toast lama hilang otomatis sebelum hitungan toast), 10 dan 19 (melepas tahanan respons dan intercept), 12 (muat ulang halaman supaya daftar item Task Detail memuat laporan terbuka sebelum Cancel Report).
- TC-FA-TAG-669 dijalankan sesudah TC-FA-TAG-619 karena precondition laporan terbuka Damaged dari Staff Auditor atas `RF-00130` sama dengan hasil TC-FA-TAG-619 (langkah 7 sampai 11).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 7); entri Changelog `Cancel Report` per Tag (langkah 17).
- Temuan untuk QA:
  - TC-FA-TAG-669 tidak menyebut respons Cancel Report ditahan; spec menahan respons seperti TC-FA-TAG-619 supaya jumlah request pada Expected "penekanan ulang diabaikan" teramati.
  - Expected TC-FA-TAG-619 butir b dan TC-FA-TAG-669 ("Toast sukses tampil sekali") tidak menyebut teks toast; spec mengasersi jumlah toast tanpa teks.
  - Post Condition TC-FA-TAG-619 ("Tepat satu laporan terbuka untuk RF-00130") dan TC-FA-TAG-669 ("Tepat satu penutupan laporan RF-00130 berstatus Canceled") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
