---
id: TC-FA-NOTIF-E2E-026-klik-path-asset-audit-dan-profil
title: "Klik Path: Asset Detail, Task Audit, dan Halaman Profil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-96
  - TC-FA-NOTIF-97
  - TC-FA-NOTIF-98
coverage:
  web: automated
---

# Klik Path: Asset Detail, Task Audit, dan Halaman Profil

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Event TC-FA-NOTIF-96" (urutan baris = urutan iterasi; item view-only diklik pada judul item bukan tombol, item actionable lewat `[Detail]`):

  | Event | Title | Tier | Aset | Path tujuan |
  |---|---|---|---|---|
  | `damaged_repaired` | `Asset has been repaired` | view-only | AST-2024-0141 | `/fams/asset/detail/AST-2024-0141` |
  | `damaged_reminder` | `Damaged asset is still unresolved` | actionable | AST-2024-0141 | `/fams/asset/detail/AST-2024-0141` |
  | `missing_found` | `Asset has been found` | view-only | AST-2024-0067 | `/fams/asset/detail/AST-2024-0067` |
  | `missing_reminder` | `Missing asset is still under investigation` | actionable | AST-2024-0067 | `/fams/asset/detail/AST-2024-0067` |

- Tabel "Event TC-FA-NOTIF-97" (task audit TASK-Q3-A; `audit_task_overdue` memakai varian Auditor):

  | Event | Title | Tier | Path tujuan |
  |---|---|---|---|
  | `audit_task_started` | `New audit task started` | actionable | `/fams/audit/task/TASK-Q3-A` |
  | `audit_task_grace_period` | `Audit task entering grace period` | actionable | `/fams/audit/task/TASK-Q3-A` |
  | `audit_task_overdue` (Auditor) | `Audit task is overdue` | view-only | `/fams/audit/task/TASK-Q3-A` |

- Tabel "Event TC-FA-NOTIF-98" (semua view-only, diklik pada judul item bukan tombol; `[Group Name]` mengikuti fixture):

  | Event | Title | Path tujuan |
  |---|---|---|
  | `access_total_control_removed` | `Your Total Control access was removed` | `/fams/profile` |
  | `access_read_only_removed` | `Your Read Only access was removed` | `/fams/profile` |
  | `access_group_manager_removed` | `You are no longer Group Manager for [Group Name]` | `/fams/profile` |
  | `access_total_control_auto_reverted` | `Your Total Control access was removed` | `/fams/profile` |
  | `access_read_only_auto_reverted` | `Your Read Only access was removed` | `/fams/profile` |
  | `access_group_manager_auto_reverted` | `You are no longer Group Manager for [Group Name]` | `/fams/profile` |

- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 dan Laptop - 1 AST-2024-0067 (Pre-setup #24), task audit TASK-Q3-A (#23). Total Control memegang kapabilitas yang diperlukan untuk membuka halaman tujuan.
- Fixture BE pemicu event (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan, di awal tiap iterasi, hanya notifikasi event baris itu berstatus Unread sebagai notifikasi terbaru akun aktor, sehingga menjadi item teratas Dropdown Panel; transaksi, tiket, task, dan aset sumbernya masih menunggu tindakan untuk event actionable. Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta di awal tiap iterasi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi, aset, dan task Pre-setup #19 sampai #24 menjadi sasaran pemicu event oleh fixture BE dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-96: Navigasi Klik -> Path Asset Detail terkait

1. Untuk setiap baris tabel "Event TC-FA-NOTIF-96" (langkah 1 sampai 7): pulihkan seed lewat fixture BE pemulih, siapkan hanya notifikasi baris itu berstatus Unread sebagai notifikasi terbaru lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
2. Klik Bell icon
3. Klik `[Detail]` (tier actionable) atau judul item (tier view-only) pada item teratas Dropdown Panel
4. Verifikasi browser berpindah ke path tujuan baris itu
5. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
6. Klik Bell icon
7. Verifikasi item teratas Dropdown Panel tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-97: Navigasi Klik -> Path Audit Task Detail terkait

8. Untuk setiap baris tabel "Event TC-FA-NOTIF-97" (langkah 8 sampai 14): pulihkan seed lewat fixture BE pemulih, siapkan hanya notifikasi baris itu berstatus Unread sebagai notifikasi terbaru lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
9. Klik Bell icon
10. Klik `[Detail]` (tier actionable) atau judul item (tier view-only) pada item teratas Dropdown Panel
11. Verifikasi browser berpindah ke path tujuan baris itu
12. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
13. Klik Bell icon
14. Verifikasi item teratas Dropdown Panel tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-98: Navigasi Klik -> Path halaman profil user sendiri

15. Untuk setiap baris tabel "Event TC-FA-NOTIF-98" (langkah 15 sampai 21): pulihkan seed lewat fixture BE pemulih, siapkan hanya notifikasi baris itu berstatus Unread sebagai notifikasi terbaru lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
16. Klik Bell icon
17. Klik judul item teratas Dropdown Panel (bukan tombol)
18. Verifikasi browser berpindah ke path tujuan baris itu
19. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
20. Klik Bell icon
21. Verifikasi item teratas Dropdown Panel tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 7 diulang untuk empat baris tabel TC-FA-NOTIF-96, langkah 8 sampai 14 untuk tiga baris tabel TC-FA-NOTIF-97, dan langkah 15 sampai 21 untuk enam baris tabel TC-FA-NOTIF-98 (91 langkah setelah ekspansi). Nomor langkah pada rujukan memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang 35 langkah (bila ekspansi dihitung): semua blok satu kelas (navigasi Klik -> Path) dan tiap iterasi berdiri sendiri; kegagalan satu event tidak membuat event lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, 8, dan 15 (pemulihan seed dan penyiapan notifikasi per baris); langkah 5, 12, dan 19 (kembali ke daftar, sesuai langkah TC "lalu kembali ke daftar"); langkah 2, 9, dan 16 (membuka Dropdown Panel).
- Item sasaran adalah item teratas Dropdown Panel karena Title yang sama dimiliki seed Pre-setup #17 (N-03, N-04, N-05, N-07) dan lebih dari satu event (`access_*_removed` dan `access_*_auto_reverted`). Tier menentukan kontrol yang diklik (TC "sesuai tier"); tier tiap event diambil dari katalog PRD §5.1. Status Unread diasumsikan dari penyiapan notifikasi baru.
- Topik Klik Path dipisah per modul tujuan (023 Approvals dan detail transaksi, 024 My Asset, 025 Assignment, Transfer, dan Disposal, 026 Asset Detail, Audit, dan Profil, 110 almost timeout dan auto canceled) walau berbagi seed dan transaksi Pre-setup #19 sampai #24, karena tiap spec butuh penyiapan fixture pemicu event dan halaman tujuan berbeda dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-97 tidak menyebut varian `audit_task_overdue` (Auditor view-only atau Asset Admin / Group Manager actionable); spec memakai varian Auditor.
  - TC-FA-NOTIF-96 sampai 98 tidak menyebut Body item per event dan `[Group Name]` untuk event Group Manager; Title tidak diasersi.
  - Event actionable (`damaged_reminder`, `missing_reminder`, `audit_task_started`, `audit_task_grace_period`) hanya menavigasi bila pre-check berhasil; TC tidak menyebut state tiket atau task, sehingga spec mengandalkan fixture BE (seed N-07 `audit_task_started` berstatus Read karena task Completed).
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
