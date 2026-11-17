---
id: TC-FA-TDC-E2E-270-absence-log-request-langsung-effective-from-dan-allowed-methods-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung Allowed Methods dan Effective From Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-841
  - TC-FA-TDC-845
  - TC-FA-TDC-846
  - TC-FA-TDC-927
sourceRules: ["F-FATDC-02.k6a", "F-FATDC-02.k6c", "FATDC-LOGIC-10a", "FATDC-LOGIC-10b.3", "§8.4#r7", "J-04", "F-FATDC-02.k7a", "V-20", "FATDC-LOGIC-04f.1", "V-22", "FATDC-LOGIC-04af"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-02.k6a": 4
  "F-FATDC-02.k6c": 4
  "FATDC-LOGIC-10a": 4
  "FATDC-LOGIC-10b.3": 4
  "§8.4#r7": [6, 7, 8, 12, 13, 14, 20, 21, 22, 28, 29, 30]
  "J-04": [6, 7, 8, 12, 13, 14, 20, 21, 22, 28, 29, 30]
  "F-FATDC-02.k7a": 11
  "V-20": [11, 26]
  "FATDC-LOGIC-04f.1": 18
  "V-22": 18
  "FATDC-LOGIC-04af": 26
coverage:
  web: automated
---

# Absence Log: Request Langsung Allowed Methods dan Effective From Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung, seed dan pemulihan lewat API (Used By lewat Asset Class pemakai dan versi Scheduled, Current, dan Past), serta kendali jam sistem (jam server dan jam browser diatur bersama). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam diatur sesudah baseline TC yang memakainya dan dipulihkan sebelum jumlah entri dibaca (S-09, R-10); TC-FA-TDC-841, TC-FA-TDC-846, dan TC-FA-TDC-927 memakai jam (langkah 2, 5, 16, 19, 24, 27). Hook `after` memulihkan jam bila spec berhenti di tengah. Sesi UI dan sesi API tetap valid selama jam digeser (dinyatakan di `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb2` | `NB-2` | Active, Used By 3 (Asset Class pemakai disediakan tim FE/BE), Straight Line dan Declining Balance, satu versi; Asset Class `AC-MESIN` memakainya dengan Tax Method Declining Balance |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, hanya satu versi (versi pertama tanpa Effective From) |
| `khsJ2028` | `KHS-J2028` | memiliki versi Current dan versi Scheduled mulai Jan 2028 sebagai versi terakhir (pengganti `NB-2` untuk TC-FA-TDC-846 agar tidak berbagi class dengan TC-FA-TDC-841) |

- State global yang diubah spec: jam server dan jam browser (langkah 2, 5, 16, 19, 24, 27), dipulihkan segera sesudah anchor penolakan tiap TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-841: Persempit Allowed Methods yang masih dipakai

1. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
3. Kirim request langsung dengan sesi API Total Control untuk mengubah Allowed Methods `NB-2` menjadi `Straight Line` saja dengan Effective From `1 Januari 2026` tanpa melalui UI
4. Verifikasi server menolak request tanpa membentuk versi baru
5. Pulihkan jam server dan jam browser
6. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
7. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
8. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-845: Effective From bukan awal tahun pajak

9. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
10. Kirim request langsung dengan sesi API Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Maret 2027` tanpa melalui UI
11. Verifikasi server menolak request tanpa membentuk versi baru
12. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
13. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
14. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-846: Effective From lebih awal dari versi terakhir

15. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
16. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
17. Kirim request langsung dengan sesi API Total Control untuk mengubah Useful Life `KHS-J2028` menjadi `12` dengan Effective From `1 Januari 2027` tanpa melalui UI
18. Verifikasi server menolak request tanpa membentuk versi baru
19. Pulihkan jam server dan jam browser
20. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
21. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
22. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

### TC-FA-TDC-927: Effective From lebih dari 5 tahun pajak setelah tahun pajak berjalan

23. Catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
24. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
25. Kirim request langsung dengan sesi API Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2032` tanpa melalui UI
26. Verifikasi server menolak request tanpa membentuk versi baru
27. Pulihkan jam server dan jam browser
28. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline TC ini
29. Verifikasi jumlah entri System Log Total Control sama dengan baseline TC ini
30. Verifikasi jumlah entri Activity Log sama dengan baseline TC ini

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-841, TC-FA-TDC-845, TC-FA-TDC-846, dan TC-FA-TDC-927. Status respons dan state data atas request yang sama berada di spec 220 (TC-FA-TDC-841), 221 (TC-FA-TDC-845, TC-FA-TDC-846), dan 223 (TC-FA-TDC-927).
- Anchor positif (8b.2): `Verifikasi` penolakan server sesudah tiap request sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Jumlah langkah: nominal 30, tanpa perulangan (ekspansi 30); tiap blok TC memuat baseline, request, anchor, dan tiga `Verifikasi` jumlah entri.
- Jam: TC-FA-TDC-841, TC-FA-TDC-846, dan TC-FA-TDC-927 bergantung pada tahun pajak berjalan (Effective From awal tahun pajak, versi terakhir, dan batas 5 tahun pajak); jam diatur sesudah baseline TC itu dan dipulihkan sebelum jumlah entri dibaca, sehingga baseline dan pembacaan dilakukan pada jam yang sama dengan sistem (S-09, R-10). TC-FA-TDC-845 tidak bergantung pada jam.
- Langkah penghubung (S-03): langkah 1, 9, 15, 23 (mencatat baseline tiap TC, S-12); langkah 2, 5, 16, 19, 24, 27 (mengatur dan memulihkan jam).
- Temuan untuk QA:
  - Klausa Expected c TC-FA-TDC-841 sampai TC-FA-TDC-927 menyebut "Changelog dan Activity Log untuk class tersebut" atau "entri log baru" tanpa surface; spec membaca ketiga surface (Changelog, System Log Total Control, Activity Log) berdasarkan jumlah entri total, bukan filter per class.
  - TC-FA-TDC-846 memakai `NB-2` dengan versi Scheduled Jan 2028 sebagai versi terakhir, sedangkan TC-FA-TDC-841 memakai `NB-2` dengan Used By 3; spec memakai `KHS-J2028` untuk TC-FA-TDC-846 agar penolakan TC-FA-TDC-841 tidak tertutup alasan penolakan lain. Konfirmasi QA bila `NB-2` bersama dikehendaki.
  - TC-FA-TDC-841 menyebut "Effective From awal tahun pajak berjalan" tanpa nilai tanggal; spec memakai `1 Januari 2026` (Fiscal Year Start Januari, tanggal sistem uji 15 Okt 2026).
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
