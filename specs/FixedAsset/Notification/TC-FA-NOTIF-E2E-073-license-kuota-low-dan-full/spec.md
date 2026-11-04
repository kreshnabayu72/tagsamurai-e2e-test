---
id: TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full
title: "Penerimaan Notifikasi License: Kuota Low dan Full serta Kondisi yang Tidak Mengirim Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-441
  - TC-FA-NOTIF-442
  - TC-FA-NOTIF-443
  - TC-FA-NOTIF-444
  - TC-FA-NOTIF-447
coverage:
  web: automated
---
# Penerimaan Notifikasi License: Kuota Low dan Full serta Kondisi yang Tidak Mengirim Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Manage global license | #33 | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` | `Fixture.fixedAssetNotification.manageGlobalLicense` |

- Login akun aktor pertama (Manage global license, Pre-setup #33) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): client Pre-setup #34 (plan Paid, Total Asset License 500, Used 440, Reserved 0, Remaining 60, tingkat peringatan Normal; Gedung A beralokasi, sekurangnya 60 draf aset siap Submit for Approval dengan approval ON). Used, Reserved, Total, dan penanda tingkat (Normal, Low, Full) diatur lewat fixture BE pada langkah penyiapan; pemulihan di hook `before` dan `after`. Akun Manage global license Pre-setup #33 (dimensi Update, tanpa Total Control). Seed notifikasi Pre-setup #17 akun #33 memuat sekurangnya satu item sebagai item pembanding pada Dropdown Panel (anchor absence TC-FA-NOTIF-447).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Bulk Submit for Approval dan Submit for Approval draf aset Gedung A serta pengaturan kuota pada client Pre-setup #34 milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); fixture BE pengatur Used, Reserved, Total, dan penanda tingkat peringatan kuota Asset License client Pre-setup #34; kemampuan baca BE atas Remaining tenant client Pre-setup #34 (langkah 61).
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_MGL_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-441: Notifikasi license_quota_low diterima: Remaining turun ke 10% Total

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 0, Remaining 60, tingkat Normal; 10 draf aset di Gedung A siap Submit for Approval dengan approval ON dan lolos check kuota, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
3. Bulk Submit for Approval 10 draf aset di Gedung A lewat fixture BE pemicu hingga Reserved 10 dan Remaining 50 tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Manage global license bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Asset license quota is running low"` dan Body `"50 of 500 asset licenses remain available."` (dari template `"[Remaining] of [Total] asset licenses remain available."`)
10. Verifikasi icon `time-line` dengan severity `warning` pada item
11. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
12. Klik judul item tersebut (bukan tombol)
13. Verifikasi halaman tujuan `/fams/license` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-442: Notifikasi license_quota_full diterima: Remaining mencapai 0 setelah tingkat Low tercatat

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 490, Reserved 0, Remaining 10, tingkat tercatat Low; license_quota_low sudah terkirim dan Read; 10 draf aset di Gedung A siap Submit for Approval dengan approval ON
16. Muat ulang halaman Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
18. Bulk Submit for Approval 10 draf aset di Gedung A lewat fixture BE pemicu hingga Reserved 10 dan Remaining 0 tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Manage global license bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Asset license quota is full"` dan Body `"No asset license remains available. New asset registrations are blocked until more quota is added."`
25. Verifikasi icon `time-line` dengan severity `warning` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/license` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-443: Remaining turun dari Normal langsung ke 0 hanya mengirim license_quota_full

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 0, Remaining 60, tingkat Normal; 60 draf aset di Gedung A siap Submit for Approval dengan approval ON
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
33. Bulk Submit for Approval 60 draf aset di Gedung A dalam satu perubahan lewat fixture BE pemicu hingga Remaining 0 tersimpan
34. Muat ulang halaman Fixed Asset > Dashboard
35. Klik Bell icon
36. Verifikasi badge Bell icon Manage global license bertambah 1 dari baseline langkah 32
37. Verifikasi item baru `"Asset license quota is full"` tampil di posisi teratas Dropdown Panel
38. Verifikasi item baru `"Asset license quota is full"` memiliki dot Unread
39. Tunggu 5 detik tanpa memuat ulang halaman
40. Verifikasi item baru `"Asset license quota is running low"` tidak tampil pada Dropdown Panel

### TC-FA-NOTIF-444: Perubahan berikutnya yang masih di tingkat Low tidak mengirim ulang license_quota_low

41. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 10, Remaining 50, tingkat tercatat Low; license_quota_low sudah terkirim dan Read; 5 draf aset di Gedung A siap Submit for Approval dengan approval ON
42. Muat ulang halaman Fixed Asset > Dashboard
43. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
44. Submit for Approval 5 draf aset di Gedung A lewat fixture BE pemicu hingga Remaining 45 tersimpan
45. Tunggu 5 detik tanpa memuat ulang halaman
46. Klik Bell icon
47. Verifikasi item lama `"Asset license quota is running low"` tetap Read (tanpa dot Unread) pada Dropdown Panel (anchor positif)
48. Verifikasi item `"Asset license quota is running low"` baru tidak tampil pada Dropdown Panel
49. Verifikasi badge Bell icon Manage global license sama dengan baseline langkah 43 (tidak bertambah)

### TC-FA-NOTIF-447: Kuota grup habis tidak memicu notifikasi kuota tenant

50. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 0, Remaining 60; Gedung A beralokasi 100 dan terpakai 100 (Remaining grup 0); 1 draf aset di Gedung A siap Submit for Approval
51. Muat ulang halaman Fixed Asset > Dashboard
52. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
53. Submit for Approval 1 draf aset di Gedung A lewat fixture BE pemicu hingga penolakan `QUOTA_EXCEEDED` diterima
54. Tunggu 5 detik tanpa memuat ulang halaman
55. Klik Bell icon
56. Verifikasi Dropdown Panel Manage global license tampil
57. Verifikasi Dropdown Panel Manage global license memuat item seed Pre-setup #17 milik akun itu (item pembanding pada surface yang sama, anchor absence)
58. Verifikasi item `"Asset license quota is running low"` baru tidak tampil pada Dropdown Panel
59. Verifikasi item `"Asset license quota is full"` baru tidak tampil pada Dropdown Panel
60. Verifikasi badge Bell icon Manage global license sama dengan baseline langkah 52 (tidak bertambah)
61. Verifikasi Remaining tenant tetap 60 (dibaca lewat kemampuan baca BE)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30, 41, 50 (penyiapan kondisi data lewat fixture BE); langkah 2, 17, 32, 43, 52 (pencatatan baseline badge Bell icon (S-12)); langkah 39, 45, 54 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)); langkah 16, 31, 42 dan 51 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Bell icon adalah toggle: langkah 16, 31, 42, dan 51 (muat ulang halaman sebelum baseline) serta langkah 34 (muat ulang halaman sesudah pemicu) menutup Dropdown Panel yang masih terbuka dari blok sebelumnya sebelum Bell icon diklik lagi; blok TC-FA-NOTIF-444 dan 447 tidak memakai langkah Tutup Dropdown Panel terpisah karena panel sudah tertutup oleh muat ulang halaman sebelum baseline dan Bell icon tidak diklik di antara baseline dan pemicu; langkah penghubung tanpa Verifikasi (S-03, S-14).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (61 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, hingga sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-443: asersi absence item `Asset license quota is running low` didahului anchor positif (item `Asset license quota is full` tampil). Pemicu Bulk Submit for Approval dijalankan oleh pelaku yang disediakan tim FE/BE.
- Blok TC-FA-NOTIF-441: Remaining 50 setelah pemicu adalah tepat 10% Total (kondisi hasil pemicu dari TC, bukan bagian penyiapan); nilainya diasersi pada Body item (langkah 9).
- Asersi tambahan di luar Expected TC (S-03): langkah 56 (Dropdown Panel tampil sebagai anchor permukaan), langkah 57 (item seed pembanding sebagai anchor absence langkah 58 dan 59), dan langkah 60 (badge tidak bertambah, TC-FA-NOTIF-447).
- Event `license_quota_*` dikecualikan dari atomisitas FANOTIF-LOGIC-06a dan 06b (FANOTIF-LOGIC-06e); identitasnya tenant + stempel waktu penurunan tingkat terbaru.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-444 dan 447 tidak punya anchor positif yang terhubung ke pemicu (tidak ada notifikasi sebagai hasil); spec memakai item lama Read (444) dan Dropdown Panel termuat beserta item seed pembanding (447) sebagai anchor permukaan, dan klausa badge di 447 dicatat sebagai asersi tambahan (S-03).
  - TC-FA-NOTIF-441 sampai 443 tidak menyebut akun pelaku Bulk Submit for Approval; pelaku disediakan tim FE/BE (S-13).
  - Body `license_quota_full` pada TC-FA-NOTIF-442 tidak memuat template; spec tidak menulis template.
