---
id: TC-AC-PF-E2E-217-resilience-edit-custom-plan-5xx-tanpa-respons-dan-timing-toast
title: "Resilience: Edit Custom Plan Gagal 5xx dan Tanpa Respons serta Timing Toast Sukses, Error, dan Pengganti"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-215
  - TC-AC-PF-718
  - TC-AC-PF-600
coverage:
  web: automated
---

# Resilience: Edit Custom Plan Gagal 5xx dan Tanpa Respons serta Timing Toast Sukses, Error, dan Pengganti

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; custom `Growth Tier` v20 dengan Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; satu client `PT Wahana Nusantara` memegang v20) dan Dataset Plan G (Pre-setup #27; custom plan `Paket Tanpa Client` dengan 0 subscription).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum aksi pertama): Version `Growth Tier` (`v20`) dan jumlah entri Changelog Custom (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 dan `Paket Tanpa Client` Pre-setup literal tanpa suffix menjadi target Edit (TC-AC-PF-600 menyimpan Edit yang berhasil dua kali) atau target Archive yang digagalkan intercept. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; efek yang tersisa: kolom Last Updated `Growth Tier` berubah dan dua entri Changelog Custom `Edit` baru (permanen, tidak dapat dihapus lewat UI); suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Save Edit Custom Plan dan Archive (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC): (a) respons server error 5xx dan (b) respons tidak pernah diterima FE. Intercept dilepas segera setelah pemicu (S-09). Fixture BE untuk membaca Version dan jumlah entri Changelog serta memulihkan Dataset; sesi API aktor.
- Jeda nyata: langkah 37 menunggu 10 detik tanpa menutup toast error (batas 30 detik); jeda ini objek uji TC-AC-PF-600.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-215: Edit Custom Plan gagal 5xx: form tetap terbuka, input dipertahankan, versi tidak naik

1. Klik tab Custom
2. Buka Overlay Row Action `Growth Tier` → klik `Edit`
3. Ubah Group count menjadi `3`
4. Pasang intercept: respons Save Edit Custom Plan dijawab server error
5. Klik `[Save]`
6. Lepas intercept
7. Verifikasi muncul toast error: "Error, failed to update plan."
8. Verifikasi form tetap terbuka
9. Verifikasi input dipertahankan: Group count `3`
10. Verifikasi tombol `[Save]` aktif kembali
11. Verifikasi (dibaca lewat fixture BE) Version `Growth Tier` tetap `v20`
12. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-718: Edit Custom Plan tanpa respons (timeout atau jaringan terputus): toast Connection problem, form terbuka, input dipertahankan

13. Dismiss toast error
14. Pilih ulang Group count `3`
15. Pasang intercept: respons Save Edit Custom Plan tidak pernah diterima FE
16. Klik `[Save]` dan tunggu sampai FE menampilkan kegagalan
17. Lepas intercept
18. Verifikasi muncul toast error: "Connection problem. Please try again."
19. Verifikasi form tetap terbuka
20. Verifikasi Group count `3` dipertahankan
21. Verifikasi tombol `[Save]` aktif kembali untuk retry manual
22. Klik segmen Breadcrumb `Plans & Features`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`
25. Klik tab Custom

### TC-AC-PF-600: Toast sukses hilang otomatis sekitar 4 detik, toast error bertahan sampai di-dismiss, dan toast baru menggantikan yang lama

26. Buka Overlay Row Action `Growth Tier` → klik `Edit`
27. Ubah Group count menjadi `3`
28. Klik `[Save]`
29. Catat waktu toast sukses muncul
30. Verifikasi toast sukses hilang otomatis sekitar 4 detik setelah muncul (toleransi 1 detik)
31. Klik breadcrumb sub-tab `Active` pada Plan Detail `Growth Tier` yang terbuka sesudah `[Save]`
32. Ketik Search `Paket Tanpa Client`, tekan Enter
33. Pasang intercept: respons Archive dijawab server error
34. Buka Overlay Row Action `Paket Tanpa Client` → klik `Archive`
35. Klik `[Archive]`
36. Lepas intercept
37. Tunggu 10 detik tanpa menutup toast
38. Verifikasi toast error masih tampil setelah 10 detik (bertahan sampai di-dismiss manual)
39. Klik `[Cancel]` pada dialog `Archive Plan`
40. Klik `(←)` pada kotak Search
41. Buka Overlay Row Action `Growth Tier` → klik `Edit`
42. Ubah Group count menjadi `25`
43. Klik `[Save]`
44. Verifikasi toast sukses baru menggantikan toast error yang sedang tampil
45. Verifikasi hanya satu toast yang tampil (satu slot, tidak bertumpuk)
46. Verifikasi toast tampil di kanan bawah layar

## Notes

- Alasan di atas sekitar 35 langkah (46 langkah): ketiga blok satu kelas harness (b, kegagalan atau tanpa respons yang dipaksakan beserta perilaku toast-nya), berdiri sendiri pada `Growth Tier` atau `Paket Tanpa Client`, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan lebih lanjut menambah login, hook, dan pemulihan Dataset per spec.
- Penyimpangan urutan (S-10): TC-AC-PF-718 ditulis sebelum TC-AC-PF-600 karena form yang sama dipakai berulang dengan input dipertahankan; TC-AC-PF-600 menyimpan Edit yang berhasil sehingga diletakkan paling akhir.
- Langkah penghubung (S-03): langkah 1 mengarahkan layar ke tab Custom; langkah 13 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 29 dan 37 mencatat dan menunggu waktu toast; langkah 31 klik breadcrumb sub-tab `Active` karena sesudah `[Save]` sukses Plan Detail terbuka dan kotak Search hanya ada di Plans List; langkah 32 menemukan baris target (R-16); langkah 39 menutup dialog dan langkah 40 mengosongkan Search; langkah 22 sampai 24 menutup form dirty (S-08; `Verifikasi` dialog `Unsaved Changes` pada langkah 23 diwajibkan S-08) dan langkah 25 membuka tab Custom sebagai tab tujuan sesudah `[Leave]`.
- Langkah 45 (hitungan satu toast) sengaja tidak didahului "Tunggu toast lama hilang otomatis": toast error lama harus masih tampil karena penggantiannya oleh toast sukses baru adalah objek uji TC-AC-PF-600 (langkah 44 menjadi anchor positif).
- Langkah 11 dan 12 membaca Version dan jumlah entri Changelog lewat fixture BE (state data) karena form masih terbuka sampai langkah 22.
- Temuan untuk QA:
  - TC-AC-PF-215: langkah 4 TC meminta mengamati kolom Version dan membuka Changelog sementara Expected b menyatakan form tetap terbuka; keduanya tidak dapat dilakukan bersamaan di UI. Spec membaca Version dan Changelog lewat fixture BE.
  - TC-AC-PF-600: aksi Archive yang digagalkan, objek Edit yang disimpan, dan nilai Group count tidak disebut; spec memakai `Paket Tanpa Client` untuk Archive dan `Growth Tier` dengan Group count `3` lalu `25` untuk Edit. Sumber waktu "catat waktu toast" dan toleransi "sekitar 4 detik" tidak disebut; spec memakai toleransi 1 detik sebagai pilihan spec.
