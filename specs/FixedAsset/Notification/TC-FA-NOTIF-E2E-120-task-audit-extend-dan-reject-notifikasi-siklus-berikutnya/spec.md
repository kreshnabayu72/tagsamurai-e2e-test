---
id: TC-FA-NOTIF-E2E-120-task-audit-extend-dan-reject-notifikasi-siklus-berikutnya
title: "Task Audit Extend dan Reject: Notifikasi Grace Period dan Overdue Siklus Berikutnya"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-395
  - TC-FA-NOTIF-420
coverage:
  web: automated
---

# Task Audit Extend dan Reject: Notifikasi Grace Period dan Overdue Siklus Berikutnya

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: siklus berikutnya notifikasi task audit setelah Extend dan Reject menjadi objek uji.
- Akun aktor pertama Auditor (Rina Wijaya): Pre-setup #13 (`auditorRina_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_AUDITOR_PASSWORD`, `Fixture.fixedAssetNotification.auditorRina`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai lewat langkah Ganti akun eksplisit di `## Test Steps`.
- Akun Approver (Audit): Pre-setup #7 (`approverAudit_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERAUD_PASSWORD`, `Fixture.fixedAssetNotification.approverAudit`). Dipakai hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Kemampuan menjalankan job latar (scheduler harian audit), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di akhir blok terakhir yang menggeser jam. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): task audit `Task Audit Q3-Gedung A` (Pre-setup #23; status Waiting for Approval pada TC-FA-NOTIF-420, siklus pertama selesai pada TC-FA-NOTIF-395). Status task, siklus pertama yang sudah mengirim notifikasi Grace Period dan Overdue, dan jadwal disiapkan fixture BE penyetel state sumber sebelum tiap TC; tanggal tiap perpindahan dibaca dari state task itu. Reject task (alasan dari `Fixture.fixedAssetNotification.rejectionReason`) dikerjakan sesi API Approver Audit Pre-setup #7 hingga tersimpan; Update Task Extend dikerjakan sesi API Asset Admin Pre-setup #8 hingga tersimpan.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah scheduler harian, Reject, dan Update Task Extend pada Task Audit Q3-Gedung A (Pre-setup #23) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (status job selesai lewat kueri fixture BE hanya penanda pemicu selesai, bukan anchor absence) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERAUD_PASSWORD`, `FA_ASSETADMIN_PASSWORD`, `FA_AUDITOR_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.

## Test Steps


### TC-FA-NOTIF-420: Reject, notifikasi Grace Period dan Overdue siklus berikutnya

1. Pulihkan seed lewat fixture BE pemulih, siapkan Task Audit Q3-Gedung A Waiting for Approval setelah Finish Audit dengan notifikasi Grace Period dan Overdue siklus pertama sudah terkirim, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat lewat kemampuan baca BE jumlah item ber-Title `Audit task entering grace period` dan jumlah item ber-Title `Audit task is overdue` milik Auditor Rina Wijaya sebagai jumlah awal masing-masing
3. Reject Task Audit Q3-Gedung A dengan alasan `Fixture.fixedAssetNotification.rejectionReason` lewat sesi API Approver Audit hingga tersimpan sehingga task kembali In Audit
4. Atur jam server dan jam browser ke tanggal task memasuki Grace Period, lalu jalankan scheduler harian hingga selesai
5. Atur jam server dan jam browser ke tanggal task memasuki Overdue lagi, lalu jalankan scheduler harian hingga selesai
6. Klik Bell icon
7. Verifikasi item ber-Title `Your request has been rejected` diterima
8. Verifikasi Body item `Your request has been rejected` adalah `Task Audit Q3-Gedung A: ` diikuti `Fixture.fixedAssetNotification.rejectionReason`
9. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task entering grace period` milik Auditor sama dengan jumlah awal langkah 2 + 1 (siklus pertama tetap ada dan satu item baru dari siklus berikutnya)
10. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task is overdue` milik Auditor sama dengan jumlah awal langkah 2 + 1 (siklus pertama tetap ada dan satu item baru dari siklus berikutnya)

### TC-FA-NOTIF-395: Extend, notifikasi Grace Period dan Overdue siklus berikutnya

11. Pulihkan seed lewat fixture BE pemulih, siapkan Task Audit Q3-Gedung A yang sudah melewati In Audit, Grace Period, dan Overdue pada siklus pertama (notifikasi `Audit task is overdue` varian Asset Admin dan Group Manager siklus pertama Unread, Auditor Rina Wijaya menerima tiga notifikasi siklus pertama), lalu muat ulang halaman Fixed Asset > Dashboard
12. Catat lewat kemampuan baca BE jumlah item ber-Title `Audit task entering grace period` dan jumlah item ber-Title `Audit task is overdue` milik Auditor Rina Wijaya sebagai jumlah awal masing-masing
13. Catat lewat kemampuan baca BE jumlah item ber-Title `Audit task is overdue` milik Asset Admin sebagai jumlah awal
14. Update Task Extend pada Task Audit Q3-Gedung A lewat sesi API Asset Admin hingga tersimpan sehingga task kembali In Audit
15. Atur jam server dan jam browser ke tanggal task memasuki Grace Period, lalu jalankan scheduler harian hingga selesai
16. Atur jam server dan jam browser ke tanggal task memasuki Overdue lagi, lalu jalankan scheduler harian hingga selesai
17. Klik Bell icon sebagai Auditor
18. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task entering grace period` milik Auditor sama dengan jumlah awal langkah 12 + 1 (siklus pertama tetap ada dan satu item baru dari siklus kedua)
19. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task is overdue` milik Auditor sama dengan jumlah awal langkah 12 + 1 (siklus pertama tetap ada dan satu item baru dari siklus kedua)
20. Catat jumlah badge Bell icon Auditor sebagai baseline
21. Ganti akun: Logout, lalu login sebagai Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`)
22. Buka halaman Fixed Asset > Dashboard
23. Klik Bell icon sebagai Asset Admin
24. Verifikasi item `Audit task is overdue` siklus pertama berstatus Read
25. Verifikasi item `Audit task is overdue` siklus pertama tanpa tombol `[Detail]`
26. Verifikasi (kemampuan baca BE) jumlah item ber-Title `Audit task is overdue` milik Asset Admin sama dengan jumlah awal langkah 13 + 1 (siklus pertama tetap ada dan satu item baru dari siklus kedua)
27. Verifikasi satu item `Audit task is overdue` baru berstatus Unread
28. Verifikasi item `Audit task is overdue` baru memiliki tombol `[Detail]` (siklus kedua, bukan duplikat yang diabaikan)
29. Catat jumlah badge Bell icon Asset Admin sebagai baseline
30. Jalankan scheduler harian sekali lagi pada hari yang sama hingga selesai
31. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi Dropdown Panel Asset Admin masih memuat item `Audit task is overdue` siklus kedua (item pembanding pada surface yang sama, anchor absence)
34. Verifikasi badge Bell icon Asset Admin sama dengan baseline (selisih 0)
35. Ganti akun: Logout, lalu login sebagai Auditor Pre-setup #13 (`auditorRina_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_AUDITOR_PASSWORD`)
36. Buka halaman Fixed Asset > Dashboard
37. Klik Bell icon sebagai Auditor
38. Verifikasi Dropdown Panel Auditor memuat item `Audit task is overdue` (item pembanding pada surface yang sama, anchor absence)
39. Verifikasi badge Bell icon Auditor sama dengan baseline (selisih 0)
40. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Urutan: TC-FA-NOTIF-420 lebih dulu dan TC-FA-NOTIF-395 sesudahnya; pada TC-FA-NOTIF-395 pengamatan Auditor didahulukan sebelum Asset Admin dan Ganti akun hanya dua kali (S-07), sedangkan TC mengamati Asset Admin lebih dulu. Hasil yang diasersi sama.
- Langkah penghubung (S-03): langkah pembuka tiap TC (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11); "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); Reject dan Update Task Extend lewat sesi API (R-20, "hingga tersimpan"); pengaturan jam ke tanggal tiap perpindahan (dibaca dari state task); langkah 40 (pemulihan jam server dan jam browser ke waktu nyata, S-09 dan R-08).
- Alasan melewati ambang sekitar 35 langkah (40 langkah): dua TC satu kelas (siklus berikutnya notifikasi task audit, kelas d) pada Task Audit Q3-Gedung A, tiap TC berdiri sendiri dengan seed dipulihkan, dan langkah ke-40 hanya pemulihan jam.
- Pembagian TC lintas spec: TC-FA-NOTIF-347, 348, dan 349 (perpindahan status satu siklus) ada di spec 099.
- Asersi tambahan di luar Expected TC (S-03): "dua item ber-Title yang sama" menyatakan item siklus pertama masih ada di samping item baru; jumlah item per Title (langkah 9, 10, 18, 19, dan 26) dibaca lewat kemampuan baca BE terhadap jumlah awal (langkah 2, 12, dan 13), bukan hitungan item Dropdown Panel (bagian 8b butir 10); asersi badge sama dengan baseline mengikuti Expected TC-FA-NOTIF-395 butir c ("tidak menambah notifikasi pada kedua akun") dengan baseline per akun (bagian 8b butir 10).
- Tidak ada butir `P-n`.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (langkah 33 dan 38: item `Audit task is overdue` hasil siklus pada surface yang sama, bukan seed Pre-setup #17) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Spec 120 menguji siklus berikutnya setelah Extend dan Reject atas Task Audit Q3-Gedung A, yang juga dipakai spec 099 (satu siklus perpindahan status); keduanya dibedakan per topik dengan state task disiapkan ulang fixture BE sebelum tiap TC.
- Temuan untuk QA:
  - TC-FA-NOTIF-395 dan 420 tidak menyebut tanggal perpindahan task; spec membaca tanggal dari state task fixture.
  - TC-FA-NOTIF-420 menyebut Rejection Reason `Budget belum tersedia` sebagai data rekaan fixture dan Role Auditor tanpa kolom penerima Approver; Body item ditulis persis menurut TC.
  - TC-FA-NOTIF-395 menyebut Role Asset Admin tanpa nomor Pre-setup; spec memakai Pre-setup #8.
  - Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
