---
id: TC-FA-TDC-E2E-274-absence-log-bypass-ui-edit-ditolak-server-tidak-menulis-entri
title: "Absence Log: Edit Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-244
  - TC-FA-TDC-245
sourceRules: ["V-14", "§8.4#r7", "V-18"]
smoke: []
dependsOn: []
trace:
  "V-14": 6
  "§8.4#r7": [7, 8, 9, 17, 18, 19]
  "V-18": 16
coverage:
  web: automated
---

# Absence Log: Edit Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan intercept: `Spectra.intercept()` di atas backend nyata untuk mengganti payload request Save yang dikirim Drawer Edit; intercept dilepas segera setelah pemicu selesai (S-09). Seed dan pemulihan lewat API mengikuti `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `bgnE1` | `BGN-E1` | Asset Type Building, Useful Life 20, Allowed Methods Straight Line, Active, Used By 0 |
| `lhnE1` | `LHN-E1` | Asset Type Land, Active, Used By 0 |

- Tabel berisi tujuh class seed bawaan ditambah `BGN-E1` dan `LHN-E1` (9 baris dalam satu halaman Pagination dengan 10 baris per halaman), sehingga baris target Edit tampil tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-244: Edit Building dengan Declining Balance

1. Klik link Class Code `BGN-E1` pada tabel
2. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
3. Aktifkan intercept request Save: ganti payload Allowed Methods menjadi `Straight Line, Declining Balance`
4. Klik `[Save]`
5. Lepas intercept request Save
6. Verifikasi caption error "Declining balance does not apply to buildings." tampil di bawah field Allowed Methods
7. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
8. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
9. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini
10. Klik `[×]` pada header Drawer Edit

### TC-FA-TDC-245: Edit Land dengan Useful Life atau Allowed Methods terisi

11. Klik link Class Code `LHN-E1` pada tabel
12. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
13. Aktifkan intercept request Save: ganti payload Useful Life menjadi `10` dan Allowed Methods menjadi `Straight Line`
14. Klik `[Save]`
15. Lepas intercept request Save
16. Verifikasi caption error "Land is not depreciated." tampil di bawah field terkait (Useful Life atau Allowed Methods yang terisi)
17. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
18. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
19. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini
20. Klik `[×]` pada header Drawer Edit

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-244, dan TC-FA-TDC-245. Status respons dan state data atas request yang sama berada di spec 257 (TC-FA-TDC-244, TC-FA-TDC-245).
- Anchor positif (8b.2): caption error validasi sesudah tiap `[Save]` sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 20, tanpa perulangan (ekspansi 20); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Menutup Drawer Edit yang field-nya tidak diubah lewat UI tidak memunculkan dialog `Unsaved Changes` (payload diganti di jaringan, bukan di field), sehingga langkah penutup hanya `[×]`.
- Langkah penghubung (S-03): langkah 2, 12 (mencatat baseline tiap TC, S-12).
- Temuan untuk QA:
  - TC-FA-TDC-244 dan 245 menyebut "Kirim ulang request Save"; spec memakai intercept atas request `[Save]`.
  - Klausa log TC-FA-TDC-244 dan 245 tidak menyebut surface; spec membaca ketiga surface berdasarkan jumlah entri total.
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
