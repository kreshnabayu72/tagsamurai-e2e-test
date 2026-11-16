---
id: TC-FA-TDC-E2E-262-absence-log-request-langsung-create-tidak-valid-state-tenant-dan-periode-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung pada Plan Starter, Entitas Suspended, dan Periode Tertutup yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-831
  - TC-FA-TDC-888
  - TC-FA-TDC-847
sourceRules: ["E-FATDC-67", "E-FATDC-62", "E-FATDC-18"]
smoke: []
dependsOn: []
trace:
  "E-FATDC-67": [4, 6, 7, 8]
  "E-FATDC-62": [12, 14, 15, 16]
  "E-FATDC-18": [21, 24, 25, 26]
coverage:
  web: automated
---

# Absence Log: Request Langsung pada Plan Starter, Entitas Suspended, dan Periode Tertutup yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung, seed dan pemulihan lewat API (periode Accounting Period), kendali jam sistem (jam server dan jam browser diatur bersama), serta perubahan plan company dan status company (disediakan tim FE/BE). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam diatur sesudah baseline TC yang memakainya dan dipulihkan sebelum jumlah entri dibaca (S-09, R-10); TC-FA-TDC-847 memakai jam (langkah 18, 22). Hook `after` memulihkan jam bila spec berhenti di tengah. Sesi UI dan sesi API tetap valid selama jam digeser (dinyatakan di `suite.md`).
- Perubahan plan company, status client, dan status periode Accounting Period dilakukan lewat kemampuan fixture BE yang tidak menulis entri ke Changelog, System Log, dan Activity Log modul ini (disediakan tim FE/BE); baseline tiap TC dicatat sebelum perubahan state pertama TC itu, dan state dipulihkan sebelum jumlah entri dibaca.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, hanya satu versi (versi pertama tanpa Effective From) |
| `periode2026` | `Accounting Period tahun pajak 2026` | 12 periode berstatus Open (nilai awal); ditutup (Closed) pada langkah 19 dan dikembalikan pada langkah 23 |

- State global yang diubah spec: plan company (Starter, langkah 2, dipulihkan langkah 5), status entitas client (Suspended, langkah 10, dipulihkan langkah 13), status 12 periode Accounting Period tahun pajak 2026 (Closed langkah 19, dipulihkan langkah 23), dan jam server serta jam browser (langkah 18, 22); hook `after` memulihkan semuanya bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-831: Request tulis pada plan Starter

1. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Turunkan plan company dari Growth ke Starter tanpa menghapus data class
3. Kirim request langsung dengan sesi API Total Control untuk mengubah Class Name `NB-4` menjadi `Kelompok 4 Starter` tanpa melalui UI
4. Verifikasi server menolak request dengan 403 Forbidden
5. Pulihkan plan company ke Growth
6. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
7. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
8. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-888: Deactivate saat entitas Suspended

9. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
10. Ubah status entitas client menjadi Suspended
11. Kirim request langsung dengan sesi API Total Control untuk menonaktifkan class `NB-4` tanpa melalui UI
12. Verifikasi server menolak request dengan 403 Forbidden walau aktor adalah Total Control
13. Pulihkan status entitas client ke Active
14. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
15. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
16. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-847: Effective From pada tahun pajak tertutup

17. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
18. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
19. Tutup seluruh 12 periode Accounting Period tahun pajak 2026 (status Closed)
20. Kirim request langsung dengan sesi API Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2026` tanpa melalui UI
21. Verifikasi server menolak request tanpa membentuk versi baru
22. Pulihkan jam server dan jam browser
23. Kembalikan seluruh 12 periode Accounting Period tahun pajak 2026 ke status Open
24. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
25. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
26. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-831, TC-FA-TDC-888, dan TC-FA-TDC-847. Status respons dan state data atas request yang sama berada di spec 217 (TC-FA-TDC-831, TC-FA-TDC-888) dan 221 (TC-FA-TDC-847).
- Anchor positif (8b.2): `Verifikasi` penolakan server sesudah tiap request sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 26, tanpa perulangan (ekspansi 26); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Jam: TC-FA-TDC-847 mensyaratkan tanggal sistem uji 15 Okt 2026 (Effective From Jan 2026 = awal tahun pajak berjalan); jam diatur sesudah baseline TC itu dan dipulihkan sebelum jumlah entri dibaca (S-09, R-10).
- State pemicu: plan Starter (TC-FA-TDC-831), status Suspended (TC-FA-TDC-888), dan periode Closed (TC-FA-TDC-847) hanya mengondisikan request yang ditolak; state itu dipulihkan sebelum pembacaan log agar surface log dapat dibuka dan dibaca.
- Langkah penghubung (S-03): langkah 1, 9, 17 (mencatat baseline tiap TC, S-12); langkah 18, 22 (mengatur dan memulihkan jam); langkah 2, 5, 10, 13, 19, 23 (membentuk dan memulihkan state pemicu).
- Temuan untuk QA:
  - TC-FA-TDC-831, TC-FA-TDC-888, dan TC-FA-TDC-847 menyebut "Tidak ada entri log baru" tanpa surface; spec membaca ketiga surface (Changelog, System Log Total Control, Activity Log) berdasarkan jumlah entri total, bukan filter per class.
  - TC-FA-TDC-831, 888, dan 847 membutuhkan perubahan plan, status client, dan data Accounting Period tanpa mekanisme di TC; kemampuannya disediakan tim FE/BE, dan perubahan itu harus tidak menulis entri ke tiga surface log (bila menulis, baseline TC perlu dicatat ulang sesudah tiap perubahan).
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
