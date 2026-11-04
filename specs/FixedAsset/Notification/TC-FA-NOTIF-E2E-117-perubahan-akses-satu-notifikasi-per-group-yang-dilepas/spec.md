---
id: TC-FA-NOTIF-E2E-117-perubahan-akses-satu-notifikasi-per-group-yang-dilepas
title: "Penerimaan Notifikasi Perubahan Akses Group Manager: Satu Notifikasi per Group yang Dilepas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-323
  - TC-FA-NOTIF-414
coverage:
  web: automated
---
# Penerimaan Notifikasi Perubahan Akses Group Manager: Satu Notifikasi per Group yang Dilepas

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Citra Lestari (target perubahan akses) | #14 | `targetCitra_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TARGETCITRA_PASSWORD` | `Fixture.fixedAssetNotification.targetCitra` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Total Control (Admin Alpha) (Pre-setup #1, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Memberi Total Control dan Edit CRUD peran individual Citra Lestari.
- Login akun aktor pertama (Citra Lestari (target perubahan akses), Pre-setup #14) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): Citra Lestari (Pre-setup #14, target perubahan akses; pemegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A); Admin Alpha Pre-setup #1 (aktor, nama tampil pada Body). Peran Citra (Total Control, Read Only, Group Manager) diatur lewat fixture BE pada langkah penyiapan tiap blok; pemulihan di hook `before` dan `after`. Pada kedua blok Citra Lestari Group Manager Gedung A dan Gedung B.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu perubahan state akun Pre-setup #14 (Citra Lestari): pemberian akses Total Control (butir (iii)) dan Edit CRUD peran individual, milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10); format tanggal item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TARGETCITRA_PASSWORD`, `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-323: access_group_manager_removed mengirim satu notifikasi per group yang dilepas

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari Group Manager Gedung A dan Gedung B, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), beri Total Control kepada Citra Lestari sehingga penugasan Group Manager dilepas otomatis hingga perubahan tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Citra Lestari bertambah 2 dari baseline langkah 2 (satu notifikasi per group)
6. Verifikasi item `"You are no longer Group Manager for Gedung A"` tampil sebagai notifikasi terpisah
7. Verifikasi item `"You are no longer Group Manager for Gedung B"` tampil sebagai notifikasi terpisah

### TC-FA-NOTIF-414: access_group_manager_auto_reverted mengirim satu notifikasi per group yang dilepas

8. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Citra Lestari Group Manager Gedung A dan Gedung B, lalu muat ulang halaman Fixed Asset > Dashboard
9. Catat jumlah pada badge Bell icon Citra Lestari sebagai baseline (0 bila badge tidak tampil)
10. Dari akun Admin Alpha (Total Control, Pre-setup #1, sesi API), Edit CRUD peran individual Citra Lestari sehingga menyimpangkan pola Group Manager hingga perubahan tersimpan
11. Klik Bell icon
12. Verifikasi badge Bell icon Citra Lestari bertambah 2 dari baseline langkah 9 (satu notifikasi per group)
13. Verifikasi item `"You are no longer Group Manager for Gedung A"` dengan Body `"Admin Alpha removed your Group Manager status for Gedung A on 18/06/26."` tampil sebagai notifikasi terpisah
14. Verifikasi item `"You are no longer Group Manager for Gedung B"` dengan Body `"Admin Alpha removed your Group Manager status for Gedung B on 18/06/26."` tampil sebagai notifikasi terpisah

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor; asersi hanya pada Bell icon dan Dropdown Panel.
- Langkah penghubung (S-03): langkah 1, 8 (penyiapan kondisi data lewat fixture BE); langkah 2, 9 (pencatatan baseline badge Bell icon (S-12)). Muat ulang halaman pada langkah 8 menutup Dropdown Panel blok sebelumnya (Bell icon adalah toggle) dan menyegarkan badge sebelum baseline langkah 9 (S-14).
- Spec 117 memuat satu notifikasi per group yang dilepas atas Citra Lestari yang juga dipakai spec 069 sampai 072; dibedakan karena dua penugasan Group Manager (Gedung A dan B) harus diatur ulang fixture BE di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-323 menulis Expected dua Title tanpa Body; spec hanya mengasersi Title. Selisih badge 2 dari baseline ditambahkan sebagai bukti "dua notifikasi terpisah" (S-03).
