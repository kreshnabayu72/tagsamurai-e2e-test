---
id: TC-FA-TAG-E2E-167-batas-karakter-reason-dialog-cancel-report-tag
title: "Batas Karakter Reason Dialog Cancel Report TAG"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1396
  - TC-FA-TAG-1397
  - TC-FA-TAG-1398
  - TC-FA-TAG-1399
coverage:
  web: automated
---

# Batas Karakter Reason Dialog Cancel Report TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |

- State yang diubah dan pemulihannya: laporan `RF-00130` yang dibatalkan (Canceled) oleh spec ini dan yang diatur ulang dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Cancel Report` per Tag (langkah 17, 24). Aksi tulis pada langkah 5, 9 ditolak dan tidak menambah entri.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Reason 361 karakter ditolak (TC-FA-TAG-1397)

2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Isi Textarea "Reason" dengan teks 361 karakter (huruf `a` diulang 361 kali)
4. Verifikasi pesan error "Max. 360 characters" tampil pada Textarea "Reason" langsung setelah teks diisi
5. Klik tombol [Cancel Report]
6. Verifikasi [Cancel Report] diblok selama error masih tampil (tidak ada toast sukses dan error "Max. 360 characters" masih tampil)
7. Verifikasi dialog "Cancel Report" tetap terbuka

### Reason hanya berisi spasi ditolak (TC-FA-TAG-1399)

8. Ganti isi Textarea "Reason" dengan lima spasi saja (tanpa karakter lain)
9. Klik tombol [Cancel Report]
10. Verifikasi pesan error "Reason must not be empty" tampil pada Textarea "Reason" karena isian dihitung kosong setelah trim
11. Verifikasi dialog "Cancel Report" tetap terbuka
12. Verifikasi tidak ada toast sukses
13. Klik tombol [Keep Report]

### Reason tepat 360 karakter diterima (TC-FA-TAG-1396)

14. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
15. Isi Textarea "Reason" dengan teks 360 karakter (huruf `a` diulang 360 kali)
16. Verifikasi tidak ada pesan error "Max. 360 characters" pada Textarea "Reason"
17. Klik tombol [Cancel Report]
18. Verifikasi dialog "Cancel Report" menutup
19. Verifikasi toast "Success, report has been canceled." tampil

### Reason 360 karakter dengan kelebihan spasi di ujung (TC-FA-TAG-1398)

20. Atur ulang data lewat fixture backend: Tag RF-00130 laporan terbuka Damaged dari Staff Auditor hingga tersimpan, lalu muat ulang halaman Task Detail
21. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
22. Isi Textarea "Reason" dengan teks 360 karakter (huruf `a` diulang 360 kali) diikuti 10 spasi di akhir
23. Verifikasi tidak ada pesan error "Max. 360 characters" karena panjang dihitung setelah trim
24. Klik tombol [Cancel Report]
25. Verifikasi dialog "Cancel Report" menutup
26. Verifikasi toast "Success, report has been canceled." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1396 s.d. 1399). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-1397, TC-1399, TC-1396, TC-1398. Validasi yang diblokir dijalankan sebelum Submit yang berhasil; TC-1399 melanjutkan dialog TC-1397; laporan `RF-00130` diatur ulang sebelum TC-1398 karena TC-1396 sudah membatalkannya (langkah 20).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13 (menutup dialog dengan [Keep Report], yang menutup langsung tanpa dialog konfirmasi walau Reason terisi) dan 20 (mengatur ulang state laporan lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Cancel Report` per Tag (langkah 17, 24). Aksi tulis pada langkah 5, 9 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Panjang teks dihitung setelah trim sesuai Expected TC; nilai 360 dan 361 karakter ditulis tepat sebagai huruf `a` yang diulang tanpa suffix karena asersi bergantung pada panjang persis.
  - Post Condition TC-FA-TAG-1396 s.d. 1399 (laporan RF-00130 berstatus Canceled atau tetap terbuka) tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
