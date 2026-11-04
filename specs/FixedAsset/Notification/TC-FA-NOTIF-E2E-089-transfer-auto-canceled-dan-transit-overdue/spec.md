---
id: TC-FA-NOTIF-E2E-089-transfer-auto-canceled-dan-transit-overdue
title: "Transfer Auto Canceled dan Transit Overdue"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-281
  - TC-FA-NOTIF-286
coverage:
  web: automated
---

# Transfer Auto Canceled dan Transit Overdue

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: job terjadwal dan batas waktu menjadi objek uji.
- Akun aktor pertama Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (`F-FATX-07`, job transit overdue) dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): transaksi Transfer TRF-2026-0055 (Pre-setup #21), aset (#24). Status transaksi dan batas waktu disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16: TRF-2026-0055 dipakai literal tanpa suffix `{runId}-089` sebagai pemicu job, karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec memakai data Pre-setup bersama yang diubah job dan dipulihkan fixture BE, yang memengaruhi spec lain.
- Tabel "Event TC-FA-NOTIF-281 dan 286" (urutan baris = urutan iterasi):

  | TC | Event | State | Job pemicu | Title | Body | Icon, severity | Tombol | Klik | Path tujuan |
  |---|---|---|---|---|---|---|---|---|---|
  | TC-FA-NOTIF-281 | `transfer_auto_canceled` | TRF-2026-0055 pra-komitmen, batas auto-cancel terlampaui | `F-FATX-07` langkah 3 (batas waktu auto-cancel terlewati dan transaksi Transfer belum committed) | `Your request was canceled automatically` | `TRF-2026-0055 (1 Asset): not completed in time` | `close-circle-line`, `danger` | view-only: `[Mark as Read]` tampil tanpa `[Detail]` | judul item | `/fams/transactions-transfer/TRF-2026-0055` |
  | TC-FA-NOTIF-286 | `transfer_transit_overdue` | TRF-2026-0055 In Transfer Process, batas transit terlampaui, penerima uji pemohon | Batas maksimum waktu transit Transfer (snapshot) terlampaui tanpa konfirmasi tiba (FATX-LOGIC-02, E-FATX-06), dijalankan lewat job transit | `Your transfer is overdue` | `TRF-2026-0055 was due on 25/06/26.` | `time-line`, `warning` | view-only: `[Mark as Read]` tampil tanpa `[Detail]` | judul item | `/fams/transactions-transfer/TRF-2026-0055` |


## Test Steps


### TC-FA-NOTIF-281 dan TC-FA-NOTIF-286: transfer auto canceled dan transit overdue

1. Untuk setiap baris tabel "Event TC-FA-NOTIF-281 dan 286" (langkah 1 sampai 16): pulihkan seed lewat fixture BE pemulih, siapkan state transaksi atau aset baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah badge Bell icon akun aktor sebagai baseline
3. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
4. Verifikasi badge Bell icon bertambah 1 terhadap baseline
5. Klik Bell icon
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru tampil bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item baru ber-Title dan Body sesuai kolom Title dan Body baris itu
10. Verifikasi icon dan severity item baru sesuai kolom Icon baris itu
11. Verifikasi tombol item baru sesuai kolom Tombol baris itu
12. Klik kontrol pada kolom Klik baris itu pada item baru
13. Verifikasi browser berpindah ke path tujuan baris itu
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item baru tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 16 diulang untuk dua baris tabel "Event TC-FA-NOTIF-281 dan 286" (32 langkah setelah ekspansi, di bawah ambang). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Topik auto canceled dan transit overdue Transfer berbagi dataset TRF-2026-0055 (Pre-setup #21); keduanya satu spec karena entity, akun, kelas harness (job terjadwal), dan alur verifikasi sama, sedangkan entity Borrow dan Disposal diuji di spec lain karena penerima, Title, dan path tujuan berbeda.
- Langkah penghubung (S-03): langkah 1 (pemulihan seed dan penyiapan state); langkah kembali ke Fixed Asset > Dashboard dan membuka Bell icon (untuk mengamati status baca); langkah "Catat jumlah badge Bell icon" (baseline S-12). Kolom Klik tabel menentukan kontrol yang diklik per tier.
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-281 dan 286 menyebut Role Asset Admin tanpa nomor Pre-setup (PIC pembuat dan pemohon); spec memakai Pre-setup #8. Email akun pemohon tidak tertulis eksplisit di TC.
  - TC-FA-NOTIF-286 menulis Body `TRF-2026-0055 was due on 25/06/26.` tetapi tidak menyebut jam fixture saat job transit berjalan atau batas transit dalam hari; spec mengandalkan fixture BE menyiapkan state "batas transit terlampaui" dengan tanggal jatuh tempo 25/06/26.
  - Langkah TC berakhir pada klik item; asersi "tanpa mengubah status baca" membutuhkan pengamatan setelah navigasi, sehingga spec menambah langkah kembali dan membuka Bell icon (langkah penghubung).
  - Post Condition kedua TC kosong (`-`); tidak ada yang diasersi.
