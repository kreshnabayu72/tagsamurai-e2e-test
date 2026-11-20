---
id: TC-FA-TDC-E2E-276-konflik-d-09-d-08-versi-scheduled-asset-class-terbentuk-antara-save-dan-apply
title: "Konflik D-09 dan D-08: Versi Scheduled Asset Class Terbentuk Antara Save dan Apply"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-963
sourceRules: ["FATDC-LOGIC-10b.3", "FATDC-LOGIC-10c", "F-FATDC-02.k6a", "F-FATDC-02.k6d", "D-08", "E-FATDC-94", "D-09"]
smoke: []
dependsOn: []
trace:
  "D-09": [5, 8]
  "FATDC-LOGIC-10b.3": 10
  "FATDC-LOGIC-10c": [10, 11]
  "F-FATDC-02.k6a": 10
  "F-FATDC-02.k6d": [10, 11]
  "D-08": [10, 11]
  "E-FATDC-94": [12, 13]
coverage:
  web: automated
---

# Konflik D-09 dan D-08: Versi Scheduled Asset Class Terbentuk Antara Save dan Apply

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env yang sama dengan spec 245). Sesi B hanya memicu perubahan state (membentuk versi Scheduled Asset Class di modul Asset Class) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai), sesi API aktor, kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah versi dan jumlah entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Kolom Automation TC-963 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2) dan kebutuhannya ditulis di sini: dua sesi (A lewat UI, B lewat sesi API), versi Scheduled Asset Class dibentuk sesi B setelah D-09 terbuka di sesi A.
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00; Fiscal Year Start Januari); dipulihkan dengan langkah eksplisit (langkah 18) dan di hook `after` sebagai cadangan. Versi Scheduled Jan 2027 `AC-SCH4` dihapus di hook `after`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsV17` | `KHS-V17` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Used By 1 (Asset Class `AC-SCH4 – Mesin Frais` memakai Straight Line, tanpa versi Scheduled) |

- Tabel memuat tujuh class seed bawaan dan satu class milik spec (8 baris dalam satu halaman) sehingga baris target dibuka tanpa Search (8b.13, R-23).
- Suite berjalan serial (`parallel: false`) karena jam sistem global dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-963: Versi Scheduled Asset Class terbentuk antara Save dan Apply, server menolak dengan D-08 yang sama

1. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`
2. Klik link Class Code `KHS-V17` pada tabel
3. Lepas centang Allowed Methods `Declining Balance`
4. Klik `[Save]`
5. Verifikasi dialog Save Changes D-09 tampil
6. Sesi B (sesi API, modul Asset Class): bentuk versi Scheduled Jan 2027 untuk `AC-SCH4` dengan Tax Method Declining Balance hingga versi tersimpan
7. Catat baseline jumlah versi dan jumlah entri Changelog class `KHS-V17` lewat fixture BE
8. Sesi A: pilih Effective From `Jan 2027` pada dialog D-09
9. Sesi A: klik `[Apply]`
10. Verifikasi dialog D-08 muncul dengan teks `1 asset class uses Declining Balance. Change it first.`
11. Verifikasi dialog D-08 memuat bullet `• AC-SCH4 – Mesin Frais`
12. Verifikasi tidak ada versi baru: jumlah versi `KHS-V17` sama dengan baseline langkah 7
13. Verifikasi tidak ada entri log baru: jumlah entri Changelog class `KHS-V17` sama dengan baseline langkah 7
14. Klik `[OK]` pada dialog D-08
15. Klik ikon ✕ pada Drawer
16. Verifikasi dialog Unsaved Changes tampil
17. Klik `[Leave]`
18. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Langkah penghubung (S-03): langkah 1 dan 18 (mengatur dan memulihkan jam), langkah 7 (baseline, S-12), langkah 14 (menutup dialog D-08 dengan `[OK]`; Drawer tetap terbuka), langkah 15 sampai 17 (menutup Drawer dirty deterministik; S-08). Langkah 5 adalah anchor positif (8b.2) bahwa D-09 terbuka sebelum sesi B bertindak (TC menulis keadaan itu dalam tanda kurung pada langkah 1; R-02).
- Langkah 6 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20).
- Langkah 12 dan 13 (absence): dialog D-08 langkah 10 adalah respons server yang sudah diasersi dan menjadi anchor positif; selisih terhadap baseline langkah 7 (S-12, S-05; dua-sesi diuji di spec ini, P-1).
- Spec terpisah dari spec 245 (TC-282 dan TC-291, juga dua sesi) supaya tidak melewati ~35 langkah; TC-963 memakai data dan jam sendiri.
- Pembagian TC lintas spec: TC-962 dan TC-965 (D-08 karena versi Scheduled Asset Class lewat satu sesi) ada di spec 275; TC-964 (request langsung) di spec 220 dan 270.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-V17` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-963 tidak menyebut tombol penutup dialog D-08, cara menutup Drawer sesudahnya, dan cara pembacaan jumlah versi dan entri log; spec memakai `[OK]` seperti dialog D-08 pada TC lain, `✕` dengan dialog Unsaved Changes dan `[Leave]`, serta kemampuan baca fixture BE.
  - TC-963 butir b ("tidak ada versi baru dan tidak ada entri log") tanpa surface log; spec membaca Changelog class (seperti TC-291).
