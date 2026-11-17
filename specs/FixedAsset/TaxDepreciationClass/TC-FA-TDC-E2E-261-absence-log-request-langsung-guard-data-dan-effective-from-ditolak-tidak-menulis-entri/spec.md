---
id: TC-FA-TDC-E2E-261-absence-log-request-langsung-guard-data-dan-effective-from-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung Guard Data (Used By, Last Posted Tax Year, Asset Type, Class Code) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-834
  - TC-FA-TDC-835
  - TC-FA-TDC-836
  - TC-FA-TDC-839
  - TC-FA-TDC-840
sourceRules: ["E-FATDC-24", "E-FATDC-26", "E-FATDC-27", "E-FATDC-60", "E-FATDC-10"]
smoke: []
dependsOn: []
trace:
  "E-FATDC-24": [3, 4, 5, 6]
  "E-FATDC-26": [9, 10, 11, 12]
  "E-FATDC-27": [15, 16, 17, 18]
  "E-FATDC-60": [21, 22, 23, 24]
  "E-FATDC-10": [27, 28, 29, 30]
coverage:
  web: automated
---

# Absence Log: Request Langsung Guard Data (Used By, Last Posted Tax Year, Asset Type, Class Code) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung, seed dan pemulihan lewat API (Used By lewat Asset Class pemakai dan class berkunci). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb2` | `NB-2` | Active, Used By 3 (Asset Class pemakai disediakan tim FE/BE), tanpa Last Posted Tax Year, Straight Line dan Declining Balance, satu versi; Asset Class `AC-MESIN` memakainya dengan Tax Method Declining Balance |
| `nbKhs` | `NB-KHS` | Last Posted Tax Year 2026, Used By 0 |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Asset Type Non-building, Active, Used By 0, hanya satu versi (versi pertama tanpa Effective From) |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-834: Deactivate class dengan Used By lebih dari 0

1. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Kirim request langsung dengan sesi API Total Control untuk menonaktifkan class `NB-2` tanpa melalui UI
3. Verifikasi server menolak request tanpa mengubah data
4. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
5. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
6. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-835: Delete class yang pernah diposting

7. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
8. Kirim request langsung dengan sesi API Total Control untuk menghapus class `NB-KHS` tanpa melalui UI
9. Verifikasi server menolak request tanpa mengubah data
10. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
11. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
12. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-836: Delete class dengan Used By lebih dari 0

13. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
14. Kirim request langsung dengan sesi API Total Control untuk menghapus class `NB-2` tanpa melalui UI
15. Verifikasi server menolak request tanpa mengubah data
16. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
17. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
18. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-839: Ubah Asset Type class yang sudah disimpan

19. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
20. Kirim request langsung dengan sesi API Total Control untuk mengubah Asset Type `NB-4` menjadi `Building` tanpa melalui UI
21. Verifikasi server menolak request tanpa mengubah data
22. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
23. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
24. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-840: Ubah Class Code yang terkunci

25. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
26. Kirim request langsung dengan sesi API Total Control untuk mengubah Class Code `NB-KHS` menjadi `NB-KHS2` tanpa melalui UI
27. Verifikasi server menolak request tanpa mengubah data
28. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
29. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
30. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-834, TC-FA-TDC-835, TC-FA-TDC-836, TC-FA-TDC-839, dan TC-FA-TDC-840. Status respons dan state data atas request yang sama berada di spec 219 (TC-FA-TDC-834, TC-FA-TDC-835, TC-FA-TDC-836) dan 220 (TC-FA-TDC-839, TC-FA-TDC-840).
- Anchor positif (8b.2): `Verifikasi` penolakan server sesudah tiap request sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 30, tanpa perulangan (ekspansi 30); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Langkah penghubung (S-03): langkah 1, 7, 13, 19, 25 (mencatat baseline tiap TC, S-12).
- Temuan untuk QA:
  - Klausa Expected c TC-FA-TDC-834 sampai TC-FA-TDC-840 menyebut "Changelog dan Activity Log untuk class tersebut" atau "entri log baru" tanpa surface; spec membaca ketiga surface (Changelog, System Log Total Control, Activity Log) berdasarkan jumlah entri total, bukan filter per class.
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
