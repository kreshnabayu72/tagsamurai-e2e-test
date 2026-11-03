---
id: TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu
title: "Persistensi State List: F5, Back Browser, Search Sidebar, dan Klik Ulang Menu Group"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-227
  - TC-AC-SG-228
  - TC-AC-SG-229
  - TC-AC-SG-230
coverage:
  web: automated
---

# Persistensi State List: F5, Back Browser, Search Sidebar, dan Klik Ulang Menu Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #20), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Nilai yang dipakai: `Region A` memiliki descendant `Branch 1` dan `Branch 2` (Modified By `Admin B`); Total User bervariasi (2 sampai 5) sehingga sort Total User bermakna (S-11).
- Akses ke menu `Settings > User` pada sidebar navigasi Admin Console (Pre-setup #40) untuk TC-AC-SG-228.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-227: F5 mempertahankan Search, Sort, Filter, Pagination, dan node sidebar terpilih

1. Klik node `Region A` di sidebar
2. Ketik Search `Branch`, tekan Enter
3. Klik header kolom Total User sekali (ascending)
4. Klik ikon Filter pada toolbar
5. Pilih `Admin B` pada Modified By, klik `[Apply]`
6. Pilih page size 25
7. Tekan F5
8. Verifikasi node `Region A` tetap terpilih di sidebar
9. Verifikasi Search `Branch` dipertahankan
10. Verifikasi sort Total User ascending dipertahankan
11. Verifikasi filter Modified By `Admin B` dipertahankan
12. Verifikasi page size 25 dipertahankan
13. Verifikasi halaman aktif dipertahankan (halaman 1)

### TC-AC-SG-228: Back browser setelah berpindah halaman mempertahankan state List

14. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
15. Ketik Search `Region`, tekan Enter
16. Pilih page size 25
17. Klik menu `Settings > User`
18. Klik tombol Back browser
19. Verifikasi Search `Region` dipertahankan
20. Verifikasi page size 25 dipertahankan
21. Verifikasi node sidebar terpilih sama seperti sebelumnya (`All Groups`)

### TC-AC-SG-229: Search sidebar dan state expand tidak dipertahankan setelah F5

22. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
23. Ketik `Branch` pada Search sidebar
24. Collapse node `Region A`
25. Tekan F5
26. Verifikasi input Search sidebar kosong
27. Verifikasi seluruh tree kembali ter-expand default

### TC-AC-SG-230: Klik ulang menu Group dari sidebar navigasi mereset ke default

28. Ketik Search `Region`, tekan Enter
29. Klik node `Region A` di sidebar
30. Klik menu `Settings > Group` pada sidebar navigasi
31. Verifikasi Search kosong
32. Verifikasi sort default Group A-Z
33. Verifikasi node `All Groups` terpilih
34. Verifikasi halaman aktif 1 (fresh entry)
35. Pilih page size 10

## Notes

- Langkah penghubung (S-03): langkah 14 dan 22 (klik menu `Settings > Group` pada sidebar navigasi mereset Search, Sort, dan Filter sebelum blok berikutnya; perilaku yang sama diuji TC-AC-SG-230, S-09), dan langkah 35 (memulihkan page size bawaan 10 sesudah blok terakhir, S-09).
- Langkah 6 menambah perubahan page size supaya Expected TC-AC-SG-227 "halaman aktif dan page size dipertahankan" dapat diasersi (S-14); langkah TC tidak mengubah halaman atau page size.
- Temuan untuk QA:
  - TC-AC-SG-227: langkah TC tidak menyebut perubahan page size atau pindah halaman padahal Expected menyebutnya; dengan hasil 2 baris (Search `Branch`, Modified By `Admin B`, node `Region A`) halaman 2 tidak tersedia, sehingga hanya halaman 1 yang diasersi. Usulan: tambahkan langkah pindah halaman pada data yang lebih dari satu halaman.
  - TC-AC-SG-228: Expected menyebut "node sidebar terpilih yang sama" tanpa node yang dipilih di langkah; spec memakai `All Groups` (node bawaan).
  - TC-AC-SG-230: Expected "sort default Group A-Z" tidak didahului langkah yang mengubah sort.
