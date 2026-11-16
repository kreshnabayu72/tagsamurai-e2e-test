---
id: TC-FA-TDC-E2E-272-absence-log-request-langsung-create-payload-tidak-valid-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung Create dengan Payload Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-851
  - TC-FA-TDC-852
  - TC-FA-TDC-853
  - TC-FA-TDC-854
  - TC-FA-TDC-855
  - TC-FA-TDC-856
  - TC-FA-TDC-857
  - TC-FA-TDC-858
sourceRules: ["E-FATDC-03", "V-07", "V-06", "E-FATDC-02", "V-02", "V-03", "V-09", "E-FATDC-05", "V-12", "E-FATDC-04", "V-05", "§8.4#r7", "J-04"]
smoke: []
dependsOn: []
trace:
  "E-FATDC-03": 3
  "V-07": 3
  "V-06": 3
  "E-FATDC-02": 3
  "V-02": 3
  "V-03": 3
  "V-09": 3
  "E-FATDC-05": 3
  "V-12": 3
  "E-FATDC-04": 3
  "V-05": 3
  "§8.4#r7": [4, 5, 6]
  "J-04": [4, 5, 6]
coverage:
  web: automated
---

# Absence Log: Request Langsung Create dengan Payload Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (akun default suite). Email akun, company uji, dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung, seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (Total Control), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb9` | `NB-9` | belum ada di daftar |

- Nilai request dasar Create `NB-9`: Class Name `Kelompok 9 uji`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`, Regulation Reference `UU HPP 7/2021`.
- Tabel "Payload Create tidak valid" (tiap baris mengubah satu field dari nilai request dasar `NB-9`; satu baris satu TC):

| TC | Field yang diubah | Nilai |
|---|---|---|
| 851 | Class Name | `Kelompok 🙂` |
| 852 | Class Name | sepanjang 121 karakter |
| 853 | Class Code | `NB 9/x` |
| 854 | Class Code | `ABCDEFGHIJKLMNOP` (16 karakter) |
| 855 | Regulation Reference | sepanjang 256 karakter |
| 856 | Useful Life | `101` |
| 857 | Useful Life | `7.5` |
| 858 | Class Name | hanya spasi |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Untuk setiap baris tabel "Payload Create tidak valid" (langkah 1 sampai 6), catat baseline jumlah entri Changelog, System Log Total Control, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding) untuk baris iterasi
2. Kirim request langsung dengan sesi API Total Control untuk membuat class `NB-9` dengan nilai request dasar dan field yang diubah sesuai baris iterasi tanpa melalui UI
3. Verifikasi server menolak request baris iterasi tanpa membuat class
4. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline baris iterasi
5. Verifikasi jumlah entri System Log Total Control sama dengan baseline baris iterasi
6. Verifikasi jumlah entri Activity Log sama dengan baseline baris iterasi

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c TC-FA-TDC-851, TC-FA-TDC-852, TC-FA-TDC-853, TC-FA-TDC-854, TC-FA-TDC-855, TC-FA-TDC-856, TC-FA-TDC-857, dan TC-FA-TDC-858. Status respons dan state data atas request yang sama berada di spec 222 (TC-FA-TDC-851, TC-FA-TDC-852, TC-FA-TDC-853, TC-FA-TDC-854, TC-FA-TDC-855) dan 223 (TC-FA-TDC-856, TC-FA-TDC-857, TC-FA-TDC-858).
- Anchor positif (8b.2): `Verifikasi` penolakan server pada tiap iterasi sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2).
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki baseline sendiri yang dicatat sesudah TC sebelumnya selesai dibaca dan tepat sebelum request TC itu, lalu tiga `Verifikasi` selisih jumlah entri sendiri (satu TC satu blok).
- Perulangan atas baris tabel "Payload Create tidak valid" (langkah 1 sampai 6 diulang untuk 8 baris): keenam langkah tiap iterasi identik dan hanya satu field payload yang berbeda; baseline dicatat di dalam badan perulangan, jadi tiap baris (satu TC) punya baseline sendiri.
- Jumlah langkah: nominal 6, ekspansi loop 48 langkah (8 baris x 6 langkah).
- Alasan ekspansi di atas ~35 langkah (48): 8 TC berkelas sama (absence log, kelas g) dengan request, surface log, dan anchor penolakan yang identik; panjangnya adalah perulangan 8 baris payload dengan baseline sendiri per TC, bukan topik berbeda.
- Langkah penghubung (S-03): langkah 1 (mencatat baseline tiap TC, S-12).
- Temuan untuk QA:
  - TC-FA-TDC-851 sampai TC-FA-TDC-858 menyebut "Server menolak request" tanpa status HTTP dan "Tidak ada entri log baru" tanpa surface; spec mengasersi penolakan tanpa kode dan membaca ketiga surface berdasarkan jumlah entri total.
  - TC-FA-TDC-851 sampai 858 memakai `NB-9` dan nilai request dasar yang tidak disebut lengkap oleh TC; spec memakai nilai dasar yang sama dengan spec asal. Karakter dan panjang string pada TC-FA-TDC-852 dan 855 dibentuk oleh penulis script.
  - TC-FA-TDC-853 dan 854 mengasersi "Class NB-9 tidak ada di daftar" walau kode yang dikirim berbeda (`NB 9/x` dan 16 karakter); request tetap dikirim dengan Class Code pada tabel payload.
  - Akun, email, dan company Total Control tidak tertulis di TC.
  - Class Code dibatasi 15 karakter, sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
