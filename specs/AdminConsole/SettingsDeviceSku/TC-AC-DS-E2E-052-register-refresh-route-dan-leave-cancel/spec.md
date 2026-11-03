---
id: TC-AC-DS-E2E-052-register-refresh-route-dan-leave-cancel
title: "Register SKU: Refresh Browser, Berpindah Route, Leave, dan Guard Dilepas Setelah Submit Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-171
  - TC-AC-DS-172
  - TC-AC-DS-173
  - TC-AC-DS-572
coverage:
  web: automated
---

# Register SKU: Refresh Browser, Berpindah Route, Leave, dan Guard Dilepas Setelah Submit Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-GUARD-{runId}-052`, dibuat oleh TC-AC-DS-173. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-052` milik Principal.
- Kemampuan teknis (disediakan tim FE): penanganan dialog konfirmasi bawaan browser (`beforeunload`) pada muat ulang F5, yaitu mengamati kemunculannya dan membatalkan muat ulang (S-08).
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-171: Refresh browser pada popup Register yang terisi memicu konfirmasi bawaan browser

2. Klik tombol `[+ SKU]` pada toolbar
3. Ketik `H-RELOAD` pada field Model/Type
4. Muat ulang halaman dengan F5
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
6. Batalkan muat ulang
7. Kosongkan isi field Model/Type
8. Muat ulang halaman dengan F5
9. Verifikasi tidak ada konfirmasi bawaan browser
10. Verifikasi halaman dimuat ulang

### TC-AC-DS-172: Berpindah route di dalam aplikasi saat popup Register terisi menampilkan dialog Unsaved Changes

11. Klik tombol `[+ SKU]` pada toolbar
12. Ketik `H-ROUTE` pada field Model/Type
13. Klik item sidebar `Settings`
14. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
15. Klik `[Cancel]`
16. Verifikasi navigasi dibatalkan
17. Verifikasi popup Register tetap terbuka
18. Verifikasi input `H-ROUTE` dipertahankan
19. Klik tombol Back browser
20. Klik `[Cancel]` pada dialog Unsaved Changes

### TC-AC-DS-173: Submit sukses tidak memicu konfirmasi browser pada muat ulang berikutnya

21. Klik `[Clear Field]`
22. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
23. Klik field Device Name lalu pilih `Asset TAG`
24. Klik field Brand lalu pilih `Arcturus`
25. Ketik `T-GD` pada field Model/Type
26. Ketik `NEW-GUARD-{runId}-052` pada field SKU
27. Unggah `foto-a.jpg` pada field Photo
28. Klik `[Submit]`
29. Tunggu popup Register tertutup (aksi selesai)
30. Muat ulang halaman dengan F5
31. Verifikasi tidak ada konfirmasi bawaan browser
32. Verifikasi halaman dimuat ulang normal

### TC-AC-DS-572: Berpindah route saat popup Register terisi lalu memilih Leave menutup popup tanpa menyimpan

33. Klik tombol `[+ SKU]` pada toolbar
34. Ketik `H-ROUTE2` pada field Model/Type
35. Klik item sidebar `Settings`
36. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
37. Klik `[Leave]`
38. Verifikasi navigasi dilanjutkan dan halaman Device SKU ditinggalkan
39. Verifikasi popup Register tertutup
40. Buka Settings > Device > Device SKU
41. Verifikasi jumlah total SKU pada footer pagination bernilai N + 1: hanya SKU `NEW-GUARD-{runId}-052` yang tersimpan dan tidak ada SKU baru dari TC-AC-DS-572

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 20 membatalkan dialog yang dicegat oleh Back browser (langkah 6 TC-AC-DS-172 tidak memiliki Expected, dialog diasumsikan sama dengan langkah 4); langkah 21 (`[Clear Field]`) mengosongkan popup yang masih berisi `H-ROUTE` agar TC-AC-DS-173 mulai dari popup kosong (S-09); langkah 29 menunggu Submit selesai sebelum muat ulang (bagian 8b butir 8); langkah 40 membuka kembali halaman Device SKU setelah navigasi untuk membaca footer.
- Ukuran spec (di atas sekitar 35 langkah): keempat blok adalah kelas fungsional yang sama (perilaku guard Unsaved Changes saat meninggalkan form Register melalui muat ulang dan navigasi) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan blok yang meninggalkan halaman ada di akhir spec (S-10). Hanya TC-AC-DS-173 membuat data.
- Asersi "tidak ada SKU baru" Post Condition TC-AC-DS-572 diasersi sebagai N + 1 di langkah akhir (S-12).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-052` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-172 langkah 6 (tombol Back browser) tidak punya Expected dan hasilnya (dialog dicegat) hanya tertulis di tanda panah langkah; spec menambahkan klik `[Cancel]` sebagai penghubung.
  - TC-AC-DS-172 dan TC-AC-DS-572 menyebut item sidebar `Settings` tanpa jalur menu penuh; spec mengikuti teks TC.
