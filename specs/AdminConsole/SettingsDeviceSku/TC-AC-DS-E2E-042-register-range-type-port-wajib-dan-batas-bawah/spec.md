---
id: TC-AC-DS-E2E-042-register-range-type-port-wajib-dan-batas-bawah
title: "Register SKU: Range Type Wajib, Port Wajib, dan Port 0 Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-146
  - TC-AC-DS-147
  - TC-AC-DS-148
coverage:
  web: automated
---

# Register SKU: Range Type Wajib, Port Wajib, dan Port 0 Diblokir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`, `Hardware > Smart Fixed Reader > Portal Reader`); Device Name #26 (`UHF Handheld Reader`, `4-Port Fixed Reader`); Brand Principal #27 (`Arcturus`, `Veltrix`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Seluruh Submit pada spec ini ditolak sehingga tidak ada SKU dibuat dan tidak ada cleanup. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut).
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-146: Submit Handheld Reader tanpa Range Type menampilkan pesan wajib diisi

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `UHF Handheld Reader`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `H-NR` pada field Model/Type
7. Ketik `NEW-NORNG` pada field SKU
8. Unggah `foto-a.jpg` pada field Photo
9. Klik `[Submit]` dengan Range Type dibiarkan kosong
10. Verifikasi pesan inline pada Range Type: "Range type must not be empty"
11. Verifikasi popup Register tetap terbuka

### TC-AC-DS-147: Submit Smart Fixed Reader dengan Port kosong menampilkan pesan minimum

12. Klik `[Clear Field]`
13. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
14. Klik field Device Name lalu pilih `4-Port Fixed Reader`
15. Klik field Brand lalu pilih `Veltrix`
16. Ketik `SF-NP` pada field Model/Type
17. Ketik `NEW-NOPORT` pada field SKU
18. Unggah `foto-a.jpg` pada field Photo
19. Klik `[Submit]` dengan Port dibiarkan kosong
20. Verifikasi pesan inline pada Port: "Port must be at least 1"
21. Verifikasi popup Register tetap terbuka

### TC-AC-DS-148: Submit Smart Fixed Reader dengan Port 0 menampilkan pesan minimum

22. Klik `[Clear Field]`
23. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
24. Klik field Device Name lalu pilih `4-Port Fixed Reader`
25. Klik field Brand lalu pilih `Veltrix`
26. Ketik `SF-P0` pada field Model/Type
27. Ketik `NEW-PORT0` pada field SKU
28. Ketik `0` pada field Port
29. Unggah `foto-a.jpg` pada field Photo
30. Klik `[Submit]`
31. Verifikasi pesan inline pada Port: "Port must be at least 1"
32. Verifikasi popup Register tetap terbuka
33. Klik ikon close `[✕]`
34. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
35. Klik `[Leave]`
36. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga percobaan Submit

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 12 dan 22 (`[Clear Field]`) mengosongkan popup dan membersihkan error identik sebelum TC berikutnya (S-09, R-12); langkah 33 sampai 35 menutup form dirty secara deterministik (S-08).
- Butir "tidak ada SKU baru" pada Expected b ketiga TC diasersi sekali di langkah akhir dengan selisih terhadap baseline N (S-12); kode `NEW-NORNG`, `NEW-NOPORT`, `NEW-PORT0` dan Model/Type terkait tidak pernah tersimpan sehingga ditulis literal sesuai TC.
- Ukuran spec (sedikit di atas sekitar 35 langkah): ketiga blok adalah kelas fungsional yang sama (validasi field kondisional Register yang ditolak) dengan pola isi form yang sama dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-042` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
