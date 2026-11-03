---
id: TC-FA-TAG-E2E-151-decline-report-screening-dan-validasi-bagian-1
title: "Decline Report: Screening Dialog dan Validasi Reason (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-636
  - TC-FA-TAG-637
  - TC-FA-TAG-638
  - TC-FA-TAG-639
coverage:
  web: automated
---

# Decline Report: Screening Dialog dan Validasi Reason (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Total Control [TC]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |

- State yang diubah dan pemulihannya: laporan yang diatur ulang pada langkah 22 dipulihkan lewat fixture backend di hook `after`; tidak ada laporan yang ditutup oleh spec ini.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Screening dialog pada aset satu Tag berlaporan (TC-FA-TAG-636)

2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Verifikasi dialog "Decline Report" (Size MD) terbuka
5. Verifikasi Summary menampilkan "AST-0020 — Excavator 20 Ton"
6. Verifikasi bagian "TAG to decline" bertanda wajib (*) menampilkan satu opsi tanpa checkbox
7. Verifikasi opsi pada bagian "TAG to decline" otomatis terpilih
8. Verifikasi opsi berlabel tipe Tag "RFID" dan Report Type "Damaged"
9. Verifikasi Textarea "Reason" bertanda wajib (*) kosong
10. Verifikasi footer berisi tombol [Cancel] dan [Submit]

### Submit tanpa Reason (TC-FA-TAG-639)

11. Klik [Submit] dengan Textarea "Reason" dibiarkan kosong
12. Verifikasi pesan error "Reason must not be empty" tampil pada Textarea "Reason"
13. Verifikasi dialog "Decline Report" tetap terbuka
14. Klik [Cancel] pada dialog "Decline Report"

### Screening dialog pada aset dua Tag berlaporan (TC-FA-TAG-637)

15. Buka menu aksi baris Excavator 20 Ton - 44
16. Klik "Decline Report"
17. Verifikasi bagian "TAG to decline" menampilkan dua checkbox tersusun mendatar
18. Verifikasi tiap opsi berlabel tipe Tag dan Report Type-nya (RFID dengan Missing, QR dengan Unreadable)
19. Verifikasi kedua checkbox belum tercentang
20. Verifikasi Textarea "Reason" kosong
21. Klik [Cancel] pada dialog "Decline Report"

### Dialog hanya menampilkan Tag berlaporan terbuka (TC-FA-TAG-638)

22. Atur ulang data lewat fixture backend: hanya Tag RF-00132 yang punya laporan terbuka Missing (Tag QR-00232 tanpa laporan terbuka) hingga tersimpan, lalu muat ulang halaman
23. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
24. Buka menu aksi baris Excavator 20 Ton - 44
25. Klik "Decline Report"
26. Verifikasi hanya satu opsi (RFID dengan Missing) tampil tanpa checkbox
27. Verifikasi opsi RFID dengan Missing otomatis terpilih
28. Verifikasi Tag QR-00232 tidak ditawarkan
29. Klik [Cancel] pada dialog "Decline Report"

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-636 s.d. 639). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: validasi Decline Report multi-Tag tanpa mencentang Tag (TC-FA-TAG-640) ada di spec 152.
- Urutan TC di dalam spec: TC-636, TC-639, TC-637, TC-638. TC-639 melanjutkan dialog TC-636 (aset dan state identik) dan dialog ditutup dengan [Cancel] sebelum TC-637; TC-638 diletakkan terakhir karena membutuhkan state laporan berbeda pada AST-0044.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14, 21, dan 29 (menutup dialog yang belum diisi dengan [Cancel]) serta langkah 22 (mengatur ulang state laporan lewat fixture backend).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-639 ("Laporan RF-00130 tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - TC tidak menyatakan apakah satu-satunya opsi yang terpilih otomatis membuat dialog dianggap terisi saat ditutup; spec menutup dialog yang belum diisi pengguna dengan [Cancel] tanpa dialog Unsaved Changes.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
