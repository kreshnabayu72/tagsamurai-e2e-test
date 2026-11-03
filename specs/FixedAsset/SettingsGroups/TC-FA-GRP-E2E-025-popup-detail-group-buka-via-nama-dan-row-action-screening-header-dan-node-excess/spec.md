---
id: TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess
title: "Popup Detail Group: Buka via Nama dan Row Action, Screening Header Stacked Read-Only, Function None, dan Node Excess"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-270
  - TC-FA-GRP-271
  - TC-FA-GRP-272
  - TC-FA-GRP-273
  - TC-FA-GRP-274
coverage:
  web: automated
---

# Popup Detail Group: Buka via Nama dan Row Action, Screening Header Stacked Read-Only, Function None, dan Node Excess

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Head Office (Function None, Description kosong) > Floor 2 > IT Department (Code `ITD`, Description terisi, Function Assignable); Warehouse A; Warehouse B (Excess). Spec ini tidak menjalankan aksi tulis.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-270: Buka Popup Detail Group via klik nama

1. Klik toggle expand-all pada sidebar
2. Klik Floor 2 di sidebar
3. Klik nama IT Department di tabel
4. Verifikasi Popup Detail Group terbuka (modal besar, body scrollable)
5. Tutup popup dengan [X]

### TC-FA-GRP-271: Buka Popup Detail Group via row action Detail dan elipsis sidebar

6. Klik node `All Groups` di sidebar
7. Ketik Search `Warehouse A`, tekan Enter
8. Klik (⋯) pada baris Warehouse A
9. Klik `Detail`
10. Verifikasi Popup Detail Group Warehouse A terbuka
11. Tutup popup dengan [X]
12. Klik (⋯) pada node Warehouse A di sidebar
13. Klik `Detail`
14. Verifikasi Popup Detail Group yang sama (Warehouse A) terbuka dari elipsis sidebar
15. Tutup popup dengan [X]
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-GRP-272: Screening header Popup Detail Group

17. Klik Floor 2 di sidebar
18. Klik (⋯) pada baris IT Department
19. Klik `Detail`
20. Verifikasi Title popup `Group Detail` (flat, tidak diinterpolasi)
21. Verifikasi Group Name berupa full path `Head Office > Floor 2 > IT Department` disertai badge Assignable pada baris yang sama
22. Verifikasi Code `ITD` pada baris terpisah
23. Verifikasi Description full-width dan terisi
24. Verifikasi ikon close [X] tampil
25. Verifikasi tidak ada tombol Edit atau Delete dan tidak ada Section Impact Summary
26. Verifikasi Body memuat Tab Assets (aktif default) dan Tab Users
27. Tutup popup dengan [X]

### TC-FA-GRP-273: Header Detail Function None dan Description kosong

28. Klik node `All Groups` di sidebar
29. Ketik Search `Head Office`, tekan Enter
30. Klik (⋯) pada baris Head Office
31. Klik `Detail`
32. Verifikasi badge Function tidak dirender
33. Verifikasi Description tampil `—`
34. Tutup popup dengan [X]

### TC-FA-GRP-274: Header Detail node Excess

35. Ganti isi kotak search dengan `Warehouse B`, tekan Enter
36. Klik (⋯) pada baris Warehouse B
37. Klik `Detail`
38. Verifikasi Popup Detail Group terbuka (Detail tidak kena CRU Lock)
39. Hover Group Name di header popup
40. Verifikasi Group Name di-dim tanpa badge tambahan
41. Verifikasi tooltip `Read-only — over your plan's group limit` tampil
42. Tutup popup dengan [X]

## Notes

- Spec melewati sekitar 35 langkah (42 langkah): seluruh blok adalah satu kelas (screening Popup Detail Group, hanya membaca) pada dataset Tabel A yang sama, tiap blok berdiri sendiri, dan memisahkannya hanya menggandakan login, hook, dan cleanup.
- Langkah penghubung (S-03): langkah 1 (expand-all), langkah 6, 17, 28 (memilih node agar baris target tampil), langkah 5, 11, 15, 27, 34, 42 (menutup popup). Langkah 7, 29, dan 35 (Search `Warehouse A`, `Head Office`, lalu ganti isi kotak search dengan `Warehouse B`) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; langkah 16 (`(←)` pada kotak Search) mengembalikan tabel penuh sebelum memilih node berikutnya (R-16).
- Urutan TC dalam spec: 270, 271, 272, 273, 274.
- Temuan untuk QA:
  - TC-FA-GRP-272 tidak menyebut isi Description; spec mengasersi Description terisi sesuai precondition.
