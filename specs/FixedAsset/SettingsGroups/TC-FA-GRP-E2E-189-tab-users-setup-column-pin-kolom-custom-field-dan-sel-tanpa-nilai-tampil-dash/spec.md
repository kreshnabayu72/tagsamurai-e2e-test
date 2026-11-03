---
id: TC-FA-GRP-E2E-189-tab-users-setup-column-pin-kolom-custom-field-dan-sel-tanpa-nilai-tampil-dash
title: "Tab Users Setup Column: Pin Kolom Custom Field dan Sel Tanpa Nilai Tampil Dash (Bukan Blank)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-664
  - TC-FA-GRP-1061
coverage:
  web: automated
---

# Tab Users Setup Column: Pin Kolom Custom Field dan Sel Tanpa Nilai Tampil Dash (Bukan Blank)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user, termasuk user tanpa Position, user tanpa Division, user non-Temporary (Temporary Until kosong), user tanpa TAG, dan user tanpa nilai pada Custom Field aktif Phone (Data Dinamis, dibaca saja). Data ini tidak punya tabel konkret di TC (lihat Temuan untuk QA).
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Lebar viewport 900px sehingga tabel dapat di-scroll horizontal; viewport disetel pada langkah 2 dan dipulihkan pada langkah 34.
- Kolom Temporary Until, TAG, dan Custom Field Phone adalah kolom curated yang ditampilkan lewat Column Visibility; pemulihan lewat hook `after`.

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Setel lebar viewport 900px

### TC-664: Pin kolom Custom Field Phone

3. Buka Popup Setup Column
4. Centang kolom Custom Field aktif Phone
5. Klik icon Pin Custom Field aktif Phone
6. Klik [Save]
7. Scroll tabel horizontal
8. Verifikasi kolom Custom Field aktif Phone membeku (sticky) saat scroll horizontal
9. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
10. Scroll tabel horizontal
11. Verifikasi pin bertahan setelah F5 (kolom tetap membeku)
12. Buka Popup Setup Column, unpin kolom Custom Field aktif Phone, lalu klik [Save]
13. Scroll tabel horizontal
14. Verifikasi setelah unpin kolom kembali ikut scroll

### TC-1061: Sel tanpa nilai tampil dash

15. Tampilkan kolom Temporary Until, TAG, dan Custom Field aktif Phone via Column Visibility
16. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat nama satu user tanpa Position, satu user tanpa Division, satu user non-Temporary, satu user tanpa TAG, dan satu user tanpa nilai Custom Field aktif Phone
17. Kembali ke halaman 1 pagination tabel
18. Ketik Search nama user tanpa Position yang dicatat pada langkah 16, tekan Enter
19. Verifikasi sel Position user itu tampil `—`
20. Verifikasi sel tersebut tidak blank dan tidak berisi teks null
21. Ganti isi kotak search dengan nama user tanpa Division yang dicatat pada langkah 16, tekan Enter
22. Verifikasi sel Division user itu tampil `—`
23. Verifikasi sel tersebut tidak blank dan tidak berisi teks null
24. Ganti isi kotak search dengan nama user non-Temporary yang dicatat pada langkah 16, tekan Enter
25. Verifikasi sel Temporary Until user itu tampil `—`
26. Verifikasi sel tersebut tidak blank dan tidak berisi teks null
27. Ganti isi kotak search dengan nama user tanpa TAG yang dicatat pada langkah 16, tekan Enter
28. Verifikasi sel TAG user itu tampil `—`
29. Verifikasi sel tersebut tidak blank dan tidak berisi teks null
30. Ganti isi kotak search dengan nama user tanpa nilai Custom Field aktif Phone yang dicatat pada langkah 16, tekan Enter
31. Verifikasi sel Custom Field aktif Phone user itu tampil `—`
32. Verifikasi sel tersebut tidak blank dan tidak berisi teks null
33. Klik `(←)` pada kotak Search
34. Pulihkan lebar viewport

## Notes

- Langkah penghubung (S-03): `Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A`, scroll horizontal sebelum asersi, dan unpin di akhir TC-664.
- Spec memiliki 34 langkah, di bawah smell 35 langkah. Scroll horizontal membutuhkan tabel yang lebih lebar dari viewport; spec menyetel lebar viewport 900px (langkah 2) dan memulihkannya (langkah 34), pola spec 186.
- User tanpa nilai tidak dijamin berada di halaman 1 (page size 10, >= 12 user): langkah 16 menelusuri semua halaman dan mencatat nama user target, lalu tiap user dicari lewat Search (S-14). Satu `Verifikasi` per klausa (S-01): nilai `—` dan tidak blank/null dipisah.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - TC-1061 menyebut data user tanpa nilai tanpa tabel konkret; spec memakai Warehouse A (Prerequisites).
  - TC-664 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
