---
id: TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat
title: "Auto Canceled Transaksi Pra-Komitmen dan Almost Timeout PIC Admin pada Fase Lanjut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-277
  - TC-FA-NOTIF-285
  - TC-FA-NOTIF-373
  - TC-FA-NOTIF-374
coverage:
  web: automated
---

# Auto Canceled Transaksi Pra-Komitmen dan Almost Timeout PIC Admin pada Fase Lanjut

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: job terjadwal dan batas waktu menjadi objek uji.
- Akun aktor pertama Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (`F-FATX-07`) dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (Pre-setup #19), Transfer TRF-2026-0055 (#21), Disposal DSP-2026-0030 (#22), aset (#24). Status transaksi dan sisa waktu disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16: BRW-2026-0342, DSP-2026-0030, dipakai literal tanpa suffix `{runId}-087` sebagai pemicu job, karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec memakai data Pre-setup bersama yang diubah job dan dipulihkan fixture BE, yang memengaruhi spec lain.
- Tabel "Event TC-FA-NOTIF-277 dan 285" (urutan baris = urutan iterasi):

  | TC | Event | State | Job pemicu | Title | Body | Icon, severity | Tombol | Klik | Path tujuan |
  |---|---|---|---|---|---|---|---|---|---|
  | TC-FA-NOTIF-277 | `borrow_auto_canceled` | BRW-2026-0342 pra-komitmen, batas auto-cancel terlampaui | `F-FATX-07` langkah 3 (batas waktu auto-cancel terlewati dan transaksi Borrow belum committed) | `Your request was canceled automatically` | `BRW-2026-0342 (1 Asset): not completed in time` | `close-circle-line`, `danger` | view-only: `[Mark as Read]` tampil tanpa `[Detail]` | judul item | `/fams/borrow/BRW-2026-0342` |
  | TC-FA-NOTIF-285 | `disposal_auto_canceled` | DSP-2026-0030 pra-komitmen, batas auto-cancel terlampaui | `F-FATX-07` langkah 3 (batas waktu auto-cancel terlewati dan transaksi Disposal belum committed) | `Your request was canceled automatically` | `DSP-2026-0030 (1 Asset): not completed in time` | `close-circle-line`, `danger` | view-only: `[Mark as Read]` tampil tanpa `[Detail]` | judul item | `/fams/transactions-disposal/DSP-2026-0030` |

- Tabel "Event TC-FA-NOTIF-373 dan 374" (item actionable; urutan baris = urutan iterasi):

  | TC | Event | State | Job pemicu | Title | Body | Icon, severity | Tombol | Klik | Path tujuan |
  |---|---|---|---|---|---|---|---|---|---|
  | TC-FA-NOTIF-373 | `borrow_almost_timeout` (PIC admin) | BRW-2026-0342 Ready for Handover, timeout snapshot 3 hari, sisa 24 jam | `F-FATX-07` langkah 2 | `Please finish this transaction — expiring soon` | `BRW-2026-0342 (1 Asset) — 24h left or less` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/borrow/BRW-2026-0342` |
  | TC-FA-NOTIF-374 | `disposal_almost_timeout` (PIC admin) | DSP-2026-0030 On Progress, timeout snapshot 3 hari, sisa 24 jam | `F-FATX-07` langkah 2 | `Please finish this transaction — expiring soon` | `DSP-2026-0030 (1 Asset) — 24h left or less` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/transactions-disposal/DSP-2026-0030` |


## Test Steps


### TC-FA-NOTIF-277 dan TC-FA-NOTIF-285: auto canceled transaksi pra-komitmen

1. Untuk setiap baris tabel "Event TC-FA-NOTIF-277 dan 285" (langkah 1 sampai 16): pulihkan seed lewat fixture BE pemulih, siapkan state transaksi atau aset baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
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

### TC-FA-NOTIF-373 dan TC-FA-NOTIF-374: almost timeout PIC admin pada fase lanjut

17. Untuk setiap baris tabel "Event TC-FA-NOTIF-373 dan 374" (langkah 17 sampai 27): pulihkan seed lewat fixture BE pemulih, siapkan state transaksi baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
18. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
19. Klik Bell icon
20. Verifikasi item baru ber-Title dan Body sesuai kolom Title dan Body baris itu
21. Verifikasi icon dan severity item baru sesuai kolom Icon baris itu
22. Verifikasi item baru menampilkan tombol `[Detail]` tanpa `[Mark as Read]`
23. Klik kontrol pada kolom Klik baris itu pada item baru
24. Verifikasi browser berpindah ke path tujuan baris itu
25. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
26. Klik Bell icon
27. Verifikasi item baru tetap Unread (status baca tidak berubah oleh klik)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 16 diulang untuk dua baris tabel "Event TC-FA-NOTIF-277 dan 285" dan langkah 17 sampai 27 untuk dua baris tabel "Event TC-FA-NOTIF-373 dan 374" (54 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi, 54 langkah): semua blok satu kelas (job terjadwal dan batas waktu, kelas d) dengan akun yang sama, dan tiap iterasi berdiri sendiri dengan seed dipulihkan.
- Topik auto canceled dan almost timeout fase lanjut berbagi dataset transaksi Pre-setup #19 sampai #24 dan akun Asset Admin yang sama; keduanya satu spec karena kelas harness, akun, dan pemulihan seed sama, sedangkan almost timeout varian Approver dan Requester (penerima berbeda) diuji di spec entity masing-masing.
- Langkah penghubung (S-03): langkah 1 dan 17 (pemulihan seed dan penyiapan state); langkah kembali ke Fixed Asset > Dashboard dan membuka Bell icon di tiap iterasi (untuk mengamati status baca); langkah "Catat jumlah badge Bell icon" (baseline S-12, hanya untuk TC yang Expected-nya memuat penambahan badge). Kolom Klik tabel menentukan kontrol yang diklik per tier.
- TC-FA-NOTIF-373 dan 374 tidak memuat Expected badge bertambah atau posisi teratas; spec tidak menambahkannya dan hanya mengasersi item dengan Title dan Body yang disebut TC.
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-277, 285, 373, dan 374 menyebut Role Asset Admin tanpa nomor Pre-setup (PIC pembuat); spec memakai Pre-setup #8. Email akun pemohon tidak tertulis eksplisit di TC.
  - Langkah TC berakhir pada klik item; asersi "tanpa mengubah status baca" membutuhkan pengamatan setelah navigasi, sehingga spec menambah langkah kembali dan membuka Bell icon (langkah penghubung).
  - TC-FA-NOTIF-373 dan 374 tidak menyebut kondisi pengingat belum pernah dikirim dan tidak punya Expected badge; spec mengikuti teks TC.
  - Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
