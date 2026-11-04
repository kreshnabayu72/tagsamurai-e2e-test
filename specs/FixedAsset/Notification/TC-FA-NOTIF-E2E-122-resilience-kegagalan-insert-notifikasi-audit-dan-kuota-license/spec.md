---
id: TC-FA-NOTIF-E2E-122-resilience-kegagalan-insert-notifikasi-audit-dan-kuota-license
title: "Resilience Server: Kegagalan Insert Notifikasi pada Task Audit dan Penilaian Kuota License"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-419
  - TC-FA-NOTIF-448
coverage:
  web: automated
---

# Resilience Server: Kegagalan Insert Notifikasi pada Task Audit dan Penilaian Kuota License

## Prerequisites

- Mode: FE+BE (kegagalan insert dipaksa di sisi server lewat fixture BE; tidak dapat di-intercept dari browser).
- Akun aktor pertama: Auditor Rina Wijaya (Pre-setup #13), `auditorRina_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AUDITOR_PASSWORD`, `Fixture.fixedAssetNotification.auditorRina`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit pada langkah 16): pengelola lisensi global (Pre-setup #33, Global Role Manage global license dimensi Update, tanpa Total Control), `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MGL_PASSWORD` (nama env sudah terdaftar), `Fixture.fixedAssetNotification.manageGlobalLicense`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pelaku (hanya sesi API aktor, butir "Sesi API aktor" di `suite.md`): Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, sebagai Approver tiket registrasi dan pelaku Submit for Approval pada TC-FA-NOTIF-448.
- Data Pre-setup: Task Audit `Task Audit Q3-Gedung A` (Pre-setup #23, In Audit dengan durasi berakhir untuk TC-FA-NOTIF-419); client Pre-setup #34 diatur Total Asset License 500, Used 440, Reserved 10 (Remaining 50), penanda tingkat peringatan Normal, dengan tiket registrasi 10 aset Waiting for Approval dan sekurangnya satu draf aset siap Submit for Approval (Pre-setup #34). Spec mengubah task audit (langkah 4 dan 11) serta kuota dan penanda tingkat (langkah 17 dan 26); fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dan pemulihan Pre-setup #34 dijalankan di hook `before`, pada langkah 1 dan 17, dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan, S-13):
  - fixture BE kegagalan: pemaksaan kegagalan insert notifikasi `audit_task_grace_period` dan kegagalan Create Notification `license_quota_low`, beserta pemulihannya (butir "Fixture BE kegagalan" di `suite.md`);
  - kemampuan menjalankan scheduler harian audit dan job penilaian kuota (butir "Kemampuan menjalankan job latar" di `suite.md`);
  - fixture BE penyetel Total Asset License, Used, Reserved, dan penanda tingkat (Pre-setup #34), serta pembaca status Task Audit dan tiket registrasi.
- Asersi absence atas notifikasi in-app memakai baseline badge per penerima yang dicatat tepat sebelum pemicu, `Verifikasi` item seed pembanding `Asset has been repaired` (Read, view-only; Pre-setup #17) pada Dropdown Panel yang sama, dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Env var `FA_AUDITOR_PASSWORD`, `FA_MGL_PASSWORD`, dan `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Pengecualian S-06/S-12 butir A-16: `Task Audit Q3-Gedung A` (Pre-setup #23, butir (ii)) dipakai literal tanpa suffix `{runId}-122` sebagai target scheduler dan pemicu status, dan kuota serta penanda tingkat client Pre-setup #34 (butir (iii)) diatur Fixture BE sebagai pemicu, karena nama task ditulis literal di Expected TC dan ID transaksi dibangkitkan sistem; notifikasi seed Pre-setup #17 hanya dibaca sebagai item pembanding. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (langkah 1 dan 17); kuota client Pre-setup #34 mengikuti pemulihan fixture BE yang sama; suite berjalan serial (`parallel: false`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-419: Kegagalan insert saat perpindahan status task audit di-rollback dan dievaluasi ulang

1. Pulihkan seed lewat fixture BE pemulih, atur `Task Audit Q3-Gedung A` berstatus In Audit dengan durasi berakhir lewat fixture BE, lalu muat ulang halaman Fixed Asset > Dashboard
2. Klik Bell icon, lalu catat nilai badge Bell icon (baseline) dan, lewat kemampuan baca BE, jumlah item ber-Title `"Audit task entering grace period"` milik Auditor sebagai jumlah awal
3. Paksa kegagalan insert notifikasi `audit_task_grace_period` lewat fixture BE
4. Jalankan scheduler harian hingga selesai
5. Periksa status `Task Audit Q3-Gedung A` lewat fixture BE
6. Verifikasi task tetap In Audit
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Verifikasi Dropdown Panel Auditor memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik Auditor (item pembanding pada surface yang sama, anchor absence)
9. Verifikasi tidak ada notifikasi `"Audit task entering grace period"` pada Dropdown Panel
10. Verifikasi badge Bell icon sama dengan baseline langkah 2
11. Pulihkan kegagalan insert lewat fixture BE, lalu jalankan scheduler harian hingga selesai
12. Periksa status `Task Audit Q3-Gedung A` lewat fixture BE
13. Verifikasi task berstatus Grace Period
14. Verifikasi (kemampuan baca BE) jumlah item ber-Title `"Audit task entering grace period"` milik Auditor sama dengan jumlah awal langkah 2 + 1
15. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 2

### TC-FA-NOTIF-448: Kegagalan pembuatan event tidak memblokir Approve dan penilaian berikutnya mengirimnya

16. Logout, lalu login sebagai pengelola lisensi global (Pre-setup #33) dengan `Spectra.env.FA_MGL_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Pulihkan seed lewat fixture BE pemulih, atur client Pre-setup #34 Total Asset License 500, Used 440, Reserved 10 (Remaining 50), penanda tingkat Normal, dengan tiket registrasi 10 aset Waiting for Approval lewat fixture BE, lalu muat ulang halaman Fixed Asset > Dashboard
18. Klik Bell icon, lalu catat nilai badge Bell icon (baseline) dan, lewat kemampuan baca BE, jumlah item ber-Title `"Asset license quota is running low"` milik pengelola lisensi global sebagai jumlah awal
19. Paksa kegagalan Create Notification untuk event `license_quota_low` lewat fixture BE
20. Dari akun Approver (Pre-setup #1, sesi API), Approve tiket registrasi hingga status Approved tersimpan
21. Periksa status tiket registrasi lewat fixture BE
22. Verifikasi Approve berhasil (tiket registrasi berstatus Approved)
23. Tunggu 5 detik tanpa memuat ulang halaman
24. Verifikasi Dropdown Panel pengelola lisensi global memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun itu (item pembanding pada surface yang sama, anchor absence)
25. Verifikasi tidak ada notifikasi kuota `"Asset license quota is running low"` pada Dropdown Panel
26. Pulihkan kegagalan Create Notification lewat fixture BE, lalu picu penilaian berikutnya dengan Submit for Approval 1 draf (akun Pre-setup #1, sesi API) hingga tersimpan
27. Verifikasi (kemampuan baca BE) jumlah item ber-Title `"Asset license quota is running low"` milik pengelola lisensi global sama dengan jumlah awal langkah 18 + 1
28. Verifikasi notifikasi baru `"Asset license quota is running low"` pada Dropdown Panel berstatus Unread
29. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 18

## Notes

- Kegagalan sisi server (kelas b) tidak dapat di-intercept dari browser; pemicunya fixture BE, kemampuan teknisnya tercantum di Prerequisites, dan pemulihannya ditulis sebagai langkah (langkah 11 dan 26) serta di hook `after`.
- Langkah penghubung (S-03): langkah 1 dan 17 (pengaturan state awal, pemulihan antar TC, S-09); langkah 2 dan 18 (membuka Dropdown Panel dan baseline badge, S-12); langkah 5, 12, dan 21 (membaca status lewat fixture BE); langkah 7 dan 23 (jendela 5 detik, bagian 6 konvensi); langkah 16 (ganti akun eksplisit, S-07); langkah 20 dan 26 (pelaku lewat sesi API).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 9 dan 25 didahului langkah 8 dan 24 (Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) sebagai item pembanding) dan langkah 6 dan 22 (aksi pemicu terbukti berjalan).
- Pada TC-FA-NOTIF-448 urutan TC "Klik Bell icon sebagai penerima" (langkah 4 TC) dipecah: Dropdown Panel sudah terbuka sejak langkah 18 dan diamati setelah Approve (langkah 24 dan 25) dan setelah penilaian berikutnya (langkah 27 dan 28), supaya Expected a dan b masing-masing punya `Verifikasi` tepat setelah aksinya (R-03).
- `P-2`: scheduler harian audit (kelas d; langkah 4 dan 11) dan job penilaian kuota (langkah 26) hanya memicu kondisi yang diuji; objek asersinya adalah kegagalan insert atau Create Notification di server (kelas b), bukan perilaku scheduler atau job.
- Pembagian TC lintas spec: TC kegagalan insert pada Submit Borrow dan job terjadwal Borrow (TC-FA-NOTIF-360, 361, dan 418) ada di spec 107, karena datasetnya berbeda (transaksi Borrow Pre-setup #19 dan #24, bukan task audit dan kuota client) sehingga pemulihan state dan akun penerimanya berbeda.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Asersi tambahan di luar Expected TC (S-03): badge sama dengan baseline (langkah 10) dan badge bertambah 1 (langkah 15 dan 29) memakai baseline badge per penerima (bagian 8b butir 10); jumlah item per Title (langkah 14 dan 27) dibaca lewat kemampuan baca BE terhadap jumlah awal (langkah 2 dan 18), bukan hitungan item Dropdown Panel.
- Temuan untuk QA:
  - TC-FA-NOTIF-419: Expected tidak menulis cara membaca status task (UI atau fixture BE); status diperiksa lewat fixture BE. Cara menjalankan "scheduler harian" tidak ditulis (kemampuan tim FE/BE).
  - TC-FA-NOTIF-448: "Approver (akun Pre-setup #1)" dan pelaku "Submit for Approval 1 draf" tidak menyebut akun pelaku Submit; spec memakai akun Pre-setup #1 lewat sesi API. Nilai Reserved 10 dan Remaining 50 pada Precondition tidak berubah oleh Approve menurut TC; tidak diasersi. "Klik Bell icon sebagai penerima" tidak menyebut apakah penerima selain Pre-setup #33; hanya #33 yang diasersi.
  - TC-FA-NOTIF-419 dan 448: Post Condition kosong (`-`); tidak ada asersi tambahan.
