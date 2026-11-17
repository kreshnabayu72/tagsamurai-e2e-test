---
id: TC-FA-TDC-E2E-273-absence-log-request-langsung-create-melanggar-aturan-data-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung Create yang Melanggar Aturan Data (Land, Building, Class Code Kembar) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-842
  - TC-FA-TDC-843
  - TC-FA-TDC-844
sourceRules: ["F-FATDC-01.k6", "§8.4#r7", "F-FATDC-01.k7", "F-FATDC-01.k1"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-01.k6": 3
  "§8.4#r7": [4, 5, 6, 10, 11, 12, 16, 17, 18]
  "F-FATDC-01.k7": 9
  "F-FATDC-01.k1": 15
coverage:
  web: automated
---

# Absence Log: Request Langsung Create yang Melanggar Aturan Data (Land, Building, Class Code Kembar) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung, seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, hanya satu versi (versi pertama tanpa Effective From); tidak ada class lain berkode `nb-4` |
| `land2` | `LAND2` | belum ada di daftar |
| `bldX` | `BLD-X` | belum ada di daftar |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-842: Create Land dengan Useful Life terisi

1. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Kirim request langsung dengan sesi API Total Control untuk membuat class `LAND2` bertipe Land dengan Useful Life `10` dan Allowed Methods `Straight Line` tanpa melalui UI
3. Verifikasi server menolak request tanpa membuat class
4. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
5. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
6. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-843: Create Building dengan Declining Balance

7. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
8. Kirim request langsung dengan sesi API Total Control untuk membuat class `BLD-X` bertipe Building dengan Useful Life `20` dan Allowed Methods `Declining Balance` tanpa melalui UI
9. Verifikasi server menolak request tanpa membuat class
10. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
11. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
12. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-844: Create dengan Class Code kembar berbeda kapital

13. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
14. Kirim request langsung dengan sesi API Total Control untuk membuat class dengan Class Code `nb-4` (Class Name `Kelompok kembar`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`) tanpa melalui UI
15. Verifikasi server menolak request tanpa membuat class
16. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
17. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
18. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-842, TC-FA-TDC-843, dan TC-FA-TDC-844. Status respons dan state data atas request yang sama berada di spec 220 (TC-FA-TDC-842, TC-FA-TDC-843) dan 221 (TC-FA-TDC-844).
- Anchor positif (8b.2): `Verifikasi` penolakan server sesudah tiap request sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 18, tanpa perulangan (ekspansi 18); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Langkah penghubung (S-03): langkah 1, 7, 13 (mencatat baseline tiap TC, S-12).
- Temuan untuk QA:
  - TC-FA-TDC-842 sampai TC-FA-TDC-844 menyebut "Tidak ada entri log baru" tanpa surface; spec membaca ketiga surface (Changelog, System Log Total Control, Activity Log) berdasarkan jumlah entri total, bukan filter per class.
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
