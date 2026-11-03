---
id: TC-AC-ACC-E2E-230-app-access-dan-activation-email-term-pertama-client
title: "App Access Dibuat per Produk dan Activation Email Sekali pada Term Pertama Client, Tidak Lagi saat Renew"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-242
coverage:
  web: automated
---

# App Access Dibuat per Produk dan Activation Email Sekali pada Term Pertama Client, Tidak Lagi saat Renew

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix): Client "PT Baru Daftar {runId}-230" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-09 (Tabel A2): Active, Direct (tanpa relasi manager), Group Cabang Menteng, belum pernah memiliki subscription, Default User Not Yet Activated (Default User Hadi Prasetyo, Email `hadi.prasetyo+{runId}-230@qwertysystem.net`, Position kosong). Hook `after` menghapus Client lewat API.
- Kemampuan teknis (kelas d, harness eksternal): inbox email asli atau mail-catcher untuk alamat Default User `hadi.prasetyo+{runId}-230@qwertysystem.net` (TC Manual Only (c) inbox email asli); baseline jumlah email dicatat per alamat sebelum aksi pertama (S-12, R-11); kemampuan membaca App Access Default User per produk (FAMS, SAMS) disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Kemampuan teknis tambahan: halaman Admin Console > Client Subscription untuk aktivasi term pertama FAMS dan SAMS serta Renewal yang terotorisasi langsung. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-242: App Access produk dibuat saat term pertama produk itu Active; Activation Email sekali saat term pertama Client dan tidak lagi saat Renew

1. Catat jumlah email pada inbox `hadi.prasetyo+{runId}-230@qwertysystem.net` sebagai baseline (E0)
2. Ketik Search `PT Baru Daftar {runId}-230`, tekan Enter, lalu klik Company Name "PT Baru Daftar {runId}-230" untuk membuka Detail
3. Aktifkan term pertama FAMS "PT Baru Daftar {runId}-230" dari Client Subscription
4. Aktifkan term pertama SAMS "PT Baru Daftar {runId}-230"
5. Tunggu aksi selesai, lalu periksa App Access dan inbox Default User
6. Verifikasi App Access FAMS dibuat saat term FAMS Active
7. Verifikasi App Access SAMS dibuat saat term SAMS Active
8. Verifikasi jumlah email pada inbox Default User bertambah tepat satu Activation Email dari baseline E0 (dikirim saat term pertama Client, yaitu FAMS; tidak dikirim lagi saat term SAMS)
9. Lakukan Renewal FAMS yang terotorisasi langsung dari Client Subscription
10. Tunggu aksi selesai, lalu periksa inbox Default User
11. Verifikasi tidak ada Activation Email kedua setelah Renewal FAMS; inbox tetap berisi satu Activation Email

## Notes

- Langkah "Catat jumlah email ... (E0)" dan "Tunggu aksi selesai" adalah langkah penghubung (S-03, bagian 8b butir 8). Asersi "tidak ada Activation Email kedua" memakai baseline (E0 + 1) dari Verifikasi sebelumnya sebagai anchor positif (bagian 8b butir 2).
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Temuan untuk QA (S-15): TC-242 tidak menyebut cara memeriksa App Access (halaman atau endpoint) sehingga kemampuan baca disediakan tim FE/BE; Langkah 4 menyebut "Renewal FAMS yang terotorisasi langsung" tanpa menyebut prasyarat term yang memenuhi syarat Renewal. TC menyebut Client Default User Hadi Prasetyo dengan email tanpa suffix (`hadi.prasetyo@qwertysystem.net`) yang diganti email bersuffix (S-12). Post Condition (seed ulang C-09) dipenuhi hook `after`.
