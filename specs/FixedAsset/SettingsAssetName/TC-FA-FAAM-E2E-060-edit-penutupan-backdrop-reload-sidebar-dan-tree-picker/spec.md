---
id: TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker
title: "Edit: Backdrop, Nilai Dikembalikan, Esc, Reload F5, Sidebar, dan Esc pada Tree Picker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-177
  - TC-FA-FAAM-178
  - TC-FA-FAAM-179
  - TC-FA-FAAM-180
  - TC-FA-FAAM-181
  - TC-FA-FAAM-742
coverage:
  web: automated
---

# Edit: Backdrop, Nilai Dikembalikan, Esc, Reload F5, Sidebar, dan Esc pada Tree Picker

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`. Pada spec ini baris itu hanya dibuka, divalidasi, dan dibatalkan atau ditolak validasi; tidak ada yang disimpan sehingga Last Updated tidak berubah (S-06, pengecualian aksi dibatalkan atau ditolak).
- Kemampuan teknis: runner menangani dialog `beforeunload` browser (menampilkan, lalu memilih tetap di halaman); kemampuan disediakan tim FE (S-08).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-177: Klik backdrop Popup Edit yang berubah tidak menutup modal

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Ubah Code menjadi `ETI9`
4. Klik area gelap di luar modal
5. Verifikasi modal Edit tetap terbuka
6. Verifikasi input Code `ETI9` dipertahankan
7. Verifikasi tidak ada dialog Unsaved Changes

### TC-FA-FAAM-179: Esc pada Popup Edit yang berubah memunculkan Unsaved Changes

8. Tekan Esc
9. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` tampil
10. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-180: Reload F5 saat Popup Edit berubah memunculkan konfirmasi bawaan browser

11. Tekan F5
12. Verifikasi konfirmasi bawaan browser muncul
13. Pilih tetap di halaman pada konfirmasi bawaan browser

### TC-FA-FAAM-181: Navigasi sidebar saat Popup Edit berubah memunculkan Unsaved Changes

14. Klik menu sidebar lain
15. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` tampil
16. Verifikasi halaman masih Fixed Asset > Settings > Asset Master > Asset Name (route belum berubah)
17. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-178: Field diubah lalu dikembalikan ke nilai awal dianggap bersih

18. Ubah Code dari `ETI9` kembali menjadi `ETI`
19. Klik `[✕]` pada modal Edit
20. Verifikasi modal Edit tertutup
21. Verifikasi baris `Edit Target Item` tampil di tabel
22. Verifikasi tidak ada dialog Unsaved Changes

### TC-FA-FAAM-742: Esc pada Tree Picker yang terbuka di atas modal Edit hanya menutup Tree Picker

23. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
24. Klik `[Select Category]`
25. Tekan Esc
26. Verifikasi Tree Picker tertutup
27. Verifikasi Popup Edit tetap terbuka
28. Verifikasi tidak ada dialog Unsaved Changes
29. Verifikasi teks Category tetap `IT Equipment`
30. Klik `[✕]` pada modal Edit

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `Edit Target Item` pada langkah 1 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 10 dan 17 serta pilihan tetap di halaman pada langkah 13 agar form dirty tetap terbuka untuk TC berikutnya; penutupan modal bersih pada langkah 30 (form tidak dirty, tanpa dialog).
- Urutan TC: TC-FA-FAAM-177, 179, 180, 181 berurutan pada satu pembukaan form dirty (Code `ETI9`), lalu TC-FA-FAAM-178 mengembalikan Code ke `ETI` dan menutup bersih (prinsip 6 bagian 3, S-09). Langkah Uji TC-FA-FAAM-178 ("ubah lalu kembalikan") dijalankan dengan Code `ETI9` yang sudah ada dari TC-FA-FAAM-177.
- Langkah 13 memakai kemampuan menangani dialog `beforeunload` di Prerequisites; form dirty tidak dimuat ulang sungguhan dan tetap terbuka.
- Temuan untuk QA:
  - TC-FA-FAAM-181 Expected "tampil sebelum route berubah" tidak menyebut cara mengamati route; spec mengasersi halaman masih Asset Name sebagai kriterianya (diputuskan penulis).
