---
id: TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder
title: "Notifikasi TAG Reported dan TAG Report Still Open: Report TAG, Unreadable Otomatis, Laporan Ganda, dan Job Pengingat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-459
  - TC-FA-NOTIF-460
  - TC-FA-NOTIF-461
  - TC-FA-NOTIF-462
coverage:
  web: automated
---

# Notifikasi TAG Reported dan TAG Report Still Open: Report TAG, Unreadable Otomatis, Laporan Ganda, dan Job Pengingat

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena penerima berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-459 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |
  | TC-FA-NOTIF-460, 461, 462 | Manage asset & TAG Update Gedung A (Dewi Anggraini) | #35 | `manageAssetTagGedungA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MATAGA_PASSWORD` | `Fixture.fixedAssetNotification.manageAssetTagGedungA` |

- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Dewi Anggraini (Pre-setup #35, `Spectra.env.FA_MATAGA_PASSWORD`) untuk TC-FA-NOTIF-459 dan Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) untuk TC-FA-NOTIF-460 dan 461.
- Data Pre-setup (tetap di environment): Proyektor AST-2024-0150 (Tag `RF-00150`, Available) dan Laptop - 2 AST-2024-0068 (Tag `RF-00068`, pada langkah scan ASG-2026-0121; Pre-setup #20, #24, dan #38). Laporan terbuka pada `RF-00150` dan `RF-00068` diberikan fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); seed dipulihkan fixture BE pemulih (butir "Fixture BE pemulih seed notifikasi dan transaksi") di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu Report TAG dan pilihan `[I can't scan the TAG]` pada langkah scan Assignment lewat sesi API aktor; menjalankan job pengingat laporan terbuka dan menggeser jam fixture melewati batas pengingat (butir "Kemampuan menjalankan job latar" di `suite.md`); membaca jumlah notifikasi per penerima dan per Title serta nilai badge (baseline dan pembacaan sesudah pemicu pada TC-FA-NOTIF-459, 460, dan 462 lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- State global: jam fixture pada blok TC-FA-NOTIF-462 digeser melewati batas pengingat laporan terbuka (sesuai `tag.md` §9.5, angka batas tidak diulang) lalu dipulihkan ke 18/06/26 sesudah job selesai dan di hook `after`.
- Jendela amat notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu Report TAG, langkah scan Assignment (ASG-2026-0121), dan job pengingat pada `RF-00150`, `RF-00068`, AST-2024-0150, dan AST-2024-0068 milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD`, `FA_MATAGA_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-459: tag_report_created dari Report TAG

1. Muat ulang halaman Fixed Asset > Dashboard, lalu catat jumlah item `"TAG reported"` dan nilai badge Bell icon milik Total Control Pre-setup #1 (baseline) lewat fixture BE
2. Dari akun Dewi Anggraini (Pre-setup #35, sesi API), Report TAG pada `RF-00150` dengan Report Type Damaged hingga laporan tersimpan
3. Muat ulang halaman Fixed Asset > Dashboard
4. Klik Bell icon sebagai penerima
5. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Total Control Pre-setup #1 bertambah 1 dari baseline
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item teratas dengan Title `"TAG reported"` dan Body `"RF-00150 (AST-2024-0150) was reported as Damaged."`
10. Verifikasi item teratas memakai icon `time-line` dengan severity `primary`
11. Verifikasi tombol `[Detail]` tampil dan `[Mark as Read]` tidak tampil pada item teratas
12. Klik judul item notifikasi teratas (bukan tombol)
13. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`
14. Klik Bell icon
15. Verifikasi item `"TAG reported"` tetap berstatus Unread (status baca tidak berubah)

### TC-FA-NOTIF-460: tag_report_created dari Report Unreadable otomatis

16. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24 dan #38) lewat fixture BE
17. Catat jumlah item `"TAG reported"` dan nilai badge Bell icon milik Dewi Anggraini (baseline) lewat fixture BE
18. Dari akun Asset Admin (Pre-setup #8, sesi API), pilih `[I can't scan the TAG]` pada langkah scan ASG-2026-0121 (Laptop - 2 AST-2024-0068), pilih Tag `RF-00068`, isi foto aset, lalu lanjutkan langkah hingga laporan Unreadable tersimpan
19. Logout, lalu login sebagai Dewi Anggraini (Pre-setup #35), lalu buka Fixed Asset > Dashboard
20. Klik Bell icon sebagai penerima
21. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Dewi Anggraini bertambah 1 dari baseline
22. Verifikasi item baru berada di posisi teratas Dropdown Panel
23. Verifikasi Title item baru bold
24. Verifikasi dot Unread tampil pada item baru
25. Verifikasi item teratas dengan Title `"TAG reported"` dan Body `"RF-00068 (AST-2024-0068) was reported as Unreadable."`
26. Verifikasi item teratas memakai icon `time-line` dengan severity `primary`
27. Verifikasi tombol `[Detail]` tampil dan `[Mark as Read]` tidak tampil pada item teratas
28. Klik judul item notifikasi teratas (bukan tombol)
29. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`
30. Klik Bell icon
31. Verifikasi item `"TAG reported"` tetap berstatus Unread (status baca tidak berubah)

### TC-FA-NOTIF-461: laporan ganda tidak mengirim tag_report_created

32. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24 dan #38) lewat fixture BE
33. Atur `RF-00068` pada Laptop - 2 (AST-2024-0068) memiliki laporan terbuka Damaged dan satu notifikasi `"TAG reported"` lama berstatus Read untuk Dewi Anggraini lewat fixture BE
34. Muat ulang halaman Fixed Asset > Dashboard
35. Buka Notification Center
36. Scroll sampai akhir list hingga seluruh item termuat, lalu catat jumlah item di Notification Center dan nilai badge Bell icon (baseline)
37. Verifikasi item `"TAG reported"` lama berstatus Read tampil pada Notification Center
38. Dari akun Asset Admin (Pre-setup #8, sesi API), pilih `[I can't scan the TAG]` pada langkah scan ASG-2026-0121 dan pilih Tag `RF-00068`, lalu lanjutkan langkah hingga tersimpan
39. Tunggu 5 detik tanpa memuat ulang halaman
40. Klik Bell icon
41. Verifikasi badge Bell icon sama dengan baseline
42. Tutup Dropdown Panel
43. Buka Notification Center, lalu scroll sampai akhir list hingga seluruh item termuat
44. Verifikasi jumlah item di Notification Center sama dengan baseline (tidak ada notifikasi `"TAG reported"` baru)

### TC-FA-NOTIF-462: tag_report_open_reminder dari job pengingat

45. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24 dan #38) lewat fixture BE
46. Catat jumlah item `"TAG report is still open"` dan nilai badge Bell icon milik Dewi Anggraini (baseline) lewat fixture BE
47. Atur `RF-00150` pada Proyektor (AST-2024-0150) memiliki laporan terbuka Damaged lewat fixture BE
48. Geser jam fixture melewati batas pengingat laporan terbuka
49. Jalankan job pengingat laporan terbuka hingga notifikasi tersimpan
50. Pulihkan jam fixture ke 18/06/26
51. Muat ulang halaman Fixed Asset > Dashboard
52. Klik Bell icon sebagai penerima
53. Verifikasi (kemampuan baca BE) nilai badge Bell icon milik Dewi Anggraini bertambah 1 dari baseline
54. Verifikasi item baru berada di posisi teratas Dropdown Panel
55. Verifikasi Title item baru bold
56. Verifikasi dot Unread tampil pada item baru
57. Verifikasi item teratas dengan Title `"TAG report is still open"` dan Body `"The report on RF-00150 (AST-2024-0150) is still waiting for action."`
58. Verifikasi item teratas memakai icon `time-line` dengan severity `warning`
59. Verifikasi tombol `[Detail]` tampil dan `[Mark as Read]` tidak tampil pada item teratas
60. Klik judul item notifikasi teratas (bukan tombol)
61. Verifikasi halaman berpindah ke `/fams/tag?tab=paired`
62. Klik Bell icon
63. Verifikasi item `"TAG report is still open"` tetap berstatus Unread (status baca tidak berubah)

## Notes

- Langkah penghubung (S-03): langkah 3, 51 (muat ulang agar notifikasi hasil pemicu termuat); langkah 34 (muat ulang agar baseline UI TC-FA-NOTIF-461 diambil dari halaman segar, bukan dari sisa state langkah 32 dan 33); langkah 16, 32, dan 45 (pulihkan seed antar blok); langkah 1, 17, 36, dan 46 (baseline per TC); langkah 33, 47 (precondition TC lewat fixture BE); langkah 14, 30, dan 62 (buka ulang Bell icon sesudah navigasi untuk mengamati status baca); langkah 19 (ganti akun dan buka Fixed Asset > Dashboard); langkah 35 dan 43 (buka Notification Center; langkah 36 dan 43 memuat seluruh item, S-14); langkah 42 (tutup Dropdown Panel); langkah 39 (jendela 5 detik untuk absence in-app, bagian 6); langkah 50 (pulihkan jam sebelum akun penerima dibuka, S-09).
- Asersi tambahan langkah 37 (S-03): notifikasi `"TAG reported"` lama berstatus Read tampil sebagai anchor positif untuk asersi absence langkah 41 dan 44 (bagian 8b butir 2); badge dan jumlah item dibaca dari sumber yang sama pada baseline dan sesudah pemicu (bagian 8b butir 10), bukan dari Dropdown Panel yang hanya memuat 5 item; precondition TC-FA-NOTIF-461 menyebut notifikasi itu sudah ada dan Read.
- Pada TC-FA-NOTIF-459, 460, dan 462 baseline badge dan pembacaan sesudah pemicu sama-sama lewat kemampuan baca BE (langkah 1 dan 5; langkah 17 dan 21; langkah 46 dan 53); pada TC-FA-NOTIF-461 keduanya dibaca dari UI (langkah 36 dan 41).
- Topik Reported dan Reminder dipisah dari spec 085 (Declined dan Canceled) meski sama-sama memakai `RF-00150`: event, Title, dan penerima berbeda, dan tiap blok memulihkan seed lewat fixture BE sehingga tidak ada keadaan yang dibawa antar spec.
- Job pengingat (langkah 49) hanya pemicu keadaan, bukan objek uji.
- Pembagian per TC: TC-FA-NOTIF-459 (langkah 1 sampai 15), TC-FA-NOTIF-460 (langkah 16 sampai 31), TC-FA-NOTIF-461 (langkah 32 sampai 44), TC-FA-NOTIF-462 (langkah 45 sampai 63).
- Spec ini melewati batas 35 langkah (63 langkah). Alasan: seluruh blok satu topik (event Tag `tag_report_created` dan `tag_report_open_reminder`), tiap blok berdiri sendiri karena diawali pemulihan seed, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected TC-FA-NOTIF-459, 460, dan 462 masing-masing memuat lima butir asersi tampilan.
- Temuan untuk QA:
  - TC-FA-NOTIF-460 dan 461 menulis pelaku pemicu Asset Admin pada langkah scan Assignment; spec memakai sesi API Asset Admin (Pre-setup #8) dan fixture BE pemicu pilihan `[I can't scan the TAG]`.
  - Expected butir e TC-FA-NOTIF-459, 460, dan 462 ("tanpa mengubah status baca") tidak menyebut langkah observasi status baca; spec membuka ulang Bell icon sesudah navigasi.
  - TC-FA-NOTIF-461 langkah 1 "Catat jumlah item di Notification Center" tidak menyebut cara membuka Notification Center; spec memakai langkah "Buka Notification Center".
  - TC-FA-NOTIF-462 tidak menyebut angka batas pengingat laporan terbuka (merujuk `tag.md` §9.5); spec menggeser jam melewati batas tanpa angka.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
