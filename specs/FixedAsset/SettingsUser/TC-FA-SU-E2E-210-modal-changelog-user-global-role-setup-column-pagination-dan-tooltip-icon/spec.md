---
id: TC-FA-SU-E2E-210-modal-changelog-user-global-role-setup-column-pagination-dan-tooltip-icon
title: "Modal Changelog User > Global Role: Setup Column, Pagination, dan Tooltip Icon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-631
  - TC-FA-SU-632
  - TC-FA-SU-637
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Setup Column, Pagination, dan Tooltip Icon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-631: Reset to Default, Discard, independensi cache

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Buka Setup Column, sembunyikan satu kolom dan pin satu kolom
3. Klik `[Reset to Default]`
4. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
5. Klik `[Save]`
6. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
7. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
8. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
9. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
10. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
11. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain yang punya Setup Column (User List)
12. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-632: Pagination

14. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
15. Verifikasi default 10 baris per halaman
16. Klik dropdown page size
17. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
18. Tekan Esc untuk menutup pilihan page size
19. Isi nomor halaman `0`, tekan Enter
20. Verifikasi tabel tetap di halaman 1
21. Isi nomor halaman `-1`, tekan Enter
22. Verifikasi tabel tetap di halaman 1
23. Isi nomor halaman `999`, tekan Enter
24. Verifikasi tabel tetap di halaman 1
25. Isi nomor halaman `abc`, tekan Enter
26. Verifikasi tabel tetap di halaman 1
27. Ganti page size ke 25
28. Verifikasi tabel menampilkan halaman 1
29. Ganti page size kembali ke 10
30. Verifikasi tabel menampilkan halaman 1
31. Klik header Date satu kali
32. Verifikasi tabel menampilkan halaman 1
33. Ketik Search `Assign`, tekan Enter
34. Verifikasi tabel menampilkan halaman 1
35. Klik `(←)` pada kotak Search

### TC-FA-SU-637: Tooltip icon Table Tools dan header Actions

36. Hover icon Search
37. Verifikasi tooltip `Search`
38. Hover icon Filter
39. Verifikasi tooltip `Filter`
40. Hover icon Download
41. Verifikasi tooltip `Download`
42. Hover header kolom Actions (⋯)
43. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09). Sesudah muat ulang halaman pada langkah 13, kotak Search User List mempertahankan nilainya (bagian 8b butir 9) sehingga langkah 14 membuka Detail tanpa Search ulang.
- Langkah penghubung tambahan (S-03): langkah 14 (buka ulang Detail > Role > Global Role > icon Changelog) memulihkan modal yang tertutup oleh muat ulang halaman pada langkah 13 sebelum blok pagination (S-14); klik dropdown page size (langkah 16) dan `Esc` (langkah 18) membuka dan menutup pilihan page size untuk `Verifikasi` pilihan page size (TC-FA-SU-632 Langkah 2, S-14).
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) Expected e (fixture hanya satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. (2) Langkah `[Save]` pada langkah 11 ("Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain") ditambahkan spec tanpa dasar TC: TC-FA-SU-631 langkah 5 hanya menutup lewat Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); pemilik TC perlu mengonfirmasi atau menyatakan cara lain. `[Save]` pada langkah 5 berasal dari TC-FA-SU-631 langkah 3 (Reset to Default lalu Save).
