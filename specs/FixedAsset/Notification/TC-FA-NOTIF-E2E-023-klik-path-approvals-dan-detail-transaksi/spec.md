---
id: TC-FA-NOTIF-E2E-023-klik-path-approvals-dan-detail-transaksi
title: "Klik Path: Approvals dan Detail Transaksi per Kelompok Event"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-85
  - TC-FA-NOTIF-86
coverage:
  web: automated
---

# Klik Path: Approvals dan Detail Transaksi per Kelompok Event

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Kelompok event TC-FA-NOTIF-85" (transaksi masih menunggu tindakan; semua item actionable, diklik lewat `[Detail]`; urutan baris = urutan iterasi):

  | Event | Title | Item sasaran | Path tujuan |
  |---|---|---|---|
  | `borrow_waiting_approval` | `Waiting for your approval` | BRW-2026-0342 | `/fams/approvals/borrowing-assignment/BRW-2026-0342` |
  | `assignment_waiting_approval` | `Waiting for your approval` | ASG-2026-0120 | `/fams/approvals/borrowing-assignment/ASG-2026-0120` |
  | `transfer_waiting_approval` | `Waiting for your approval` | TRF-2026-0055 | `/fams/approvals/transfer/TRF-2026-0055` |
  | `disposal_waiting_approval` | `Waiting for your approval` | DSP-2026-0030 | `/fams/approvals/disposal/DSP-2026-0030` |
  | `audit_waiting_approval` | `Waiting for your approval` | TASK-Q3-A | `/fams/approvals/audit/TASK-Q3-A` |

- Tabel "Kelompok event TC-FA-NOTIF-86" (semua item view-only, diklik pada judul item bukan tombol; Title mengikuti varian Approved atau Rejected pada seed fixture):

  | Event | Title | Item sasaran | Path tujuan |
  |---|---|---|---|
  | `borrow_resolved` | `Your request has been approved` atau `Your request has been rejected` | BRW-2026-0341 | `/fams/borrow/BRW-2026-0341` |
  | `assignment_resolved` | `Your request has been approved` atau `Your request has been rejected` | ASG-2026-0120 | `/fams/transactions-assignment/ASG-2026-0120` |
  | `transfer_resolved` | `Your request has been approved` atau `Your request has been rejected` | TRF-2026-0055 | `/fams/transactions-transfer/TRF-2026-0055` |
  | `disposal_resolved` | `Your request has been approved` atau `Your request has been rejected` | DSP-2026-0030 | `/fams/transactions-disposal/DSP-2026-0030` |
  | `audit_resolved` | `Your request has been approved` atau `Your request has been rejected` | TASK-Q3-A | `/fams/audit/task/TASK-Q3-A` |

- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0341 dan BRW-2026-0342 (Pre-setup #19), Assignment ASG-2026-0120 (#20), Transfer TRF-2026-0055 (#21), Disposal DSP-2026-0030 (#22), task audit TASK-Q3-A (#23), aset (#24). Total Control memegang Transaction Role Approver pada transaksi yang menunggu tindakan.
- Fixture BE pemicu event (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan, sebagai langkah penghubung sebelum tiap TC, lima notifikasi kelompok event TC itu berstatus Unread sebagai lima notifikasi terbaru akun aktor sehingga seluruhnya tampil pada Dropdown Panel (maksimum lima item). Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi, aset, dan task Pre-setup #19 sampai #24 menjadi sasaran pemicu event oleh fixture BE dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-85: Navigasi Klik -> Path kelompok event Approvals

1. Pulihkan seed lewat fixture BE pemulih, siapkan lima notifikasi kelompok event TC-FA-NOTIF-85 berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
2. Untuk setiap baris tabel "Kelompok event TC-FA-NOTIF-85" (langkah 2 sampai 8): muat ulang halaman Fixed Asset > Dashboard
3. Klik Bell icon
4. Klik `[Detail]` pada item sasaran baris itu
5. Verifikasi browser berpindah ke path tujuan baris itu
6. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
7. Klik Bell icon
8. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-86: Navigasi Klik -> Path kelompok event detail transaksi di modul asal

9. Pulihkan seed lewat fixture BE pemulih, siapkan lima notifikasi kelompok event TC-FA-NOTIF-86 berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
10. Untuk setiap baris tabel "Kelompok event TC-FA-NOTIF-86" (langkah 10 sampai 16): muat ulang halaman Fixed Asset > Dashboard
11. Klik Bell icon
12. Klik judul item sasaran baris itu (bukan tombol)
13. Verifikasi browser berpindah ke path tujuan baris itu
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 2 sampai 8 diulang untuk lima baris tabel TC-FA-NOTIF-85 dan langkah 10 sampai 16 untuk lima baris tabel TC-FA-NOTIF-86 (72 langkah setelah ekspansi). Nomor langkah pada rujukan di atas memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang 35 langkah (bila ekspansi dihitung): semua blok satu kelas (navigasi Klik -> Path) dan tiap iterasi berdiri sendiri; kegagalan satu event tidak membuat event lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 dan 9 (pemulihan seed dan penyiapan notifikasi kelompok event); langkah 6 dan 14 (kembali ke daftar, sesuai langkah TC "lalu kembali ke daftar"); langkah 2 dan 10 (muat ulang di awal tiap iterasi agar Dropdown Panel iterasi sebelumnya tertutup dan klik Bell icon berikutnya tidak menutup panel kembali); langkah 3 dan 11 (membuka Dropdown Panel di awal iterasi).
- Tier menentukan kontrol yang diklik (TC "sesuai tier"): item actionable memakai `[Detail]` (pre-check lalu navigasi), item view-only memakai judul item; tier tiap event diambil dari katalog PRD §5.1. Status Unread pada langkah 8 dan 16 diasumsikan dari penyiapan langkah 1 dan 9 karena notifikasi baru selalu Unread.
- Topik Klik Path dipisah per modul tujuan (023 Approvals dan detail transaksi, 024 My Asset, 025 Assignment, Transfer, dan Disposal, 026 Asset Detail, Audit, dan Profil, 110 almost timeout dan auto canceled) walau berbagi seed dan transaksi Pre-setup #19 sampai #24, karena tiap spec butuh penyiapan fixture pemicu event dan halaman tujuan berbeda dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-85 dan 86 tidak menyebut Title dan Body item per event, dan TC-FA-NOTIF-86 tidak menyebut varian Approved atau Rejected; spec mengidentifikasi item lewat ID transaksi pada Body dan tidak mengasersi Title per event.
  - TC-FA-NOTIF-85 dan 86 tidak menyebut cara memastikan lima item tampil pada Dropdown Panel yang hanya memuat lima notifikasi terbaru; spec mengandalkan fixture BE pemicu event menjadikan lima notifikasi itu yang terbaru.
  - Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
