---
id: TC-FA-TDC-E2E-220-request-langsung-asset-type-class-code-terkunci-persempit-land-building
title: "Request Langsung: Asset Type, Class Code Terkunci, Persempit Allowed Methods, serta Land dan Building Ditolak"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-839
  - TC-FA-TDC-840
  - TC-FA-TDC-841
  - TC-FA-TDC-842
  - TC-FA-TDC-843
  - TC-FA-TDC-964
sourceRules: ["F-FATDC-02.k13", "FATDC-LOGIC-03a.3", "F-FATDC-02.k1", "FATDC-LOGIC-07c", "FATDC-LOGIC-10b.3", "FATDC-LOGIC-10a", "V-18", "FATDC-LOGIC-03b", "V-14", "FATDC-LOGIC-03c", "FATDC-LOGIC-10c", "F-FATDC-02.k6d"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-02.k13": [3, 6]
  "FATDC-LOGIC-03a.3": 5
  "F-FATDC-02.k1": 8
  "FATDC-LOGIC-07c": 10
  "FATDC-LOGIC-10b.3": [13, 15]
  "FATDC-LOGIC-10a": 16
  "V-18": 18
  "FATDC-LOGIC-03b": 21
  "V-14": 23
  "FATDC-LOGIC-03c": [23, 26]
  "FATDC-LOGIC-10c": 29
  "F-FATDC-02.k6d": 29
anchor: [20, 25]
coverage:
  web: automated
---

# Request Langsung: Asset Type, Class Code Terkunci, Persempit Allowed Methods, serta Land dan Building Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, serta seed dan pemulihan lewat API (Used By lewat Asset Class pemakai dan class berkunci). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Asset Type Non-building, Active, Used By 0 |
| `nbKhs` | `NB-KHS` | Last Posted Tax Year 2026, Used By 0 |
| `nb2` | `NB-2` | Allowed Methods Straight Line dan Declining Balance |
| `assetClassPemakai` | Asset Class `AC-MESIN` | memakai `NB-2` dengan Tax Method Declining Balance (Used By lebih dari 0) |
| `khsV18` | `KHS-V18` | Allowed Methods Straight Line dan Declining Balance, Used By 1: Asset Class `AC-SCH7 – Boiler` memakai Straight Line pada versi Current dan Declining Balance pada versi Scheduled Jan 2027 Asset Class (TC-964) |
| `land2` | `LAND2` | belum ada di daftar |
| `bldX` | `BLD-X` | belum ada di daftar |

- Fiscal Year Start Januari (nilai awal); tanggal sistem tidak diatur spec.
- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-839: Request langsung mengubah Asset Type class yang sudah disimpan ditolak

1. Baca jumlah versi class `NB-4` lewat request baca dan catat sebagai baseline
2. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Asset Type `NB-4` menjadi Building tanpa melalui UI
3. Verifikasi server menolak request tanpa mengubah data
4. Baca ulang class `NB-4` lewat request baca
5. Verifikasi Asset Type `NB-4` tetap Non-building
6. Verifikasi jumlah versi class `NB-4` sama dengan baseline langkah 1

### TC-FA-TDC-840: Request langsung mengubah Class Code yang terkunci ditolak

7. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Class Code `NB-KHS` menjadi `NB-KHS2` tanpa melalui UI
8. Verifikasi server menolak request tanpa mengubah data
9. Baca ulang class `NB-KHS` lewat request baca
10. Verifikasi Class Code tetap `NB-KHS`

### TC-FA-TDC-841: Request langsung mempersempit Allowed Methods yang masih dipakai ditolak

11. Baca jumlah versi class `NB-2` lewat request baca dan catat sebagai baseline
12. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Allowed Methods `NB-2` menjadi Straight Line saja dengan Effective From awal tahun pajak berjalan tanpa melalui UI
13. Verifikasi server menolak request tanpa membentuk versi baru
14. Baca ulang daftar versi `NB-2` lewat request baca
15. Verifikasi jumlah versi `NB-2` sama dengan baseline langkah 11
16. Verifikasi Allowed Methods versi Current `NB-2` tetap Straight Line dan Declining Balance

### TC-FA-TDC-842: Request langsung membuat class Land dengan Useful Life terisi ditolak

17. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `LAND2` bertipe Land dengan Useful Life `10` dan Allowed Methods `Straight Line` tanpa melalui UI
18. Verifikasi server menolak request tanpa membuat class
19. Baca ulang daftar class lewat request baca
20. Verifikasi daftar class memuat sedikitnya satu class lain
21. Verifikasi class `LAND2` tidak ada di daftar

### TC-FA-TDC-843: Request langsung membuat class Building dengan Declining Balance ditolak

22. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `BLD-X` bertipe Building dengan Useful Life `20` dan Allowed Methods `Declining Balance` tanpa melalui UI
23. Verifikasi server menolak request tanpa membuat class
24. Baca ulang daftar class lewat request baca
25. Verifikasi daftar class memuat sedikitnya satu class lain
26. Verifikasi class `BLD-X` tidak ada di daftar

### TC-FA-TDC-964: Request langsung mempersempit Allowed Methods yang dipakai hanya pada versi Scheduled Asset Class ditolak

27. Baca jumlah versi class `KHS-V18` lewat request baca dan catat sebagai baseline
28. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Allowed Methods `KHS-V18` menjadi Straight Line saja dengan Effective From awal tahun pajak berjalan tanpa melalui UI
29. Verifikasi server menolak request dengan blok D-08 yang sama (memuat `AC-SCH7 – Boiler`) tanpa membentuk versi baru
30. Baca ulang daftar versi `KHS-V18` lewat request baca
31. Verifikasi jumlah versi `KHS-V18` sama dengan baseline langkah 27
32. Verifikasi Allowed Methods versi Current `KHS-V18` tetap Straight Line dan Declining Balance

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-839, TC-FA-TDC-840, TC-FA-TDC-841, dan TC-FA-TDC-964 (tidak ada entri log baru di Changelog dan Activity Log) tidak diasersi di spec ini; asersinya ada di spec absence 261 (TC-FA-TDC-839, TC-FA-TDC-840) dan 270 (TC-FA-TDC-841 dan TC-FA-TDC-964) dengan aksi nyata dan baseline sendiri per TC (S-05). Klausa yang sama pada TC-FA-TDC-842 dan TC-FA-TDC-843 ada di spec absence 273.
- Langkah penghubung (S-03): langkah 1, 11, dan 27 (baseline jumlah versi untuk asersi "versi tidak berubah" dan "tanpa versi baru"); langkah 4, 9, 14, 19, 24, dan 30 (membaca state data lewat request baca). Langkah 20 dan 25 adalah anchor positif untuk asersi absence langkah 21 dan 26 (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-839 sampai 843 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan tanpa kode status.
  - TC-FA-TDC-841 menyebut "Effective From awal tahun pajak berjalan" tanpa nilai tanggal dan tanpa tanggal sistem uji; spec mengikuti TC.
  - TC-FA-TDC-841 menyebut Asset Class `AC-MESIN`; spec memakainya sebagai Asset Class pemakai yang disediakan tim FE.
  - TC-FA-TDC-964 menyebut "dialog blok D-08 yang sama" pada request langsung tanpa UI dan tidak menyebut bentuk respons; spec mengasersi penolakan server dengan muatan blok D-08 yang memuat `AC-SCH7 – Boiler`, tanpa kode status.
  - TC-FA-TDC-964 tidak menyebut tanggal sistem uji dan menulis "Effective From awal tahun pajak berjalan" tanpa nilai tanggal (sama dengan TC-FA-TDC-841); spec mengikuti TC.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
