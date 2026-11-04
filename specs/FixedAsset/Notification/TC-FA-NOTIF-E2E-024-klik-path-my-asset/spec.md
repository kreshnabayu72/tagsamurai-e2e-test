---
id: TC-FA-NOTIF-E2E-024-klik-path-my-asset
title: "Klik Path: My Asset Task, Borrowed, Assigned, dan Borrow List Ter-highlight"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-87
  - TC-FA-NOTIF-88
  - TC-FA-NOTIF-89
  - TC-FA-NOTIF-91
coverage:
  web: automated
---

# Klik Path: My Asset Task, Borrowed, Assigned, dan Borrow List Ter-highlight

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Event TC-FA-NOTIF-87" (transaksi masih menunggu tindakan; item actionable, diklik lewat `[Detail]`):

  | Event | Title | Item sasaran | Path tujuan |
  |---|---|---|---|
  | `borrow_confirmation_required` | `Please confirm your borrowed asset` | BRW-2026-0342 | `/fams/my-asset/task/borrow/BRW-2026-0342` |
  | `assignment_acceptance_required` | `Please accept your asset assignment` | ASG-2026-0120 | `/fams/my-asset/task/assignment/ASG-2026-0120` |

- Tabel "Event TC-FA-NOTIF-88" (item view-only, diklik pada judul item bukan tombol):

  | Event | Title | Item sasaran | Path tujuan |
  |---|---|---|---|
  | `borrow_handover_completed` | `Asset handover completed` | BRW-2026-0342 | `/fams/my-asset/borrowed/BRW-2026-0342` |
  | `assignment_handover_completed` | `Asset handover completed` | ASG-2026-0120 | `/fams/my-asset/assigned/ASG-2026-0120` |

- Tabel "Event TC-FA-NOTIF-89" (transaksi masih menunggu tindakan; hanya varian PIC admin / Group Manager `borrow_overdue` yang actionable dan diklik lewat `[Detail]`, tiga baris lain view-only dan diklik pada judul item):

  | Event | Title | Tier | Item sasaran | Path tujuan |
  |---|---|---|---|---|
  | `borrow_due_soon` (Borrower) | `Your borrowed asset is due soon` | view-only | BRW-2026-0342 | `/fams/my-asset/borrowed/BRW-2026-0342` |
  | `borrow_due_soon` (PIC admin) | `Your borrowed asset is due soon` | view-only | BRW-2026-0342 | `/fams/borrow?tab=active&highlight=BRW-2026-0342` |
  | `borrow_overdue` (Borrower) | `Your borrowed asset is overdue` | view-only | BRW-2026-0342 | `/fams/my-asset/borrowed/BRW-2026-0342` |
  | `borrow_overdue` (PIC admin / Group Manager) | `Your borrowed asset is overdue` | actionable | BRW-2026-0342 | `/fams/borrow?tab=active&highlight=BRW-2026-0342` |

- Event TC-FA-NOTIF-91: `assignment_acceptance_expired` varian Assignee, Title `Assignment acceptance expired`, view-only, diklik pada judul item, Item sasaran ASG-2026-0120, path tujuan `/fams/my-asset/task/assignment`.
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (Pre-setup #19), Assignment ASG-2026-0120 (#20), aset (#24). Total Control memegang kapabilitas yang diperlukan untuk membuka halaman tujuan.
- Fixture BE pemicu event (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan notifikasi berstatus Unread sebagai notifikasi terbaru akun aktor sehingga item sasaran tampil pada Dropdown Panel (maksimum lima item); pada TC-FA-NOTIF-89 hanya notifikasi baris iterasi yang disiapkan karena empat baris berbagi ID transaksi. Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi, aset, dan task Pre-setup #19 sampai #24 menjadi sasaran pemicu event oleh fixture BE dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-87: Navigasi Klik -> Path My Asset > Task

1. Pulihkan seed lewat fixture BE pemulih, siapkan notifikasi kedua event TC-FA-NOTIF-87 berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
2. Untuk setiap baris tabel "Event TC-FA-NOTIF-87" (langkah 2 sampai 8): muat ulang halaman Fixed Asset > Dashboard
3. Klik Bell icon
4. Klik `[Detail]` pada item sasaran baris itu
5. Verifikasi browser berpindah ke path tujuan baris itu
6. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
7. Klik Bell icon
8. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-88: Navigasi Klik -> Path My Asset > Borrowed dan Assigned

9. Pulihkan seed lewat fixture BE pemulih, siapkan notifikasi kedua event TC-FA-NOTIF-88 berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
10. Untuk setiap baris tabel "Event TC-FA-NOTIF-88" (langkah 10 sampai 16): muat ulang halaman Fixed Asset > Dashboard
11. Klik Bell icon
12. Klik judul item sasaran baris itu (bukan tombol)
13. Verifikasi browser berpindah ke path tujuan baris itu
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-89: Navigasi Klik -> Path My Asset > Borrowed dan Borrow list ter-highlight

17. Untuk setiap baris tabel "Event TC-FA-NOTIF-89" (langkah 17 sampai 23): pulihkan seed lewat fixture BE pemulih, siapkan hanya notifikasi baris itu berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
18. Klik Bell icon
19. Klik `[Detail]` (tier actionable) atau judul item (tier view-only) pada item sasaran baris itu
20. Verifikasi browser berpindah ke path tujuan baris itu
21. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
22. Klik Bell icon
23. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-91: Navigasi Klik -> Path My Asset > Task > Assignment

24. Pulihkan seed lewat fixture BE pemulih, siapkan notifikasi `assignment_acceptance_expired` varian Assignee berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
25. Klik Bell icon
26. Klik judul item `Assignment acceptance expired` untuk ASG-2026-0120 (bukan tombol)
27. Verifikasi browser berpindah ke halaman My Asset > Task > Assignment, path `/fams/my-asset/task/assignment`
28. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
29. Klik Bell icon
30. Verifikasi item `Assignment acceptance expired` untuk ASG-2026-0120 tetap Unread (status baca tidak berubah oleh klik ini)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 2 sampai 8 diulang untuk dua baris tabel TC-FA-NOTIF-87, langkah 10 sampai 16 untuk dua baris tabel TC-FA-NOTIF-88, dan langkah 17 sampai 23 untuk empat baris tabel TC-FA-NOTIF-89 (65 langkah setelah ekspansi). Nomor langkah pada rujukan memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang 35 langkah (bila ekspansi dihitung): semua blok satu kelas (navigasi Klik -> Path) dan tiap iterasi berdiri sendiri; kegagalan satu event tidak membuat event lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, 9, 17, dan 24 (pemulihan seed dan penyiapan notifikasi); langkah 6, 14, 21, dan 28 (kembali ke daftar, sesuai langkah TC "lalu kembali ke daftar"); langkah 2 dan 10 (muat ulang di awal tiap iterasi agar Dropdown Panel iterasi sebelumnya tertutup dan klik Bell icon berikutnya tidak menutup panel kembali); langkah 3, 11, 18, dan 25 (membuka Dropdown Panel di awal iterasi).
- Tier menentukan kontrol yang diklik (TC "sesuai tier"); tier tiap event diambil dari katalog PRD §5.1. Status Unread pada langkah 8, 16, 23, dan 30 diasumsikan dari penyiapan notifikasi baru.
- Topik Klik Path dipisah per modul tujuan (023 Approvals dan detail transaksi, 024 My Asset, 025 Assignment, Transfer, dan Disposal, 026 Asset Detail, Audit, dan Profil, 110 almost timeout dan auto canceled) walau berbagi seed dan transaksi Pre-setup #19 sampai #24, karena tiap spec butuh penyiapan fixture pemicu event dan halaman tujuan berbeda dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-87 sampai 89 dan 91 tidak menyebut Body item per event; spec mengidentifikasi item lewat Title katalog PRD §5.1 dan ID transaksi.
  - TC-FA-NOTIF-89 tidak menyebut akun penerima varian Borrower dan PIC admin untuk Total Control; spec memakai fixture BE yang menyiapkan tiap varian untuk akun aktor.
  - Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
