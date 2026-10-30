---
id: TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong
title: "Popup Changelog: Sumber Opsi Dropdown Filter (Loading, Entitas Tanpa Log, Opsi Bertambah, dan Position yang Dihapus)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-218
  - TC-GS-POS-288
  - TC-GS-POS-289
  - TC-GS-POS-290
coverage:
  web: automated
---

# Popup Changelog: Sumber Opsi Dropdown Filter (Loading, Entitas Tanpa Log, Opsi Bertambah, dan Position yang Dihapus)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Total Control Client Kosong (Pre-setup 18, baca-saja) untuk TC-GS-POS-218: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTEMPTY_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA). Spec kembali ke akun Total Control lewat langkah ganti akun eksplisit; hook `after` mengembalikan sesi ke akun Total Control default suite.
  - Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2), hanya sebagai pemicu penghapusan pada TC-GS-POS-290, dengan `Spectra.env.GS_TC2_PASSWORD`. Tidak ada asersi pada sesi Admin B.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Entitas Pre-setup 18 `Client Kosong` (tanpa entri Changelog; dipakai TC-GS-POS-218). Entitas ini baca-saja: tidak ada spec yang menulis (Create atau Delete) ke Client Kosong, sehingga Changelog-nya selalu kosong dan TC-GS-POS-218 tidak bergantung pada urutan spec. Spec yang menulis Position pada entitas kosong memakai Client Tulis (Pre-setup 27).
- Data Dinamis (nama bersuffix per run; fixture baru `Fixture.position.changelogSeed056`):
  - Di-seed lewat API di hook `before` oleh Budi Santoso: Create `Seed Opsi {runId}-056` sehingga Changelog entitas Total Control memuat minimal satu entri oleh `Budi S` untuk asersi opsi `Modified By` pada TC-GS-POS-289.
  - Dibuat spec lewat UI (TC-GS-POS-288): `Customs Officer {runId}-056`; dihapus oleh sesi Admin B pada TC-GS-POS-290.
  - Entri Changelog entitas Total Control bersifat audit trail permanen dan tidak dibersihkan.
- Hook `beforeEach`: membuka Global Settings > User > Position pada akun Total Control; layar awal dibuka di hook ini sehingga `## Test Steps` tidak mengulang langkah buka untuk akun pertama.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-056` yang masih ada (`Seed Opsi`, `Customs Officer`); kembalikan sesi ke akun Total Control default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Total Control dan Total Control Client Kosong) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding lewat API dengan sesi Budi; sesi API Admin B untuk menghapus Position (pemicu); penahanan respons (intercept parsial di atas backend nyata) pada permintaan opsi dropdown filter Changelog untuk TC-GS-POS-289 (endpoint tidak tertulis di TC, PRD, atau LLD; disediakan tim FE/BE), dipasang sebelum pemicu dan dilepas segera sesudah asersi Loading; pembacaan chip, centang opsi, dan teks opsi dropdown; logout dan login untuk ganti akun.
- State global: tidak ada yang diubah selain sesi akun dan intercept pada TC-GS-POS-289 (dilepas di langkah yang sama).

## Test Steps

### TC-GS-POS-289: Loading state dropdown filter saat opsi dimuat

1. Pasang intercept yang menahan respons permintaan opsi dropdown filter Changelog
2. Klik ikon Changelog
3. Klik ikon Filter
4. Buka dropdown `Modified By`
5. Verifikasi dropdown menampilkan skeleton atau spinner
6. Verifikasi dropdown tidak menampilkan daftar kosong tanpa indikator
7. Lepaskan respons yang ditahan dan lepas intercept
8. Verifikasi opsi `Budi S` termuat di dropdown `Modified By`
9. Tutup dropdown `Modified By` dengan menekan Esc
10. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-218: Dropdown filter tanpa sumber data (Client Kosong)

11. Ganti akun: logout dari akun Total Control
12. Login sebagai Total Control Client Kosong (Pre-setup 18) dengan `Spectra.env.GS_CLIENTEMPTY_TC_PASSWORD`
13. Buka Global Settings > User > Position
14. Klik ikon Changelog
15. Klik ikon Filter
16. Buka dropdown `Action`
17. Verifikasi dropdown menampilkan "No options available"
18. Tutup dropdown `Action` dengan menekan Esc
19. Tutup Popup Changelog dengan klik `✕` di header
20. Ganti akun: logout dari akun Total Control Client Kosong
21. Login sebagai Total Control (Budi Santoso) dengan `Spectra.env.GS_TC_PASSWORD`
22. Buka Global Settings > User > Position

### TC-GS-POS-288: Opsi filter Position Name bertambah setelah Create baru

23. Klik `[+ Position]`
24. Ketik `Customs Officer {runId}-056` pada Position Name
25. Klik `[Submit]`
26. Tunggu aksi selesai (Popup Create Position tertutup)
27. Klik ikon Changelog
28. Klik ikon Filter
29. Buka dropdown `Position Name`
30. Verifikasi opsi `Customs Officer {runId}-056` tersedia tanpa memuat ulang halaman

### TC-GS-POS-290: Filter Position Name aktif tetap aman setelah Position-nya dihapus

31. Centang `Customs Officer {runId}-056` pada dropdown `Position Name`
32. Klik `[Apply]`
33. Verifikasi tabel menampilkan entri Create `Customs Officer {runId}-056`
34. Sesi Admin B menghapus `Customs Officer {runId}-056`
35. Klik ikon Filter
36. Klik `[Apply]`
37. Verifikasi tidak ada crash atau error
38. Verifikasi tabel menampilkan entri Create dan Delete `Customs Officer {runId}-056`
39. Klik ikon Filter
40. Buka dropdown `Position Name`
41. Verifikasi opsi `Customs Officer {runId}-056` tetap ada karena tercatat di log
42. Tutup dropdown `Position Name` dengan menekan Esc
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 45 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik (sumber opsi dropdown filter Popup Changelog) dengan satu akun utama; dua TC pertama (289, 218) tidak mengubah data dan berada di awal, sedangkan dua TC yang membuat dan menghapus data (288, 290) berada di akhir sehingga kegagalannya tidak menghilangkan makna dua TC awal.
- Urutan TC dalam spec: 289, 218, 288, 290. Urutan ini menyimpang dari urutan TC sumber (218, 288, 289, 290): TC yang tidak mengubah data (289, 218) lebih dulu, TC yang membuat dan menghapus data (288, 290) terakhir. TC-GS-POS-289 memerlukan Popup Changelog yang baru dibuka (opsi dimuat saat dropdown dibuka) sehingga ditaruh pertama. TC-GS-POS-218 memakai akun lain: ganti akun ke Client Kosong (langkah 11 sampai 12) dan kembali ke Total Control (langkah 20 sampai 21) ditulis sebagai langkah eksplisit, dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal. Popup Changelog dibuka tiga kali (langkah 2, 14, 27) dan ditutup tiga kali (langkah 10, 19, 45).
- Form Create Position dibuka sekali (langkah 23) dan ditutup oleh Submit sukses (langkah 26 menunggu penutupan); stay checkbox tidak dicentang.
- P-2: intercept pada TC-GS-POS-289 hanya menahan respons untuk mengamati state Loading (bukan kegagalan yang dipaksakan) dan dilepas segera sesudah asersi (langkah 7). Sesi Admin B pada TC-GS-POS-290 hanya pemicu penghapusan; tidak ada asersi pada sesi Admin B, yang diasersi adalah perilaku Popup Changelog Admin A sesudah Position dihapus.
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan intercept (langkah 1), penutupan dropdown (langkah 9, 18, 42), penutupan Popup Changelog (langkah 10, 19, 45), ganti akun dan pembukaan halaman (langkah 11 sampai 13, 20 sampai 22), menunggu Create selesai (langkah 26), pembukaan Filter (langkah 3, 15, 28, 35, 39), serta `[Clear Field]` + `[Apply]` di akhir (langkah 43 sampai 44).
- Langkah 33 (`Verifikasi` tabel menampilkan entri Create `Customs Officer {runId}-056` sesudah `[Apply]` pertama) adalah anchor positif bahwa filter aktif dan entri ada sebelum Sesi Admin B menghapus; langkah ini tidak ada di Expected TC-GS-POS-290.
- Langkah 1 sampai 2 memakai urutan pasang intercept lalu buka Popup Changelog supaya penahanan respons sudah aktif sebelum opsi dimuat.
- Filter, chip, dan logika AND/OR Popup Changelog (TC-GS-POS-211 sampai 217, 219, 220) ada di spec 040; Search dan Sort di spec 039 dan 041.
- Temuan untuk QA:
  - TC-GS-POS-218 memakai Client Kosong yang email akunnya tidak tertulis di Pre-setup 18; env var `GS_CLIENTEMPTY_TC_PASSWORD` baru.
  - TC-GS-POS-289 menyebut "diperlambat via DevTools" tanpa endpoint dan tanpa menyatakan apakah opsi dimuat saat Popup dibuka atau saat dropdown dibuka; spec memasang penahanan sebelum Popup dibuka dan mengasersi sesudah dropdown dibuka. Bentuk indikator (skeleton atau spinner) tidak dipastikan oleh TC. Precondition TC tidak menyebut entri oleh `Budi S`; spec men-seed satu Position lewat API agar opsi `Budi S` dapat diasersi sesudah dimuat.
  - TC-GS-POS-288 langkah 1 tidak menyebut tombol; spec mengikuti konvensi (`[+ Position]` dan `[Submit]`).
  - TC-GS-POS-290 tidak menyebut cara sesi Admin B menghapus (UI atau API); spec memakai sesi Admin B tanpa mengasersi sesinya. Expected b memuat penjelasan "opsi tetap ada karena tercatat di log" yang di spec menjadi Verifikasi tersendiri (langkah 41).
  - TC-GS-POS-290 dan 288 tidak menyebut apakah Filter Panel tertutup sesudah `[Apply]`; spec membuka Filter lagi sebelum langkah berikutnya (langkah 35 dan 39).
