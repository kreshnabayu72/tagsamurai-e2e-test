---
id: TC-FA-NOTIF-E2E-090-almost-timeout-disposal-penerima-approver-requester-pic
title: "Almost Timeout Disposal: Penerima Approver, Requester, dan PIC Admin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-282
  - TC-FA-NOTIF-283
  - TC-FA-NOTIF-284
coverage:
  web: automated
---

# Almost Timeout Disposal: Penerima Approver, Requester, dan PIC Admin

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: job terjadwal dan batas waktu menjadi objek uji.
- Akun aktor pertama Approver (Disposal, Gedung A): Pre-setup #6 (`approverDisposal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERDSP_PASSWORD`, `Fixture.fixedAssetNotification.approverDisposal`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai lewat langkah Ganti akun eksplisit di `## Test Steps`.
- Kemampuan menjalankan job latar (`F-FATX-07`) dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): transaksi Disposal DSP-2026-0030 (Pre-setup #19 sampai #24) dan aset terkait. Status transaksi dan sisa waktu disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16: DSP-2026-0030 dipakai literal tanpa suffix `{runId}-090` sebagai pemicu job, karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERDSP_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec memakai data Pre-setup bersama yang diubah job dan dipulihkan fixture BE, yang memengaruhi spec lain.
- Tabel "Event TC-FA-NOTIF-283 dan 284" (urutan baris = urutan iterasi; TC-FA-NOTIF-284 satu iterasi per status sesuai Precondition TC):

  | TC | Event | State | Job pemicu | Title | Body | Icon, severity | Tombol | Klik | Path tujuan |
  |---|---|---|---|---|---|---|---|---|---|
  | TC-FA-NOTIF-283 | `disposal_almost_timeout` (Requester) | DSP-2026-0030 Waiting for Approval, timeout snapshot 3 hari, sisa 24 jam, pengingat belum pernah dikirim | `F-FATX-07` langkah 2 (varian Requester: kondisi sama dengan varian Approver) | `Your request is expiring soon` | `Your request is awaiting decision and will expire in 24 hours if not resolved.` | `time-line`, `warning` | view-only: `[Mark as Read]` tampil tanpa `[Detail]` | judul item | `/fams/transactions-disposal/DSP-2026-0030` |
  | TC-FA-NOTIF-284 (Waiting for Verification) | `disposal_almost_timeout` (PIC admin) | DSP-2026-0030 Waiting for Verification, timeout snapshot 3 hari, sisa 24 jam | `F-FATX-07` langkah 2 untuk transaksi Disposal berstatus Waiting for Verification (sisa waktu ≤ 1 hari dan snapshot batas waktu transaksi lebih dari 1 hari) | `Please finish this transaction — expiring soon` | `DSP-2026-0030 (1 Asset) — 24h left or less` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/transactions-disposal/DSP-2026-0030` |
  | TC-FA-NOTIF-284 (On Progress) | `disposal_almost_timeout` (PIC admin) | DSP-2026-0030 On Progress, timeout snapshot 3 hari, sisa 24 jam | `F-FATX-07` langkah 2 untuk transaksi Disposal berstatus On Progress (sisa waktu ≤ 1 hari dan snapshot batas waktu transaksi lebih dari 1 hari) | `Please finish this transaction — expiring soon` | `DSP-2026-0030 (1 Asset) — 24h left or less` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/transactions-disposal/DSP-2026-0030` |


## Test Steps


### TC-FA-NOTIF-282: disposal_almost_timeout varian Approver

1. Pulihkan seed lewat fixture BE pemulih, siapkan DSP-2026-0030 Waiting for Approval, timeout snapshot 3 hari, sisa 24 jam, pengingat belum pernah dikirim lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline
3. Jalankan `F-FATX-07` langkah 2 lewat kemampuan job latar hingga selesai
4. Verifikasi badge Bell icon bertambah 1 terhadap baseline
5. Klik Bell icon
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru tampil bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item baru ber-Title `"Please finish this approval — expiring soon"` dan Body `"Request DSP-2026-0030 will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request."`
10. Verifikasi item baru memakai icon `time-line` dengan severity `warning`
11. Verifikasi item baru menampilkan tombol `[Detail]` tanpa `[Mark as Read]`
12. Klik `[Detail]` pada item baru
13. Verifikasi browser berpindah ke `/fams/approvals/disposal/DSP-2026-0030`
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item baru tetap Unread (status baca tidak berubah oleh klik)

### TC-FA-NOTIF-283 dan TC-FA-NOTIF-284: disposal_almost_timeout varian Requester dan PIC admin

17. Ganti akun: Logout, lalu login sebagai Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`)
18. Buka halaman Fixed Asset > Dashboard
19. Untuk setiap baris tabel "Event TC-FA-NOTIF-283 dan 284" (langkah 19 sampai 34): pulihkan seed lewat fixture BE pemulih, siapkan state transaksi atau aset baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
20. Catat jumlah badge Bell icon akun aktor sebagai baseline
21. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
22. Verifikasi badge Bell icon bertambah 1 terhadap baseline
23. Klik Bell icon
24. Verifikasi item baru berada di posisi teratas Dropdown Panel
25. Verifikasi Title item baru tampil bold
26. Verifikasi dot Unread tampil pada item baru
27. Verifikasi item baru ber-Title dan Body sesuai kolom Title dan Body baris itu
28. Verifikasi icon dan severity item baru sesuai kolom Icon baris itu
29. Verifikasi tombol item baru sesuai kolom Tombol baris itu
30. Klik kontrol pada kolom Klik baris itu pada item baru
31. Verifikasi browser berpindah ke path tujuan baris itu
32. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
33. Klik Bell icon
34. Verifikasi item baru tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 19 sampai 34 diulang untuk tiga baris tabel "Event TC-FA-NOTIF-283 dan 284" (TC-FA-NOTIF-283, lalu TC-FA-NOTIF-284 satu iterasi per status Waiting for Verification dan On Progress sesuai Precondition TC); langkah 1 sampai 16 berdiri sendiri (66 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi, 66 langkah): semua blok satu kelas (job terjadwal dan batas waktu, kelas d), tiap blok berdiri sendiri dengan seed dipulihkan, dan kegagalan satu varian penerima atau status tidak membuat varian lain kehilangan makna.
- Tiap entity transaksi (Borrow, Transfer, Disposal) diuji di spec berbeda walau berbagi dataset transaksi Pre-setup #19 sampai #24, karena tiap entity memiliki penerima, Title, dan path tujuan sendiri serta seed dipulihkan per spec.
- Langkah penghubung (S-03): langkah 1 dan 19 (pemulihan seed dan penyiapan state); langkah kembali ke Fixed Asset > Dashboard dan membuka Bell icon di tiap blok (untuk mengamati status baca); Ganti akun dan pembukaan Dashboard sebelum blok kedua; langkah "Catat jumlah badge Bell icon" (baseline S-12). Kolom Klik tabel menentukan kontrol yang diklik per tier (TC "sesuai tier").
- Urutan: varian Approver (akun hook `before`) lebih dulu, lalu satu kali Ganti akun ke Asset Admin untuk varian Requester dan PIC admin (S-07).
- Pelaku transaksi lain tidak dipakai; seluruh pemicu adalah job latar yang dijalankan fixture BE. Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-283 dan TC-FA-NOTIF-284 menyebut Role Asset Admin tanpa nomor Pre-setup (pemohon dan PIC pembuat); spec memakai Pre-setup #8 (Asset Admin, PIC admin). Email akun pemohon tidak tertulis eksplisit di TC.
  - Langkah TC berakhir pada klik item; asersi "tanpa mengubah status baca" membutuhkan pengamatan setelah navigasi, sehingga spec menambah langkah kembali dan membuka Bell icon (langkah penghubung). TC tidak memberi langkah itu.
  - TC tidak menyebut jam absolut job (hanya "sisa 24 jam"); jam diatur fixture BE sesuai state transaksi.
  - Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
