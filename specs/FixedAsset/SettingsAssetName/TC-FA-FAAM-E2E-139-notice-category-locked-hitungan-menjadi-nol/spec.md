---
id: TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol
title: "Notice Category Locked: Hitungan Menjadi 0 lewat Edit, Sesi Lain, atau Delete serta Hitungan 0 Sejak Awal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-689
  - TC-FA-FAAM-703
  - TC-FA-FAAM-704
  - TC-FA-FAAM-727
coverage:
  web: automated
---

# Notice Category Locked: Hitungan Menjadi 0 lewat Edit, Sesi Lain, atau Delete serta Hitungan 0 Sejak Awal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor awal: Total Control client `AutoStarter` (Pre-setup #16); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_STARTER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun client lain dipakai lewat Step ganti akun eksplisit (tabel di bawah).
- Client yang dipakai (tiap client khusus TC ini; akun Total Control tiap client tidak tertulis di Pre-setup TC, lihat Temuan untuk QA; password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`):

  | TC | Client | Data (Pre-setup) | Env password |
  |---|---|---|---|
  | TC-FA-FAAM-689 | `AutoStarter` (#16) | 10 Asset Name tanpa Category Locked | `Spectra.env.FA_TC_STARTER_PASSWORD` |
  | TC-FA-FAAM-703 | `AutoLocked1b` (#12e) | `Solo Locked Edit`, Category internal `Electronics`, Total Asset 0; hitungan Needs Update 1 | `Spectra.env.FA_TC_LOCKED1B_PASSWORD` |
  | TC-FA-FAAM-704 | `AutoLocked1c` (#12f) | `Solo Locked Race`, Category internal `Electronics`, Total Asset 0; hitungan Needs Update 1 | `Spectra.env.FA_TC_LOCKED1C_PASSWORD` |
  | TC-FA-FAAM-727 | `AutoLocked1d` (#12g) | `Solo Locked Delete` dan `Anchor Item`, Total Asset 0; hitungan Needs Update 1 | `Spectra.env.FA_TC_LOCKED1D_PASSWORD` |

- Client `AutoLocked1b`, `AutoLocked1c`, dan `AutoLocked1d` diubah spec ini (Edit atau Delete) dan dipulihkan ke keadaan Pre-setup lewat seed API di hook `before` dan `after` (disediakan tim BE/FE); efek pada Last Updated dan entri Changelog client itu dicatat di sini dan tidak memengaruhi spec lain karena client khusus TC ini.
- Kemampuan teknis: sesi API aktor sebagai pelaku kedua untuk TC-FA-FAAM-704 (mengubah Category `Solo Locked Race` menjadi leaf `Laptop`; bukan konteks UI kedua); jendela tunggu 5 detik untuk propagasi SSE tanpa memuat ulang halaman adalah pilihan spec (bukan nilai TC atau PRD).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada. Client khusus TC ini dipulihkan lewat seed API (lihat butir client). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-689: Notice Category Locked tidak tampil saat hitungan Needs Update 0
1. Verifikasi tabel tampil normal: sedikitnya satu baris tampil
2. Verifikasi tidak ada notice Category Locked
3. Verifikasi tidak ada chip quick filter
### Ganti akun: client AutoLocked1b
4. Logout, lalu login sebagai Total Control client `AutoLocked1b` (Pre-setup #12e) dengan `Spectra.env.FA_TC_LOCKED1B_PASSWORD`
### TC-FA-FAAM-703: Hitungan menjadi 0 saat quick filter aktif: notice hilang dan quick filter terlepas otomatis
5. Klik `Show only this`
6. Klik `⋯` baris `Solo Locked Edit`, lalu klik `Edit`
7. Klik `[Select Category]`, pilih leaf `Laptop` lewat Tree Picker, klik `[Select]`
8. Klik `[Save]`
9. Verifikasi toast `Success, asset name has been updated.`
10. Verifikasi notice hilang
11. Verifikasi chip `Needs Update` hilang
12. Verifikasi quick filter terlepas: tabel memuat seluruh Asset Name sesuai Search dan Filter Panel yang tersisa
13. Verifikasi tidak ada pesan error
### Ganti akun: client AutoLocked1c
14. Logout, lalu login sebagai Total Control client `AutoLocked1c` (Pre-setup #12f) dengan `Spectra.env.FA_TC_LOCKED1C_PASSWORD`
### TC-FA-FAAM-704: Hitungan menjadi 0 oleh sesi lain saat quick filter aktif: notice hilang dan quick filter terlepas otomatis
15. Klik `Show only this`
16. Ubah Category `Solo Locked Race` menjadi leaf `Laptop` lewat sesi API aktor hingga perubahan tersimpan
17. Tunggu 5 detik tanpa memuat ulang halaman
18. Verifikasi notice hilang otomatis
19. Verifikasi chip `Needs Update` hilang otomatis
20. Verifikasi quick filter terlepas otomatis: tabel memuat Asset Name sesuai Search dan Filter Panel yang tersisa
21. Verifikasi tidak ada pesan error
### Ganti akun: client AutoLocked1d
22. Logout, lalu login sebagai Total Control client `AutoLocked1d` (Pre-setup #12g) dengan `Spectra.env.FA_TC_LOCKED1D_PASSWORD`
### TC-FA-FAAM-727: Delete Asset Name Category Locked terakhir saat quick filter aktif: notice hilang dan quick filter terlepas otomatis
23. Klik `Show only this`
24. Klik `⋯` baris `Solo Locked Delete`, lalu klik `Delete`
25. Klik `[Delete]` pada dialog
26. Verifikasi toast `Success, asset name has been deleted.`
27. Verifikasi notice hilang
28. Verifikasi chip `Needs Update` hilang
29. Verifikasi quick filter terlepas: tabel memuat `Anchor Item`
30. Verifikasi tidak ada pesan error

## Notes

- Urutan di spec: TC-FA-FAAM-689 (baca saja) lebih dulu, lalu TC-FA-FAAM-703 dan 704 (Edit), TC-FA-FAAM-727 (Delete) di akhir (S-10). Pergantian client memakai Step ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua TC-FA-FAAM-704 memakai sesi API aktor, bukan konteks UI kedua; tidak ada butir P-2. Pada TC-FA-FAAM-704 Expected hanya diamati di sesi A (UI).
- Asersi absence notice dan chip pada TC-FA-FAAM-689 beranchor Verifikasi tabel menampilkan sedikitnya satu baris (bagian 8b butir 2); pada TC-FA-FAAM-703, 704, dan 727 beranchor toast hasil atau baris tabel yang tampil.
- Langkah "Tunggu 5 detik tanpa memuat ulang halaman" pada TC-FA-FAAM-704 adalah langkah penghubung untuk propagasi SSE (bagian 6).
- Spec berjumlah 30 langkah; empat client dipakai berurutan dan setiap blok berdiri sendiri.
- Temuan untuk QA: Pre-setup #12e sampai #12g dan #16 berupa client tanpa baris akun Total Control (email tidak tertulis). TC-FA-FAAM-727 punya Post Condition (Model per Brand, baris policy transaksi, dan scope custom field ikut dihapus) tanpa langkah observasi; tidak diasersi. Pernyataan pemulihan client Pre-setup yang diubah (S-06) belum tertulis di `suite.md`; pemilik suite perlu menambahkannya.
