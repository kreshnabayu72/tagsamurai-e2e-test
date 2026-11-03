---
id: TC-AC-DS-E2E-041-register-foto-wajib-dan-aria-error
title: "Register SKU: Foto Wajib Diisi, Hapus Semua Foto, dan Aria Error Foto"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-139
  - TC-AC-DS-141
  - TC-AC-DS-145
coverage:
  web: automated
---

# Register SKU: Foto Wajib Diisi, Hapus Semua Foto, dan Aria Error Foto

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); File foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Seluruh Submit pada spec ini ditolak sehingga tidak ada SKU dibuat dan tidak ada cleanup. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut).
- Kemampuan teknis (disediakan tim FE): pembacaan atribut DOM (`aria-describedby`) pada slot Photo untuk TC-AC-DS-145.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-139: Submit tanpa foto menampilkan pesan Photo must not be empty

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `Asset TAG`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `T-NP` pada field Model/Type
7. Ketik `NEW-NOPH` pada field SKU
8. Klik `[Submit]` tanpa mengunggah foto
9. Verifikasi pesan inline pada slot Photo: "Photo must not be empty"
10. Verifikasi popup Register tetap terbuka

### TC-AC-DS-145: Error foto memakai aria-describedby agar terbaca screen reader

11. Periksa atribut field Photo pada DOM
12. Verifikasi slot Photo memiliki atribut aria-describedby yang menunjuk ke elemen pesan "Photo must not be empty"

### TC-AC-DS-141: Menghapus semua foto lalu Submit menampilkan pesan wajib foto

13. Klik `[Clear Field]`
14. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
15. Klik field Device Name lalu pilih `Asset TAG`
16. Klik field Brand lalu pilih `Arcturus`
17. Ketik `T-NP2` pada field Model/Type
18. Ketik `NEW-NOPH2` pada field SKU
19. Unggah `foto-a.jpg` pada field Photo
20. Hapus satu-satunya foto `foto-a.jpg`
21. Verifikasi slot Photo kembali menampilkan placeholder
22. Klik `[Submit]`
23. Verifikasi pesan inline "Photo must not be empty" tampil pada slot Photo
24. Verifikasi popup Register tetap terbuka
25. Klik ikon close `[✕]`
26. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
27. Klik `[Leave]`
28. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga percobaan Submit

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 13 (`[Clear Field]`) membersihkan error foto sebelum TC-AC-DS-141 agar error identik tidak terbawa (R-12); langkah 25 sampai 27 menutup form dirty secara deterministik (S-08).
- Urutan TC diubah: TC-AC-DS-145 dijalankan sebelum TC-AC-DS-141 karena memakai error foto yang sama dengan TC-AC-DS-139 (form dipakai ulang, bagian 3); kode `NEW-A11Y` dan `T-A11Y` pada TC-AC-DS-145 diganti isian form TC-AC-DS-139 dan tidak diasersi.
- Butir "tidak ada SKU baru" pada Expected TC-AC-DS-139 dan TC-AC-DS-141 diasersi sekali di langkah akhir dengan selisih terhadap baseline N (S-12); kode `NEW-NOPH`, `NEW-NOPH2`, `T-NP`, `T-NP2` tidak pernah tersimpan sehingga ditulis literal sesuai TC.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-041` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
