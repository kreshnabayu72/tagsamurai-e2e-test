---
id: TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom
title: "Setup Column: Overlay, Popup, Discard, dan Batas Satu Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-407
  - TC-FA-CF-408
  - TC-FA-CF-414
  - TC-FA-CF-415
  - TC-FA-CF-417
coverage:
  web: automated
---

# Setup Column: Overlay, Popup, Discard, dan Batas Satu Kolom

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: drag handle pada daftar kolom, hover tooltip pada checkbox, dan muat ulang halaman (F5).
- State global: preferensi kolom tabel utama tersimpan di browser (Overlay Column Visibility berlaku langsung tanpa `[Save]`). Kolom `Value Type` disembunyikan pada langkah 18 dan ditampilkan kembali pada langkah 24. Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-CF-407: Screening Overlay Column Visibility menampilkan sepuluh kolom dan item Setup Column

1. Klik header kolom Actions `(⋯)`
2. Verifikasi Overlay Column Visibility tampil sebagai overlay (bukan popup)
3. Verifikasi overlay memuat daftar sepuluh kolom data berurutan dengan checkbox tercentang: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`
4. Verifikasi setiap kolom pada daftar overlay dapat di-reorder dengan drag handle
5. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
6. Verifikasi kolom `Checkbox` dan `Actions` tidak muncul sebagai baris pada daftar overlay

### TC-FA-CF-408: Screening Popup Setup Column memuat judul, deskripsi, daftar kolom, live preview, dan footer

7. Klik `Setup Column...`
8. Verifikasi Header: judul `Setup Column`
9. Verifikasi Header: teks `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi Header: icon close `[✕]` tampil
11. Verifikasi Body: sepuluh kolom ber-checkbox tercentang
12. Verifikasi Body: drag handle dan icon Pin tampil pada tiap kolom
13. Verifikasi Body: Live Preview tabel tampil
14. Verifikasi Footer: `[Reset to Default]` dan `[Save]` tampil rata kanan
15. Verifikasi Footer tidak memuat `[Cancel]`
16. Klik icon `[✕]` untuk menutup popup

### TC-FA-CF-417: Perubahan di Overlay Column Visibility langsung berlaku tanpa tombol Save

17. Klik header kolom Actions `(⋯)`
18. Hapus centang `Value Type` pada Overlay Column Visibility
19. Verifikasi kolom `Value Type` langsung hilang dari tabel
20. Verifikasi Overlay Column Visibility tidak memiliki tombol `[Save]`
21. Muat ulang halaman (F5)
22. Verifikasi header kolom `Field Name` tampil pada tabel
23. Verifikasi kolom `Value Type` tetap hilang dari tabel setelah reload
24. Klik header kolom Actions `(⋯)`, centang kembali `Value Type`, lalu tutup overlay

### TC-FA-CF-414: Menutup popup dengan icon close atau Esc membuang perubahan preview

25. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
26. Hapus centang `Placeholder` pada Popup Setup Column
27. Klik icon `[✕]`
28. Verifikasi Popup Setup Column tertutup
29. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom `Placeholder` tetap tampil)
30. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
31. Hapus centang `Placeholder` pada Popup Setup Column
32. Tekan `Esc`
33. Verifikasi Popup Setup Column tertutup
34. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom `Placeholder` tetap tampil)

### TC-FA-CF-415: Kolom yang menjadi satu-satunya kolom visible tidak dapat di-uncheck

35. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
36. Hapus centang sembilan kolom hingga tersisa `Field Name` (`Active`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`)
37. Arahkan kursor ke checkbox `Field Name`
38. Verifikasi checkbox `Field Name` disabled dengan tooltip `At least one column must remain visible.`
39. Klik icon `[✕]` untuk menutup popup tanpa menyimpan

## Notes

- Spec memuat 39 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (Overlay dan Popup Setup Column tabel utama), satu akun, satu dataset (Company Alpha baseline), tanpa membuat atau mengubah data; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan memecahnya hanya menambah login dan hook.
- Urutan TC di spec: 407, 408, 417, 414, 415. TC-FA-CF-417 diletakkan sebelum 414 supaya visibilitas kolom yang disimpannya dipulihkan (langkah 24) sebelum TC-FA-CF-414 yang mengandalkan kolom `Placeholder` tampil (S-09); TC-FA-CF-415 di akhir karena membuang perubahan lewat `[✕]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 (menutup popup), langkah 24 (memulihkan kolom `Value Type` dan menutup overlay), langkah 39 (menutup popup tanpa menyimpan).
- Anchor absence: langkah 22 (header `Field Name` tampil) mendahului absence langkah 23 (bagian 8b butir 2); absence langkah 6 dan 15 didahului daftar kolom dan footer yang tampil pada langkah 3 dan 14.
- Temuan untuk QA:
  - TC-FA-CF-407 Expected b ("dapat di-reorder dengan drag handle") dibaca sebagai ketersediaan drag handle pada tiap kolom; langkah uji TC tidak menyeret kolom (reorder diuji TC-FA-CF-410).
  - TC-FA-CF-408 Expected "rata kanan" tidak menyatakan cara memeriksa posisi; spec menyatakannya pada Verifikasi footer.
  - TC-FA-CF-417 Expected "tanpa tombol Save" tidak menyatakan elemen yang diperiksa; spec memeriksa bahwa Overlay Column Visibility tidak memuat tombol `[Save]`.
  - TC-FA-CF-415 langkah 2 ("sembilan kolom") tidak menyebut daftarnya; spec memakai semua kolom selain `Field Name`.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
