---
id: TC-FA-NOTIF-E2E-025-klik-path-assignment-transfer-disposal
title: "Klik Path: Detail Transaksi Assignment, Transfer, dan Disposal Reported"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-90
  - TC-FA-NOTIF-92
  - TC-FA-NOTIF-93
coverage:
  web: automated
---

# Klik Path: Detail Transaksi Assignment, Transfer, dan Disposal Reported

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Event TC-FA-NOTIF-90" (urutan baris = urutan iterasi; item view-only diklik pada judul item bukan tombol, item actionable lewat `[Detail]`):

  | Event | Title | Tier | Item sasaran | Path tujuan |
  |---|---|---|---|---|
  | `assignment_declined` | `Assignment was declined` | view-only | ASG-2026-0120 | `/fams/transactions-assignment/ASG-2026-0120` |
  | `assignment_accepted` | `Assignment was accepted` | actionable | ASG-2026-0120 | `/fams/transactions-assignment/ASG-2026-0120` |
  | `assignment_acceptance_expired` (PIC admin) | `Assignment acceptance expired` | view-only | ASG-2026-0120 | `/fams/transactions-assignment/ASG-2026-0120` |

- Event TC-FA-NOTIF-92 (transaksi masih menunggu tindakan; ditulis eksplisit karena hanya `transfer_departed` yang membuka tab Incoming): `transfer_departed` (Title `Asset incoming transfer ready for arrival`, actionable, `[Detail]`) dan `transfer_transit_overdue` (Title `Your transfer is overdue`, view-only, judul item), Item sasaran TRF-2026-0055, path tujuan `/fams/transactions-transfer/TRF-2026-0055`.
- Event TC-FA-NOTIF-93: `disposal_reported` (Title `Asset reported for disposal`, view-only, judul item), Item sasaran aset Kendaraan Operasional AST-2024-0088, path tujuan `/fams/transactions-disposal?tab=reported&highlight=AST-2024-0088`.
- Data Pre-setup (tetap di environment): Assignment ASG-2026-0120 (Pre-setup #20), Transfer TRF-2026-0055 (#21), Disposal DSP-2026-0030 dan aset Kendaraan Operasional AST-2024-0088 In Use (#22), aset (#24). Total Control memegang kapabilitas yang diperlukan untuk membuka halaman tujuan.
- Fixture BE pemicu event (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan notifikasi berstatus Unread sebagai notifikasi terbaru akun aktor sehingga item sasaran tampil pada Dropdown Panel (maksimum lima item). Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi, aset, dan task Pre-setup #19 sampai #24 menjadi sasaran pemicu event oleh fixture BE dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-90: Navigasi Klik -> Path detail transaksi Assignment

1. Pulihkan seed lewat fixture BE pemulih, siapkan tiga notifikasi event TC-FA-NOTIF-90 berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
2. Untuk setiap baris tabel "Event TC-FA-NOTIF-90" (langkah 2 sampai 8): muat ulang halaman Fixed Asset > Dashboard
3. Klik Bell icon
4. Klik `[Detail]` (tier actionable) atau judul item (tier view-only) pada item sasaran baris itu
5. Verifikasi browser berpindah ke path tujuan baris itu
6. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
7. Klik Bell icon
8. Verifikasi item sasaran baris itu tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-92: Navigasi Klik -> Path detail transaksi Transfer

9. Pulihkan seed lewat fixture BE pemulih, siapkan notifikasi `transfer_departed` dan `transfer_transit_overdue` berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
10. Klik Bell icon
11. Klik `[Detail]` pada item `Asset incoming transfer ready for arrival` untuk TRF-2026-0055
12. Verifikasi browser berpindah ke `/fams/transactions-transfer/TRF-2026-0055`
13. Verifikasi tab Incoming aktif
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item `Asset incoming transfer ready for arrival` tetap Unread (status baca tidak berubah oleh klik)
17. Klik judul item `Your transfer is overdue` untuk TRF-2026-0055 (bukan tombol)
18. Verifikasi browser berpindah ke `/fams/transactions-transfer/TRF-2026-0055`
19. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
20. Klik Bell icon
21. Verifikasi item `Your transfer is overdue` tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-93: Navigasi Klik -> Path Disposal tab Reported

22. Pulihkan seed lewat fixture BE pemulih, siapkan notifikasi `disposal_reported` berstatus Unread lewat fixture BE pemicu event, lalu muat ulang halaman Fixed Asset > Dashboard
23. Klik Bell icon
24. Klik judul item `Asset reported for disposal` untuk AST-2024-0088 (bukan tombol)
25. Verifikasi browser berpindah ke halaman Disposal tab Reported, path `/fams/transactions-disposal?tab=reported&highlight=AST-2024-0088`
26. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
27. Klik Bell icon
28. Verifikasi item `Asset reported for disposal` tetap Unread (status baca tidak berubah oleh klik ini)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 2 sampai 8 diulang untuk tiga baris tabel TC-FA-NOTIF-90 (42 langkah setelah ekspansi). Nomor langkah pada rujukan memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang 35 langkah (bila ekspansi dihitung): semua blok satu kelas (navigasi Klik -> Path) dan tiap iterasi berdiri sendiri; kegagalan satu event tidak membuat event lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, 9, dan 22 (pemulihan seed dan penyiapan notifikasi); langkah 6, 14, 19, dan 26 (kembali ke daftar, sesuai langkah TC "lalu kembali ke daftar"); langkah 2 (muat ulang di awal tiap iterasi agar Dropdown Panel iterasi sebelumnya tertutup dan klik Bell icon berikutnya tidak menutup panel kembali); langkah 3, 10, 15, 20, dan 23 (membuka Dropdown Panel).
- Tier menentukan kontrol yang diklik (TC "sesuai tier"); tier tiap event diambil dari katalog PRD §5.1. Status Unread diasumsikan dari penyiapan notifikasi baru.
- Topik Klik Path dipisah per modul tujuan (023 Approvals dan detail transaksi, 024 My Asset, 025 Assignment, Transfer, dan Disposal, 026 Asset Detail, Audit, dan Profil, 110 almost timeout dan auto canceled) walau berbagi seed dan transaksi Pre-setup #19 sampai #24, karena tiap spec butuh penyiapan fixture pemicu event dan halaman tujuan berbeda dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-90, 92, dan 93 tidak menyebut Body item per event; spec mengidentifikasi item lewat Title katalog PRD §5.1 dan ID transaksi atau aset.
  - Copy `assignment_accepted`, `assignment_acceptance_expired`, `transfer_departed`, dan `disposal_reported` menunggu persetujuan PM (Open Item #2 PRD); Title pada langkah memakai teks PRD saat ini.
  - Penerima `transfer_departed` dan `transfer_transit_overdue` belum diputuskan produk (Open Item #3 PRD); spec mengikuti TC dengan fixture BE yang menyiapkan item untuk akun aktor.
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
