---
id: TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off
title: "Interval Pengingat Damaged dan Missing: Batas Hari dan Pengaturan OFF"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-431
  - TC-FA-NOTIF-432
  - TC-FA-NOTIF-433
  - TC-FA-NOTIF-437
  - TC-FA-NOTIF-438
  - TC-FA-NOTIF-439
coverage:
  web: automated
---

# Interval Pengingat Damaged dan Missing: Batas Hari dan Pengaturan OFF

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: interval pengingat dan batas waktu job menjadi objek uji.
- Akun aktor pertama Group Manager (Gedung A): Pre-setup #3 (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`, `Fixture.fixedAssetNotification.groupManager`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan menjalankan job latar (`F-FATX-11`), menggeser jam server dan jam fixture, dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam server dan jam browser diatur bersama ke waktu absolut yang disebut langkah (bukan digeser relatif) dan dipulihkan di hook `after` serta oleh langkah penghubung "Pulihkan jam server dan jam browser ke waktu nyata" di akhir blok terakhir yang menggeser jam. Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 dan Laptop - 1 AST-2024-0067 (Pre-setup #24). Tiket Damaged dan Missing, tanggal pelaporan, pengaturan pengingat (aktif atau OFF), interval, dan penanda pengingat terkirim disiapkan fixture BE penyetel state sumber sebelum tiap TC; pengaturan pengingat yang di-OFF dipulihkan fixture BE pemulih.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job pada aset Pre-setup bersama (AST-2024-0141, AST-2024-0067) yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta antar TC; suite berjalan serial.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10). Jumlah item per Title (atau Body) dibaca lewat kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan) sebagai jumlah awal sebelum pemicu dan pembacaan sesudah pemicu dari sumber yang sama (bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru; bagian 8b butir 10).
- Asersi absence notifikasi in-app didahului `Verifikasi` item pembanding di surface yang sama (item seed pembanding akun aktor `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 dan disediakan fixture BE; kueri status job selesai lewat fixture BE hanya menandai pemicu selesai, bukan bukti panel memuat item) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman"; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec mengubah jam server dan jam fixture, yang memengaruhi spec lain.
- Tabel "Kasus tidak dikirim TC-FA-NOTIF-431, 437, 439, dan 433" (urutan baris = urutan iterasi; Waktu job diatur ke jam server dan jam browser secara absolut):

  | TC | Event | State | Waktu job | Notifikasi yang tidak boleh ada |
  |---|---|---|---|---|
  | TC-FA-NOTIF-431 | `damaged_reminder` | AST-2024-0141 tiket Damaged dilaporkan 11/06/26, belum selesai; pengingat Damaged aktif dengan interval 7 hari; belum ada pengingat terkirim | 17/06/26 (selisih 6 hari) | `Damaged asset is still unresolved` untuk AST-2024-0141 |
  | TC-FA-NOTIF-437 | `missing_reminder` | AST-2024-0067 tiket Missing dilaporkan 11/06/26, belum selesai; pengingat Missing aktif dengan interval 7 hari; belum ada pengingat terkirim | 17/06/26 (selisih 6 hari) | `Missing asset is still under investigation` untuk AST-2024-0067 |
  | TC-FA-NOTIF-439 | `damaged_reminder` | Pengaturan pengingat Damaged OFF; AST-2024-0141 tiket Damaged belum selesai dan interval tercapai (dilaporkan 11/06/26, interval 7 hari) | 18/06/26 | `Damaged asset is still unresolved` untuk AST-2024-0141 |
  | TC-FA-NOTIF-433 | `missing_reminder` | Pengaturan pengingat Missing OFF; AST-2024-0067 tiket Missing belum selesai dan interval tercapai (dilaporkan 11/06/26, interval 7 hari) | 18/06/26 | `Missing asset is still under investigation` untuk AST-2024-0067 |

- Tabel "Kasus dikirim TC-FA-NOTIF-432 dan 438" (urutan baris = urutan iterasi):

  | TC | Event | State | Waktu job | Title | Body |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-432 | `damaged_reminder` | AST-2024-0141 tiket Damaged dilaporkan 11/06/26, belum selesai; pengingat Damaged aktif dengan interval 7 hari; belum ada pengingat terkirim | 18/06/26 (selisih 7 hari) | `Damaged asset is still unresolved` | `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` |
  | TC-FA-NOTIF-438 | `missing_reminder` | AST-2024-0067 tiket Missing dilaporkan 11/06/26, belum selesai; pengingat Missing aktif dengan interval 7 hari; belum ada pengingat terkirim | 18/06/26 (selisih 7 hari) | `Missing asset is still under investigation` | `Laptop - 1 (AST-2024-0067) has not been found yet.` |


## Test Steps


### TC-FA-NOTIF-431, 437, 439, dan 433: pengingat tidak dikirim

1. Untuk setiap baris tabel "Kasus tidak dikirim TC-FA-NOTIF-431, 437, 439, dan 433" (langkah 1 sampai 10): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
2. Atur jam server dan jam browser ke waktu job pada baris itu
3. Catat jumlah badge Bell icon akun aktor sebagai baseline
4. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
5. Kueri status job lewat fixture BE hingga job berstatus selesai (penanda pemicu selesai, bukan anchor absence)
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Klik Bell icon
8. Verifikasi Dropdown Panel memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun aktor (item pembanding pada surface yang sama, anchor absence)
9. Verifikasi badge Bell icon sama dengan baseline (selisih 0)
10. Verifikasi Dropdown Panel tidak memuat item dengan Title dan aset pada kolom "Notifikasi yang tidak boleh ada" baris itu

### TC-FA-NOTIF-432 dan 438: pengingat dikirim tepat pada hari interval tercapai

11. Untuk setiap baris tabel "Kasus dikirim TC-FA-NOTIF-432 dan 438" (langkah 11 sampai 17): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
12. Atur jam server dan jam browser ke waktu job pada baris itu
13. Catat jumlah badge Bell icon akun aktor sebagai baseline dan, lewat kemampuan baca BE, jumlah item ber-Title dan Body sesuai kolom Title dan Body baris itu milik akun aktor sebagai jumlah awal
14. Jalankan job pemicu baris itu lewat kemampuan job latar hingga selesai
15. Klik Bell icon
16. Verifikasi badge Bell icon bertambah 1 terhadap baseline
17. Verifikasi (kemampuan baca BE) jumlah item ber-Title dan Body sesuai kolom Title dan Body baris itu milik akun aktor sama dengan jumlah awal langkah 13 + 1 (satu item pengingat baru diterima)
18. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 10 diulang untuk empat baris tabel "Kasus tidak dikirim TC-FA-NOTIF-431, 437, 439, dan 433" dan langkah 11 sampai 17 untuk dua baris tabel "Kasus dikirim TC-FA-NOTIF-432 dan 438" (55 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi): semua blok satu kelas (interval pengingat Damaged dan Missing, kelas d), nominalnya 18 langkah, 55 setelah ekspansi, dan tiap iterasi berdiri sendiri dengan seed dipulihkan.
- Urutan: kasus tidak dikirim lebih dulu, lalu kasus dikirim (S-10); urutan nomor TC tidak diikuti karena tabel dikelompokkan menurut hasil (tidak dikirim atau dikirim).
- Langkah penghubung (S-03): langkah 1 dan 11 (pemulihan seed dan penyiapan state); "Catat jumlah badge Bell icon" (baseline S-12); "Kueri status job" (penanda pemicu selesai; anchor absence adalah `Verifikasi` item pembanding, bagian 8b butir 2 dan 11) dan "Tunggu 5 detik tanpa memuat ulang halaman" (bagian 6); langkah 18 (pemulihan jam server dan jam browser ke waktu nyata, S-09 dan R-08).
- Asersi tambahan di luar Expected TC (dicatat sesuai S-03): badge sama dengan baseline pada kasus tidak dikirim dan badge bertambah 1 pada kasus dikirim, karena Dropdown Panel hanya memuat lima item terbaru dan jumlah notifikasi harus memakai baseline per penerima (bagian 8b butir 10); jumlah item ber-Title dan Body pada kasus dikirim (langkah 13 dan 17) dibaca lewat kemampuan baca BE, bukan hitungan item Dropdown Panel.
- Tidak ada butir `P-n`.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` item pembanding (item seed pembanding `Asset has been repaired`, Read, view-only, yang dijamin Pre-setup #17 untuk akun aktor dan sudah ada pada surface yang sama) ditulis sebelum asersi absence supaya asersi tidak lulus hampa (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-NOTIF-433 dan 439 tidak menyebut tanggal job, tanggal pelaporan tiket, atau interval; spec memakai tanggal fixture 18/06/26, pelaporan 11/06/26, dan interval 7 hari (nilai TC-FA-NOTIF-431, 432, 437, 438).
  - TC-FA-NOTIF-431 sampai 439 tidak menyebut isi Body untuk kasus "tidak ada notifikasi"; spec mengasersi berdasarkan Title dan aset.
  - Post Condition keenam TC kosong (`-`); tidak ada yang diasersi.
