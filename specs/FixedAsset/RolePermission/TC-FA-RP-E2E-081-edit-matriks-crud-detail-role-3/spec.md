---
id: TC-FA-RP-E2E-081-edit-matriks-crud-detail-role-3
title: "Edit matriks CRUD Detail Role (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-277
  - TC-FA-RP-278
coverage:
  web: automated
---

# Edit matriks CRUD Detail Role (3/3)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD` (sesi API pelaku kedua). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Pelaku kedua: pada TC-FA-RP-277 Sesi 2 adalah sesi API Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`, yang hanya memicu perubahan state dan hasilnya tidak diasersi di sesinya.
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Data Pre-setup: pool #15 (Ahmad Fauzi) dan #18. Ahmad Fauzi memegang dengan hanya Read aktif: Global Role `Manage accounting`; Group Role `Manage group` di `Data Center` dan di `Helpdesk`. Disiapkan lewat seed API di hook `before` dan sebagai langkah penghubung (langkah 9).
- Kemampuan teknis: pembacaan state backend lewat fixture BE (disediakan tim FE/BE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Ahmad Fauzi `Manage accounting` dan `Manage group`), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-277: Edit CRUD atas baris yang sudah dihapus admin lain

1. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
2. Verifikasi baris Ahmad Fauzi tampil di Detail Role `Manage accounting`
3. Sesi 2 (sesi API Total Control Rina Wulandari) meng-Remove baris Ahmad Fauzi pada Detail Role `Manage accounting` hingga penghapusan tersimpan
4. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
5. Di Sesi 1, centang Create pada baris Ahmad Fauzi
6. Verifikasi muncul toast netral: `This permission is no longer available.`
7. Verifikasi tabel di-refresh dan baris Ahmad Fauzi tidak ada
8. Verifikasi tidak ada perubahan tersimpan: penugasan `Manage accounting` Ahmad Fauzi tidak ada di backend (dibaca lewat fixture BE)

### TC-FA-RP-278: Edit CRUD pada Group Role (Manage group) tersimpan per baris node

9. Pulihkan state lewat seed API: Ahmad Fauzi memegang Group Role `Manage group` di `Data Center` dan di `Helpdesk` dengan hanya Read aktif
10. Klik Tab `System`, klik Role Name `Manage group` pada section Group Role
11. Klik `All Groups` di Sidebar Group Tree
12. Centang Create pada baris Ahmad Fauzi di `Data Center`
13. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
14. Verifikasi hanya baris `Data Center` yang berubah: Create tercentang
15. Verifikasi baris `Helpdesk` tetap: Create tidak tercentang

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-277, TC-FA-RP-278).
- Langkah penghubung (S-03): membuka Tab System dan Detail Role (langkah 1 dan 10); pemulihan state seed (langkah 9); "Tunggu aksi selesai" pada langkah 4 karena aktor berpindah sesi setelah aksi tanpa asersi (bagian 8b butir 8).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` baris Ahmad Fauzi tampil (langkah 2) sebagai pembuktian "melihat baris" pada langkah uji pertama TC-FA-RP-277.
- Pembagian TC lintas spec: TC-FA-RP-276 (dua sesi UI Total Control yang diasersi, kelas c) ada di spec 296. Pada TC-FA-RP-277 Sesi 2 hanya pemicu state lewat sesi API.
- Temuan untuk QA:
  - TC-FA-RP-277 dan TC-FA-RP-278 tidak menyebut keadaan awal Create pada baris Ahmad Fauzi; spec mengasumsikan hanya Read aktif.
  - TC-FA-RP-277 menyebut "dua sesi Total Control" tanpa akun sesi kedua; spec memakai Total Control kedua Pre-setup #3 (Rina Wulandari).
  - Pada TC-FA-RP-277 "tidak ada perubahan tersimpan" tidak punya langkah observasi di TC; spec mengamatinya lewat fixture BE (kemampuan disediakan tim FE/BE).
