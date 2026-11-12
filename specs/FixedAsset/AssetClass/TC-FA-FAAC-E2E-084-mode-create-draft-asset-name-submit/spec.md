---
id: TC-FA-FAAC-E2E-084-mode-create-draft-asset-name-submit
title: "Mode Create: Submit Asset Class Baru dengan Draft Asset Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-259
  - TC-FA-FAAC-654
  - TC-FA-FAAC-655
coverage:
  web: automated
---

# Mode Create: Submit Asset Class Baru dengan Draft Asset Name

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Pelaku kedua (blok TC-655): sesi API aktor (login API password, token tidak dihitung sebagai sesi web; lihat `suite.md`); bukan konteks UI kedua.
- Data Dinamis (field wajib "sesuai tabel Data Uji"): Class Code `TRUCK-084`; Class Name `Truck Equipment {runId}-084`; Method Straight Line; Useful Life 96; Depreciation Start Convention "Full month from in-service date"; Tax Depreciation Class "Bukan bangunan – Kelompok 2"; Tax Method "Declining Balance"; Tax Depreciation Start Rule "Month of expenditure". Asset Class ini dibuat ulang pada tiap blok TC dengan Class Code yang sama setelah yang sebelumnya dihapus lewat fixture BE; dihapus juga di hook `after`.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after` dan di langkah penghubung): tanpa Asset Class: Forklift 3T (6 aset aktif), Laptop Standard (120 aset aktif), Pallet Jack Electric (0 aset aktif), Meeting Table (0 aset aktif); Asset Name "Delivery Van" ter-assign ke 'Vehicles'; Asset Class Active 'Machinery' (MACHINERY). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed, penghapusan Asset Class, dan pemulihan keanggotaan Asset Name lewat fixture BE; sesi API aktor untuk assign Asset Name; kemampuan baca BE untuk jumlah entri Changelog (audit trail permanen, S-12).
- State global: keanggotaan Asset Name dan Asset Class `TRUCK-084` berubah; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-259: Submit Asset Class baru dengan draft Asset Name meng-assign draft ke Asset Class yang dibuat

1. Klik tombol "+ Asset Class"
2. Isi field wajib tab General dan Depreciation sesuai tabel Data Uji
3. Klik tab "Asset Names"
4. Klik tombol "+ Assign Asset Names"
5. Centang "Forklift 3T" dan "Laptop Standard"
6. Klik [Assign]
7. Klik [Submit] di footer
8. Verifikasi muncul toast sukses: "Success, asset class has been created."
9. Verifikasi halaman tetap terbuka dalam mode Edit dengan tab Asset Names aktif
10. Verifikasi "Forklift 3T" dan "Laptop Standard" tampil di tabel tab Asset Names sebagai Asset Name ter-assign (bukan lagi draft)

### TC-FA-FAAC-654: Submit Create dengan draft Asset Name menulis satu L-01 dan satu L-06 per Asset Name

11. Hapus Asset Class `TRUCK-084` dan pulihkan "Forklift 3T" dan "Laptop Standard" menjadi tanpa Asset Class lewat fixture BE
12. Klik breadcrumb "Asset Class"
13. Baca jumlah entri Changelog sebagai baseline
14. Klik tombol "+ Asset Class"
15. Isi field wajib tab General dan Depreciation sesuai tabel Data Uji
16. Klik tab "Asset Names"
17. Klik tombol "+ Assign Asset Names"
18. Centang "Forklift 3T" dan "Laptop Standard"
19. Klik [Assign]
20. Klik [Submit] di footer
21. Tunggu aksi selesai
22. Klik breadcrumb "Asset Class" (kembali ke tabel Asset Class)
23. Klik ikon Changelog (modal "Changelog: Asset Class")
24. Verifikasi selisih jumlah entri Changelog terhadap baseline langkah 13 adalah 3
25. Verifikasi satu entri L-01: Action "Create", Class Code `TRUCK-084`, Field "Class Code", Old Value "—", New Value `TRUCK-084`
26. Verifikasi dua entri L-06: Action "Edit", Class Code `TRUCK-084`, Field "Asset Names", Old Value "—", New Value "Forklift 3T" pada satu entri dan "Laptop Standard" pada entri lain (satu entri per Asset Name)
27. Verifikasi Modified By berisi aktor (format `[First Name] [Last Initial]`)

### TC-FA-FAAC-655: Submit Create melewati draft Asset Name yang sudah di-assign ke Asset Class lain

28. Tutup modal Changelog, lalu hapus Asset Class `TRUCK-084` dan pulihkan "Forklift 3T" dan "Laptop Standard" lewat fixture BE
29. Klik tombol "+ Asset Class"
30. Isi field wajib tab General dan Depreciation sesuai tabel Data Uji
31. Klik tab "Asset Names"
32. Klik tombol "+ Assign Asset Names"
33. Centang "Pallet Jack Electric" dan "Meeting Table"
34. Klik [Assign]
35. Assign "Pallet Jack Electric" ke Asset Class "Machinery" (MACHINERY) lewat sesi API aktor hingga tersimpan
36. Klik [Submit] di footer pada sesi pertama
37. Verifikasi Asset Class `TRUCK-084` tetap dibuat: toast sukses "Success, asset class has been created."
38. Verifikasi "Pallet Jack Electric" dilewati (tetap di MACHINERY) dan tidak tampil di tab Asset Names `TRUCK-084`
39. Verifikasi "Meeting Table" ter-assign ke `TRUCK-084` dan tampil di tab Asset Names

## Notes

- Class Code `TRUCK-084` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98) sehingga suffix itu tidak muat; `{runId}-084` dipindah ke Class Name agar unik per run (S-12; pola spec 066 sampai 069 dan 047/048); cleanup di hook `before` dan `after`.
- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 259, 654, 655 (tiap TC membuat Asset Class dengan Class Code yang sama; langkah 11 dan 28 menghapus hasil blok sebelumnya).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name dan Asset Class seed dipakai apa adanya; Class Code "TRUCK-EQ" pada TC ditulis `TRUCK-084` (maks 15 karakter); `{runId}-084` ada di Class Name (lihat butir Class Code 15 karakter).
- Langkah penghubung (S-03): langkah 11, 12, 13, 21 (Tunggu aksi selesai), 22, 23, 28 (pemulihan dan navigasi); langkah 22 membuka tabel karena halaman tetap di mode Edit setelah Submit Create (Expected TC-259 butir b).
- Spec di atas 35 langkah (39 langkah): tiga TC satu topik (Submit Create dengan draft Asset Name) pada dataset yang sama; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan tiap TC membutuhkan alur Create penuh; memecah lagi menggandakan seed dan pemulihan tanpa pemisah nyata.
- Temuan untuk QA: TC-259 menyebut "isi field wajib tab General dan Depreciation sesuai Data Uji" tanpa memuat field tab Accounts; spec mengisi hanya field yang tertulis di Data Uji. TC-654 tidak menyebut urutan dua entri L-06, sehingga spec mengasersi himpunan baris teratas sebanyak selisih tanpa mengandalkan urutan di antaranya (S-14); TC-655 tidak menyebut log untuk Asset Name yang dilewati.
