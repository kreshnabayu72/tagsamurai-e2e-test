---
id: TC-FA-TAG-E2E-155-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-1
title: "Decline Report: Backdrop dan Unsaved Changes (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-647
  - TC-FA-TAG-648
  - TC-FA-TAG-649
  - TC-FA-TAG-650
coverage:
  web: automated
---

# Decline Report: Backdrop dan Unsaved Changes (Bagian 1)

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

- State yang diubah dan pemulihannya: tidak ada laporan yang ditutup oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Klik backdrop (TC-FA-TAG-647)

2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Klik area backdrop di luar dialog
5. Verifikasi dialog "Decline Report" tetap terbuka
6. Klik [Cancel] pada dialog "Decline Report"

### Cancel pada dialog terisi (TC-FA-TAG-648)

7. Buka menu aksi baris Excavator 20 Ton - 44
8. Klik "Decline Report"
9. Isi Textarea "Reason" dengan "Tag masih terbaca"
10. Klik [Cancel] pada dialog "Decline Report"
11. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
12. Verifikasi dialog "Decline Report" tetap terbuka di bawahnya
13. Klik [Cancel] pada dialog "Unsaved Changes"

### Ikon close pada dialog terisi (TC-FA-TAG-649)

14. Klik ikon close pada header dialog "Decline Report"
15. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
16. Verifikasi dialog "Decline Report" tetap terbuka di bawahnya
17. Klik [Cancel] pada dialog "Unsaved Changes"

### Esc pada dialog terisi (TC-FA-TAG-650)

18. Tekan tombol Esc
19. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
20. Verifikasi dialog "Decline Report" tetap terbuka di bawahnya
21. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-647 s.d. 650). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dan penutupan dialog Decline Report ada juga di spec 156 (TC-FA-TAG-651 s.d. 654) dan spec 157 (TC-FA-TAG-655 s.d. 657).
- Satu dialog "Decline Report" pada AST-0044 dengan Reason "Tag masih terbaca" dipakai berurutan oleh TC-648 sampai TC-650 (precondition dan isian identik); dialog "Unsaved Changes" ditutup dengan [Cancel] antar-TC supaya isian terpertahankan (S-09), dan [Leave] pada langkah 21 menutup form dirty di akhir spec. TC-647 memakai dialog AST-0020 yang belum diisi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 (menutup dialog yang belum diisi dengan [Cancel]), 13, dan 17 (menutup dialog "Unsaved Changes" dengan [Cancel]) serta 21 (menutup form dirty dengan [Leave]).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-648 s.d. 650 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
