---
id: TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir
title: "Setup Column Tab Total Control dan Read Only: Screening, Hide/Show Kolom, Tutup Tanpa Simpan, dan Kolom Visible Terakhir"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-162
  - TC-GS-ROLE-163
  - TC-GS-ROLE-164
  - TC-GS-ROLE-165
  - TC-GS-ROLE-171
  - TC-GS-ROLE-172
coverage:
  web: automated
---

# Setup Column Tab Total Control dan Read Only: Screening, Hide/Show Kolom, Tutup Tanpa Simpan, dan Kolom Visible Terakhir

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; tabel dimuat dari backend nyata dan seluruh data Pre-setup hanya dibaca.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > Total Control dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Tab Total Control dan Tab Read Only masing-masing berisi sedikitnya 3 user dengan Position dan Division berbeda (precondition TC). Asersi spec ini hanya menyangkut kolom tabel, bukan kumpulan nama atau jumlah baris.
- Data uji: kolom K1 (default tampil, Hideable) `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`; kolom K2 (default tersembunyi) `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan Custom Field aktif `Region` (Custom Field aktif disediakan tim FE; nama `Region` mengikuti TC-GS-ROLE-188).
- Tabel "Tab yang diuji" untuk TC-GS-ROLE-162:

  | Tab |
  |---|
  | Total Control |
  | Read Only |

- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Tab Total Control dikembalikan ke default (K1 tampil berurutan, K2 tersembunyi, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel itu di browser. Tab Read Only tidak diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengarahkan kursor ke checkbox disabled untuk membaca tooltip; menekan Esc pada modal; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-ROLE-162: Screening overlay Column Visibility Tab Total Control dan Tab Read Only

Untuk setiap baris tabel "Tab yang diuji" (langkah 1 sampai 7):
1. Klik Tab sesuai baris tabel
2. Klik header kolom Column Visibility (⋯)
3. Verifikasi item `Setup Column...` di bagian bawah panel Column Visibility (di bawah daftar kolom)
4. Verifikasi kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated` tercentang dan enabled
5. Verifikasi kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region` tidak tercentang dan enabled
6. Verifikasi masing-masing kolom memiliki drag handle
7. Tekan Esc untuk menutup overlay Column Visibility

### TC-GS-ROLE-163: Screening popup Setup Column Tab Total Control

8. Klik Tab `Total Control`
9. Klik header kolom Column Visibility (⋯)
10. Klik item `Setup Column...`
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: icon close `[✕]`
13. Verifikasi Body: kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated` tercentang
14. Verifikasi Body: kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region` tidak tercentang
15. Verifikasi Body: drag handle pada tiap kolom
16. Verifikasi Body: icon pin pada tiap kolom
17. Verifikasi Footer: tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
18. Verifikasi Footer tanpa tombol `[Cancel]`

### TC-GS-ROLE-171: Setup Column: tutup tanpa Save membatalkan perubahan

19. Hilangkan centang `Position`
20. Klik `[✕]`
21. Verifikasi popup Setup Column tertutup
22. Verifikasi kolom `Position` tetap tampil di tabel
23. Klik header kolom Column Visibility (⋯)
24. Klik item `Setup Column...`
25. Hilangkan centang `Position`
26. Tekan Esc
27. Verifikasi popup Setup Column tertutup
28. Verifikasi kolom `Position` tetap tampil di tabel

### TC-GS-ROLE-172: Setup Column: kolom terakhir yang tampil tidak bisa di-uncheck

29. Klik header kolom Column Visibility (⋯)
30. Klik item `Setup Column...`
31. Hilangkan centang `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated` (kolom `Name` dibiarkan; kolom K2 sudah tidak tercentang)
32. Arahkan kursor ke checkbox `Name`
33. Verifikasi checkbox `Name` disabled
34. Verifikasi tooltip `At least one column must remain visible.`
35. Klik `[✕]` untuk menutup popup tanpa Save

### TC-GS-ROLE-164: Setup Column: Hide kolom kelas K1 default tampil lalu Save

36. Klik header kolom Column Visibility (⋯)
37. Klik item `Setup Column...`
38. Hilangkan centang `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated` (kolom `Name` dibiarkan agar sedikitnya satu kolom tersisa)
39. Verifikasi tabel di balik modal langsung tidak menampilkan kolom `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
40. Klik `[Save]`
41. Verifikasi tabel tidak menampilkan kolom `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
42. Tekan F5
43. Verifikasi tabel tetap tidak menampilkan kolom `Position`, `Division`, `Status`, `Modified By`, `Last Updated`

### TC-GS-ROLE-165: Setup Column: Show kolom kelas K2 kurasi tersembunyi lalu Save

44. Klik header kolom Column Visibility (⋯)
45. Klik item `Setup Column...`
46. Centang `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Region`
47. Verifikasi tabel di balik modal langsung menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region`
48. Klik `[Save]`
49. Verifikasi tabel menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region`
50. Tekan F5
51. Verifikasi tabel tetap menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region`

### Pemulihan

52. Klik header kolom Column Visibility (⋯)
53. Klik item `Setup Column...`
54. Klik `[Reset to Default]`
55. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 162, 163 (screening), 171, 172 (tutup tanpa Save dan kolom terakhir, tidak menyimpan perubahan), lalu 164 dan 165 (Save, mengubah konfigurasi tersimpan), dan blok Pemulihan di akhir. Urutan di `tc-role.md`: 162, 163, 164, 165, 171, 172. TC-GS-ROLE-171 dan 172 diletakkan sebelum 164 dan 165 supaya kolom `Position` masih tampil saat TC-GS-ROLE-171 dan konfigurasi default tidak perlu dipulihkan di tengah spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup overlay sebelum berpindah tab), langkah 35 (menutup popup tanpa Save agar centang yang dihilangkan tidak tersimpan), dan blok Pemulihan langkah 52 sampai 55 (mengembalikan konfigurasi default; hook `after` sebagai cadangan). Langkah 19 memakai popup yang masih terbuka dari TC-GS-ROLE-163, sehingga langkah 1 TC-GS-ROLE-171 ("Buka popup Setup Column") dipenuhi langkah 10. Langkah 1 sampai 7 diulang untuk dua tab pada tabel "Tab yang diuji" (14 langkah setelah ekspansi).
- Arah perubahan pada TC-GS-ROLE-164 (hide semua kolom K1 kecuali `Name`) dan TC-GS-ROLE-165 (show semua kolom K2) mengikuti nama TC dan data uji TC; kolom K2 pada TC-GS-ROLE-164 sudah tersembunyi sehingga tidak diubah.
- Asersi tambahan (konkretisasi Expected): TC-GS-ROLE-163 Expected c menyebut "tanpa [Cancel]", ditulis sebagai `Verifikasi` tersendiri.
- Spec melewati sekitar 35 langkah (55 langkah nominal, 62 setelah ekspansi) karena enam TC Setup Column memakai tabel dan modal yang sama dan satu kelas harness (fungsional). Setiap blok membuka popup sendiri lewat header Column Visibility, kecuali TC-GS-ROLE-171 yang meneruskan popup TC-GS-ROLE-163; kegagalan keras blok screening tidak menghilangkan makna blok TC-GS-ROLE-164 dan 165 yang mengubah konfigurasi lewat popup yang dibuka ulang. Langkah pembuka popup yang berulang (langkah 23, 29, 36, 44) merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-ROLE-166 sampai 170 dan 173 (reorder, pin, Reset to Default, isolasi per tabel) berada di spec 057; Setup Column Tab System (TC-GS-ROLE-183 dan 184) di spec 060; Setup Column Detail dipakai spec 062 untuk menampilkan kolom pada Search.
- Temuan untuk QA:
  - TC-GS-ROLE-162 menulis item "Setup Column..." sedangkan TC-GS-ROLE-163 dan 172 menulis "[Setup Column]"; spec memakai `Setup Column...` untuk item overlay.
  - TC-GS-ROLE-163: Expected tidak menyebut Subtitle dan Search input popup; keduanya tidak diasersi.
  - TC-GS-ROLE-164 dan 165: kolom "[Custom Field aktif]" tidak disebut namanya; spec memakai `Region` (sama dengan TC-GS-ROLE-188) sebagai Custom Field aktif yang disediakan tim FE. TC-GS-ROLE-165 menyebut "kecuali Name pada Show K1", rujukan yang tidak jelas karena langkah itu milik blok Show K2; spec tidak mengubah `Name`.
  - TC-GS-ROLE-164 dan 165: arah perubahan "ubah checkbox" tidak eksplisit; spec menyembunyikan K1 (kecuali `Name`) dan menampilkan K2.
  - TC-GS-ROLE-164 dan 165 Expected c ("Tetap setelah F5"): spec mengasersi setelah F5 pada konteks browser yang sama.
