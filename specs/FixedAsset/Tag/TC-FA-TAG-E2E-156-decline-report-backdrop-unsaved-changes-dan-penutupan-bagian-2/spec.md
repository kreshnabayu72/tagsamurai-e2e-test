---
id: TC-FA-TAG-E2E-156-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-2
title: "Decline Report: Unsaved Changes dan Penutupan Dialog (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-651
  - TC-FA-TAG-652
  - TC-FA-TAG-653
  - TC-FA-TAG-654
coverage:
  web: automated
---

# Decline Report: Unsaved Changes dan Penutupan Dialog (Bagian 2)

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

- State yang diubah dan pemulihannya: tidak ada laporan yang ditutup oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Cancel pada Unsaved Changes mempertahankan isian (TC-FA-TAG-651)

2. Buka menu aksi baris Excavator 20 Ton - 44
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik ikon close pada header dialog "Decline Report"
6. Pada dialog "Unsaved Changes" klik [Cancel]
7. Verifikasi dialog "Unsaved Changes" menutup
8. Verifikasi dialog "Decline Report" tetap terbuka dengan isian yang sama (Reason "Tag masih terbaca")

### Leave pada Unsaved Changes (TC-FA-TAG-652)

9. Klik ikon close pada header dialog "Decline Report"
10. Pada dialog "Unsaved Changes" klik [Leave]
11. Verifikasi dialog "Unsaved Changes" dan dialog "Decline Report" menutup
12. Verifikasi tidak ada toast

### Ikon close pada dialog yang belum terisi (TC-FA-TAG-653)

13. Buka menu aksi baris Excavator 20 Ton - 44
14. Klik "Decline Report"
15. Klik ikon close pada header dialog "Decline Report"
16. Verifikasi dialog "Decline Report" menutup langsung
17. Verifikasi dialog "Unsaved Changes" tidak tampil

### Isian dikosongkan kembali (TC-FA-TAG-654)

18. Buka menu aksi baris Excavator 20 Ton - 44
19. Klik "Decline Report"
20. Isi Textarea "Reason" dengan "Tag masih terbaca"
21. Kosongkan kembali isian yang tadi diisi
22. Klik ikon close pada header dialog "Decline Report"
23. Verifikasi dialog "Decline Report" menutup langsung
24. Verifikasi dialog "Unsaved Changes" tidak tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-651 s.d. 654). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dan penutupan dialog Decline Report ada juga di spec 155 (TC-FA-TAG-647 s.d. 650) dan spec 157 (TC-FA-TAG-655 s.d. 657).
- TC-651 dan TC-652 memakai satu dialog "Decline Report" dengan Reason "Tag masih terbaca" (isian identik); TC-652 melanjutkan state setelah [Cancel] pada dialog "Unsaved Changes".
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-651 s.d. 654 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-654 meminta "Kosongkan kembali isian yang tadi diisi" pada Textarea "Reason"; spec mengosongkan isian tanpa memicu Unsaved Changes mengikuti teks TC.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
