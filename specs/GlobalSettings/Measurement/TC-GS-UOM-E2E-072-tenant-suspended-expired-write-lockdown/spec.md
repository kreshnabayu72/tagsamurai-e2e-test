---
id: TC-GS-UOM-E2E-072-tenant-suspended-expired-write-lockdown
title: "Write Lockdown saat Client Suspended atau Expired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-239
  - TC-GS-UOM-240
coverage:
  web: automated
---

# Write Lockdown saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pengubah status Client A (hanya lewat API, tanpa login UI) | Total Control (Principal, Hendra Wijaya) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before` saat Client A berstatus Active, milik spec ini: `Liter {runId}-072` / `L` dan `Meter {runId}-072` / `m` (pengganti Liter dan Meter Pre-setup; target Edit dan Delete yang ditolak). `Grain {runId}-072` / `gr` adalah input Create yang ditolak sehingga tidak membuat data.
- Kemampuan teknis: mengubah status Client A menjadi Suspended dan Expired lewat sesi API aktor (lihat `suite.md`, bagian Hook suite) dengan akun Total Control (Principal) di atas; akun itu harus berhak mengubah status Client A dan endpoint ubah status disediakan tim FE (belum terkonfirmasi). Perubahan status dilakukan sebagai langkah eksplisit di spec.
- Kemampuan teknis (muat ulang): penanganan dialog `beforeunload` browser pada langkah muat ulang halaman (2, 5, 8, 11, 16, 19): dialog dikonfirmasi `Leave` secara otomatis oleh harness; disediakan tim FE (S-08).
- Syarat eksekusi: status Client A diubah untuk seluruh tenant, sehingga suite berjalan serial (`parallel: false`) dan spec ini dijalankan tanpa spec Client A lain yang berjalan bersamaan; spec Client A lain berjalan sebelum atau sesudahnya saat Client A Active.
- State global yang dipulihkan (hook `after`, tetap jalan walau spec gagal di tengah): status Client A dikembalikan ke Active lewat API dengan akun Principal yang sama.
- Cleanup (hook `after`, setelah status dipulihkan ke Active): hapus lewat API `Liter`, `Meter`, dan `Grain` bersuffix `{runId}-072` bila ada.
- TC-GS-UOM-239, 240: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-239: Aksi tulis saat entitas Suspended ditolak

1. Ubah status Client A menjadi Suspended (lewat API dengan akun Total Control Principal)
2. Muat ulang halaman Global Settings > Master Reference > Measurement
3. Klik [+ Unit], isi Unit Name `Grain {runId}-072` dan Symbol `gr`, klik [Submit]
4. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
5. Muat ulang halaman Measurement, ketik Search `{runId}-072`, tekan Enter
6. Klik `⋯` pada baris `Liter {runId}-072` > Edit, ubah Symbol menjadi `ltr`, klik [Save]
7. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
8. Muat ulang halaman Measurement, ketik Search `{runId}-072`, tekan Enter
9. Klik `⋯` pada baris `Meter {runId}-072` > Delete, klik [Delete] pada dialog
10. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
11. Muat ulang halaman Measurement, ketik Search `{runId}-072`, tekan Enter
12. Verifikasi `Liter {runId}-072` dan `Meter {runId}-072` tampil di tabel (anchor)
13. Verifikasi Symbol `Liter {runId}-072` tetap `L`
14. Verifikasi `Grain {runId}-072` tidak ada di tabel

### TC-GS-UOM-240: Aksi tulis saat entitas Expired ditolak

15. Ubah status Client A menjadi Expired (lewat API dengan akun Total Control Principal)
16. Muat ulang halaman Global Settings > Master Reference > Measurement
17. Klik [+ Unit], isi Unit Name `Grain {runId}-072` dan Symbol `gr`, klik [Submit]
18. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
19. Muat ulang halaman Global Settings > Master Reference > Measurement

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas state tenant (prinsip 13h): write-lockdown dipisah dari verifikasi baca murni.
- TC-GS-UOM-239 memuat tiga aksi (Create, Edit, Delete) dalam satu TC dan diasersi per aksi; "Data tidak berubah" (Expected b) diasersi pada langkah 12 sampai 14 sesudah ketiga aksi.
- Langkah penghubung: langkah 1 dan 15 (mengubah status Client A sesuai precondition TC "Client A berstatus Suspended" atau "Expired"), langkah 2 dan 16 (muat ulang agar halaman memakai status terbaru), langkah 5, 8, dan 11 (muat ulang halaman Measurement supaya state modal sesudah penolakan tidak diandalkan dan Search baris target milik spec; TC tidak menyebut apakah modal Create, Edit, atau dialog Delete tertutup sesudah penolakan).
- Langkah 19 (muat ulang halaman Measurement) mengakhiri bagian Expired dan membuang form Create yang ditolak, sehingga spec tidak berakhir dengan form dirty (S-09); langkah penghubung tanpa `Verifikasi`.
- Status Client A diubah saat sesi Total Control sudah aktif; apakah sesi tetap valid setelah status berubah adalah asumsi TC (precondition TC menyebut Client A berstatus Suspended atau Expired dan user berada di Measurement).
- Pembacaan tabel (langkah 5, 8, 11) saat Client A Suspended diasumsikan tetap tersedia; asersi baca saat Suspended berada di spec lain bila ada TC-nya.
- Temuan untuk QA:
  - Akun pengubah status Client A, hak ubahnya, dan endpoint-nya tidak disebut TC, PRD, atau LLD Measurement (S-13); disediakan tim FE.
  - TC-GS-UOM-239 dan 240 menyebut `Grain` / `gr` tanpa suffix, `Liter`, dan `Meter` Pre-setup; spec memakai unit milik spec bersuffix (S-06, S-12).
  - TC-GS-UOM-239 dan 240 tidak menyatakan apakah modal tertutup atau list di-refresh sesudah penolakan; spec tidak mengasersinya. Karena TC tidak menetapkan keadaan itu, bagian Expired diakhiri muat ulang halaman (langkah 19), bukan penutupan modal lewat `✕`.
  - TC-GS-UOM-239 dan 240 tidak punya Post Condition di luar Expected.
