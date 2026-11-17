---
id: TC-FA-TDC-E2E-263-absence-log-bypass-ui-create-dan-edit-ditolak-server-tidak-menulis-entri
title: "Absence Log: Create Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-160
  - TC-FA-TDC-161
sourceRules: ["V-14", "E-FATDC-07", "§4.2c#b1", "V-18", "E-FATDC-06"]
smoke: []
dependsOn: []
trace:
  "V-14": 12
  "E-FATDC-07": [13, 14, 15]
  "§4.2c#b1": [17, 33]
  "V-18": 28
  "E-FATDC-06": [29, 30, 31]
coverage:
  web: automated
---

# Absence Log: Create Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan intercept: `Spectra.intercept()` di atas backend nyata untuk mengganti payload request Create yang dikirim Drawer Add Tax Depreciation Class; intercept dilepas segera setelah pemicu selesai (S-09). Seed dan pemulihan lewat API mengikuti `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsB1` | `KHS-B1` | belum ada di daftar; Class Name `Bangunan uji validasi`, Asset Type Building, Useful Life 20, Allowed Methods Straight Line |
| `khsL1` | `KHS-L1` | belum ada di daftar; Class Name `Tanah uji validasi`, Asset Type Land |

- Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`) untuk Create lewat Drawer. Master Data Count Limit belum tercapai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-160: Create Building dengan Declining Balance

1. Klik `+ Class` di toolbar
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `KHS-B1`
4. Isi Class Name `Bangunan uji validasi`
5. Pilih Asset Type `Building`
6. Isi Useful Life `20`
7. Pilih Allowed Methods `Straight Line`
8. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
9. Aktifkan intercept request Create: ganti payload Allowed Methods menjadi `Straight Line, Declining Balance`
10. Klik `[Submit]`
11. Lepas intercept request Create
12. Verifikasi caption error "Declining balance does not apply to buildings." tampil di bawah field Allowed Methods
13. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
14. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
15. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini
16. Klik `[×]` pada header Drawer
17. Verifikasi dialog `Unsaved Changes` tampil
18. Klik `[Leave]`

### TC-FA-TDC-161: Create Land dengan Useful Life atau Allowed Methods terisi

19. Klik `+ Class` di toolbar
20. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
21. Isi Class Code `KHS-L1`
22. Isi Class Name `Tanah uji validasi`
23. Pilih Asset Type `Land`
24. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
25. Aktifkan intercept request Create: ganti payload Useful Life menjadi `10` dan Allowed Methods menjadi `Straight Line`
26. Klik `[Submit]`
27. Lepas intercept request Create
28. Verifikasi caption error "Land is not depreciated." tampil di bawah field terkait (Useful Life atau Allowed Methods yang terisi)
29. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
30. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
31. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini
32. Klik `[×]` pada header Drawer
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-160, dan TC-FA-TDC-161. Status respons dan state data atas request yang sama berada di spec 224 (TC-FA-TDC-160, TC-FA-TDC-161).
- Anchor positif (8b.2): caption error validasi sesudah tiap `[Submit]` sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 34, tanpa perulangan (ekspansi 34); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Menutup Drawer Create yang dirty ditulis deterministik (S-08): `[×]`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]`, sehingga tidak dapat dipadatkan.
- Langkah penghubung (S-03): langkah 8, 24 (mencatat baseline tiap TC, S-12).
- Temuan untuk QA:
  - TC-FA-TDC-160 dan 161 langkah 3 menawarkan dua cara (DOM atau payload); spec memakai intercept atas request yang dikirim `[Submit]`.
  - TC-FA-TDC-160 dan 161 menyebut "Isi Regulation Reference" tanpa nilai; spec memakai `UU HPP 7/2021; PMK 72/2023` dari fixture.
  - Klausa log TC-FA-TDC-160 dan 161 tidak menyebut surface; spec membaca ketiga surface berdasarkan jumlah entri total.
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
