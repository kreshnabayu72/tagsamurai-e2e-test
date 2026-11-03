---
id: TC-AC-DS-E2E-054-register-referensi-stale-category-device-name-brand
title: "Register SKU: Referensi Category, Device Name, dan Brand Dihapus Pelaku Lain sebelum Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-177
  - TC-AC-DS-178
  - TC-AC-DS-179
coverage:
  web: automated
---

# Register SKU: Referensi Category, Device Name, dan Brand Dihapus Pelaku Lain sebelum Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Total Control Principal kedua PT Arunika Prima (Data Pre-setup #2) `totalControlSku2_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Kurniawan`), password dari `Spectra.env.AC_DS_TC2_PASSWORD` (nama env baru, disediakan tim FE). Akun ini hanya bertindak lewat sesi API (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) sebagai pemicu perubahan state dan tidak dibuka di UI.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis (di-seed lewat API di hook `before` sebagai data milik spec, dihapus oleh pelaku kedua pada langkah 8, 19, dan 30): Subcategory `Kategori Sementara {runId}-054` di bawah `Asset TAG`; Device Name `Perangkat Sementara {runId}-054` (Category `Asset TAG`); Brand `Brand Sementara {runId}-054`. Nama bersuffix menggantikan data khusus TC (Data Pre-setup #40) karena entitas itu dihapus oleh spec. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut). Seluruh Submit ditolak sehingga tidak ada SKU dibuat.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Category, Device Name, dan Brand bersuffix `{runId}-054` yang masih tersisa.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan penghapusan Category, Device Name, dan Brand lewat sesi API; mekanisme dan endpoint-nya tidak tercantum di TC sehingga tidak disebut di sini.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-177: Referensi Category yang dihapus sesi lain sebelum Submit menampilkan error stale pada field itu

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, pilih node Subcategory `Kategori Sementara {runId}-054`, lalu klik `[Select]`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-ST1` pada field Model/Type
6. Ketik `NEW-STALE-C` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Dengan sesi API akun kedua (Budi Kurniawan) hapus Category `Kategori Sementara {runId}-054` hingga penghapusan tersimpan
9. Klik `[Submit]`
10. Verifikasi pesan inline pada field Category: "This category no longer exists. Please select another."
11. Verifikasi field Category dikosongkan otomatis
12. Klik field Category
13. Verifikasi daftar opsi Category memuat node lain seperti `Asset TAG`
14. Verifikasi daftar opsi Category dimuat ulang tanpa `Kategori Sementara {runId}-054`
15. Klik `[Cancel]` pada picker Category
16. Verifikasi field lain termasuk Photo dipertahankan

### TC-AC-DS-178: Referensi Device Name yang dihapus sesi lain sebelum Submit menampilkan error stale pada field itu

17. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
18. Klik field Device Name lalu pilih `Perangkat Sementara {runId}-054`
19. Dengan sesi API akun kedua (Budi Kurniawan) hapus Device Name `Perangkat Sementara {runId}-054` hingga penghapusan tersimpan
20. Klik `[Submit]`
21. Verifikasi pesan inline pada field Device Name: "This device name no longer exists. Please select another."
22. Verifikasi field Device Name dikosongkan otomatis
23. Klik field Device Name
24. Verifikasi daftar opsi Device Name memuat opsi lain seperti `Asset TAG`
25. Verifikasi daftar opsi Device Name dimuat ulang tanpa `Perangkat Sementara {runId}-054`
26. Tekan Esc untuk menutup daftar opsi
27. Verifikasi field lain termasuk Photo dipertahankan

### TC-AC-DS-179: Referensi Brand yang dihapus sesi lain sebelum Submit menampilkan error stale pada field itu

28. Klik field Device Name lalu pilih `Asset TAG`
29. Klik field Brand lalu pilih `Brand Sementara {runId}-054`
30. Dengan sesi API akun kedua (Budi Kurniawan) hapus Brand `Brand Sementara {runId}-054` hingga penghapusan tersimpan
31. Klik `[Submit]`
32. Verifikasi pesan inline pada field Brand: "This brand no longer exists. Please select another."
33. Verifikasi field Brand dikosongkan otomatis
34. Klik field Brand
35. Verifikasi daftar opsi Brand memuat opsi lain seperti `Arcturus`
36. Verifikasi daftar opsi Brand dimuat ulang tanpa `Brand Sementara {runId}-054`
37. Tekan Esc untuk menutup daftar opsi
38. Verifikasi field lain termasuk Photo dipertahankan
39. Klik ikon close `[✕]`
40. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
41. Klik `[Leave]`
42. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga percobaan Submit

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 8, 19, dan 30 adalah pemicu pelaku kedua lewat sesi API (sesi API bukan konteks kedua, tidak memakai `P-2`); popup yang sama dipakai ulang oleh ketiga blok (bagian 3) sehingga Brand, Model/Type, SKU, dan Photo blok sebelumnya dipertahankan dan menggantikan isian TC-AC-DS-178 dan TC-AC-DS-179 (`T-ST2`, `NEW-STALE-D`, `T-ST3`, `NEW-STALE-B`) yang tidak diasersi; langkah 39 sampai 41 menutup form dirty secara deterministik (S-08).
- Ukuran spec (di atas sekitar 35 langkah): tiga alur identik per jenis referensi (Category, Device Name, Brand) dengan pola dan satu harness yang sama (pelaku kedua lewat sesi API); tiap alur berdiri sendiri sehingga kegagalan satu alur tidak membuat alur lain kehilangan makna, dan langkah yang diulang per jenis referensi mengikuti langkah TC (bagian 8b butir 7).
- Pembagian TC lintas spec: TC-AC-DS-180 (Register oleh dua sesi dengan kode SKU sama) bukan bagian spec ini.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-054` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-177 sampai TC-AC-DS-179 ditandai Manual Only (d) dua sesi paralel di TC; spec memperlakukan pelaku kedua sebagai sesi API (bukan konteks UI kedua) dan tetap mengotomasi sesi pertama.
  - TC-AC-DS-177 tidak memilih Device Name padahal field itu wajib dan Device Name hanya muncul untuk Category yang punya Device Name; Submit dengan Device Name kosong dapat ditolak oleh validasi klien sebelum cek stale server. Spec mengikuti langkah TC.
  - Data khusus `Kategori Sementara`, `Perangkat Sementara`, dan `Brand Sementara` (Data Pre-setup #40) adalah rancangan yang belum diverifikasi ada di environment; spec memakai salinan bersuffix yang di-seed sendiri dan akun Principal kedua perlu hak menghapus ketiga entitas lewat sesi API.
