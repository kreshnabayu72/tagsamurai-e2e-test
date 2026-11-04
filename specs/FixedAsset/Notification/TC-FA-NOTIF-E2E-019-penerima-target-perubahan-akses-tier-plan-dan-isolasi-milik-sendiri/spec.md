---
id: TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri
title: "Penerima Notifikasi: Target Perubahan Akses, Tier Plan, dan Isolasi Notifikasi Milik Sendiri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-71
  - TC-FA-NOTIF-72
  - TC-FA-NOTIF-73
  - TC-FA-NOTIF-322
coverage:
  web: automated
---

# Penerima Notifikasi: Target Perubahan Akses, Tier Plan, dan Isolasi Notifikasi Milik Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Admin Alpha (Pre-setup #1, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun lain yang dipakai langkah:

  | Dipakai oleh | Peran | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-71 dan TC-FA-NOTIF-322 | Target perubahan akses Citra Lestari | #14 | `targetCitra_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TARGETCITRA_PASSWORD` | `Fixture.fixedAssetNotification.targetCitra` |
  | TC-FA-NOTIF-73 | Staff (Transaction Role Disposal, Gedung A) | #9 | `staffDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STAFFDSP_PASSWORD` | `Fixture.fixedAssetNotification.staffDisposal` |

- Tabel "Client per plan" untuk TC-FA-NOTIF-72 (Pre-setup #25; urutan baris = urutan iterasi). Email Borrower `borrower{Plan}_automated_{namaCompany}@qwertysystem.net` dan Asset Admin `assetAdmin{Plan}_automated_{namaCompany}@qwertysystem.net`; Asset Admin hanya dipakai lewat sesi API aktor:

  | Plan | Env var password Borrower | Env var password Asset Admin | Fixture |
  |---|---|---|---|
  | Starter | `Spectra.env.FA_NOTIFPLAN_BORROWER_STARTER_PASSWORD` | `Spectra.env.FA_NOTIFPLAN_ASSETADMIN_STARTER_PASSWORD` | `Fixture.fixedAssetNotification.planStarter` |
  | Growth | `Spectra.env.FA_NOTIFPLAN_BORROWER_GROWTH_PASSWORD` | `Spectra.env.FA_NOTIFPLAN_ASSETADMIN_GROWTH_PASSWORD` | `Fixture.fixedAssetNotification.planGrowth` |
  | Professional | `Spectra.env.FA_NOTIFPLAN_BORROWER_PROFESSIONAL_PASSWORD` | `Spectra.env.FA_NOTIFPLAN_ASSETADMIN_PROFESSIONAL_PASSWORD` | `Fixture.fixedAssetNotification.planProfessional` |
  | Enterprise | `Spectra.env.FA_NOTIFPLAN_BORROWER_ENTERPRISE_PASSWORD` | `Spectra.env.FA_NOTIFPLAN_ASSETADMIN_ENTERPRISE_PASSWORD` | `Fixture.fixedAssetNotification.planEnterprise` |

- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk Total Control Admin Alpha: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Admin A 18/06/26 Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Citra Lestari memegang Total Control dan Transaction Role Approver (Borrowing & Assignment) pada Gedung A (Pre-setup #14). Tiap client plan memiliki satu transaksi Borrow Ready for Handover dengan 1 aset (Pre-setup #25).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): sesi API aktor untuk Admin Alpha (pemicu Remove Total Control dan Remove Read Only di Settings > Role & Permission) dan untuk Asset Admin tiap plan (pemicu handover), serta fixture BE yang menyetel Citra Lestari memegang peran Read Only sebelum TC-FA-NOTIF-322 (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`), serta kemampuan baca BE untuk jumlah item notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca yang sama, bagian 8b butir 10; disediakan tim FE/BE, tanpa endpoint karangan).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #16 sampai #25) dijalankan di hook `before` dan `after`; pemulihan juga dijalankan sebagai langkah penghubung sebelum TC-FA-NOTIF-322 (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Akses Citra Lestari dan transaksi Borrow tiap client plan dikembalikan ke Pre-setup oleh fixture itu.
- Asersi absence atas notifikasi in-app memakai baseline jumlah item (dibaca lewat kemampuan baca BE) dan badge Bell icon Admin Alpha yang dicatat sebelum pemicu, anchor positif (target menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A, butir (i) untuk seed N-05 dan butir (iii) untuk akses Total Control akun #14 dan transaksi client per plan #25): langkah memicu perubahan akses Citra Lestari (Pre-setup #14), handover transaksi Borrow tiap client plan (Pre-setup #25), dan membaca seed N-05 milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD`, `FA_TARGETCITRA_PASSWORD`, `FA_STAFFDSP_PASSWORD`, dan delapan env var `FA_NOTIFPLAN_*` di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-71: Target perubahan akses menerima notifikasi dan aktor tidak menerima

1. Klik Bell icon sebagai Admin Alpha
2. Catat nilai badge Bell icon Admin Alpha dan, lewat fixture BE, jumlah item `Your Total Control access was removed` milik Admin Alpha (baseline)
3. Dari akun Admin Alpha (Pre-setup #1, sesi API), Remove Total Control Citra Lestari di Tab Total Control hingga perubahan akses tersimpan
4. Logout, lalu login sebagai Citra Lestari (Pre-setup #14), lalu buka Fixed Asset > Dashboard
5. Klik Bell icon
6. Verifikasi item `Your Total Control access was removed` tampil pada Dropdown Panel Citra Lestari (anchor positif)
7. Logout, lalu login sebagai Admin Alpha (Pre-setup #1), lalu buka Fixed Asset > Dashboard
8. Klik Bell icon
9. Tunggu 5 detik tanpa memuat ulang halaman
10. Verifikasi item `Waiting for your approval` BRW-2026-0341 (2 Assets) (seed N-01) tampil pada Dropdown Panel Admin Alpha (item pembanding pada surface yang sama)
11. Verifikasi badge Bell icon Admin Alpha sama dengan baseline langkah 2
12. Verifikasi (kemampuan baca BE) Admin Alpha tidak menerima item baru `Your Total Control access was removed`: jumlah item itu milik Admin Alpha sama dengan baseline langkah 2 (seed N-05 tidak dihitung sebagai item baru)

### TC-FA-NOTIF-72: Penerimaan notifikasi identik pada setiap tier plan langganan

13. Untuk setiap baris tabel "Client per plan" (langkah 13 sampai 19): dari akun Asset Admin plan baris itu (sesi API), selesaikan handover transaksi Borrow Ready for Handover hingga notifikasi `borrow_handover_completed` tersimpan
14. Logout, lalu login sebagai Borrower plan baris itu dengan env var password baris itu, lalu buka Fixed Asset > Dashboard
15. Klik Bell icon
16. Verifikasi item `Asset handover completed` tampil pada Dropdown Panel Borrower
17. Verifikasi tidak ada penghalang (gating) maupun ajakan upgrade (upsell) pada Dropdown Panel Borrower
18. Klik `[Mark as Read]` pada item `Asset handover completed`
19. Verifikasi item `Asset handover completed` menjadi Read

### TC-FA-NOTIF-73: User hanya melihat notifikasi miliknya sendiri

20. Logout, lalu login sebagai Total Control Admin Alpha (Pre-setup #1), lalu buka Fixed Asset > Dashboard
21. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
22. Scroll sampai akhir list hingga seluruh item termuat, lalu catat Title seluruh item Notification Center Admin Alpha
23. Logout, lalu login sebagai Staff (Pre-setup #9), lalu buka Fixed Asset > Dashboard
24. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
25. Scroll sampai akhir list hingga seluruh item termuat, lalu catat Title seluruh item Notification Center Staff
26. Verifikasi daftar Title item Admin Alpha (langkah 22) dan daftar Title item Staff (langkah 25) masing-masing memuat sedikitnya satu item (anchor positif; Staff memiliki item seed pembanding Pre-setup #17)
27. Verifikasi daftar Title item Staff berbeda dari daftar Title item Admin Alpha pada langkah 22
28. Verifikasi daftar item Admin Alpha dan daftar item Staff tidak memuat item milik akun lain

### TC-FA-NOTIF-322: Aktor perubahan akses tidak menerima notifikasi access_*

29. Pulihkan seed dan transaksi (Pre-setup #16 sampai #25) lewat fixture BE, lalu setel Citra Lestari memegang peran Read Only lewat fixture BE
30. Logout, lalu login sebagai Admin Alpha (Pre-setup #1), lalu buka Fixed Asset > Dashboard
31. Klik Bell icon
32. Catat, lewat fixture BE, jumlah item `Your Read Only access was removed` milik Admin Alpha (baseline)
33. Dari akun Admin Alpha (Pre-setup #1, sesi API), Remove Read Only Citra Lestari di Tab Read Only hingga perubahan akses tersimpan
34. Logout, lalu login sebagai Citra Lestari (Pre-setup #14), lalu buka Fixed Asset > Dashboard
35. Klik Bell icon
36. Verifikasi item `Your Read Only access was removed` tampil pada Dropdown Panel Citra Lestari (anchor positif)
37. Logout, lalu login sebagai Admin Alpha (Pre-setup #1), lalu buka Fixed Asset > Dashboard
38. Klik Bell icon
39. Tunggu 5 detik tanpa memuat ulang halaman
40. Verifikasi item `Waiting for your approval` BRW-2026-0341 (2 Assets) (seed N-01) tampil pada Dropdown Panel Admin Alpha (item pembanding pada surface yang sama)
41. Verifikasi (kemampuan baca BE) Admin Alpha tidak menerima item `Your Read Only access was removed`: jumlah item itu milik Admin Alpha sama dengan baseline langkah 32

## Notes

- Pengulangan (bagian 8b butir 7): langkah 13 sampai 19 diulang untuk tiap baris tabel "Client per plan" (empat baris, 28 langkah setelah ekspansi).
- Langkah penghubung (S-03): langkah 1, 8, 31, dan 38 (membuka Dropdown Panel Admin Alpha); langkah 21 dan 24 (membuka Notification Center); langkah 2 dan 32 (baseline, S-12); langkah 4, 7, 14, 20, 23, 30, 34, dan 37 (ganti akun dan buka Fixed Asset > Dashboard); langkah 9 dan 39 (jendela 5 detik, bagian 6 konvensi); langkah 22 dan 25 (memuat seluruh item dan mencatat Title untuk perbandingan, S-14); langkah 26 (anchor positif: kedua daftar tidak kosong sebelum perbandingan, bagian 8b butir 10 akhir); langkah 29 (pemulihan dan penyetelan state); langkah 3, 13, dan 33 (pemicu lewat sesi API aktor hingga tersimpan).
- Alasan melewati ambang 35 langkah: semua blok satu kelas (penerima notifikasi per akun) dan tiap TC berdiri sendiri pada state yang dipulihkan; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Baseline Admin Alpha: Admin Alpha (Pre-setup #1) pada TC-FA-NOTIF-71 dan 322 memiliki seed N-05 `Your Total Control access was removed`, sehingga asersi absence Admin Alpha memakai selisih jumlah item terhadap baseline (langkah 2 dan 32), bukan ketiadaan judul; baseline dan pembacaan sesudah pemicu sama-sama lewat kemampuan baca BE, bukan hitungan item Dropdown Panel (maksimal 5 item, bagian 8b butir 10).
- Asersi tambahan (S-03): langkah 10 dan 40 (seed N-01 sebagai item pembanding pada Dropdown Panel Admin Alpha sebelum asersi absence, bagian 8b butir 2 dan 11); langkah 11 (badge Admin Alpha sama dengan baseline langkah 2); langkah 17 mengasersi "tanpa gating atau upsell" dengan anchor langkah 16; langkah 28 menulis klausa kedua Expected TC-FA-NOTIF-73 sebagai perbandingan Title dua arah.
- Temuan untuk QA:
  - TC-FA-NOTIF-72 tidak menyebut bentuk UI gating atau upsell; langkah 17 hanya mengasersi tidak ada penghalang dan ajakan upgrade pada Dropdown Panel.
  - TC-FA-NOTIF-73 menulis Staff "punya notifikasi lain", tetapi TC-FA-NOTIF-62 menulis seed N-01 sampai N-07 tersedia untuk Staff (Pre-setup #17) yang sama dengan Total Control; asersi langkah 27 dan 28 hanya bermakna bila seed Staff berbeda dan TC tidak menyebut akun Staff (spec memakai Pre-setup #9). Pre-setup #17 kini menyediakan satu notifikasi seed pembanding untuk Staff (#9) dan Total Control (#1) memiliki N-01 sampai N-07, sehingga kedua daftar tidak kosong (langkah 26) dan perbedaan Title bermakna.
  - TC-FA-NOTIF-322 mensyaratkan Citra Lestari memegang Read Only, sedangkan Pre-setup #14 hanya menulis Total Control dan Transaction Role Approver; spec mengandalkan fixture BE penyetel akses.
  - TC-FA-NOTIF-71 dan 322 menulis aksi Remove sebagai langkah UI di Settings > Role & Permission; spec menjalankannya lewat sesi API Admin Alpha sebagai pemicu (Catatan TC). Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
