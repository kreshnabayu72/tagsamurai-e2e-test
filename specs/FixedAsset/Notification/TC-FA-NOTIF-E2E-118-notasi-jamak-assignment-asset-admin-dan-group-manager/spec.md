---
id: TC-FA-NOTIF-E2E-118-notasi-jamak-assignment-asset-admin-dan-group-manager
title: "Notasi Jamak Notifikasi Assignment untuk Asset Admin dan Group Manager: Declined, Acceptance Expired, dan Accepted"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-292
  - TC-FA-NOTIF-397
  - TC-FA-NOTIF-293
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Assignment untuk Asset Admin dan Group Manager: Declined, Acceptance Expired, dan Accepted

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena penerima berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-292, TC-FA-NOTIF-397 | Asset Admin (PIC admin ASG-2026-0121) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | TC-FA-NOTIF-293 | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |

- Login akun aktor pertama (Asset Admin, Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Assignee Siti Rahmawati (Pre-setup #12, `assigneeSiti_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSIGNEE_PASSWORD`, `Fixture.fixedAssetNotification.assigneeSiti`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): transaksi Assignment ASG-2026-0121 dengan 2 aset (Pre-setup #20 dan #24); keadaan awal per blok (Waiting for Acceptance, termasuk lebih dari 48 jam untuk TC-FA-NOTIF-397) disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu event Assignment (Decline dan Accept oleh Assignee) lewat sesi API aktor; menjalankan job terjadwal auto-cancel transaksi Waiting for Acceptance (`F-ASSIGN-11` langkah 5) (butir "Kemampuan menjalankan job latar" di `suite.md`); membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu Decline, Accept, dan job auto-cancel `F-ASSIGN-11` pada transaksi ASG-2026-0121 (Pre-setup #20 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_ASSIGNEE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-292: assignment_declined dengan 2 aset (Asset Admin)

1. Catat jumlah item `"Assignment was declined"` milik Asset Admin (baseline) lewat fixture BE
2. Dari akun Siti Rahmawati (Pre-setup #12, sesi API), Decline ASG-2026-0121 (2 aset) hingga status Declined tersimpan
3. Muat ulang halaman Fixed Asset > Dashboard
4. Klik Bell icon sebagai penerima
5. Verifikasi (kemampuan baca BE) jumlah item `"Assignment was declined"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
6. Verifikasi Title item teratas `"Assignment was declined"`
7. Verifikasi Body item teratas `"Siti Rahmawati declined ASG-2026-0121 (2 Assets)."` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-397: assignment_acceptance_expired varian PIC admin dengan 2 aset (Asset Admin)

8. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
9. Catat jumlah item `"Assignment acceptance expired"` milik Asset Admin (baseline) lewat fixture BE
10. Jalankan job terjadwal auto-cancel transaksi Waiting for Acceptance yang melewati batas 48 jam untuk ASG-2026-0121 (`F-ASSIGN-11` langkah 5) hingga notifikasi tersimpan
11. Muat ulang halaman Fixed Asset > Dashboard
12. Klik Bell icon sebagai penerima
13. Verifikasi (kemampuan baca BE) jumlah item `"Assignment acceptance expired"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
14. Verifikasi Title item teratas `"Assignment acceptance expired"`
15. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets) was not accepted in time."` memakai notasi jamak `"[Transaction ID] ([N] Assets) was not accepted in time."`

### TC-FA-NOTIF-293: assignment_accepted dengan 2 aset (Group Manager)

16. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
17. Catat jumlah item `"Assignment was accepted"` milik Group Manager Gedung A (baseline) lewat fixture BE
18. Dari akun Siti Rahmawati (Pre-setup #12, sesi API), Accept ASG-2026-0121 (2 aset) hingga status Accepted tersimpan
19. Logout, lalu login sebagai Group Manager (Gedung A, Pre-setup #3), lalu buka Fixed Asset > Dashboard
20. Klik Bell icon sebagai penerima
21. Verifikasi (kemampuan baca BE) jumlah item `"Assignment was accepted"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
22. Verifikasi Title item teratas `"Assignment was accepted"`
23. Verifikasi Body item teratas `"Siti Rahmawati accepted ASG-2026-0121 (2 Assets)."` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

## Notes

- Langkah penghubung (S-03): langkah 3 dan 11 (muat ulang agar notifikasi hasil pemicu termuat); langkah 8 dan 16 (pulihkan seed antar blok); langkah 1, 9, dan 17 (baseline per TC, bagian 8b butir 10); langkah 19 (ganti akun dan buka Fixed Asset > Dashboard).
- Urutan blok: TC-FA-NOTIF-292, 397, lalu 293, supaya dua blok Asset Admin berurutan dan ganti akun hanya satu kali.
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Bell icon dan Dropdown Panel (Catatan TC). Job auto-cancel (langkah 10) hanya pemicu keadaan; batas waktunya diuji di spec 121.
- Pembagian TC lintas spec: TC-FA-NOTIF-291, 294, dan 396 (penerima Assignee) ada di spec 076.
- Pembagian per TC: TC-FA-NOTIF-292 (langkah 1 sampai 7), TC-FA-NOTIF-397 (langkah 8 sampai 15), TC-FA-NOTIF-293 (langkah 16 sampai 23).
- Temuan untuk QA:
  - TC-FA-NOTIF-292 dan 293 menulis pemicu "Assignee Decline" dan "Assignee Accept" tanpa menyebut akun; spec memakai sesi API Siti Rahmawati (Pre-setup #12).
  - TC-FA-NOTIF-397 tidak menyebut cara membuat transaksi melewati batas 48 jam; spec mengandalkan fixture BE pemulih seed menyiapkan keadaan itu.
  - TC-FA-NOTIF-293 memakai penerima Group Manager tanpa nomor Pre-setup; spec memakai Pre-setup #3 (Group Manager Gedung A).
  - Kolom Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
