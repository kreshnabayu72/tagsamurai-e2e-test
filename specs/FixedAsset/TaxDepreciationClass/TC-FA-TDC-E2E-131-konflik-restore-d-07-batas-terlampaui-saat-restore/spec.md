---
id: TC-FA-TDC-E2E-131-konflik-restore-d-07-batas-terlampaui-saat-restore
title: "Konflik Restore Default Classes: Batas Master Data Count Limit Terlampaui Saat Klik Restore atau Konfirmasi"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-329
  - TC-FA-TDC-330
  - TC-FA-TDC-331
sourceRules: ["ST-23", "D-07", "F-FATDC-08.k3e", "F-FATDC-08.k3f", "D-12", "FATDC-LOGIC-13a", "T-10"]
smoke: []
dependsOn: []
trace:
  "ST-23": [1, 17]
  "D-07": [4, 12]
  "F-FATDC-08.k3e": 5
  "F-FATDC-08.k3f": [12, 14]
  "D-12": 20
  "FATDC-LOGIC-13a": [21, 24]
  "T-10": 23
coverage:
  web: automated
---

# Konflik Restore Default Classes: Batas Master Data Count Limit Terlampaui Saat Klik Restore atau Konfirmasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (membuat class lewat API pre-setup) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Master Data Count Limit 1000 dan tabel tanpa class sama sekali pada company/state yang disediakan tim FE khusus automation), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah total class lewat fixture BE (disediakan tim FE/BE).
- State global yang diubah: Master Data Count Limit bernilai 1000 (nilai minimum, Lifecycle Settings > System Limits) pada ketiga blok; dipulihkan ke nilai semula di hook `after`, bersama penghapusan class `KHS-P001` sampai `KHS-P994` dan seed buatan spec.
- Kuota Master Data Count Limit adalah pemicu state (P-2), bukan objek uji volume.
- Data milik spec (dikondisikan di hook `before` lewat API; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `tabelKosong` | seluruh class | tabel tanpa class sama sekali (ketujuh seed sudah dihapus), Empty State tampil |
| `bulkP` | `KHS-P001` sampai `KHS-P994` | class non-seed dibuat sesi B lewat API (994 class pada TC-FA-TDC-329 dan TC-FA-TDC-330; 993 class `KHS-P001` sampai `KHS-P993` pada TC-FA-TDC-331) |
| `seed331` | `NB-1`, `NB-2` | `NB-1` Active dan `NB-2` Inactive dibuat sesi B pada TC-FA-TDC-331 |

- Tabel dikembalikan ke keadaan tanpa class di antara blok (langkah 7 dan 15).
- Suite berjalan serial (`parallel: false`) karena Master Data Count Limit dan tabel tanpa class adalah state global.

## Test Steps

### TC-FA-TDC-329: Klik Restore default classes pada tabel basi saat sisa batas tidak cukup menampilkan D-07 menggantikan D-12

1. Verifikasi Empty State tabel tampil
2. Sesi B (sesi API): buat 994 class non-seed `KHS-P001` sampai `KHS-P994` lewat API pre-setup hingga tersimpan, sehingga sisa slot 6 sedangkan class yang akan dibuat 7
3. Sesi A (tabel belum dimuat ulang): klik `Restore default classes`
4. Verifikasi dialog D-07 muncul dengan judul `Tax Depreciation Class Limit Reached` dan teks `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.`
5. Verifikasi dialog D-12 dan pratinjau tidak tampil
6. Klik `[OK]` pada dialog D-07

### TC-FA-TDC-330: Cek ulang server saat klik Restore menolak dengan D-07 bila batas terlampaui sejak pratinjau

7. Pulihkan tabel ke keadaan tanpa class (hapus `KHS-P001` sampai `KHS-P994`) lewat seeding API
8. Muat ulang halaman (F5)
9. Klik `Restore default classes` (dialog D-12 tampil dengan tujuh class akan dibuat)
10. Sesi B (sesi API): buat 994 class non-seed `KHS-P001` sampai `KHS-P994` lewat API pre-setup hingga tersimpan, sehingga sisa slot 6
11. Sesi A: klik `[Restore]`
12. Verifikasi dialog D-07 muncul dengan teks `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.`
13. Klik `[OK]` pada dialog D-07
14. Verifikasi tidak ada seed dibuat oleh sesi A: jumlah total class lewat fixture BE tetap 994

### TC-FA-TDC-331: Hanya class yang akan dibuat yang dihitung pada batas jumlah

15. Pulihkan tabel ke keadaan tanpa class (hapus `KHS-P001` sampai `KHS-P994`) lewat seeding API
16. Muat ulang halaman (F5)
17. Verifikasi Empty State tabel tampil
18. Sesi B (sesi API): buat `NB-1` (Active), `NB-2` (Inactive), dan 993 class non-seed `KHS-P001` sampai `KHS-P993` lewat API pre-setup hingga tersimpan, sehingga total class 995
19. Sesi A: klik `Restore default classes`
20. Verifikasi dialog D-12 muncul
21. Verifikasi dialog D-07 tidak muncul
22. Klik `[Restore]`
23. Verifikasi muncul toast sukses: `Success, default classes have been restored.`
24. Verifikasi total class 1000 lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- P-2 (pemicu bukan objek uji): kuota Master Data Count Limit 1000 dengan 994 atau 995 class hanya pemicu state pada TC kelas c ini (langkah 2, 10, dan 18); spec tidak dipindah ke kelas e.
- Langkah penghubung (S-03): langkah 6 dan 13 (menutup dialog D-07 dengan `[OK]`), langkah 7 dan 15 (membentuk precondition tabel tanpa class), langkah 8 dan 16 (memuat ulang halaman agar Empty State tampil). Langkah 1 dan 17 mengamati keadaan awal "Empty State tampil" yang dinyatakan langkah TC.
- Langkah 2, 10, dan 18 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ... tersimpan" (R-20); sesi A tidak memuat ulang tabel antara pembukaan halaman dan klik `Restore default classes`.
- Langkah 5 (absence): dialog D-07 langkah 4 menjadi anchor positif (8b.2). Langkah 14 (absence): dialog D-07 langkah 12 menjadi anchor; jumlah total class dibaca lewat fixture BE (S-12).
- Langkah 9 menulis "dialog D-12 tampil dengan tujuh class akan dibuat" sebagai keterangan keadaan dari langkah TC, bukan Expected; tidak diasersi.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-P001` sampai `KHS-P994` dan seed `NB-1`, `NB-2` ditulis literal tanpa suffix `{runId}-<NNN>` (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini. Tabel tanpa class sama sekali disediakan tim FE pada company/state khusus automation.
  - TC-FA-TDC-329 Post Condition (tidak ada class dibuat, tidak ada entri log) dan TC-FA-TDC-330 Post Condition (tidak ada mutasi dan tidak ada entri log dari sesi A) tidak punya langkah observasi selain jumlah total class pada langkah 14; entri log tidak diasersi (S-01, S-05).
  - TC-FA-TDC-331 Expected c ("Total class 1000") tidak menyebut cara pengamatan; spec membaca jumlah total lewat fixture BE (langkah 24).
  - Kolom Automation TC-FA-TDC-330 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
