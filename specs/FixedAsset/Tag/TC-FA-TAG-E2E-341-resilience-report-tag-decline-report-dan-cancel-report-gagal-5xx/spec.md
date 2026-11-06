---
id: TC-FA-TAG-E2E-341-resilience-report-tag-decline-report-dan-cancel-report-gagal-5xx
title: "Resilience: Report TAG, Cancel Report, dan Decline Report Gagal (5xx) Mempertahankan Dialog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-617
  - TC-FA-TAG-645
  - TC-FA-TAG-668
coverage:
  web: automated
---

# Resilience: Report TAG, Cancel Report, dan Decline Report Gagal (5xx) Mempertahankan Dialog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |
| 2 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: blok 1 (TC-FA-TAG-617 dan TC-FA-TAG-668 memakai Staff Auditor; TC-FA-TAG-645 memakai Total Control). Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Spec selesai di akun blok 2; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial atas request Report TAG, Cancel Report, dan Decline Report: respons 5xx; hook `after` melepas semua intercept; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, task Existence Audit, dan laporan Tag terbuka; (3) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal [RFID] RF-00130; item In Audit pada task Existence Audit milik spec | `aset20Laporan` |
| Report Type | Damaged | `reportType` |
| Note | Label retak | `noteReport` |
| Reason Cancel Report | Tag ternyata terbaca | `reasonCancel` |
| Reason Decline Report | Tag masih terbaca | `reasonDecline` |

- State yang diubah dan pemulihannya: Tag `RF-00130` tanpa laporan terbuka saat spec mulai; langkah 11 membuat laporan terbuka Damaged dari Staff Auditor lewat fixture BE (precondition TC-FA-TAG-645 dan TC-FA-TAG-668) dan semua commit di spec ini gagal sehingga laporan tetap terbuka. Hook `after` menghapus laporan, task Existence Audit, dan melepas intercept walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 6, 15, 27 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Fixture backend (langkah 11) hanya menyiapkan atau memulihkan state.

## Test Steps

### Blok 1: Staff Auditor (TC-FA-TAG-617, TC-FA-TAG-668)

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris 'Excavator 20 Ton - 20'
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Pasang intercept 5xx pada request Report TAG
6. Klik tombol [Submit]
7. Verifikasi Toast "Error, failed to report TAG." tampil
8. Verifikasi dialog "Report TAG" tetap terbuka
9. Lepas intercept
10. Muat ulang halaman (F5)
11. Buat laporan terbuka Damaged untuk Tag RF-00130 dari Staff Auditor lewat fixture BE hingga tersimpan
12. Pilih row action "Cancel Report TAG" pada baris 'Excavator 20 Ton - 20'
13. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
14. Pasang intercept 5xx pada request Cancel Report
15. Klik tombol [Cancel Report]
16. Verifikasi Toast "Error, failed to cancel report." tampil
17. Verifikasi dialog "Cancel Report" tetap terbuka
18. Lepas intercept
19. Muat ulang halaman (F5)

### Blok 2: Total Control (TC-FA-TAG-645)

20. Logout dari akun Staff Auditor, lalu Login sebagai akun Total Control
21. Buka Fixed Asset > TAG > Paired
22. Klik Asset Name 'Excavator 20 Ton' pada baris group Plant B (Popup Assets)
23. Buka menu aksi baris 'Excavator 20 Ton - 20'
24. Klik "Decline Report"
25. Isi Textarea "Reason" dengan "Tag masih terbaca"
26. Pasang intercept 5xx pada request Decline Report
27. Klik tombol [Submit]
28. Verifikasi Toast "Error, failed to decline report." tampil
29. Verifikasi dialog "Decline Report" tetap terbuka
30. Lepas intercept
31. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-617, 645, 668). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-617, 668, lalu 645, supaya dua TC Staff Auditor berurutan dan hanya ada satu ganti akun. TC-FA-TAG-668 dan 645 sama-sama mensyaratkan laporan terbuka, sedangkan TC-FA-TAG-617 mensyaratkan Tag tanpa laporan terbuka, sehingga laporan dibuat sesudah TC-FA-TAG-617 (langkah 11).
- Pembagian TC lintas spec: Report TAG, Decline Report, dan Cancel Report ditekan beruntun (TC-FA-TAG-619, 646, 669) ada di spec 342 dan 343; penolakan state tenant (TC-FA-TAG-1299 s.d. 1302) ada di spec 349 dan 350.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 18, 30 (melepas intercept), 10, 19, 31 (muat ulang halaman untuk menutup dialog yang berisi isian; dialog `beforeunload` ditangani sesuai Prerequisites), 11 (membuat laporan terbuka lewat fixture BE hingga tersimpan), 20 dan 21 (ganti akun dan membuka halaman), 22 dan 23 (membuka Popup Detail dan menu aksi baris yang dipakai TC-FA-TAG-645).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 6, 15, 27 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Fixture backend (langkah 11) hanya menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-617 ("Tidak ada laporan baru untuk RF-00130 dan aset tidak mendapat status "Tag Reported""), TC-FA-TAG-645 dan TC-FA-TAG-668 ("Laporan RF-00130 tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
