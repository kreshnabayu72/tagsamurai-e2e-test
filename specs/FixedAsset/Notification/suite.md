---
name: Fixed Asset Notification
id: suite-fixed-asset-notification
description: Spec e2e turunan tc-notification.md untuk Fixed Asset > Notification
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Notification

Suite ini mencakup Notification Center pada Fixed Asset: Bell icon dan badge, Dropdown Panel, Notification Center (Tab All dan Unread, Search, Filter, Sort, infinite scroll), Guided Tooltip `fa-notification`, tampilan Android, aksi Mark as Read dan `[Detail]` (pre-check, dialog D-01), Auto-Read notifikasi task-oriented, dedup multi-role, real-time SSE, akses per role, penerimaan event dari modul sumber (Borrow, Assignment, Transfer, Disposal, Damaged, Missing, Audit, Settings > Role & Permission, License, Tag), notasi jamak, resolusi penerima kasus tepi, job terjadwal dan aturan waktunya, pencatatan (absence Activity Log), state tenant, defense-in-depth, multi-konteks, dan resilience.

`parallel: false` karena spec mengubah atau bergantung pada state global: jam server dan jam fixture (job terjadwal, tanggal hari ini 18/06/26), Date Format dan zona waktu General Settings, status Client (Suspended, Expired), Total Asset License dan penanda tingkat peringatan kuota, flag Guided Tooltip, serta seed notifikasi, transaksi, dan state akun dan client Pre-setup (rentang pemulih di butir Fixture BE pemulih) yang dipulihkan antar TC. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

Pernyataan hook dan kemampuan suite (dinyatakan sekali di sini; `## Prerequisites` tiap spec merujuknya dengan satu baris):

- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir; disediakan tim BE/FE. Pelaku kedua yang hanya memicu perubahan state di modul sumber memakai sesi ini.
- Login akun aktor pertama spec di hook `before` spec itu (akun dibaca dari `## Prerequisites`); hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1). Halaman Fixed Asset > Dashboard dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification`: hook `before` menyetelnya true untuk akun aktor spec (semua akun Pre-setup #1 sampai #36 sudah true kecuali #31) dan hook `after` memulihkannya. Spec Guided Tooltip yang menguji flag itu (akun #31) menulis pengecualiannya dan mengatur flag sendiri.
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #16 sampai #25, #34, #37, #38, status client, peran akun #1, #5, #8, status akun #11 dan #12, akses akun #14, dan flag Guided Tooltip akun #31; #16 dipulihkan ke keadaan tanpa notifikasi): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC dalam satu spec, karena TC dijalankan pada fixture yang dipulihkan ke Pre-setup (Catatan TC). Disediakan tim FE/BE (idempotent); efeknya dicatat di `## Prerequisites` spec yang bersangkutan.
- Fixture BE penukar varian seed #18 (tepat 99 Unread, semua Read, tepat 1 Unread view-only, umur 30 detik sampai lebih dari 7 hari, N-38 sampai N-41, dua notifikasi terbaru Read) dan varian #17 (N-01 sampai N-07 atau N-01 sampai N-37): menukar satu varian per blok TC lewat langkah penghubung eksplisit; disediakan tim FE/BE; endpoint tidak dikarang.
- Fixture BE pemicu event dan penyetel state sumber: transaksi Borrow, Assignment, Transfer, Disposal, tiket Damaged dan Missing, task Audit, perubahan akses Role & Permission, laporan Tag, Total Asset License dan penanda tingkat (Pre-setup #34), serta status aktif atau nonaktif Borrower dan Assignee (#11, #12). Disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan menjalankan job latar (`F-FATX-07`, `F-FATX-10`, `F-FATX-11`, `F-ASSIGN-11` auto-cancel Waiting for Acceptance, job transit overdue Transfer, scheduler harian audit, job penilaian kuota), mengkueri status job (penanda pemicu selesai, bukan anchor absence), dan menggeser jam server dan jam fixture: sesi UI dan sesi API aktor tetap valid selama jam digeser, jam dipulihkan di hook `after`, dan asersi memakai jumlah entri atau badge terhadap baseline.
- Fixture BE kegagalan: pemaksaan kegagalan insert notifikasi (global atau untuk satu transaksi) dan pemulihannya, serta pemanggilan ulang pembuatan notifikasi dengan identitas event yang sama; disediakan tim FE/BE.
- Fixture BE status client Suspended dan Expired (sesi UI tetap terbuka; status diubah sesudah sesi dibuka) dan pemulihannya di `after`.
- Intercept respons HTTP dan SSE pada browser (`Spectra.intercept()`) untuk menahan atau memaksa 5xx, timeout, dan 403 di atas backend nyata; dilepas segera setelah pemicu selesai (pengecualian: intercept SSE pemicu state basi boleh ditahan sampai akhir blok TC yang membutuhkannya, konvensi P-2 2026-11-04).
- Kemampuan membaca status respons HTTP di browser (403 dan 409, spec 022 dan 030) dan fixture BE yang mencabut serta memulihkan Transaction Role Approver akun aktor (spec 030); disediakan tim FE/BE.
- Kemampuan membaca jumlah entri Activity Log sebelum aksi (baseline, S-12) disediakan tim FE/BE untuk spec absence 055.
- Spec Android (013, 014, dan TC Android lain) membutuhkan perangkat atau emulator Android dengan aplikasi native dan memakai `coverage.mobile`; perangkat fisik bersama menulis `parallel: false` di `## Prerequisites`.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A) berlaku untuk suite ini: seed notifikasi, transaksi, state akun dan client Pre-setup bersama (butir A-16 (i)-(iii), yang daftarnya dinyatakan lengkap di Lampiran A) boleh menjadi pemicu atau target aksi tulis karena pemulihannya dijamin Fixture BE yang disediakan tim FE/BE, suite berjalan serial.
- Password akun aktor lewat env var `FA_<ROLE>_PASSWORD` (`Spectra.env.*`), didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
