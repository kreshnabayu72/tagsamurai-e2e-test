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
  | TC-GS-HHR-75, TC-GS-HHR-76 | Client B | Plan Growth, toggle `Allow Self-Purchased Device Activation` nonaktif, `Long Range` kuota 3 tersedia, belum ada reader | Total Control Client B (disediakan tim FE; pola email `totalControl_automated_{namaClient}@qwertysystem.net`, nilai `{namaClient}` dari fixture baru `fixtures/hardwareHandheldReader.json`) | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |
  | TC-GS-HHR-473 | Client A | Plan Growth, toggle aktif, Seed Reader A DD-01 s.d. DD-10 | Total Control Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
  | TC-GS-HHR-473 (pemicu) | Admin Console | memutuskan toggle BYO Client A | Principal Bambang Hartono `principal_automated_qaTeam1@qwertysystem.net`, sesi API (P-2) | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

  Login Client B di hook `before`; ganti akun ke Client A di langkah 18 sampai 20; hook `after` mengembalikan sesi ke akun default suite (Client A, `GS_TC_PASSWORD`). `GS_CLIENTB_TC_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner. Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > Hardware > Handheld Reader dibuka hook `beforeEach` untuk akun hook `before`; langkah 20 membukanya sesudah ganti akun.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`), termasuk akun Client B.
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`): Serial `SN-HHR-00302` (di luar stok Principal) dan Hardware Stock Principal HS-01 (`SN-HHR-00201`, Long Range, Zebra/RFD40, Current Power 22 dBm, Device Name bawaan `Zebra RFID Reader - 2`); Katalog Device Name Client A memuat DN-01 s.d. DN-07 (`Chainway C72` dipakai di TC-GS-HHR-473). Client A dipulihkan fixture backend ke Seed Reader A (10 reader, pagination `Showing 1 - 10 of 10 readers`) sebelum spec.
- Efek spec dan pemulihan: langkah 15 membuat reader `Zebra RFID Reader - 2` di Client B dan mengubah unit HS-01 menjadi `In Use`; langkah 31 mematikan toggle BYO Client A. Hook `after` memulihkan Client B (menghapus reader, HS-01 ke `Available`) dan menyalakan kembali toggle BYO Client A lewat sesi API Principal walau spec gagal di tengah (mekanisme pemulihan disediakan tim FE/BE).
- Kemampuan teknis:
  - Simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) yang menyajikan reader `SN-HHR-00302`, mengganti reader (cabut lalu sambungkan `SN-HHR-00201`), dan menyajikan Current Power sesuai stok. TC-GS-HHR-75, TC-GS-HHR-76, dan TC-GS-HHR-473 berlabel Manual Only (b) (TC-GS-HHR-473 juga (d), dua sesi).
  - Sesi API Principal (konteks kedua) yang mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` Client A hingga tersimpan; endpoint tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
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
32. Klik `[Submit]`
33. Verifikasi pesan inline `Self-purchased device activation is not enabled for your account.` tampil
34. Verifikasi popup tetap terbuka
35. Verifikasi input dipertahankan: `Device Name` `Chainway C72`, `Brand` `Chainway`, dan `Model/Type` `C72`
36. Klik `[✕]` di header popup, lalu klik `[Cancel Activation]` pada dialog
37. Verifikasi pagination `Showing 1 - 10 of 10 readers` (tidak ada reader baru di daftar reader)
38. Klik ikon Event Log
39. Ketik Search `Chainway C72`, tekan Enter
40. Verifikasi sedikitnya satu baris pembanding tampil: baris seed `Chainway C72 - 1` dengan Result `Waiting for Approval`
41. Verifikasi jumlah baris hasil Search sama dengan baseline pada langkah 23 ditambah satu
42. Verifikasi terdapat baris dengan Result `Failed`, Range Type `Long Range`, Device Name `Chainway C72`, dan PIC `Sari D`
43. Klik `[✕]` di header popup Event Log

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB, ditambah state tenant (toggle BYO) pada TC-GS-HHR-473. Dua Client dalam satu spec dengan Step ganti akun eksplisit (langkah 18 sampai 20); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (43 langkah). Alasan: 17 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01), dan TC-GS-HHR-473 mengulang prefix aktivasi dan membaca Event Log dengan baseline; blok Client B (langkah 1 sampai 17) dan blok Client A (langkah 21 sampai 43) berdiri sendiri dengan Step ganti akun, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-GS-HHR-75 dan TC-GS-HHR-76 berbagi satu popup (satu pembukaan): TC-GS-HHR-76 melanjutkan dari state penolakan TC-GS-HHR-75 (langkah 3 TC-GS-HHR-76 identik dengan langkah 4 TC-GS-HHR-75). Asersi "tidak ada record dibuat" (TC-GS-HHR-75 Expected a) diamati pada langkah 17 sesudah aktivasi sukses TC-GS-HHR-76, karena tabel di belakang popup tidak diamati selama popup terbuka; langkah 16 menjadi anchor positif bagi asersi universal langkah 17.
- P-2 (pemicu bukan objek uji): Principal mematikan toggle Client A lewat sesi API pada langkah 31 hanya sebagai pemicu state; hasil yang diasersi ada di sesi UI Client A. Tidak ada sesi UI kedua yang diasersi.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 11, 27 (menyiapkan reader di simulator); langkah 18 sampai 20 (ganti akun dan buka halaman); langkah 21 sampai 24 (baseline Event Log, S-12); langkah 22 dan 39 (Search untuk menemukan baris target); langkah 36 (menutup popup berisi input; TC-GS-HHR-473 menyebut `[✕]` lalu `[Cancel Activation]`); langkah 43 (menutup popup Event Log).
- Asersi jumlah baris Event Log (langkah 41) memakai baseline hasil Search `Chainway C72` dengan anchor positif langkah 40 (baris seed EL-02); asersi daftar reader (langkah 37) memakai jumlah Seed Reader A sebagai baseline karena Client A dipulihkan ke Seed Reader A sebelum spec. Langkah 40 adalah `Verifikasi` tambahan di luar Expected TC-GS-HHR-473 yang berfungsi sebagai anchor.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (penyajian serial, pergantian reader, Current Power) dan mekanisme Principal mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` Client A tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint.
  - TC-GS-HHR-473 menyebut "sesi kedua" Principal; sesuai konvensi pelaku kedua yang hanya memicu state memakai sesi API (P-2), bukan sesi UI. Bila QA menghendaki sesi UI kedua, spec perlu diubah.
  - Email akun Principal di Tabel Pre-setup TC (`principal_automated_qaTeam1@qwertysystem.net`) berbeda dari deskripsi `GS_PRINCIPAL_TC_PASSWORD` di `.env.example` (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`); spec memakai email Tabel Pre-setup TC dan `GS_PRINCIPAL_TC_PASSWORD` sesuai rencana; QA/tim FE perlu memastikan akun dan env var yang sama.
  - Email akun Client B mengikuti pola `{namaClient}` yang nilainya tidak tertulis di Tabel Pre-setup TC; env var `GS_CLIENTB_TC_PASSWORD` baru dan belum terdaftar.
  - TC-GS-HHR-473 Expected c menyebut "satu baris `Failed` baru" tanpa kolom pembeda baris baru dari baris `Failed` run sebelumnya; spec memakai selisih jumlah baris hasil Search sebagai penanda baris baru (langkah 41) dan mengasersi atribut baris pada langkah 42.
  - TC-GS-HHR-473 tidak menyatakan state Event Log Activate lain yang ikut berubah; baseline hanya untuk hasil Search `Chainway C72`.
  - TC-GS-HHR-75 Expected a ("tidak ada record dibuat") tidak dapat diamati selama popup terbuka; spec mengamatinya pada langkah 17.
  - Judul dan isi dialog yang memuat `[Cancel Activation]` (langkah 36) tidak tertulis di TC sumber slice ini; langkah dibuat tanpa `Verifikasi` dialog.
