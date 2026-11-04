---
id: TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event
title: "Dedup Multi-Role: Satu Notifikasi per Event untuk Pengguna dengan Beberapa Peran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-162
  - TC-FA-NOTIF-163
  - TC-FA-NOTIF-164
  - TC-FA-NOTIF-165
  - TC-FA-NOTIF-166
  - TC-FA-NOTIF-167
  - TC-FA-NOTIF-168
coverage:
  web: automated
---

# Dedup Multi-Role: Satu Notifikasi per Event untuk Pengguna dengan Beberapa Peran

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena tiap TC memakai kombinasi peran yang berbeda pada satu akun dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-162, 163, 164, 165, 168 (Asset Admin dengan peran tambahan Borrower BRW-2026-0342, Assignee ASG-2026-0120, Auditor Task Audit Q3-Gedung A, atau Approver Disposal Gedung A sesuai TC) | Asset Admin (PIC admin) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | TC-FA-NOTIF-166 (Approver Transfer yang juga Requester TRF-2026-0055) | Approver (Transfer) | #5 | `approverTransfer_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERTRF_PASSWORD` | `Fixture.fixedAssetNotification.approverTransfer` |
  | TC-FA-NOTIF-167 (Total Control yang juga Group Manager dan Asset Admin Gedung A) | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |
  | TC-FA-NOTIF-167 (hanya aktor sesi API pemicu Accept ASG-2026-0120, tanpa login UI) | Assignee Siti Rahmawati | #12 | `assigneeSiti_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSIGNEE_PASSWORD` | `Fixture.fixedAssetNotification.assigneeSiti` |

- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah item notifikasi per penerima dan per Title/aset; baseline dan pembacaan sesudah pemicu memakai kemampuan baca yang sama, bukan hitungan item Dropdown Panel (bagian 8b butir 10).
- Peran tambahan per blok (Borrower, Assignee, Auditor, Requester, Group Manager, Approver Disposal) diatur fixture BE penyetel peran dan dipulihkan di hook `after`; TC tidak menyebut akunnya (lihat Temuan untuk QA).
- Login akun aktor pertama (Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu event (Report Disposal, Accept) memakai sesi API aktor lewat fixture BE pemicu event; Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: transaksi Borrow BRW-2026-0342, Assignment ASG-2026-0120, Transfer TRF-2026-0055, aset Kendaraan Operasional AST-2024-0088 (Pre-setup #19 sampai #22 dan #24) dan `Task Audit Q3-Gedung A` (Pre-setup #23). Asersi jumlah notifikasi memakai baseline per penerima yang dicatat tepat sebelum pemicu (bagian 8b butir 10), bukan seed bersih.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job overdue harian, job due soon, job expiry Acceptance, scheduler harian audit, dan job `F-FATX-07`. Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0342, ASG-2026-0120, TRF-2026-0055, AST-2024-0088, Task Audit Q3-Gedung A) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-162: Borrower dan PIC admin pada borrow_overdue menerima satu notifikasi varian actionable

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Your borrowed asset is overdue` untuk aset BRW-2026-0342 milik akun aktor (baseline)
2. Atur jam server dan jam fixture ke setelah Due Date BRW-2026-0342, jalankan job overdue harian hingga notifikasi tersimpan, lalu pulihkan jam
3. Klik Bell icon
4. Verifikasi (kemampuan baca BE) jumlah item `Your borrowed asset is overdue` untuk aset BRW-2026-0342 bertambah tepat 1 dari baseline langkah 1
5. Verifikasi notifikasi itu varian PIC admin/Group Manager dengan tombol `[Detail]`
6. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 1
7. Klik `[Detail]` pada notifikasi itu
8. Verifikasi path tujuan `/fams/borrow?tab=active&highlight=BRW-2026-0342`

### TC-FA-NOTIF-163: Borrower dan PIC admin pada borrow_due_soon (tier sama) memakai varian Borrower

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Your borrowed asset is due soon` untuk aset BRW-2026-0342 milik akun aktor (baseline)
10. Atur jam server dan jam fixture ke ambang due soon BRW-2026-0342, jalankan job due soon hingga notifikasi tersimpan, lalu pulihkan jam
11. Klik Bell icon
12. Verifikasi (kemampuan baca BE) jumlah item `Your borrowed asset is due soon` untuk aset BRW-2026-0342 bertambah tepat 1 dari baseline langkah 9
13. Verifikasi notifikasi itu view-only dengan tombol `[Mark as Read]`
14. Klik area item notifikasi `Your borrowed asset is due soon`
15. Verifikasi navigasi ke `/fams/my-asset/borrowed/BRW-2026-0342` (varian Borrower)

### TC-FA-NOTIF-164: Assignee yang juga PIC admin pada assignment_acceptance_expired memakai varian Assignee

16. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Assignment acceptance expired` untuk ASG-2026-0120 milik akun aktor (baseline)
17. Atur jam server dan jam fixture ke setelah batas 48 jam sejak waktu terbit ASG-2026-0120 (dibaca lewat fixture BE), jalankan job expiry hingga kedaluwarsa tersimpan, lalu pulihkan jam
18. Klik Bell icon
19. Verifikasi (kemampuan baca BE) jumlah item `Assignment acceptance expired` untuk ASG-2026-0120 bertambah tepat 1 dari baseline langkah 16
20. Verifikasi notifikasi itu view-only dengan tombol `[Mark as Read]`
21. Klik area item notifikasi `Assignment acceptance expired`
22. Verifikasi navigasi ke `/fams/my-asset/task/assignment` (varian Assignee)

### TC-FA-NOTIF-165: Auditor yang juga Asset Admin pada audit_task_overdue menerima varian actionable

23. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Audit task is overdue` untuk Task Audit Q3-Gedung A milik akun aktor (baseline)
24. Atur jam server dan jam fixture ke waktu Task Audit Q3-Gedung A memasuki Overdue, jalankan scheduler harian audit hingga tersimpan, lalu pulihkan jam
25. Klik Bell icon
26. Verifikasi (kemampuan baca BE) jumlah item `Audit task is overdue` untuk Task Audit Q3-Gedung A bertambah tepat 1 dari baseline langkah 23
27. Verifikasi notifikasi itu varian Asset Admin / Group Manager dengan tombol `[Detail]`

### TC-FA-NOTIF-168: Pengguna pada sisi maker dan approver Disposal menerima satu disposal_reported

28. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Asset reported for disposal` untuk AST-2024-0088 milik akun aktor (baseline)
29. Lewat sesi API aktor, Report Disposal aset AST-2024-0088 hingga tersimpan
30. Klik Bell icon
31. Verifikasi (kemampuan baca BE) jumlah item `Asset reported for disposal` untuk AST-2024-0088 bertambah tepat 1 dari baseline langkah 28

### TC-FA-NOTIF-166: Requester yang juga Approver pada almost_timeout menerima varian Approver actionable

32. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver (Transfer) yang juga Requester TRF-2026-0055 (Pre-setup #5), buka Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Please finish this approval — expiring soon` untuk TRF-2026-0055 milik akun aktor (baseline)
33. Atur jam server dan jam fixture ke waktu sisa 24 jam TRF-2026-0055 (dibaca lewat fixture BE), jalankan job `F-FATX-07` hingga notifikasi tersimpan, lalu pulihkan jam
34. Klik Bell icon
35. Verifikasi (kemampuan baca BE) jumlah item `Please finish this approval — expiring soon` untuk TRF-2026-0055 bertambah tepat 1 dari baseline langkah 32
36. Verifikasi notifikasi itu varian Approver dengan tombol `[Detail]`

### TC-FA-NOTIF-167: Pemegang beberapa kapabilitas Handover menerima satu assignment_accepted

37. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Total Control yang juga Group Manager dan Asset Admin Gedung A (Pre-setup #1), buka Fixed Asset > Dashboard, lalu catat, lewat fixture BE, jumlah item `Assignment was accepted` untuk ASG-2026-0120 milik akun aktor (baseline)
38. Lewat sesi API Assignee Siti Rahmawati (Pre-setup #12), Accept ASG-2026-0120 hingga tersimpan
39. Klik Bell icon
40. Verifikasi (kemampuan baca BE) jumlah item `Assignment was accepted` untuk ASG-2026-0120 bertambah tepat 1 dari baseline langkah 37

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 2, 9, 10, 16, 17, 23, 24, 28, 29, 32, 33, 37 dan 38. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu. Baseline dicatat sebelum pemicu tiap TC (S-12); langkah `[Detail]` dan klik area item tidak termasuk langkah penghubung (itu aksi yang diasersi path-nya).
- Pembagian per TC: TC-FA-NOTIF-162 (langkah 1 sampai 8), TC-FA-NOTIF-163 (langkah 9 sampai 15), TC-FA-NOTIF-164 (langkah 16 sampai 22), TC-FA-NOTIF-165 (langkah 23 sampai 27), TC-FA-NOTIF-168 (langkah 28 sampai 31), TC-FA-NOTIF-166 (langkah 32 sampai 36), TC-FA-NOTIF-167 (langkah 37 sampai 40).
- Job (overdue, due soon, expiry, scheduler audit, `F-FATX-07`) hanya pemicu keadaan, bukan objek uji; yang diasersi adalah notifikasi yang dihasilkannya.
- Urutan TC di spec: 162, 163, 164, 165, 168 (Asset Admin), 166 (Approver Transfer), lalu 167 (Total Control), dikelompokkan per akun.
- Klausa "Hitung item ... untuk aset itu" (Langkah TC-FA-NOTIF-162) diasersi sebagai selisih jumlah item terhadap baseline sebelum pemicu; baseline dan pembacaan sesudah pemicu sama-sama lewat kemampuan baca BE, bukan hitungan item Dropdown Panel (hanya memuat 5 notifikasi terbaru; bagian 8b butir 10). Item di Dropdown Panel dipakai untuk Verifikasi varian, tombol, dan path tujuan.
- Spec ini 40 langkah (di atas smell sekitar 35 langkah): ketujuh TC satu topik (dedup notifikasi untuk pengguna multi-peran) dengan pola baseline, pemicu, dan asersi jumlah yang sama; tiap blok berdiri sendiri karena seed dipulihkan di antara blok dan baseline dicatat ulang per blok, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-FA-NOTIF-162 sampai 168 menulis kombinasi peran akun ("Asset Admin (juga Borrower BRW-2026-0342)" dan sejenisnya) tanpa nomor Pre-setup, dan tabel Pre-setup TC tidak memuat akun dengan kombinasi peran itu; spec memakai Pre-setup #8, #5, dan #1 sebagai akun dasar dengan peran tambahan lewat fixture BE (disediakan tim FE/BE, mekanisme tidak dikarang).
  - TC-FA-NOTIF-162 dan 163 menulis "Jalankan job overdue harian" dan "Jalankan job due soon" tanpa jam pasti; nilai pastinya ditetapkan tim FE/BE. TC-FA-NOTIF-166 menulis "sisa waktu 24 jam" tanpa menyebut cara mencapainya; spec memakai pengaturan jam lewat fixture BE.
  - TC-FA-NOTIF-162 menulis Expected "path `/fams/borrow?tab=active&highlight=BRW-2026-0342`" sebagai bagian Expected a tanpa menyebut aksi yang menampilkannya; spec membukanya lewat `[Detail]`. TC-FA-NOTIF-165, 166, 167, dan 168 tidak menyebut cara membedakan varian selain tombol; spec mengasersi tombol sesuai Expected TC.
