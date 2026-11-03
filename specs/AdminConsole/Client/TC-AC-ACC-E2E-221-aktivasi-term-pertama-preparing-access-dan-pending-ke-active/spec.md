---
id: TC-AC-ACC-E2E-221-aktivasi-term-pertama-preparing-access-dan-pending-ke-active
title: "Aktivasi Term Pertama: Indikator Preparing Access dan Term Pending Menjadi Active pada Tanggal Mulai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-243
  - TC-AC-ACC-245
coverage:
  web: automated
---

# Aktivasi Term Pertama: Indikator Preparing Access dan Term Pending Menjadi Active pada Tanggal Mulai

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix; di-seed hook `before` lewat Fixture BE yang disediakan tim FE/BE): (a) "PT Baru Daftar A {runId}-221" dengan atribut C-09 (Tabel A2): Active, Direct (tanpa relasi manager), Group Cabang Menteng, belum pernah memiliki subscription, Default User Not Yet Activated (TC-243); (b) "PT Mulai Terjadwal {runId}-221" (atribut C-W3LIF-4: Active, Client Code `W3L-004`, FAMS satu-satunya term Pending mode New dengan Start (S) = tanggal seed + 7 hari, SAMS dan SIEM tidak pernah berlangganan, Default User Not Yet Activated) (TC-245). Hook `after` menghapus kedua Client lewat API.
- Kemampuan teknis (kelas d, harness eksternal): simulasi penyediaan instance produk FAMS (tertunda atau gagal pada setiap percobaan) untuk tenant uji; job scheduler antrean percobaan ulang; disediakan tim FE/BE tanpa endpoint karangan (S-13). Hook `after` membatalkan simulasi penyediaan dan memulihkan jam server.
- Manipulasi jam TC-245: jam server diset absolut ke pukul 22:30 pada hari sebelum S, lalu pukul 01:00 pada S (zona waktu General Settings) dan job terjadwal ditunggu berjalan; jam server dipulihkan di hook `after`. Margin terhadap batas tengah malam 00:00 pada S adalah 1 jam 30 menit; S dibaca dari Subscription Details pada langkah pertama (bagian 8b butir 3).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-243: Indikator Preparing access selama penyediaan akses produk belum siap

1. Aktifkan simulasi penyediaan instance FAMS tertunda untuk tenant "PT Baru Daftar A {runId}-221"
2. Aktifkan term pertama FAMS "PT Baru Daftar A {runId}-221" (mode New, terotorisasi langsung) dari Admin Console > Client Subscription
3. Tunggu aksi selesai, lalu buka Admin Console > Client, ketik Search `PT Baru Daftar A {runId}-221`, tekan Enter
4. Klik Company Name "PT Baru Daftar A {runId}-221", lalu buka Tab `Subscription` sub-tab `FAMS`
5. Verifikasi sub-tab `FAMS` menampilkan badge term `Active`
6. Verifikasi sub-tab `FAMS` menampilkan indikator terpisah "Preparing access" (bukan badge status)
7. Batalkan simulasi penyediaan tertunda

### TC-AC-ACC-245: Term pertama Pending menjadi Active pada tanggal mulai, dan tetap Pending sebelum tanggal mulai

8. Kembali ke List lewat breadcrumb Client, klik sub-tab `Active`, ketik Search `PT Mulai Terjadwal {runId}-221`, tekan Enter
9. Verifikasi sel FAMS baris "PT Mulai Terjadwal {runId}-221" menampilkan badge `Pending`
10. Klik Company Name "PT Mulai Terjadwal {runId}-221", buka Tab `Subscription` sub-tab `FAMS`, lalu catat Start pada Subscription Details sebagai S
11. Verifikasi Status badge `Pending`
12. Verifikasi Start terisi tanggal mulai term
13. Majukan waktu sistem ke pukul 22:30 pada hari sebelum S (zona waktu General Settings), lalu tunggu job terjadwal berjalan (job berjalan sebelum pukul 00:00 pada hari S)
14. Muat ulang Tab `Subscription` sub-tab `FAMS`
15. Verifikasi Status badge tetap `Pending`
16. Majukan waktu sistem ke pukul 01:00 pada S (zona waktu General Settings), 
17. Kembali ke Admin Console > Client, klik sub-tab `Active`, ketik Search `PT Mulai Terjadwal {runId}-221`, tekan Enter, lalu muat ulang List tiap 5 detik sampai sel FAMS baris tersebut menampilkan badge `Active` (batas tunggu 2 menit)
18. Verifikasi sel FAMS baris "PT Mulai Terjadwal {runId}-221" menampilkan badge `Active`
19. Klik Company Name "PT Mulai Terjadwal {runId}-221", buka Tab `Subscription` sub-tab `FAMS`
20. Verifikasi Status badge `Active` tanpa aksi manual

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Batalkan simulasi", "Tunggu aksi selesai", "catat Start", Majukan waktu, dan polling List langkah 17 (muat ulang tiap 5 detik, batas tunggu 2 menit, idiom bagian 6) adalah langkah penghubung atau pemicu (S-03, R-16, bagian 6). Langkah 13 sampai 15 (Pending tetap sebelum S) tidak memiliki anchor teramati bahwa job sudah berjalan dan ditandai untuk QA. Jam sistem dipulihkan di hook `after` sebelum spec lain membaca tanggal (S-09).
- Temuan untuk QA (S-15): TC-243 mock "penyediaan instance FAMS tertunda" dan TC-245 pemajuan jam/job bukan bagian aplikasi (alasan Manual Only (b)); keduanya ditulis sebagai kemampuan disediakan tim FE/BE. TC-245 menyebut "batas waktu mengikuti License Allocation Subscription" tanpa nilai; spec memakai 22:30 dan 01:00 sesuai Langkah. Post Condition TC-243 dan TC-245 (matikan mock, seed ulang, pulihkan waktu) dipenuhi hook `after` karena Client milik spec dihapus.
