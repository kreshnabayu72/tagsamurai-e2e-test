---
id: TC-AC-DC-E2E-007-floating-toggle-sidebar
title: "Floating Open/Collapse Toggle Button Sidebar Category: Tutup dan Buka, Persistensi per User, dan State Independen per Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-17
  - TC-AC-DC-18
  - TC-AC-DC-19
coverage:
  web: automated
---

# Floating Open/Collapse Toggle Button Sidebar Category: Tutup dan Buka, Persistensi per User, dan State Independen per Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah dan dipulihkan: state Open atau Collapsed sidebar per user dan per halaman (localStorage browser) serta pilihan filter Category. Kemampuan menghapus preferensi sidebar tersimpan (kunci localStorage ditunjuk tim FE dari PRD; tidak dikarang di spec ini) disediakan tim FE; hook `before` dan `after` memakainya, dan langkah 18 memakainya untuk membentuk kunjungan pertama.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-17: Floating Toggle Button menutup dan membuka kembali Sidebar Category

1. Expand `Hardware` dan `Handheld Reader`, lalu klik node `Dipakai Leaf`
2. Hover tombol toggle di tepi kiri panel
3. Verifikasi tombol toggle berada di tepi kiri panel
4. Verifikasi tombol toggle memakai ikon panah kanan
5. Verifikasi tooltip tombol toggle berisi "Collapse Category Tree"
6. Klik tombol toggle
7. Verifikasi sidebar tidak tampil
8. Verifikasi tabel Device Name melebar penuh
9. Hover tombol toggle di tepi kanan layar
10. Verifikasi tombol toggle berada di tepi kanan layar
11. Verifikasi tombol toggle memakai ikon panah kiri
12. Verifikasi tooltip tombol toggle berisi "Open Category Tree"
13. Klik tombol toggle
14. Verifikasi sidebar tampil kembali
15. Verifikasi pilihan filter sebelumnya masih ada (`Dipakai Leaf` tercentang)
16. Verifikasi state tree sebelumnya masih ada (`Handheld Reader` masih ter-expand)
17. Klik baris `All Categories`

### TC-AC-DC-18: State Open atau Collapsed sidebar tersimpan per user dan dipulihkan setelah refresh

18. Hapus preferensi sidebar tersimpan akun aktor lalu muat ulang halaman dengan F5 (membentuk kunjungan pertama)
19. Verifikasi sidebar berstatus Open pada kunjungan pertama
20. Klik tombol toggle
21. Muat ulang halaman dengan F5
22. Verifikasi sidebar tetap Collapsed setelah refresh
23. Klik tombol toggle
24. Muat ulang halaman dengan F5
25. Verifikasi sidebar tetap Open setelah dibuka lagi dan refresh

### TC-AC-DC-19: State sidebar tersimpan per halaman: Device Name dan Device SKU independen

26. Klik tombol toggle pada halaman Device Name
27. Pindah ke sub-tab `Device SKU`
28. Verifikasi sidebar pada Device SKU tetap Open (state Device Name tidak ikut berlaku)
29. Pindah kembali ke sub-tab `Device Name`
30. Verifikasi sidebar pada Device Name masih Collapsed
31. Klik tombol toggle

## Notes

- Langkah penghubung (S-03): langkah 1 membentuk pilihan filter dan state expand yang diasersi langkah 15 dan 16 (S-14; TC-AC-DC-17 tidak menyebut keduanya di langkah tetapi Expected c mengasersinya); langkah 17 melepas pilihan filter; langkah 18 menggantikan "kunjungan pertama" TC-AC-DC-18; langkah 31 memulihkan sidebar Open sebelum spec berakhir (S-09).
- TC-AC-DC-20 dan TC-AC-DC-21 (viewport kecil dan localStorage diblokir) ada di spec 089.
- Temuan untuk QA: (1) TC-AC-DC-17 Expected c ("pilihan filter dan state tree sebelumnya masih ada") tidak menyebut pilihan atau state apa; spec membentuknya di langkah 1 (`Dipakai Leaf` dicentang, `Handheld Reader` di-expand). (2) Kunci localStorage dan cara menghapus preferensi tersimpan tidak disebut TC maupun PRD; kemampuan disediakan tim FE (S-13).
