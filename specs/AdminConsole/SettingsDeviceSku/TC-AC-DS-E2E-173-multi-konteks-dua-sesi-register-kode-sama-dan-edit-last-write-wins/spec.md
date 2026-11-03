---
id: TC-AC-DS-E2E-173-multi-konteks-dua-sesi-register-kode-sama-dan-edit-last-write-wins
title: "Multi-konteks: Dua Sesi Register Kode Sama Ditolak Duplikat dan Dua Sesi Edit Last-write-wins"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-180
  - TC-AC-DS-542
  - TC-AC-DS-543
coverage:
  web: automated
---

# Multi-konteks: Dua Sesi Register Kode Sama Ditolak Duplikat dan Dua Sesi Edit Last-write-wins

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Konteks browser kedua: Total Control Principal kedua (Budi Kurniawan, Modified By `Budi K`): `totalControlSku2_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC2_PASSWORD` (Pre-setup #2), login pada langkah 1 (jendela kedua dipertahankan sampai akhir spec dan ditutup di hook `after`).
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35).
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `RACE-001` (Data Dinamis #25) dibuat sesi kedua; hook `before` menghapus sisa kode itu bila ada dan hook `after` menghapusnya. Target Edit `HHR-ARC-200` (Pre-setup #29) dipulihkan fixture BE di antara blok TC.
- Kemampuan baca (disediakan tim FE/BE): jumlah entri Changelog dicatat sebagai baseline sebelum aksi pemicu; audit trail permanen sehingga asersi memakai selisih terhadap baseline (S-12).
- Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

1. Buka konteks browser kedua (jendela terpisah) dan login sebagai Total Control Principal kedua (`totalControlSku2_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC2_PASSWORD`), lalu buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-180: Register oleh dua sesi dengan kode SKU sama: Submit kedua ditolak duplikat

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `Asset TAG`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `T-RC1` pada field Model/Type
7. Ketik `RACE-001` pada field SKU
8. Unggah `foto-a.jpg` pada field Photo
9. Pindah ke konteks browser kedua, klik `[+ SKU]`, isi SKU `RACE-001` (Asset TAG, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-RC2`, foto `foto-a.jpg`), lalu klik `[Submit]` lebih dulu
10. Tunggu aksi selesai (SKU `RACE-001` tersimpan, popup kedua tertutup)
11. Kembali ke konteks browser pertama lalu klik `[Submit]`
12. Verifikasi pesan inline "SKU already exists" tampil di bawah field SKU pada sesi pertama
13. Verifikasi Popup Register SKU tetap terbuka dengan input dipertahankan
14. Klik `[✕]`
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`
17. Ketik Search `RACE-001`, tekan Enter
18. Verifikasi hanya satu SKU `RACE-001` yang ada
19. Klik `(←)` pada kotak Search; hapus `RACE-001` lewat fixture BE

### TC-AC-DS-542: Dua sesi mengedit SKU yang sama mengikuti last-write-wins

20. Klik ikon Changelog, catat jumlah entri sebagai baseline N_CL, lalu tutup modal
21. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
22. Ubah Model/Type menjadi `H-A` (belum Save)
23. Pindah ke konteks browser kedua, buka Edit `HHR-ARC-200`, ubah Model/Type menjadi `H-B` lalu klik `[Save]`
24. Tunggu aksi selesai (Model/Type `H-B` tersimpan)
25. Kembali ke konteks browser pertama lalu klik `[Save]`
26. Verifikasi Save sesi pertama sukses dengan toast sukses: "Success, device SKU has been updated."
27. Verifikasi tidak ada dialog konflik
28. Muat ulang List, ketik Search `HHR-ARC-200`, tekan Enter
29. Verifikasi nilai akhir Model/Type `HHR-ARC-200` adalah `H-A` (Save terakhir yang diterima server menimpa)
30. Klik ikon Changelog
31. Verifikasi jumlah entri Changelog bertambah 2 dari baseline N_CL
32. Verifikasi kedua Edit tercatat sebagai entri Edit terpisah: Model/Type `H200` > `H-B` lalu `H-B` > `H-A`
33. Tutup modal Changelog; pulihkan `HHR-ARC-200` ke keadaan awal Pre-setup lewat fixture BE

### TC-AC-DS-543: Save kedua dengan nilai sama dengan nilai tersimpan adalah tanpa perubahan

34. Klik ikon Changelog, catat jumlah entri sebagai baseline N_CL2, lalu tutup modal
35. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
36. Ubah Model/Type menjadi `H-C` (belum Save)
37. Pindah ke konteks browser kedua, ubah Model/Type `HHR-ARC-200` menjadi `H-C` lalu klik `[Save]`
38. Tunggu aksi selesai (Model/Type `H-C` tersimpan)
39. Kembali ke konteks browser pertama lalu klik `[Save]`
40. Verifikasi muncul toast info: "No changes to save."
41. Verifikasi popup tertutup
42. Klik ikon Changelog
43. Verifikasi jumlah entri Changelog bertambah 1 dari baseline N_CL2 dan entri itu Edit Model/Type `H200` > `H-C` dari sesi kedua
44. Tutup modal Changelog; pulihkan `HHR-ARC-200` ke keadaan awal Pre-setup lewat fixture BE; klik `(←)` pada kotak Search

## Notes

- Sesi kedua memakai konteks browser UI karena TC 180, 542, dan 543 adalah multi-konteks dua sesi UI (kelas c); race dua sesi adalah objek uji sehingga tidak ada butir `P-2`.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (login konteks kedua), pencatatan baseline, Search untuk menemukan baris target (R-16, langkah 17 dan 21), menunggu aksi selesai sebelum berpindah konteks (8b butir 8), langkah 14 dan 16 (menutup form dirty dengan dialog `Unsaved Changes` mengikuti S-08), langkah 19 (membersihkan `RACE-001`), serta langkah 33 dan 44 (pemulihan data antar blok, S-09).
- Spec berada di atas sekitar 35 langkah (44 langkah); alasan: semua blok satu kelas harness (c, dua sesi UI) dan berdiri sendiri karena data dipulihkan antar blok, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pengecualian S-12 A-11: `HHR-ARC-200` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target Edit; pemulihan ke keadaan awal Pre-setup dijamin fixture BE di antara blok TC (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - TC 180 dan 542 tidak menyebut isi lengkap Register oleh sesi kedua selain kode `RACE-001`; spec memakai nilai valid lain (Model/Type `T-RC2`). TC 542 Expected butir c menyebut dua entri Edit tanpa menyebut aktor; entri Changelog dibaca lewat selisih dengan baseline. TC 543 Expected butir b menyebut entri "dari sesi kedua" yaitu Budi K.
  - S-12: kode Data Dinamis `RACE-001` mengikuti TC tanpa suffix `{runId}` dan tidak tercakup A-11; spec membersihkan sisa kode itu di hook `before` dan `after` (R-13); butuh keputusan pengecualian atau penggantian kode oleh QA.
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
