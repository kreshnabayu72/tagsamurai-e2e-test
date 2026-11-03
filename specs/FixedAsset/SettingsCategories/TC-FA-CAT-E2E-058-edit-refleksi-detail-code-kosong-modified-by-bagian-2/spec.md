---
id: TC-FA-CAT-E2E-058-edit-refleksi-detail-code-kosong-modified-by-bagian-2
title: "Edit: Aksesibilitas Popup, Modified By dan Last Updated, serta Node Dihapus User Lain (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-625
  - TC-FA-CAT-204
  - TC-FA-CAT-206
coverage:
  web: automated
---

# Edit: Aksesibilitas Popup, Modified By dan Last Updated, serta Node Dihapus User Lain (Bagian 2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Pelaku kedua TC-206 (menghapus node): Total Control (Pre-setup #1) lewat sesi API aktor (butir hook `suite.md`; kemampuan disediakan tim BE/FE).
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed tidak diubah.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Edit Root {runId}-058` | `E058ROOT` | L1; dipilih di sidebar |
  | Target TC-625 | `Furniture {runId}-058` | `E058FURN` | anak `Edit Root`, leaf; menggantikan `Furniture` |
  | Target TC-204 | `Peripheral {runId}-058` | `E058PERI` | anak `Edit Root`, internal; menggantikan `Peripheral` |
  | Anak `Peripheral` | `Keyboard {runId}-058` | `E058KB` | leaf |
  | Subcategory baru TC-204 | `Stamp Child {runId}-058` | `STMP` | dibuat spec (Code literal TC); hook `before` menghapus sisa kategori ber-Code `STMP` |
  | Target TC-206 | `Vehicle {runId}-058` | `E058VEH` | anak `Edit Root`, leaf; dihapus pelaku kedua pada TC-206 |

- Seed dibuat oleh aktor seed yang berbeda dari akun aktor spec (disediakan tim FE) agar perubahan Modified By pada TC-204 teramati. Hook `before` menunggu sampai menit berganti (maksimum 60 detik) setelah seeding agar perubahan Last Updated pada ketelitian menit teramati (bagian 6).
- Kemampuan teknis: pembacaan nama tampil akun aktor untuk asersi Modified By; jam server dan jam browser sinkron untuk asersi Last Updated; inspeksi atribut ARIA field popup (`aria-required`, `aria-describedby`); Modal Changelog dapat dibaca dan dicari.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-625: Accessibility popup Edit: aria-required, aria-describedby, dan focus trap

1. Klik node `Edit Root {runId}-058` di sidebar
2. Klik elipsis (⋯) pada baris `Furniture {runId}-058` > `Edit`
3. Verifikasi field Category Name memiliki `aria-required="true"`
4. Verifikasi field Code dan Description tidak memiliki `aria-required="true"`
5. Kosongkan Category Name
6. Klik `[Save]`
7. Verifikasi error inline V-01 `Category name must not be empty` tampil pada field Category Name
8. Verifikasi field Category Name memiliki `aria-describedby` yang menunjuk ke pesan error inline
9. Tekan Tab berulang sampai fokus kembali ke awal popup
10. Verifikasi fokus terjebak di dalam popup dan tidak keluar ke halaman di belakang
11. Klik `✕` pada header popup
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-CAT-204: Modified By dan Last Updated diperbarui oleh Edit tetapi tidak oleh penambahan subcategory

14. Catat Modified By dan Last Updated baris `Peripheral {runId}-058`
15. Klik elipsis (⋯) pada baris `Peripheral {runId}-058` > `+ Add Subcategory`
16. Isi Category Name `Stamp Child {runId}-058`
17. Isi Code `STMP`
18. Klik `[Submit]`
19. Tunggu aksi selesai (popup New Subcategory tertutup)
20. Catat ulang Modified By dan Last Updated baris `Peripheral {runId}-058`
21. Verifikasi Modified By baris `Peripheral {runId}-058` tidak berubah dari nilai yang dicatat pada langkah 14
22. Verifikasi Last Updated baris `Peripheral {runId}-058` tidak berubah dari nilai yang dicatat pada langkah 14
23. Klik elipsis (⋯) pada baris `Peripheral {runId}-058` > `Edit`
24. Isi Description `Stamp desc`
25. Klik `[Save]` lalu catat waktu aksi
26. Verifikasi Modified By baris `Peripheral {runId}-058` adalah aktor (format `[First Name] [Last Initial]`)
27. Verifikasi Last Updated baris `Peripheral {runId}-058` sesuai waktu Save (toleransi satu menit)

### TC-FA-CAT-206: Edit pada node yang sudah dihapus user lain: ditolak dengan toast netral T-12

28. Klik elipsis (⋯) pada baris `Vehicle {runId}-058` > `Edit`
29. Tunggu aksi selesai (popup Edit terbuka dengan data terisi)
30. Pelaku kedua (sesi API) menghapus `Vehicle {runId}-058` hingga penghapusan tersimpan
31. Ubah Description menjadi `Late edit`
32. Klik `[Save]`
33. Verifikasi toast netral `This category is no longer available.`
34. Verifikasi tabel di-refresh tanpa baris `Vehicle {runId}-058`
35. Verifikasi sidebar di-refresh tanpa node `Vehicle {runId}-058`
36. Buka Modal Changelog
37. Ketik Search `Vehicle {runId}-058`, tekan Enter
38. Verifikasi baris Action `Delete` untuk `Vehicle {runId}-058` (dari pelaku kedua) tampil
39. Verifikasi tidak ada baris Edit dengan New Value `Late edit`
40. Tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-625, TC-204, dan TC-206 ada di spec ini; TC-199, TC-200, dan TC-202 ada di spec 057.
- Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan Search/Changelog dipakai untuk asersi log. Ketiga blok (TC-625, TC-204, TC-206) berkelas fungsional yang sama, memakai node milik sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: TC-625 (validasi diblokir), TC-204 (aksi sukses), TC-206 (node dihapus di akhir) mengikuti S-10; urutan nomor TC sumber berbeda.
- Penyesuaian data (S-06, S-12): TC memakai baris `Furniture`, `Peripheral`, `Vehicle` Pre-setup #20 sebagai target; spec memakai node milik spec bersuffix `{runId}-058` di bawah `Edit Root`.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node `Edit Root` di sidebar; menunggu aksi selesai (langkah 19 dan 29); mencatat nilai dan waktu aksi; membuka, Search, dan menutup Modal Changelog. Search memakai nama bersuffix sehingga baseline nol (S-12).
- P-1: asersi "tidak ada baris log baru" TC-206 ditulis di spec ini dan bukan di spec absence, karena kondisi "node dihapus pihak lain saat Edit terbuka" dibangun berurutan oleh langkah 28 sampai 30 dan tidak dapat dibangun ulang tanpa biaya besar di spec lain. Anchor positif: baris `Delete` dari pelaku kedua (langkah 38); baseline nol karena nama bersuffix.
- Langkah 21 dan 22 membandingkan dengan nilai yang dicatat pada langkah 14; langkah 26 dan 27 dibandingkan dengan aktor dan waktu pada langkah 25.
- Temuan untuk QA:
  - TC-625 Expected b menyebut "error V-01" tanpa teks; spec memakai teks V-01 dari PRD §6 `Category name must not be empty`.
  - TC-204 Expected b menyebut Modified By berubah menjadi aktor; perubahan hanya teramati bila Modified By awal berbeda dari aktor. Spec mensyaratkan aktor seed berbeda (Prerequisites).
  - TC-204 menyebut baris `Peripheral` internal dengan anak seed; spec memakai anak `Keyboard {runId}-058` agar node tetap internal sebelum subcategory ditambahkan.
  - TC-206 Expected b ("tidak ada baris log baru") tidak menyebut surface; spec memakai Modal Changelog. System Log dan Activity Log tidak diperiksa di spec ini.
