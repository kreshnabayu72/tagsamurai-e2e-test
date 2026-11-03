---
id: TC-FA-SU-E2E-025-aktor-read-only-tab-role-read-only-dan-akses-detail-pengguna-di-luar-fams
title: "Aktor Read Only: Tab Role Read-only dan Akses Tab Informasi Detail Pengguna"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-82
  - TC-FA-SU-83
coverage:
  web: automated
---

# Aktor Read Only: Tab Role Read-only dan Akses Tab Informasi Detail Pengguna

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Read Only (Citra Lestari, Pre-setup #3, `readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Nama env `FA_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Role yang diuji: hanya Read Only (Citra Lestari); tidak ada ganti akun.
- Tabel "Target tier" (TC-FA-SU-82, langkah 11 sampai 16): Ahmad Dahlan (Default User), Lina Marlina (Total Control), Citra Lestari (Read Only).
- Tabel "Tab informasi" (TC-FA-SU-83, langkah 20 sampai 22): Responsibilities, Non-Login User, Changelog, System Log, Transaction Admin Log, User Log.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20), tier dan penugasan (#23), Responsibilities Budi Santoso (#24 dan #25), Non-Login User Budi Santoso (#26), Changelog (#27), System Log (#28), Transaction Admin Log (#29), User Log (#30). Target Detail: Budi Santoso (Group Role Manage group pada Finance & Accounting).
- Data Dinamis: tidak ada.
- Kemampuan teknis: hover elemen.
- State global: tidak ada yang diubah; data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-82: Tab Role Read Only, switch dan CRUD Disabled, `[Detail]` tetap tersedia

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
3. Hover switch Global Role dan checkbox C/R/U/D
4. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You don't have permission to edit.`
5. Buka Sub-tab Group Role
6. Verifikasi `[Detail]` pada baris Group Role Show Enabled
7. Verifikasi `[Assign Group]` Hidden
8. Klik `[Detail]` pada baris Group Role Manage group
9. Verifikasi Popup Detail Group Assignment terbuka dan read-only
10. Tutup Popup Detail Group Assignment dengan ✕

Untuk setiap target pada tabel "Target tier" di `## Prerequisites` (Ahmad Dahlan, Lina Marlina, lalu Citra Lestari), jalankan langkah 11 sampai 16.

11. Buka Settings > User dari sidebar
12. Ketik Search nama target, tekan Enter
13. Buka Detail target lalu Tab Role (Sub-tab Group Role)
14. Klik `[Detail]` pada baris Group Role
15. Verifikasi Popup Detail Group Assignment target terbuka dan read-only
16. Tutup Popup Detail Group Assignment dengan ✕

### TC-FA-SU-83: Akses langsung Detail oleh aktor Read Only, tab informasi dapat dibaca

17. Buka Settings > User dari sidebar
18. Ketik Search `Budi Santoso`, tekan Enter
19. Buka Detail Budi Santoso

Untuk setiap tab pada tabel "Tab informasi" di `## Prerequisites`, jalankan langkah 20 sampai 22.

20. Klik tab informasi
21. Verifikasi sedikitnya satu baris data tampil pada tab informasi
22. Verifikasi tidak ada tombol aksi tulis pada tab informasi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec memuat satu aktor (Read Only) sehingga tidak ada ganti akun; ditulis sebagai spec Role Matrix untuk satu role.
- Langkah yang diulang: langkah 11 sampai 16 untuk tiga target (ekspansi +12) dan langkah 20 sampai 22 untuk enam tab (ekspansi +15); parameter ada di tabel `## Prerequisites`. Spec 22 langkah nominal, 49 langkah dengan ekspansi, melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Role Matrix Read Only, hanya membaca), kedua TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan ekspansi berasal dari parameter tabel, bukan langkah berbeda.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 1, 12, 18 (R-16); langkah 10 dan 16 (menutup popup); langkah 11 dan 17 (membuka Settings > User).
- Langkah 6 adalah anchor positif untuk asersi Hidden langkah 7 (bagian 8b butir 2). Langkah 21 adalah anchor positif untuk asersi langkah 22.
- Temuan untuk QA:
  - TC-FA-SU-83 berjudul "Akses langsung Detail oleh aktor Read Only ke pengguna di luar FAMS", tetapi langkah dan Expected hanya membaca tab informasi Budi Santoso (pengguna FAMS); tidak ada pengguna di luar FAMS di Data Uji. Spec mengikuti langkah TC.
  - TC-FA-SU-83 Expected b ("Tidak ada aksi tulis pada tab tersebut") tidak menyebut kontrol yang diamati; spec mengasersi tidak adanya tombol aksi tulis secara umum (langkah 22). QA perlu mendaftar kontrol tulis per tab agar asersi dapat dibuat spesifik.
  - TC-FA-SU-82 Expected b menyebut `[Detail]` terbuka "termasuk pada target Default User, Total Control, dan Read Only"; Pre-setup #23 tidak menyebut baris Group Role untuk ketiga tier, sehingga langkah 13 dan 14 bergantung pada baris Group Role yang tampil pada target itu.
  - Email dan nama env password Read Only tidak diberi nama env di TC; nama `FA_RO_PASSWORD` diusulkan.
