---
id: TC-FA-NOTIF-E2E-110-klik-path-almost-timeout-dan-auto-canceled
title: "Klik Path: Almost Timeout Approver, Almost Timeout Requester dan PIC Admin, serta Auto Canceled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-94
  - TC-FA-NOTIF-95
coverage:
  web: automated
---

# Klik Path: Almost Timeout Approver, Almost Timeout Requester dan PIC Admin, serta Auto Canceled

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Event TC-FA-NOTIF-94" (varian Approver, transaksi masih menunggu tindakan; semua item actionable, diklik lewat `[Detail]`; urutan baris = urutan iterasi):

  | Event | Title | Item sasaran | Path tujuan |
  |---|---|---|---|
  | `borrow_almost_timeout` (Approver) | `Please finish this approval — expiring soon` | BRW-2026-0342 | `/fams/approvals/borrowing-assignment/BRW-2026-0342` |
  | `transfer_almost_timeout` (Approver) | `Please finish this approval — expiring soon` | TRF-2026-0055 | `/fams/approvals/transfer/TRF-2026-0055` |
  | `disposal_almost_timeout` (Approver) | `Please finish this approval — expiring soon` | DSP-2026-0030 | `/fams/approvals/disposal/DSP-2026-0030` |

- Tabel "Event TC-FA-NOTIF-95" (urutan baris = urutan iterasi; item view-only diklik pada judul item bukan tombol, item actionable lewat `[Detail]`):

  | Event | Title | Tier | Klik | Item sasaran | Path tujuan |
  |---|---|---|---|---|---|
  | `borrow_almost_timeout` (Requester) | `Your request is expiring soon` | view-only | judul item | BRW-2026-0342 | `/fams/borrow/BRW-2026-0342` |
  | `borrow_almost_timeout` (PIC admin) | `Please finish this transaction — expiring soon` | actionable | `[Detail]` | BRW-2026-0342 | `/fams/borrow/BRW-2026-0342` |
  | `borrow_auto_canceled` | `Your request was canceled automatically` | view-only | judul item | BRW-2026-0342 | `/fams/borrow/BRW-2026-0342` |
  | `transfer_almost_timeout` (Requester) | `Your request is expiring soon` | view-only | judul item | TRF-2026-0055 | `/fams/transactions-transfer/TRF-2026-0055` |
  | `transfer_almost_timeout` (PIC admin) | `Please finish this transaction — expiring soon` | actionable | `[Detail]` | TRF-2026-0055 | `/fams/transactions-transfer/TRF-2026-0055` |
  | `transfer_auto_canceled` | `Your request was canceled automatically` | view-only | judul item | TRF-2026-0055 | `/fams/transactions-transfer/TRF-2026-0055` |
  | `disposal_almost_timeout` (Requester) | `Your request is expiring soon` | view-only | judul item | DSP-2026-0030 | `/fams/transactions-disposal/DSP-2026-0030` |
  | `disposal_almost_timeout` (PIC admin) | `Please finish this transaction — expiring soon` | actionable | `[Detail]` | DSP-2026-0030 | `/fams/transactions-disposal/DSP-2026-0030` |
  | `disposal_auto_canceled` | `Your request was canceled automatically` | view-only | judul item | DSP-2026-0030 | `/fams/transactions-disposal/DSP-2026-0030` |

- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (Pre-setup #19), Transfer TRF-2026-0055 (#21), Disposal DSP-2026-0030 (#22), aset (#24). Total Control memegang Transaction Role Approver pada transaksi yang menunggu tindakan.
- Fixture BE pemicu event (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan notifikasi berstatus Unread sebagai notifikasi terbaru akun aktor, sehingga item sasaran tampil pada Dropdown Panel (maksimum lima item). Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi dan aset Pre-setup #19 sampai #24 menjadi sasaran pemicu event oleh fixture BE dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-94: Navigasi Klik -> Path almost timeout varian Approver

1. Pulihkan seed lewat fixture BE pemulih, siapkan tiga notifikasi almost timeout varian Approver berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
2. Untuk setiap baris tabel "Event TC-FA-NOTIF-94" (langkah 2 sampai 8): muat ulang halaman Fixed Asset > Dashboard
3. Klik Bell icon
4. Klik `[Detail]` pada item sasaran baris itu
5. Verifikasi browser berpindah ke path tujuan baris itu
6. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
7. Klik Bell icon
8. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-95: Navigasi Klik -> Path almost timeout Requester dan PIC admin serta auto canceled

9. Pulihkan seed lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
10. Untuk setiap baris tabel "Event TC-FA-NOTIF-95" (langkah 10 sampai 16): siapkan notifikasi baris itu berstatus Unread sebagai notifikasi terbaru lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
11. Klik Bell icon
12. Klik kontrol pada kolom Klik baris itu pada item sasaran baris itu
13. Verifikasi browser berpindah ke path tujuan baris itu
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 2 sampai 8 diulang untuk tiga baris tabel TC-FA-NOTIF-94 dan langkah 10 sampai 16 untuk sembilan baris tabel TC-FA-NOTIF-95 (86 langkah setelah ekspansi). Nomor langkah pada rujukan memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi, 86 langkah): semua blok satu kelas (navigasi Klik -> Path) dan tiap iterasi berdiri sendiri; kegagalan satu event tidak membuat event lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 dan 9 (pemulihan seed dan penyiapan notifikasi); langkah 10 (penyiapan notifikasi per baris karena sembilan baris melebihi lima item Dropdown Panel); langkah 6 dan 14 (kembali ke daftar, sesuai langkah TC "lalu kembali ke daftar"); langkah 2 (muat ulang di awal tiap iterasi TC-FA-NOTIF-94 agar Dropdown Panel iterasi sebelumnya tertutup dan klik Bell icon berikutnya tidak menutup panel kembali); langkah 3 (membuka Dropdown Panel di awal iterasi), langkah 11 (membuka Dropdown Panel di awal iterasi).
- Tier menentukan kontrol yang diklik, tertulis pada kolom Klik tabel TC-FA-NOTIF-95 (TC "sesuai tier"); tier tiap event diambil dari katalog PRD §5.1. Status Unread pada langkah 8 dan 16 diasumsikan dari penyiapan notifikasi baru.
- Topik Klik Path dipisah per modul tujuan (023 Approvals dan detail transaksi, 024 My Asset, 025 Assignment, Transfer, dan Disposal, 026 Asset Detail, Audit, dan Profil, 110 almost timeout dan auto canceled) walau berbagi seed dan transaksi Pre-setup #19 sampai #24, karena tiap spec butuh penyiapan fixture pemicu event dan halaman tujuan berbeda dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-94 dan 95 tidak menyebut Title dan Body per event; spec mengidentifikasi item lewat ID transaksi dan Title katalog PRD §5.1h.
  - TC-FA-NOTIF-95 tidak menyebut state transaksi untuk item actionable varian PIC admin (sehingga pre-check `[Detail]` berhasil menavigasi); spec mengandalkan fixture BE menyiapkan transaksi masih menunggu tindakan.
  - TC-FA-NOTIF-95 hanya menyebut path varian Requester dan PIC admin bersama; spec mengujinya per varian dengan path yang sama.
  - Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
