---
id: TC-FA-TAG-E2E-152-decline-report-screening-dan-validasi-bagian-2
title: "Decline Report: Validasi Tag dan Label Opsi Tag Bertipe Sama (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-640
  - TC-FA-TAG-1485
coverage:
  web: automated
---

# Decline Report: Validasi Tag dan Label Opsi Tag Bertipe Sama (Bagian 2)

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
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan dua Tag RFID | AST-0044, Group Plant B; dua Tag RFID Paired `RF-00132` (laporan terbuka Missing) dan `RF-00133` (laporan terbuka Damaged) | `aset44DuaRfid` |

- State yang diubah dan pemulihannya: laporan yang diatur ulang pada langkah 11 dipulihkan lewat fixture backend di hook `after`; tidak ada laporan yang ditutup oleh spec ini.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Submit tanpa mencentang Tag pada aset multi-Tag (TC-FA-TAG-640)

2. Buka menu aksi baris Excavator 20 Ton - 44
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik [Submit]
6. Verifikasi pesan error "TAG must not be empty" tampil pada bagian "TAG to decline"
7. Verifikasi dialog "Decline Report" tetap terbuka
8. Klik ikon close pada header dialog "Decline Report"
9. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
10. Klik [Leave]

### Label opsi pada aset dengan dua Tag bertipe sama (TC-FA-TAG-1485)

11. Atur ulang data lewat fixture backend: Aset AST-0044 dengan dua Tag RFID Paired, RF-00132 laporan terbuka Missing dan RF-00133 laporan terbuka Damaged, hingga tersimpan, lalu muat ulang halaman
12. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
13. Buka menu aksi baris Excavator 20 Ton - 44
14. Klik "Decline Report"
15. Verifikasi bagian "TAG to decline" menampilkan dua checkbox tersusun mendatar
16. Verifikasi label tiap opsi memuat tipe Tag RFID, TAG Code (`RF-00132` dan `RF-00133`), dan Report Type-nya (Missing dan Damaged) sehingga kedua opsi dapat dibedakan
17. Verifikasi kedua checkbox belum tercentang
18. Klik [Cancel] pada dialog "Decline Report"

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-640, 1485). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: screening dan validasi Reason Decline Report ada di spec 151 (TC-FA-TAG-636 s.d. 639).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 8 sampai 10 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]), 11 (mengatur ulang state laporan lewat fixture backend), dan 18 (menutup dialog yang belum diisi).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-640 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
