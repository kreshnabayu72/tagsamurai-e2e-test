---
id: TC-FA-TDC-E2E-268-absence-log-request-langsung-role-matrix-cancel-scheduled-version-ditolak-tidak-menulis-entri
title: "Absence Log: Request Langsung Role Matrix Cancel Scheduled Version yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-823
  - TC-FA-TDC-824
  - TC-FA-TDC-825
  - TC-FA-TDC-826
sourceRules: ["§[F-FATDC-03] Cancel Scheduled Version#p1", "§9.3#p1", "§8.4#r7", "J-04"]
smoke: []
dependsOn: []
trace:
  "§[F-FATDC-03] Cancel Scheduled Version#p1": 3
  "§9.3#p1": 3
  "§8.4#r7": [4, 5, 6]
  "J-04": [4, 5, 6]
coverage:
  web: automated
---

# Absence Log: Request Langsung Role Matrix Cancel Scheduled Version yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (akun default suite; password `Spectra.env.FA_TC_PASSWORD`) untuk seeding; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI: request yang diuji memakai sesi API role iterasi, sedangkan setiap langkah baca (baseline dan jumlah entri sesudah request) memakai kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding) karena role iterasi tidak tentu punya akses Read. Nama env pada tabel didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh penulis script.
- Role yang diuji (akun tiap role disediakan tim FE karena tidak ada nomor Pre-setup di TC; sesi API dibuka dengan login API per role dan tidak dihitung sebagai sesi web):

| Role | Password (env) |
|---|---|
| Read Only | `Spectra.env.FA_RO_PASSWORD` |
| Manage accounting (Read saja) | `Spectra.env.FA_READ_PASSWORD` |
| Manage accounting (Create saja) | `Spectra.env.FA_CREATEONLY_PASSWORD` |
| Manage accounting (Delete saja) | `Spectra.env.FA_DELETEONLY_PASSWORD` |

- Tabel "Request yang diuji": tiap baris dikirim satu per satu oleh setiap role pada kolom Role, tanpa melalui UI; baseline log dicatat per role sebelum request role itu (satu TC satu iterasi, S-12).

| Jenis request | Role (sesi API) | TC |
|---|---|---|
| Cancel Scheduled Version | Read Only; Manage accounting (Read saja); Manage accounting (Create saja); Manage accounting (Delete saja) | 823, 824, 825, 826 |

- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor role iterasi untuk request yang diuji (login API per role) dan aktor Total Control (sesi seeding) untuk pembacaan log, seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13). Langkah spec tidak memakai UI selain pembacaan log.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13): kemampuan baca log fixture BE yang membaca jumlah entri Changelog (modul Tax Depreciation Class), System Log (akun role iterasi), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`) dengan sesi API aktor Total Control (sesi seeding). Baseline dicatat tepat sebelum request tiap TC dan dibandingkan dengan jumlah entri sesudah request TC itu; baseline dan jumlah sesudahnya dibaca lewat sumber yang sama (8b.10, S-12). Bila selisih terbukti, entri baru dibaca pada baris teratas urutan default Date terbaru di surface UI-nya (S-14).
- Spec absence (kelas g, S-05, P-5 butir a): request yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi status respons dan state data atas request yang sama berada di spec asal.

- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `bldNp` | `BLD-NP` | memiliki versi Scheduled mulai Jan 2027 yang tahun pajaknya belum dimulai |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Cancel Scheduled Version (TC 823, 824, 825, 826)

1. Untuk setiap role pada baris Cancel Scheduled Version tabel "Request yang diuji" (langkah 1 sampai 6), catat baseline jumlah entri Changelog, System Log akun role iterasi, dan Activity Log lewat kemampuan baca log fixture BE dengan sesi API aktor Total Control (sesi seeding)
2. Kirim request langsung untuk membatalkan versi Scheduled `BLD-NP` tanpa melalui UI dengan sesi API role iterasi
3. Verifikasi server menolak request role iterasi dengan 403 Forbidden
4. Verifikasi jumlah entri Changelog (dibaca lewat kemampuan baca log fixture BE) sama dengan baseline role iterasi
5. Verifikasi jumlah entri System Log akun role iterasi sama dengan baseline role iterasi
6. Verifikasi jumlah entri Activity Log sama dengan baseline role iterasi

## Notes

- S-05 dan prinsip 13g: spec ini memuat aksi nyata (request langsung ditolak) dan baseline sendiri per TC (S-12) untuk klausa "tidak ada entri log baru" Expected c berikut: Cancel Scheduled Version (TC-FA-TDC-823, TC-FA-TDC-824, TC-FA-TDC-825, dan TC-FA-TDC-826). Status respons dan state data atas request yang sama berada di spec Role Matrix 215 (Cancel Scheduled Version).
- Anchor positif (8b.2): `Verifikasi` penolakan 403 Forbidden pada tiap iterasi sebelum asersi jumlah entri. Pemicu tidak menyentuh satu entitas log tertentu, sehingga asersinya memakai surface agregat (jumlah total entri sebelum dan sesudah, 8b.2). System Log dibaca untuk akun role iterasi, yaitu akun pemanggil request.
- P-5 butir (a): request langsung yang ditolak hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memiliki sesi API role sendiri, baseline sendiri, request sendiri, dan pembacaan jumlah entri sendiri (satu iterasi satu TC).
- Perulangan atas role pada baris tabel "Request yang diuji" (Cancel Scheduled Version: langkah 1 sampai 6 diulang untuk 4 role): tiap role membuka sesi API sendiri dan keenam langkah tiap iterasi identik; hanya sesi API dan akun yang dibaca System Log-nya yang berbeda.
- Jumlah langkah: nominal 6, ekspansi loop 24 langkah (4 x 6).
- Langkah penghubung (S-03): langkah 1 (mencatat baseline pada tiap iterasi, S-12).
- Sesi pembaca state: baseline dan jumlah entri sesudah request dibaca dengan sesi API aktor Total Control (sesi seeding), bukan sesi role iterasi, supaya hasil baca tidak bergantung pada akses Read role yang diuji; role iterasi hanya mengirim request yang diuji (8b.1).
- Temuan untuk QA:
  - Klausa Expected c TC-FA-TDC-823 sampai TC-FA-TDC-826 menyebut surface secara berbeda ("Changelog dan Activity Log untuk class tersebut", "untuk kedua class", atau "entri log baru" tanpa surface); spec membaca ketiga surface (Changelog, System Log akun role pemanggil, Activity Log) berdasarkan jumlah entri total, bukan filter per class.
  - Akun, email, dan company tiap role tidak tertulis di TC (tanpa nomor Pre-setup); nama env password adalah usulan.
  - TC memakai class Pre-setup (`NB-OLD`, `NB-4`, `BLD-NP`, dan lain-lain) sebagai target; spec memakai kode literal yang sama sebagai data milik spec yang di-seed idempotent, karena Class Code maksimal 15 karakter (S-12).
  - Cara membaca jumlah entri ketiga surface tidak disebut TC; spec memakai kemampuan baca log fixture BE yang disediakan tim FE/BE.
