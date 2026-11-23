---
id: TC-FA-TDC-E2E-288-absence-log-request-langsung-declining-balance-rate-end-of-life-treatment-dan-land-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung dengan Declining Balance Rate, End-of-Life Treatment, atau Land yang Tidak Valid dan Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-955
  - TC-FA-TDC-956
  - TC-FA-TDC-957
  - TC-FA-TDC-959
sourceRules: ["V-16", "F-FATDC-01.k4h", "V-17", "F-FATDC-01.k14", "V-23", "F-FATDC-01.k4i", "V-18", "F-FATDC-01.k6"]
smoke: []
dependsOn: []
trace:
  "V-16": [3, 4, 5, 6]
  "F-FATDC-01.k4h": 3
  "V-17": [9, 11, 13, 14, 15, 16]
  "F-FATDC-01.k14": [9, 11, 13]
  "V-23": [19, 21, 22, 23, 24]
  "F-FATDC-01.k4i": [19, 21]
  "V-18": [27, 28, 29, 30]
  "F-FATDC-01.k6": 27
coverage:
  web: automated
---

# Absence Log: Request Langsung dengan Declining Balance Rate, End-of-Life Treatment, atau Land yang Tidak Valid dan Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal 287.
- Data milik spec (kode literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; hook `before` menghapus sisa class berkode sama dari run sebelumnya lewat API; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Keadaan |
|---|---|---|
| `rApi1` | `R-API1` | belum ada di daftar |
| `rApi2` | `R-API2` | belum ada di daftar |
| `rApi3` | `R-API3` | belum ada di daftar |
| `land3` | `LAND3` | belum ada di daftar |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-955: Request langsung membuat class dengan Declining Balance tanpa Declining Balance Rate ditolak

1. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API1` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Straight Line dan Declining Balance, dan End-of-Life Treatment Charge in final period, tanpa Declining Balance Rate
3. Verifikasi server menolak request tanpa membuat class dengan pesan V-16 "Declining rate must not be empty"
4. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
5. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
6. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-956: Request langsung dengan Declining Balance Rate di luar rentang atau lebih dari 2 desimal ditolak

7. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
8. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API2` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Declining Balance, End-of-Life Treatment Charge in final period, dan Declining Balance Rate 0
9. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
10. Kirim request langsung yang sama dengan Declining Balance Rate 100.01
11. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
12. Kirim request langsung yang sama dengan Declining Balance Rate 12.345
13. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
14. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
15. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
16. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-957: Request langsung dengan Declining Balance tanpa End-of-Life Treatment atau dengan nilai di luar opsi ditolak

17. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
18. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API3` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Declining Balance, Declining Balance Rate 25, tanpa End-of-Life Treatment
19. Verifikasi server menolak request tanpa membuat class dengan pesan V-23 "End-of-life treatment must not be empty"
20. Kirim request langsung yang sama dengan End-of-Life Treatment bernilai "Switch to declining"
21. Verifikasi server menolak request tanpa membuat class
22. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
23. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
24. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-959: Request langsung membuat class Land dengan Declining Balance Rate atau End-of-Life Treatment terisi ditolak

25. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
26. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `LAND3` bertipe Land dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, tanpa Useful Life dan Allowed Methods, dengan Declining Balance Rate 25 dan End-of-Life Treatment Charge in final period
27. Verifikasi server menolak request tanpa membuat class dengan pesan V-18 "Land is not depreciated."
28. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
29. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
30. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-955, TC-FA-TDC-956, TC-FA-TDC-957, dan TC-FA-TDC-959. Status respons dan state data atas request yang sama berada di spec 287.
- Anchor positif (8b.2): `Verifikasi` penolakan server sesudah tiap request (langkah 3, 9, 11, 13, 19, 21, 27) sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat tepat sebelum request TC itu (langkah 1, 7, 17, 25), lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 30, tanpa perulangan (ekspansi 30).
- Langkah penghubung (S-03): langkah 1, 7, 17, 25 (mencatat baseline tiap TC, S-12); langkah 10, 12, dan 20 menulis "yang sama" merujuk langkah 8 dan 18 (S-04: nilai data lengkap ditulis di langkah pertama tiap TC).
- Temuan untuk QA:
  - Klausa Expected c TC-FA-TDC-955, 956, 957, dan 959 menyebut "entri log baru di Changelog, System Log aktor, dan Activity Log"; spec membaca ketiga surface berdasarkan jumlah entri total, bukan filter per class.
  - TC-FA-TDC-957 tidak menyebut pesan untuk nilai "Switch to declining"; langkah 21 hanya mengasersi penolakan (sama dengan spec 287).
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
