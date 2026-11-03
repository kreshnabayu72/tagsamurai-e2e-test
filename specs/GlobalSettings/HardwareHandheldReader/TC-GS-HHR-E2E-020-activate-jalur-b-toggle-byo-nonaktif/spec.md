---
id: TC-GS-HHR-E2E-020-activate-jalur-b-toggle-byo-nonaktif
title: "Aktivasi Jalur B saat Toggle Self-Purchased Device Activation Nonaktif: Ditolak saat Sync, Pulih dengan Reader Stok, dan Ditolak saat Submit setelah Toggle Dimatikan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-75
  - TC-GS-HHR-76
  - TC-GS-HHR-473
coverage:
  web: automated
---

# Aktivasi Jalur B saat Toggle Self-Purchased Device Activation Nonaktif: Ditolak saat Sync, Pulih dengan Reader Stok, dan Ditolak saat Submit setelah Toggle Dimatikan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state tenant (toggle `Allow Self-Purchased Device Activation` Client A dimatikan di langkah 31), membuat reader di Client B, memakai simulator USB bersama, dan berganti akun antar Client.
- Akun aktor:

  | Blok | Client | Kondisi | Akun | Env var password |
  |---|---|---|---|---|
  | TC-GS-HHR-75, TC-GS-HHR-76 | Client B | Plan Growth, toggle `Allow Self-Purchased Device Activation` nonaktif, `Long Range` kuota 3 tersedia, belum ada reader | Total Control Client B `totalControl_automated_qaTeam2@qwertysystem.net` | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |
  | TC-GS-HHR-473 | Client A | Plan Growth, toggle aktif, Seed Reader A DD-01 s.d. DD-10 | Total Control Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
  | TC-GS-HHR-473 (pemicu) | Admin Console | memutuskan toggle BYO Client A | Principal Bambang Hartono `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, sesi API | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

  Login Client B di hook `before`; ganti akun ke Client A di langkah 18 sampai 20; hook `after` mengembalikan sesi ke akun default suite (Client A, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > Hardware > Handheld Reader dibuka hook `beforeEach` untuk akun hook `before`; langkah 20 membukanya sesudah ganti akun.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`), termasuk akun Client B.
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`): Serial `SN-HHR-00302` (di luar stok Principal) dan Hardware Stock Principal HS-01 (`SN-HHR-00201`, Long Range, Zebra/RFD40, Current Power 22 dBm, Device Name bawaan `Zebra RFID Reader - 2`); Katalog Device Name Client A memuat DN-01 s.d. DN-07 (`Chainway C72` dipakai di TC-GS-HHR-473). Event Log Client A tidak dipulihkan dan spec lain menambah baris `Chainway C72` (audit trail permanen), sehingga baris seed (EL-02) tidak dibaca di spec ini: langkah 43 memakai pembanding generik yang tidak bergantung pada posisi atau halaman; jumlah total baris Event Log tidak diasersi (S-12). Client A dipulihkan fixture backend ke Seed Reader A (10 reader, pagination `Showing 1 - 10 of 10 readers`) sebelum spec.
- Efek spec dan pemulihan: langkah 15 membuat reader `Zebra RFID Reader - 2` di Client B dan mengubah unit HS-01 menjadi `In Use`; langkah 31 mematikan toggle BYO Client A. Hook `after` memulihkan Client B (menghapus reader, HS-01 ke `Available`) dan menyalakan kembali toggle BYO Client A lewat sesi API Principal walau spec gagal di tengah (mekanisme pemulihan disediakan tim FE/BE).
- Kemampuan teknis:
  - Simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) yang menyajikan reader `SN-HHR-00302`, mengganti reader (cabut lalu sambungkan `SN-HHR-00201`), dan menyajikan Current Power sesuai stok. TC-GS-HHR-75, TC-GS-HHR-76, dan TC-GS-HHR-473 berlabel Manual Only (b) (TC-GS-HHR-473 juga (d), dua sesi).
  - Sesi API Principal (pelaku kedua yang hanya memicu state) yang mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` Client A hingga tersimpan; endpoint tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA). Sesi API aktor tidak dihitung sebagai sesi web; lihat `suite.md`.
  - Pembacaan jumlah total baris popup Event Log Activate dan hasil Search-nya (baseline, S-12).
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Client B, toggle Client A, dan simulator; tutup popup yang masih terbuka; kembalikan sesi ke akun default.

## Test Steps

### TC-GS-HHR-75: Toggle BYO nonaktif, serial di luar stok ditolak saat Sync (Client B)

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader dengan Serial Number `SN-HHR-00302` (di luar stok Principal) lewat simulator reader USB
4. Klik `[Sync]`
5. Verifikasi state `Ditolak server` tampil inline dengan pesan `Self-purchased device activation is not enabled for your account.`
6. Verifikasi popup tetap terbuka
7. Verifikasi `Serial Number` `SN-HHR-00302` tampil read-only
8. Verifikasi `[Submit]` disabled
9. Verifikasi `[Sync]` tetap aktif
10. Verifikasi `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil

### TC-GS-HHR-76: Setelah penolakan, Sync reader yang terdaftar di stok berhasil diaktifkan (Client B)

11. Cabut reader pertama, lalu sambungkan reader dengan Serial Number `SN-HHR-00201` (stok Principal, HS-01) lewat simulator reader USB
12. Klik `[Sync]`
13. Verifikasi label `Official` tampil
14. Verifikasi `[Submit]` enabled
15. Klik `[Submit]`
16. Verifikasi baris `Zebra RFID Reader - 2` tampil dengan `Status` `Available`
17. Verifikasi tabel hanya memuat satu baris `Zebra RFID Reader - 2` (tidak ada record dari penolakan `SN-HHR-00302`)

### Ganti akun ke Client A

18. Logout dari akun Total Control Client B
19. Login sebagai Total Control Sari Dewi (Client A, `Spectra.env.GS_TC_PASSWORD`)
20. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-473: Toggle BYO dimatikan setelah Sync Jalur B berhasil, Submit ditolak (Client A)

21. Klik ikon Event Log
22. Ketik Search `Chainway C72`, tekan Enter
23. Catat jumlah baris hasil Search popup Event Log Activate sebagai baseline
24. Klik `[✕]` di header popup Event Log
25. Klik `[+ Activate Reader]`
26. Klik `Long Range` pada Overlay `Select Range Type`
27. Sambungkan reader dengan Serial Number `SN-HHR-00302` (di luar stok Principal) lewat simulator reader USB
28. Klik `[Sync]`
29. Pilih `Chainway C72` pada `Device Name`, isi `Brand` dengan `Chainway`
30. Isi `Model/Type` dengan `C72`
31. Pada sesi API Principal, matikan toggle `Allow Self-Purchased Device Activation` untuk Client A hingga perubahan tersimpan
32. Tunggu aksi selesai
33. Klik `[Submit]`
34. Verifikasi pesan inline `Self-purchased device activation is not enabled for your account.` tampil
35. Verifikasi popup tetap terbuka
36. Verifikasi input dipertahankan: `Device Name` `Chainway C72`, `Brand` `Chainway`, dan `Model/Type` `C72`
37. Klik `[✕]` di header popup
38. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
39. Klik `[Cancel Activation]`
40. Verifikasi pagination `Showing 1 - 10 of 10 readers` (tidak ada reader baru di daftar reader)
41. Klik ikon Event Log
42. Ketik Search `Chainway C72`, tekan Enter
43. Verifikasi sedikitnya satu baris tampil pada hasil Search `Chainway C72` (pembanding generik, tidak bergantung pada posisi atau halaman)
44. Verifikasi jumlah baris hasil Search sama dengan baseline pada langkah 23 ditambah satu
45. Verifikasi terdapat baris dengan Result `Failed`, Range Type `Long Range`, Device Name `Chainway C72`, dan PIC `Sari D`
46. Klik `[✕]` di header popup Event Log

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB, ditambah state tenant (toggle BYO) pada TC-GS-HHR-473. `P-7`: TC-GS-HHR-473 inheren membutuhkan simulator reader USB (`[Sync]` Jalur B, kelas d) bersama konteks lain kelas h (state tenant: toggle BYO Client A dimatikan sesi API Principal di tengah alur), dan berada satu spec dengan TC-GS-HHR-75 dan 76 yang sejenis (toggle BYO nonaktif, juga memakai simulator USB); tidak ada blok non-USB di spec ini yang perlu dipisah. Dua Client dalam satu spec dengan Step ganti akun eksplisit (langkah 18 sampai 20); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (46 langkah). Alasan: 18 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01), dan TC-GS-HHR-473 mengulang prefix aktivasi dan membaca Event Log dengan baseline; blok Client B (langkah 1 sampai 17) dan blok Client A (langkah 21 sampai 46) berdiri sendiri dengan Step ganti akun, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-GS-HHR-75 dan TC-GS-HHR-76 berbagi satu popup (satu pembukaan): TC-GS-HHR-76 melanjutkan dari state penolakan TC-GS-HHR-75 (langkah 3 TC-GS-HHR-76 identik dengan langkah 4 TC-GS-HHR-75). Asersi "tidak ada record dibuat" (TC-GS-HHR-75 Expected a) diamati pada langkah 17 sesudah aktivasi sukses TC-GS-HHR-76, karena tabel di belakang popup tidak diamati selama popup terbuka; langkah 16 menjadi anchor positif bagi asersi universal langkah 17.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 11, 27 (menyiapkan reader di simulator); langkah 18 sampai 20 (ganti akun dan buka halaman); langkah 21 sampai 24 (baseline Event Log, S-12); langkah 22 dan 42 (Search untuk menemukan baris target); langkah 37 sampai 39 (menutup popup yang berisi hasil Sync lewat dialog `Cancel Activation`, S-08; popup tetap berisi hasil Sync sesudah penolakan saat `[Submit]`; teks dialog dari Expected TC-GS-HHR-89); langkah 46 (menutup popup Event Log); langkah 32 (Tunggu aksi selesai: hasil penyimpanan toggle lewat sesi API tidak diasersi, langkah berikutnya `[Submit]` di sesi UI).
- Asersi jumlah baris Event Log (langkah 44) memakai baseline hasil Search `Chainway C72` dengan anchor positif langkah 43 (sedikitnya satu baris hasil Search); asersi daftar reader (langkah 40) memakai jumlah Seed Reader A sebagai baseline karena Client A dipulihkan ke Seed Reader A sebelum spec. Langkah 43 adalah `Verifikasi` tambahan di luar Expected TC-GS-HHR-473 yang berfungsi sebagai anchor; wording generik dipilih karena baris seed EL-02 (bertanggal Juni) dapat bergeser ke halaman berikutnya di bawah baris `Chainway C72` yang ditambah spec lain (S-14).
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (penyajian serial, pergantian reader, Current Power) dan mekanisme Principal mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` Client A tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint.
  - TC-GS-HHR-473 menyebut "sesi kedua" Principal; sesuai konvensi pelaku kedua yang hanya memicu state memakai sesi API, bukan sesi UI. Bila QA menghendaki sesi UI kedua, spec perlu diubah.
  - TC-GS-HHR-473 Expected c menyebut "satu baris `Failed` baru" tanpa kolom pembeda baris baru dari baris `Failed` run sebelumnya; spec memakai selisih jumlah baris hasil Search sebagai penanda baris baru (langkah 44) dan mengasersi atribut baris pada langkah 45.
  - TC-GS-HHR-473 tidak menyatakan state Event Log Activate lain yang ikut berubah; baseline hanya untuk hasil Search `Chainway C72`.
  - TC-GS-HHR-75 Expected a ("tidak ada record dibuat") tidak dapat diamati selama popup terbuka; spec mengamatinya pada langkah 17.
