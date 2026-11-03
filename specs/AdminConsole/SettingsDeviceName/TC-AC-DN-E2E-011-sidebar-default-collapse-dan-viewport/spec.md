---
id: TC-AC-DN-E2E-011-sidebar-default-collapse-dan-viewport
title: "Category Sidebar: Default Terbuka, Collapse, Open Kembali, Persistensi per User, dan Viewport 1279/1280 px"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-31
  - TC-AC-DN-32
  - TC-AC-DN-33
  - TC-AC-DN-34
  - TC-AC-DN-628
coverage:
  web: automated
---

# Category Sidebar: Default Terbuka, Collapse, Open Kembali, Persistensi per User, dan Viewport 1279/1280 px

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Device Name inti (#16), dan seed 120 Device Name (#17); baca-saja. Preferensi state Sidebar akun uji belum tersimpan pada TC-AC-DN-31 dan TC-AC-DN-628. Tidak ada data Dinamis.
- Kemampuan teknis (disediakan tim FE/BE): menghapus preferensi state Category Sidebar milik akun uji (reset ke kunjungan pertama), dijalankan di hook `before` spec ini dan sebagai langkah penghubung sebelum TC yang mensyaratkan preferensi belum tersimpan; hook `after` memulihkan Sidebar ke keadaan terbuka tanpa preferensi tersimpan; mengubah lebar viewport dan memulihkannya.
- State global yang diubah spec ini: preferensi state collapsed Category Sidebar milik akun uji (dipulihkan seperti di atas) dan lebar viewport (dipulihkan ke ukuran awal suite, minimal 1280 px).

## Test Steps

### TC-AC-DN-31: Category Sidebar terbuka dan tanpa filter efektif pada kunjungan pertama

1. Verifikasi Category Sidebar terbuka di sisi kanan layar dengan Floating toggle bertanda `▶` di tepi kiri panel
2. Hover Floating toggle
3. Verifikasi tooltip Floating toggle: `Collapse Category Tree`
4. Verifikasi tidak ada node yang terpilih (filter efektif kosong)
5. Verifikasi List memuat Device Name dari kategori Perangkat Pemindai Kode Batang Industri, Accessory, Antenna, UHF Handheld, dan Tag

### TC-AC-DN-32: Collapse Category Sidebar melebarkan List dan mengganti Floating toggle

6. Klik Floating toggle `▶` di tepi kiri panel Sidebar
7. Verifikasi Category Sidebar tidak tampil
8. Verifikasi area List melebar mengisi ruang sebelumnya
9. Verifikasi Floating toggle berada di tepi kanan layar dengan ikon `◀`
10. Hover Floating toggle
11. Verifikasi tooltip Floating toggle: `Open Category Tree`

### TC-AC-DN-33: Open kembali Category Sidebar dari kondisi collapsed

12. Klik Floating toggle `◀` di tepi kanan layar
13. Klik Floating toggle `▶` di tepi kiri panel Sidebar
14. Klik Floating toggle `◀` di tepi kanan layar
15. Verifikasi Category Sidebar tampil kembali di sisi kanan dengan pohon Category
16. Verifikasi Floating toggle kembali bertanda `▶` di tepi kiri panel
17. Hover Floating toggle
18. Verifikasi tooltip Floating toggle: `Collapse Category Tree`

### TC-AC-DN-34: State collapsed Sidebar dipertahankan per user per halaman setelah refresh

19. Klik Floating toggle `▶` di tepi kiri panel Sidebar
20. Refresh halaman dengan F5
21. Verifikasi setelah refresh Category Sidebar tetap tertutup
22. Verifikasi setelah refresh Floating toggle `◀` berada di tepi kanan layar
23. Verifikasi List tetap tampil
24. Verifikasi tidak ada error
25. Klik Floating toggle `◀` di tepi kanan layar

### TC-AC-DN-628: Category Sidebar tersembunyi pada viewport 1279 px dan terbuka pada 1280 px tanpa menimpa preferensi tersimpan

26. Hapus preferensi state Sidebar akun uji (kunjungan pertama)
27. Atur lebar viewport 1280 px
28. Buka ulang halaman `Settings > Device > Device Name`
29. Verifikasi pada 1280 px Category Sidebar terbuka di sisi kanan
30. Verifikasi pada 1280 px Floating toggle bertanda `▶` di tepi kiri panel
31. Ubah lebar viewport menjadi 1279 px
32. Verifikasi pada 1279 px Category Sidebar tersembunyi
33. Verifikasi pada 1279 px area List melebar
34. Verifikasi pada 1279 px Floating toggle `◀` tampil di tepi kanan layar
35. Klik Floating toggle di tepi kanan layar
36. Verifikasi setelah toggle diklik pada 1279 px Category Sidebar terbuka
37. Ubah lebar viewport kembali menjadi 1280 px
38. Verifikasi setelah viewport kembali 1280 px Category Sidebar terbuka sesuai state tersimpan (auto-collapse karena breakpoint tidak menimpa preferensi)
39. Pulihkan lebar viewport ke ukuran awal suite

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 12 membuka kembali Sidebar yang ditutup TC-AC-DN-32 supaya langkah TC-AC-DN-33 (tutup lalu buka) mulai dari Sidebar terbuka; langkah 25 membuka kembali Sidebar sesudah TC-AC-DN-34 karena state collapsed tersimpan per user; langkah 26 menghapus preferensi sebelum TC-AC-DN-628 yang mensyaratkan kunjungan pertama; langkah 39 memulihkan viewport.
- Ukuran spec (39 langkah, di atas smell sekitar 35 langkah): alasan R3 (bagian 3 prinsip 13). Seluruh TC memakai satu topik (Category Sidebar), satu dataset, dan satu kelas harness; tiap TC memulai dari state yang ditegakkan eksplisit (langkah 12, 25, 26) sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal. Langkah bertambah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- TC-AC-DN-628 dijalankan sesudah TC-AC-DN-34 karena bergantung pada penghapusan preferensi (langkah 26); spec tidak mengandalkan pembukaan ulang halaman untuk mereset state.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
