---
id: TC-FA-CF-E2E-068-cancel-remove-value-value-type-dan-change-scope
title: "Cancel pada Dialog Remove Value, Value Type, dan Change Scope"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-250
  - TC-FA-CF-267
  - TC-FA-CF-622
coverage:
  web: automated
---

# Cancel pada Dialog Remove Value, Value Type, dan Change Scope

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`, A1 = `Gold`), `Voltage Spec` (Text {Generator, Pump} Global `220V` dan `110V`), dan `Rated Power` (Numeric 1 Decimal Place {Generator, Pump}, bernilai `12.5` pada aset A1; A1 = Asset Name `Pump`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Kemampuan teknis: membaca jumlah entri Changelog tab General, System Log aktor (akun Total Control Sarah Johnson), dan Activity Log sebelum dan sesudah aksi (disediakan tim FE/BE); spec tidak menyimpan perubahan apa pun sehingga baseline jumlah entri yang dicatat sebelum aksi pertama yang diasersi berlaku untuk TC-FA-CF-267 dan TC-FA-CF-622.
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-250: Cancel pada dialog Remove Value mempertahankan opsi

2. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
3. Klik `✕` pada badge `Gold`
4. Klik `[Cancel]` pada dialog `Remove Value`
5. Verifikasi dialog tertutup
6. Verifikasi badge `Gold` tetap ada pada form
7. Klik icon close `[✕]`

### TC-FA-CF-267: Cancel pada dialog Value Type membatalkan Save

8. Catat jumlah entri Changelog tab General, System Log aktor, dan Activity Log
9. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
10. Pilih Value Type `Specific`
11. Klik `[Save]`
12. Klik `[Cancel]` pada dialog `Change to Specific Value`
13. Verifikasi dialog tertutup
14. Verifikasi modal tetap terbuka
15. Klik icon close `[✕]`
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]`
18. Verifikasi kolom Value Type baris `Voltage Spec` menampilkan `Global`
19. Buka Modal Changelog tab General, System Log aktor, dan Activity Log lalu hitung ulang jumlah entri masing-masing, kemudian kembali ke tab General
20. Verifikasi jumlah entri Changelog sama dengan baseline
21. Verifikasi jumlah entri System Log aktor sama dengan baseline
22. Verifikasi jumlah entri Activity Log sama dengan baseline
23. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-622: Cancel pada dialog Change Scope membatalkan Save tanpa perubahan data

24. Klik row action `⋯` > `Edit` pada baris `Rated Power`
25. Hapus chip `Pump` dari Scope
26. Klik `[Save]`
27. Klik `[Cancel]` pada dialog `Change Scope`
28. Verifikasi dialog tertutup
29. Verifikasi modal Edit tetap terbuka
30. Verifikasi input dipertahankan: Scope tanpa chip `Pump`
31. Klik icon close `[✕]`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`
34. Verifikasi kolom Scope baris `Rated Power` menampilkan `Generator` dan `Pump`
35. Buka Modal Changelog tab General, System Log aktor, dan Activity Log lalu hitung ulang jumlah entri masing-masing, kemudian kembali ke tab General
36. Verifikasi jumlah entri Changelog sama dengan baseline
37. Verifikasi jumlah entri System Log aktor sama dengan baseline
38. Verifikasi jumlah entri Activity Log sama dengan baseline
39. Buka Detail aset `A1`
40. Verifikasi nilai field `Rated Power` pada Detail aset `A1` tidak dibuang (`12.5`)

## Notes

- Urutan TC di spec: 250, 267, 622. Ketiganya tidak menyimpan data, sehingga field target tidak berubah antar kasus.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 23 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search; langkah 19 mengembalikan halaman ke ukuran bawaan), langkah 4, 12, dan 27 (membatalkan dialog sebagai aksi TC), langkah 7 (menutup modal yang tidak berubah: Cancel mempertahankan opsi sehingga form tidak dirty), langkah 15 sampai 17 dan 31 sampai 33 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- P-1: klausa "tidak ada entri log" pada TC-FA-CF-267 dan TC-FA-CF-622 tetap di spec ini karena menempel pada aksi pembatalan dialog yang hanya muncul dari Save field bernilai yang sedang dalam keadaan Edit. Asersi memakai baseline jumlah entri yang dicatat sebelum aksi (S-12), dan jumlah entri yang dicatat itu menjadi anchor positif untuk ketiga surface.
- Spec mencapai 40 langkah. Seluruhnya satu topik (pembatalan dialog konfirmasi pada modal Edit), satu akun, satu dataset Company Nilai; ketiga blok memakai field berbeda dan berdiri sendiri. Sekitar 10 langkah adalah blok baca-log berpola (buka surface, hitung, `Verifikasi` jumlah) yang tidak dihitung terhadap batas sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-CF-250 tidak memuat klausa log; hanya TC-FA-CF-267 dan TC-FA-CF-622 yang menyebut ketiadaan entri log.
  - Cara membuka System Log aktor dan Activity Log serta halaman Detail aset `A1` tidak dijelaskan di TC (menu atau jalur navigasi); spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
