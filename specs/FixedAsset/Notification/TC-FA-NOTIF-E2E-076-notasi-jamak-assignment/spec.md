---
id: TC-FA-NOTIF-E2E-076-notasi-jamak-assignment
title: "Notasi Jamak Notifikasi Assignment yang Diterima Assignee: Acceptance Required, Handover Completed, dan Acceptance Expired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-291
  - TC-FA-NOTIF-294
  - TC-FA-NOTIF-396
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Assignment yang Diterima Assignee: Acceptance Required, Handover Completed, dan Acceptance Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Assignee Siti Rahmawati (Pre-setup #12, `assigneeSiti_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSIGNEE_PASSWORD`, `Fixture.fixedAssetNotification.assigneeSiti`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): transaksi Assignment ASG-2026-0121 dengan 2 aset (Pre-setup #20 dan #24); keadaan awal per blok (Verified, Waiting for Handover, Waiting for Acceptance lebih dari 48 jam) disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Keadaan awal tiap blok diatur fixture BE penyetel state sumber sesudah pemulihan seed (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu event Assignment (verifikasi semua aset, handover) lewat sesi API aktor; menjalankan job terjadwal auto-cancel transaksi Waiting for Acceptance (`F-ASSIGN-11` langkah 5) (butir "Kemampuan menjalankan job latar" di `suite.md`); membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu verifikasi, handover, dan job auto-cancel `F-ASSIGN-11` pada transaksi ASG-2026-0121 (Pre-setup #20 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSIGNEE_PASSWORD` dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-291: assignment_acceptance_required dengan 2 aset

1. Pulihkan seed lalu atur ASG-2026-0121 dua aset pada keadaan awal sebelum semua aset Verified (precondition TC: Verified, dicapai pemicu langkah 3; lihat Temuan untuk QA) lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah item `"Please accept your asset assignment"` milik Siti Rahmawati (baseline) lewat fixture BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), verifikasi semua aset ASG-2026-0121 hingga status Verified tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) jumlah item `"Please accept your asset assignment"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
7. Verifikasi Title item teratas `"Please accept your asset assignment"`
8. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-294: assignment_handover_completed dengan 2 aset

9. Pulihkan seed lalu atur ASG-2026-0121 dua aset Waiting for Handover lewat fixture BE penyetel state sumber
10. Catat jumlah item `"Asset handover completed"` milik Siti Rahmawati (baseline) lewat fixture BE
11. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover ASG-2026-0121 (2 aset) hingga status Assigned tersimpan
12. Muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon sebagai penerima
14. Verifikasi (kemampuan baca BE) jumlah item `"Asset handover completed"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
15. Verifikasi Title item teratas `"Asset handover completed"`
16. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets) is now officially your responsibility."` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-396: assignment_acceptance_expired varian Assignee dengan 2 aset

17. Pulihkan seed lalu atur ASG-2026-0121 dua aset Waiting for Acceptance lebih dari 48 jam lewat fixture BE penyetel state sumber
18. Catat jumlah item `"Assignment acceptance expired"` milik Siti Rahmawati (baseline) lewat fixture BE
19. Jalankan job terjadwal auto-cancel transaksi Waiting for Acceptance yang melewati batas 48 jam untuk ASG-2026-0121 (`F-ASSIGN-11` langkah 5) hingga notifikasi tersimpan
20. Muat ulang halaman Fixed Asset > Dashboard
21. Klik Bell icon sebagai penerima
22. Verifikasi (kemampuan baca BE) jumlah item `"Assignment acceptance expired"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
23. Verifikasi Title item teratas `"Assignment acceptance expired"`
24. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets) was not accepted in time."` memakai notasi jamak `"[Transaction ID] ([N] Assets) was not accepted in time."`

## Notes

- Langkah penghubung (S-03): langkah 1 juga memuat muat ulang halaman sebelum baseline blok pertama (bagian 8b butir 10); langkah 4, 12, dan 20 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 9, dan 17 (pulihkan seed dan atur precondition TC lewat fixture BE penyetel state sumber); langkah 2, 10, dan 18 (baseline per TC, bagian 8b butir 10).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Bell icon dan Dropdown Panel (Catatan TC). Job auto-cancel (langkah 19) hanya pemicu keadaan; batas waktunya diuji di spec 121.
- Pembagian TC lintas spec: blok Assignee (TC-FA-NOTIF-291, 294, 396) ada di spec ini; TC-FA-NOTIF-292, 293, dan 397 (penerima Asset Admin dan Group Manager) ada di spec 118.
- Pembagian per TC: TC-FA-NOTIF-291 (langkah 1 sampai 8), TC-FA-NOTIF-294 (langkah 9 sampai 16), TC-FA-NOTIF-396 (langkah 17 sampai 24).
- Temuan untuk QA:
  - TC-FA-NOTIF-291 menulis precondition "Verified" dan pemicu "semua aset ASG-2026-0121 Verified" tanpa akun pelaku; spec memakai sesi API Asset Admin (Pre-setup #8), sama seperti TC-FA-NOTIF-294.
  - TC-FA-NOTIF-291 memuat konflik precondition dan pemicu: Precondition c menyatakan ASG-2026-0121 dua aset sudah Verified, sedangkan Langkah 1 memicu "semua aset ASG-2026-0121 Verified" (kondisi itu sudah terpenuhi sebelum pemicu, sehingga tidak ada transisi yang menghasilkan notifikasi). Spec mengatur keadaan awal sebelum semua aset Verified (langkah 1) agar pemicu verifikasi (langkah 3) benar-benar menghasilkan transisi; precondition TC perlu dikoreksi pemilik TC (mis. aset belum Verified atau Verified sebagian).
  - TC-FA-NOTIF-396 tidak menyebut cara membuat transaksi melewati batas 48 jam; spec mengandalkan fixture BE pemulih seed menyiapkan keadaan itu.
  - Kolom Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
