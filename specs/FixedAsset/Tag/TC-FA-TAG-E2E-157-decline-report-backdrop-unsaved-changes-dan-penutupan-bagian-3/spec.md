---
id: TC-FA-TAG-E2E-157-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-3
title: "Decline Report: Refresh dan Dialog Terisi Sebagian (Bagian 3)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-655
  - TC-FA-TAG-656
  - TC-FA-TAG-657
coverage:
  web: automated
---

# Decline Report: Refresh dan Dialog Terisi Sebagian (Bagian 3)

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
- Kemampuan teknis (disediakan tim FE/BE): penanganan dialog `beforeunload` browser (konfirmasi bawaan saat F5).
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |

- State yang diubah dan pemulihannya: tidak ada laporan yang ditutup oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Refresh halaman pada dialog terisi (TC-FA-TAG-655)

2. Buka menu aksi baris Excavator 20 Ton - 44
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Tekan F5 untuk memuat ulang halaman
6. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
7. Konfirmasi dialog beforeunload sehingga halaman dimuat ulang
8. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Dialog terisi hanya Tag tercentang (TC-FA-TAG-656)

9. Buka menu aksi baris Excavator 20 Ton - 44
10. Klik "Decline Report"
11. Centang opsi RFID
12. Klik ikon close pada header dialog "Decline Report"
13. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
14. Verifikasi dialog "Decline Report" tetap terbuka di bawahnya
15. Klik [Leave]

### Dialog terisi hanya Reason (TC-FA-TAG-657)

16. Buka menu aksi baris Excavator 20 Ton - 44
17. Klik "Decline Report"
18. Isi Textarea "Reason" dengan "Tag masih terbaca"
19. Klik ikon close pada header dialog "Decline Report"
20. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
21. Verifikasi dialog "Decline Report" tetap terbuka di bawahnya
22. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-655 s.d. 657). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dan penutupan dialog Decline Report ada juga di spec 155 dan spec 156.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 (mengonfirmasi dialog beforeunload sehingga halaman dimuat ulang; kemampuan penanganan beforeunload tertulis di Prerequisites, S-08), membuka kembali Popup Assets sesudah muat ulang, dan tiap langkah `Klik [Leave]` pada TC-656 dan TC-657 (menutup form dirty).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-655 s.d. 657 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
