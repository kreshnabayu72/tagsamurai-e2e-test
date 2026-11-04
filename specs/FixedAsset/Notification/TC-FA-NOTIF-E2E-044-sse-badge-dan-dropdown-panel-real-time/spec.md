---
id: TC-FA-NOTIF-E2E-044-sse-badge-dan-dropdown-panel-real-time
title: "SSE: Badge Bell Icon dan Dropdown Panel Real-Time"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-180
  - TC-FA-NOTIF-181
  - TC-FA-NOTIF-182
coverage:
  web: automated
---

# SSE: Badge Bell Icon dan Dropdown Panel Real-Time

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon dan Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: TC-180 dan 181 memakai seed N-01 sampai N-07 (Pre-setup #17); TC-182 memakai N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi). Varian ditukar fixture BE penukar sebagai langkah penghubung; seed dipulihkan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>` (fixture belum ada; disediakan tim FE).
- Pemicu: sesi API akun pemicu (akun tidak tertulis di Pre-setup TC; disediakan tim FE/BE) memicu `borrow_waiting_approval` BRW-2026-0342, `damaged_repaired` (view-only), dan penerima akun aktor lewat fixture BE pemicu event.
- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): memeriksa bahwa notifikasi sudah tersimpan untuk akun aktor.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip, fixture BE pemulih dan penukar seed.

## Test Steps

### TC-FA-NOTIF-180: Notifikasi baru muncul di sesi online dan push dikirim setelah commit

1. Catat nilai badge Bell icon (baseline)
2. Lewat sesi API akun pemicu, submit aksi pemicu `borrow_waiting_approval` untuk BRW-2026-0342 hingga notifikasi tersimpan
3. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 1 tanpa memuat ulang halaman
4. Klik Bell icon
5. Verifikasi item teratas Dropdown Panel berjudul `Waiting for your approval`
6. Verifikasi (kemampuan baca BE) notifikasi `borrow_waiting_approval` BRW-2026-0342 sudah tersimpan untuk akun aktor

### TC-FA-NOTIF-181: Notifikasi baru selalu berstatus Unread saat dibuat

7. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman
8. Lewat sesi API akun pemicu, picu satu notifikasi view-only `damaged_repaired` untuk akun aktor hingga notifikasi tersimpan
9. Lewat sesi API akun pemicu, picu satu notifikasi actionable `borrow_waiting_approval` untuk akun aktor hingga notifikasi tersimpan
10. Klik Bell icon
11. Verifikasi Title item actionable (teratas) dan item view-only (kedua) tampil bold
12. Verifikasi dot Unread tampil pada kedua item
13. Verifikasi item view-only memiliki tombol `[Mark as Read]` tanpa `[Detail]`
14. Verifikasi item actionable memiliki tombol `[Detail]` tanpa `[Mark as Read]`

### TC-FA-NOTIF-182: Dropdown Panel yang terbuka memperbarui list saat notifikasi baru masuk via SSE

15. Pulihkan seed notifikasi lewat fixture BE pemulih, tukar ke varian N-01 sampai N-37 (Pre-setup #17 dan #18) lewat fixture BE penukar, lalu muat ulang halaman
16. Klik Bell icon dan biarkan Dropdown Panel terbuka
17. Catat nilai badge Bell icon serta judul dan isi item kelima (terlama) pada Dropdown Panel
18. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` untuk akun aktor hingga notifikasi tersimpan
19. Verifikasi item baru berjudul `Waiting for your approval` tampil di posisi teratas Dropdown Panel tanpa memuat ulang halaman
20. Verifikasi item terlama yang dicatat pada langkah 17 tidak tampil lagi pada Dropdown Panel
21. Verifikasi Dropdown Panel tetap menampilkan 5 notifikasi terbaru
22. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 17 tanpa memuat ulang halaman
23. Pulihkan seed notifikasi Pre-setup #17 dan #18 lewat fixture BE pemulih

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7, 15 (pemulihan seed dan penukaran varian), 16 (precondition TC-182), 23 (pemulihan seed).
- Asersi tambahan (S-03): langkah 5 hanya memeriksa judul item teratas karena isi item tidak ditulis TC; langkah 6 memakai kemampuan baca BE untuk klausa "notifikasi sudah tersimpan saat badge muncul"; langkah 20 mengasersi item terlama keluar (butir a TC-182 dipecah per klausa).
- Temuan untuk QA:
  - TC-180 menulis "tersimpan saat badge muncul" tanpa cara observasi; spec memeriksanya lewat kemampuan baca BE tepat setelah badge bertambah, sehingga urutan waktu persisnya tidak teruji.
  - TC-181 tidak menyebut jenis event view-only dan actionable yang dipicu; spec memakai `damaged_repaired` dan `borrow_waiting_approval`, dan mengidentifikasi item lewat posisi teratas dan kedua pada Dropdown Panel (terbaru di atas).
  - TC-180 sampai 182 menulis "akun lain" tanpa menyebut akun pemicu.
