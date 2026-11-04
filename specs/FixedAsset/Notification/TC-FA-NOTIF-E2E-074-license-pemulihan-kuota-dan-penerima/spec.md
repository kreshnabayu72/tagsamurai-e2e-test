---
id: TC-FA-NOTIF-E2E-074-license-pemulihan-kuota-dan-penerima
title: "Penerimaan Notifikasi License: Pemulihan Kuota Setelah Top-Up dan Penerima yang Berhak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-445
  - TC-FA-NOTIF-446
coverage:
  web: automated
---
# Penerimaan Notifikasi License: Pemulihan Kuota Setelah Top-Up dan Penerima yang Berhak

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Manage global license | #33 | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` | `Fixture.fixedAssetNotification.manageGlobalLicense` |
  | Total Control (Admin Alpha) | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |
  | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | `Fixture.fixedAssetNotification.readOnly` |

- Login akun aktor pertama (Manage global license, Pre-setup #33) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): client Pre-setup #34 (plan Paid, Total Asset License 500, Used 440, Reserved 0, Remaining 60, tingkat peringatan Normal; Gedung A beralokasi, sekurangnya 60 draf aset siap Submit for Approval dengan approval ON). Used, Reserved, Total, dan penanda tingkat (Normal, Low, Full) diatur lewat fixture BE pada langkah penyiapan; pemulihan di hook `before` dan `after`. Akun Manage global license Pre-setup #33 (dimensi Update, tanpa Total Control). Top-up Asset License +200 (Total 700) tersedia di Admin Console. Penerima pembanding TC-FA-NOTIF-446: Total Control Pre-setup #1, Group Manager Pre-setup #3, Read Only Pre-setup #2.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Submit for Approval draf aset Gedung A pada client Pre-setup #34 milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); fixture BE pengatur Used, Reserved, Total, dan penanda tingkat peringatan kuota Asset License client Pre-setup #34 serta job terjadwal penilaian kuota; kemampuan menjalankan job latar dan menggeser jam server dan jam fixture bersama (butir "Kemampuan menjalankan job latar" di `suite.md`); jam server dan jam browser/perangkat diatur bersama, sesi UI dan sesi API aktor tetap valid selama jam digeser.
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Penerima pembanding TC-FA-NOTIF-446: badge Bell icon Group Manager (Pre-setup #3) dan Read Only (Pre-setup #2) dicatat sebagai baseline sesudah login, sebelum pemicu, dan dibandingkan lewat UI sesudah login berikutnya (sumber baca sama, bagian 8b butir 10); seed notifikasi Pre-setup #17 memuat item pembanding `Asset has been repaired` (Read, view-only) untuk Group Manager #3 dan Read Only #2 (daftar akun pembanding Pre-setup #17 mencakup #2 dan #3).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi dan pemulihan jam server dan jam fixture ke 18/06/26; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_MGL_PASSWORD`, `FA_TC_PASSWORD`, `FA_GM_PASSWORD`, `FA_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-445: Setelah top-up menaikkan Remaining di atas 10%, penurunan berikutnya mengirim license_quota_low lagi

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 10, Remaining 50, tingkat tercatat Low; license_quota_low sudah terkirim dan Read; 1 draf aset di Gedung A siap Submit for Approval dengan approval ON, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
3. Top-up Asset License +200 lewat fixture BE pemicu hingga Total 700 dan Remaining 250 tersimpan
4. Jalankan job terjadwal penilaian kuota lewat fixture BE hingga job selesai
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Klik Bell icon
7. Verifikasi item lama `"Asset license quota is running low"` berstatus Read tampil pada Dropdown Panel (anchor positif)
8. Verifikasi badge Bell icon Manage global license sama dengan baseline langkah 2 (tidak ada notifikasi baru)
9. Tutup Dropdown Panel
10. Atur Used lewat fixture BE sehingga Total 700 dan Remaining 71
11. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
12. Picu penilaian kuota: Submit for Approval 1 draf aset di Gedung A lewat fixture BE pemicu hingga Reserved bertambah 1, Remaining 70, dan notifikasi tersimpan
13. Klik Bell icon
14. Verifikasi badge Bell icon Manage global license bertambah 1 dari baseline langkah 11
15. Verifikasi item baru `"Asset license quota is running low"` Unread tampil pada Dropdown Panel
16. Verifikasi Body item baru `"70 of 700 asset licenses remain available."`
17. Verifikasi item baru berada di posisi teratas Dropdown Panel

### TC-FA-NOTIF-446: Hanya Manage global license (Update) dan Total Control yang menerima license_quota_low

18. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Total 500, Used 440, Reserved 0; 10 draf aset di Gedung A siap Submit for Approval dengan approval ON
19. Ganti akun: logout, lalu login sebagai Total Control (Admin Alpha) (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Dashboard
20. Catat jumlah pada badge Bell icon Total Control sebagai baseline (0 bila badge tidak tampil)
21. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
22. Catat jumlah pada badge Bell icon Group Manager sebagai baseline (0 bila badge tidak tampil)
23. Ganti akun: logout, lalu login sebagai Read Only (Pre-setup #2) dengan `Spectra.env.FA_RO_PASSWORD`, lalu buka Fixed Asset > Dashboard
24. Catat jumlah pada badge Bell icon Read Only sebagai baseline (0 bila badge tidak tampil)
25. Ganti akun: logout, lalu login sebagai Manage global license (Pre-setup #33) dengan `Spectra.env.FA_MGL_PASSWORD`, lalu buka Fixed Asset > Dashboard
26. Catat jumlah pada badge Bell icon Manage global license sebagai baseline (0 bila badge tidak tampil)
27. Bulk Submit for Approval 10 draf aset di Gedung A lewat fixture BE pemicu hingga Reserved 10 dan Remaining 50 tersimpan
28. Klik Bell icon
29. Verifikasi badge Bell icon Manage global license bertambah 1 dari baseline langkah 26
30. Verifikasi item `"Asset license quota is running low"` Unread tampil pada Dropdown Panel Manage global license
31. Ganti akun: logout, lalu login sebagai Total Control (Admin Alpha) (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Dashboard
32. Klik Bell icon
33. Verifikasi badge Bell icon Total Control bertambah 1 dari baseline langkah 20
34. Verifikasi item `"Asset license quota is running low"` Unread tampil pada Dropdown Panel Total Control
35. Ganti akun: logout, lalu login sebagai Group Manager (Gedung A) (Pre-setup #3) dengan `Spectra.env.FA_GM_PASSWORD`, lalu buka Fixed Asset > Dashboard
36. Tunggu 5 detik tanpa memuat ulang halaman
37. Klik Bell icon
38. Verifikasi Dropdown Panel Group Manager tampil
39. Verifikasi Dropdown Panel Group Manager memuat item seed Pre-setup #17 `Asset has been repaired` milik akun itu (item pembanding pada surface yang sama, anchor absence)
40. Verifikasi item `"Asset license quota is running low"` tidak tampil pada Dropdown Panel Group Manager
41. Verifikasi badge Bell icon Group Manager sama dengan baseline langkah 22 (tidak bertambah)
42. Ganti akun: logout, lalu login sebagai Read Only (Pre-setup #2) dengan `Spectra.env.FA_RO_PASSWORD`, lalu buka Fixed Asset > Dashboard
43. Tunggu 5 detik tanpa memuat ulang halaman
44. Klik Bell icon
45. Verifikasi Dropdown Panel Read Only tampil
46. Verifikasi Dropdown Panel Read Only memuat item seed Pre-setup #17 `Asset has been repaired` milik akun itu (item pembanding pada surface yang sama, anchor absence)
47. Verifikasi item `"Asset license quota is running low"` tidak tampil pada Dropdown Panel Read Only
48. Verifikasi badge Bell icon Read Only sama dengan baseline langkah 24 (tidak bertambah)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 10, 18 (penyiapan kondisi data lewat fixture BE); langkah 19, 21, 23, 25, 31, 35, 42 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 11, 20, 26 (pencatatan baseline badge Bell icon (S-12)); langkah 5, 36 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)).
- Bell icon adalah toggle: langkah 9 (Tutup Dropdown Panel) menutup Dropdown Panel blok TC-FA-NOTIF-445 yang masih terbuka sebelum Bell icon diklik lagi (S-03, S-14). Langkah 22 dan 24 adalah baseline badge per penerima (S-12); langkah 43 adalah jendela 5 detik sebelum asersi Read Only (bagian 6).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (48 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-445: job penilaian kuota sebagai pemicu (bukan objek uji); jam job diatur lewat fixture BE sehingga jam server tidak digeser dari 18/06/26.
- Langkah 38 dan 45 (Dropdown Panel tampil) serta Verifikasi posisi teratas pada blok TC-FA-NOTIF-445 adalah asersi tambahan di luar Expected TC (S-03; bagian 8b butir 2).
- Asersi tambahan di luar Expected TC (S-03) pada blok TC-FA-NOTIF-446: langkah 39 dan 46 (item seed Pre-setup #17 milik akun itu sebagai item pembanding pada surface yang sama, anchor absence, bagian 8b butir 2 dan 11) serta langkah 41 dan 48 (badge sama dengan baseline, bagian 8b butir 10).
- Client Pre-setup #34 juga dipakai spec 073 (kuota low dan full); topik pemulihan kuota setelah top-up dan penerima dibedakan karena memakai top-up +200 dan akun penerima pembanding, dengan state kuota diatur ulang fixture BE di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-445 menulis "Klik Bell icon sebagai penerima lalu amati badge" tanpa anchor positif terhubung ke pemicu; spec memakai item lama license_quota_low berstatus Read sebagai anchor.
  - TC-FA-NOTIF-446 menulis Expected (a) "satu notifikasi" per akun penerima tanpa Body; spec mengasersi Title dan selisih badge.
