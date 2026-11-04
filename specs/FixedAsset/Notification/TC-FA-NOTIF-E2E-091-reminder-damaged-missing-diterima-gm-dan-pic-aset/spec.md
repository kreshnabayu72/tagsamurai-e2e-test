---
id: TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset
title: "Reminder Damaged dan Missing: Diterima Group Manager dan PIC Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-287
  - TC-FA-NOTIF-288
  - TC-FA-NOTIF-408
  - TC-FA-NOTIF-409
coverage:
  web: automated
---

# Reminder Damaged dan Missing: Diterima Group Manager dan PIC Aset

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel). Kelas harness d: job terjadwal dan batas waktu menjadi objek uji.
- Akun aktor pertama Group Manager (Gedung A): Pre-setup #3 (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`, `Fixture.fixedAssetNotification.groupManager`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun Asset Admin (Gedung A; PIC admin): Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`). Dipakai lewat langkah Ganti akun eksplisit di `## Test Steps`.
- Kemampuan menjalankan job latar (`F-FATX-11`) dan mengkueri status job (butir "Kemampuan menjalankan job latar ..." di `suite.md`) disediakan tim FE/BE; endpoint tidak dikarang (S-13). Jam fixture acuan "hari ini" 18/06/26, zona Asia/Jakarta.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 dan Laptop - 1 AST-2024-0067 (Pre-setup #24). Tiket Damaged, tiket Missing, pengaturan pengingat, dan interval disiapkan fixture BE penyetel state sumber sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16: aset AST-2024-0141 dan AST-2024-0067 (Pre-setup #24) dipakai literal tanpa suffix `{runId}-091` sebagai pemicu job, karena ID aset dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`). Fixture BE penyetel state sumber (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`) menyiapkan status transaksi, aset, dan tiket yang disebut langkah; endpoint tidak dikarang. Transaksi dan aset Pre-setup bersama yang diubah job (dibatalkan, ditandai terkirim) dipulihkan fixture BE pemulih di hook `after` dan antar-TC; spec tidak menumpang hasil spec lain.
- Baseline: jumlah badge Bell icon akun aktor dicatat tepat sebelum job dijalankan; asersi "bertambah 1" dan "tidak ada notifikasi baru" memakai selisih terhadap baseline itu, bukan seed bersih (S-12, bagian 8b butir 10).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Nilai data (ID transaksi, aset, tanggal) dirujuk lewat fixture itu.
- Suite berjalan serial (`parallel: false`) karena spec memakai data Pre-setup bersama yang diubah job dan dipulihkan fixture BE, yang memengaruhi spec lain.
- Tabel "Event TC-FA-NOTIF-287 dan 288" (urutan baris = urutan iterasi; semua item actionable):

  | TC | Event | State | Job pemicu | Title | Body | Icon, severity | Tombol | Klik | Path tujuan |
  |---|---|---|---|---|---|---|---|---|---|
  | TC-FA-NOTIF-287 | `damaged_reminder` | AST-2024-0141 tiket Damaged belum selesai, pengingat Damaged aktif, interval tercapai | `F-FATX-11` (pengaturan pengingat Damaged aktif, tiket belum selesai, selisih hari sejak pelaporan atau pengingat terakhir ≥ interval pengingat Damaged) | `Damaged asset is still unresolved` | `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/asset/detail/AST-2024-0141` |
  | TC-FA-NOTIF-288 | `missing_reminder` | AST-2024-0067 tiket Missing belum selesai, pengingat Missing aktif, interval tercapai | `F-FATX-11` (pengaturan pengingat Missing aktif, tiket belum selesai, interval tercapai) | `Missing asset is still under investigation` | `Laptop - 1 (AST-2024-0067) has not been found yet.` | `time-line`, `warning` | actionable: `[Detail]` tampil tanpa `[Mark as Read]` | `[Detail]` | `/fams/asset/detail/AST-2024-0067` |

- Tabel "Event TC-FA-NOTIF-408 dan 409" (penerima PIC aset; urutan baris = urutan iterasi):

  | TC | Event | State | Title | Body |
  |---|---|---|---|---|
  | TC-FA-NOTIF-408 | `damaged_reminder` | AST-2024-0141 tiket Damaged belum selesai, pengingat Damaged aktif, interval tercapai | `Damaged asset is still unresolved` | `Kamera DSLR (AST-2024-0141) is still waiting to be repaired.` |
  | TC-FA-NOTIF-409 | `missing_reminder` | AST-2024-0067 tiket Missing belum selesai, pengingat Missing aktif, interval tercapai | `Missing asset is still under investigation` | `Laptop - 1 (AST-2024-0067) has not been found yet.` |


## Test Steps


### TC-FA-NOTIF-287 dan TC-FA-NOTIF-288: reminder diterima Group Manager

1. Untuk setiap baris tabel "Event TC-FA-NOTIF-287 dan 288" (langkah 1 sampai 16): pulihkan seed lewat fixture BE pemulih, siapkan state transaksi atau aset baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
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

### TC-FA-NOTIF-408 dan TC-FA-NOTIF-409: reminder diterima PIC aset

17. Ganti akun: Logout, lalu login sebagai Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`)
18. Buka halaman Fixed Asset > Dashboard
19. Untuk setiap baris tabel "Event TC-FA-NOTIF-408 dan 409" (langkah 19 sampai 23): pulihkan seed lewat fixture BE pemulih, siapkan state baris itu lewat fixture BE penyetel state sumber, lalu muat ulang halaman Fixed Asset > Dashboard
20. Jalankan job `F-FATX-11` lewat kemampuan job latar hingga selesai
21. Klik Bell icon sebagai PIC aset
22. Verifikasi item ber-Title dan Body sesuai kolom Title dan Body baris itu diterima PIC aset
23. Verifikasi item itu menampilkan tombol `[Detail]` (actionable)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 16 diulang untuk dua baris tabel "Event TC-FA-NOTIF-287 dan 288" dan langkah 19 sampai 23 untuk dua baris tabel "Event TC-FA-NOTIF-408 dan 409" (44 langkah setelah ekspansi). Rujukan nomor langkah memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang sekitar 35 langkah (dihitung dengan ekspansi, 44 langkah): semua blok satu kelas (job terjadwal pengingat, kelas d) dan tiap iterasi berdiri sendiri dengan seed dipulihkan; kegagalan satu event tidak membuat event lain kehilangan makna.
- Reminder Damaged dan Missing diterima Group Manager dan PIC aset berbagi dataset aset Pre-setup #24; keduanya satu spec karena job (`F-FATX-11`), kelas harness, dan pemulihan seed sama, dan hanya akun penerima yang berbeda.
- Langkah penghubung (S-03): langkah 1 dan 19 (pemulihan seed dan penyiapan state); langkah kembali ke Fixed Asset > Dashboard dan membuka Bell icon di blok pertama (untuk mengamati status baca); Ganti akun dan pembukaan Dashboard sebelum blok kedua; langkah "Catat jumlah badge Bell icon" (baseline S-12). Kolom Klik tabel menentukan kontrol yang diklik.
- TC-FA-NOTIF-408 dan 409 tidak memuat Expected badge bertambah atau posisi teratas; spec tidak menambahkannya.
- Tidak ada butir `P-n`.
- Temuan untuk QA:
  - TC-FA-NOTIF-408 dan 409 menyebut "PIC aset" (Asset Admin) tanpa nomor Pre-setup; spec memakai Pre-setup #8. Email akun PIC aset tidak tertulis eksplisit di TC.
  - Langkah TC 287 dan 288 berakhir pada klik `[Detail]`; asersi "tanpa mengubah status baca" membutuhkan pengamatan setelah navigasi, sehingga spec menambah langkah kembali dan membuka Bell icon (langkah penghubung).
  - TC-FA-NOTIF-408 dan 409 tidak menyebut Title bold atau dot Unread dan tidak punya langkah klik `[Detail]`; spec hanya mengasersi item dan tombol yang disebut TC.
  - Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
