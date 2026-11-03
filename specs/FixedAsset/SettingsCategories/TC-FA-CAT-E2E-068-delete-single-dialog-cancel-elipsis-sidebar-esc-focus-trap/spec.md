---
id: TC-FA-CAT-E2E-068-delete-single-dialog-cancel-elipsis-sidebar-esc-focus-trap
title: "Delete Single: Dialog Konfirmasi, Cancel, Esc, Focus Trap, dan Delete dari Elipsis Sidebar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-212
  - TC-FA-CAT-238
  - TC-FA-CAT-626
  - TC-FA-CAT-214
  - TC-FA-CAT-633
  - TC-FA-CAT-215
coverage:
  web: automated
---

# Delete Single: Dialog Konfirmasi, Cancel, Esc, Focus Trap, dan Delete dari Elipsis Sidebar

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed tidak diubah.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi sehingga Changelog memuat entri Create, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Del Root {runId}-068` | `E068ROOT` | L1; dipilih di sidebar |
  | Leaf bersih | `Vehicle {runId}-068` | `E068VEH` | anak `Del Root`, leaf, tidak ditunjuk Asset Name; menggantikan `Vehicle`; dihapus pada TC-215 |
  | Family | `Accessory {runId}-068` | `E068ACC` | anak `Del Root`, internal; menggantikan `Accessory` |
  | Subcategory | `Cable {runId}-068` | `E068CB` | anak `Accessory {runId}-068`; menggantikan `Cable` |

- Kemampuan teknis: Modal Changelog dapat dibaca dan dicari; pengujian fokus keyboard (Tab dan Shift+Tab) dan penutupan dialog lewat `Esc`.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-212: Dialog konfirmasi D-09 untuk leaf bersih (screening)

1. Klik node `Del Root {runId}-068` di sidebar
2. Klik elipsis (⋯) pada baris `Vehicle {runId}-068` > `Delete`
3. Verifikasi dialog tampil dengan Title `Delete Category`, bullet `Vehicle {runId}-068`, dan body `Are you sure you want to delete it? This action cannot be undone.`
4. Verifikasi tombol `[Cancel]` dan `[Delete]` (severity danger) tampil
5. Klik backdrop di luar dialog
6. Verifikasi dialog tidak tertutup

### TC-FA-CAT-238: Tombol dialog Delete memakai severity yang benar dan Esc setara Cancel

7. Verifikasi `[Delete]` berseverity danger dan `[Cancel]` varian text kontras
8. Tekan `Esc`
9. Verifikasi dialog tertutup seperti `[Cancel]`
10. Verifikasi `Vehicle {runId}-068` tidak terhapus: baris tetap tampil di tabel

### TC-FA-CAT-626: Accessibility dialog Delete D-09: focus trap

11. Klik elipsis (⋯) pada baris `Vehicle {runId}-068` > `Delete` sampai dialog D-09 tampil
12. Tekan Tab dan Shift+Tab berulang
13. Verifikasi fokus terjebak di dalam dialog `Delete Category` (berputar di antara kontrol dialog termasuk `[Cancel]` dan `[Delete]`)
14. Verifikasi fokus tidak keluar ke halaman di belakang dialog
15. Verifikasi tidak ada kategori yang terhapus selama pengujian fokus: `Vehicle {runId}-068` tetap tampil di tabel

### TC-FA-CAT-214: Cancel pada dialog Delete tidak menghapus apa pun

16. Klik `[Cancel]` pada dialog
17. Verifikasi dialog tertutup
18. Verifikasi `Vehicle {runId}-068` tetap ada di tabel
19. Verifikasi `Vehicle {runId}-068` tetap ada di sidebar
20. Verifikasi tidak ada toast
21. Buka Modal Changelog
22. Ketik Search `Vehicle {runId}-068`, tekan Enter
23. Verifikasi baris Action `Create` untuk `Vehicle {runId}-068` tampil
24. Verifikasi tidak ada baris Action `Delete` untuk `Vehicle {runId}-068`
25. Tutup Modal Changelog

### TC-FA-CAT-633: Cancel pada dialog Delete family D-08 tidak menghapus apa pun

26. Klik elipsis (⋯) pada baris `Accessory {runId}-068` > `Delete` sampai dialog D-08 tampil
27. Verifikasi dialog `Delete Category` dengan bullet `Accessory {runId}-068` dan kalimat satu subcategory `This category has 1 subcategory — deleting it will also delete its subcategory. This action cannot be undone. Are you sure you want to delete it?` tampil sebelum `[Cancel]`
28. Klik `[Cancel]` pada dialog
29. Verifikasi dialog tertutup
30. Verifikasi `Accessory {runId}-068` tetap ada di tabel
31. Klik node `Accessory {runId}-068` di sidebar
32. Verifikasi `Cable {runId}-068` tetap ada di tabel
33. Verifikasi sidebar menampilkan `Accessory {runId}-068` dan `Cable {runId}-068`
34. Verifikasi tidak ada toast
35. Buka Modal Changelog
36. Ketik Search `Accessory {runId}-068`, tekan Enter
37. Verifikasi baris Action `Create` untuk `Accessory {runId}-068` tampil
38. Verifikasi tidak ada baris Action `Delete` pada hasil Search
39. Tutup Modal Changelog

### TC-FA-CAT-215: Delete dari elipsis node sidebar memanggil dialog dan aksi yang sama dengan row action

40. Klik elipsis (⋯) pada node `Vehicle {runId}-068` di sidebar > `Delete`
41. Verifikasi dialog D-09 yang sama tampil dengan Title `Delete Category`, bullet `Vehicle {runId}-068`, dan body `Are you sure you want to delete it? This action cannot be undone.`
42. Klik `[Delete]`
43. Verifikasi toast `Success, category has been deleted.`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-212, TC-238, TC-626, TC-214, TC-633, dan TC-215 ada di spec ini.
- Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan asersi log memakai Modal Changelog. Keenam blok berkelas fungsional yang sama (dialog Delete), masing-masing berdiri sendiri pada dialog yang sama atau node milik spec, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-212, TC-238, TC-626, TC-214, TC-633, TC-215. Dialog TC-212 tetap terbuka untuk TC-238, dan dialog TC-626 tetap terbuka untuk TC-214, sehingga jumlah buka dialog tidak lebih dari jumlah penutupan (S-10, prinsip 6); langkah TC "Klik elipsis > Delete" pada TC-238 dan TC-214 tidak diulang karena dialog sudah terbuka dari TC sebelumnya.
- Penyesuaian data (S-06, S-12): TC memakai baris `Vehicle` dan `Accessory` Pre-setup #20; spec memakai node milik spec bersuffix `{runId}-068` di bawah `Del Root`. Teks D-08 dan D-09 dalam bullet dan body mengikuti PRD §6.
- P-1: asersi "tidak ada log" TC-214 dan TC-633 ditulis di spec ini dan bukan di spec absence, karena kondisi (dialog Delete yang baru dibuka lalu dibatalkan) dibangun oleh langkah sebelumnya dan tidak dapat dibangun ulang tanpa biaya besar di spec lain; tidak ada spec absence yang memuat aksi nyata untuk kedua TC ini. Anchor positif: baris `Create` pada Changelog; nama bersuffix memberi baseline nol untuk baris `Delete`.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node di sidebar; klik backdrop dan tombol `Esc`, Tab, dan Shift+Tab sebagai aksi pemicu asersi; membuka, Search, dan menutup Modal Changelog; memilih node `Accessory` agar `Cable` tampil di tabel.
- Temuan untuk QA:
  - TC-212 Expected b ("klik backdrop tidak menutup dialog") tidak punya langkah klik backdrop di TC; spec menambahkan aksi klik backdrop sebagai pemicu asersi.
  - TC-214 dan TC-633 Expected ("tidak ada log") tidak menyebut surface; spec memakai Modal Changelog. Asersi bergantung pada seeding lewat jalur Create resmi yang menulis entri Create (anchor); asumsi ini perlu dikonfirmasi tim BE/FE.
  - TC-633 Expected a tidak menyebut teks body D-08; spec memakai teks PRD §6 D-08 varian satu subcategory.
  - TC-626 tidak menyatakan jumlah penekanan Tab; spec memakai "berulang" sampai fokus berputar.
