---
id: TC-FA-CF-E2E-067-cancel-dialog-change-data-type-dan-dialog-berurutan
title: "Cancel pada Dialog Change Data Type dan Dialog Berurutan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-227
  - TC-FA-CF-239
coverage:
  web: automated
---

# Cancel pada Dialog Change Data Type dan Dialog Berurutan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Rated Power` (Numeric 1 Decimal Place {Generator, Pump} Specific, bernilai `12.5` pada aset A1; A1 = Asset Name `Pump`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Kemampuan teknis: membaca jumlah entri Changelog tab General, System Log aktor (akun Total Control Sarah Johnson), dan Activity Log sebelum dan sesudah aksi (disediakan tim FE/BE); spec tidak menyimpan perubahan apa pun sehingga baseline jumlah entri yang dicatat sebelum aksi pertama berlaku untuk kedua TC.
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-227: Cancel pada dialog Change Data Type membatalkan Save tanpa perubahan data

2. Catat jumlah entri Changelog tab General, System Log aktor, dan Activity Log
3. Klik row action `⋯` > `Edit` pada baris `Rated Power`
4. Ganti Data Type menjadi `Text`
5. Klik `[Save]`
6. Klik `[Cancel]` pada dialog `Change Data Type`
7. Verifikasi dialog tertutup
8. Verifikasi modal Edit tetap terbuka
9. Verifikasi input dipertahankan: Data Type masih `Text`
10. Klik icon close `[✕]`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Verifikasi kolom Data Type baris `Rated Power` menampilkan `Numeric`
14. Buka Modal Changelog tab General, System Log aktor, dan Activity Log lalu hitung ulang jumlah entri masing-masing, kemudian kembali ke tab General
15. Verifikasi jumlah entri Changelog sama dengan baseline
16. Verifikasi jumlah entri System Log aktor sama dengan baseline
17. Verifikasi jumlah entri Activity Log sama dengan baseline
18. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-239: Cancel pada salah satu dialog berurutan membatalkan seluruh Save

19. Klik row action `⋯` > `Edit` pada baris `Rated Power`
20. Ganti Data Type menjadi `Text`
21. Pilih Value Type `Global` dan isi Value `Generator` dengan `Gen` dan `Pump` dengan `Pmp`
22. Klik `[Save]`
23. Klik `[Change Data Type]` pada dialog `Change Data Type`
24. Klik `[Cancel]` pada dialog `Change to Global Value`
25. Verifikasi seluruh Save dibatalkan: dialog tertutup
26. Verifikasi modal Edit tetap terbuka
27. Klik icon close `[✕]`
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`
30. Verifikasi kolom Data Type baris `Rated Power` menampilkan `Numeric`
31. Verifikasi kolom Value Type baris `Rated Power` menampilkan `Specific`
32. Buka Modal Changelog tab General, System Log aktor, dan Activity Log lalu hitung ulang jumlah entri masing-masing, kemudian kembali ke tab General
33. Verifikasi jumlah entri Changelog sama dengan baseline
34. Verifikasi jumlah entri System Log aktor sama dengan baseline
35. Verifikasi jumlah entri Activity Log sama dengan baseline
36. Buka Detail aset `A1`
37. Verifikasi nilai field `Rated Power` pada Detail aset `A1` tidak berubah (`12.5`)

## Notes

- Urutan TC di spec: 227, 239. Keduanya tidak menyimpan data, sehingga `Rated Power` tetap Numeric untuk kasus kedua tanpa pemulihan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 18 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search; langkah 14 mengembalikan halaman ke ukuran bawaan), langkah 6 dan 23 sampai 24 (membatalkan dialog sebagai aksi TC), langkah 10 sampai 12 dan 27 sampai 29 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- P-1: klausa "tidak ada entri log" pada TC-FA-CF-227 dan TC-FA-CF-239 tetap di spec ini karena menempel pada aksi pembatalan dialog yang dibangun langkah sebelumnya pada field bernilai (dialog `Change Data Type` dan dialog berurutan hanya muncul dari Save field `Rated Power` yang sedang dalam keadaan Edit). Asersi memakai baseline jumlah entri yang dicatat sebelum aksi pertama (S-12), dan jumlah entri yang dicatat itu menjadi anchor positif untuk ketiga surface.
- Spec mencapai 37 langkah. Seluruhnya satu topik (pembatalan dialog konfirmasi pada penggantian Data Type), satu akun, satu field; sekitar 10 langkah adalah blok baca-log berpola (buka surface, hitung, `Verifikasi` jumlah) yang tidak dihitung terhadap batas sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-CF-239 menyebut "dengan Value" tanpa nilai; spec memakai pola `Gen` dan `Pmp` dari TC-FA-CF-238.
  - Cara membuka System Log aktor dan Activity Log serta halaman Detail aset `A1` tidak dijelaskan di TC (menu atau jalur navigasi); spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
