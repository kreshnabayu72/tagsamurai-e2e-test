---
id: TC-AC-DS-E2E-168-resilience-register-5xx-dan-timeout
title: "Resilience Register: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-175
  - TC-AC-DS-176
coverage:
  web: automated
---

# Resilience Register: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37).
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `NEW-5XX` (Data Dinamis #24) terbentuk setelah retry; SKU `NEW-TMO` tidak boleh tersimpan. Hook `before` menghapus sisa kedua kode itu bila ada; hook `after` menghapusnya.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata (bukan `Mode: mock`) untuk memaksa respons 500 atau menunda respons sampai timeout; intercept dilepas segera setelah pemicu selesai (S-09). Plan: backend nyata dipertahankan agar tidak membutuhkan daftar endpoint mock (R-15).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-175: Kegagalan server 5xx saat Submit mempertahankan input dan tombol aktif

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category; expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `UHF Handheld Reader`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `H-5X` pada field Model/Type
6. Ketik `NEW-5XX` pada field SKU
7. Pilih Range Type `Long Range`
8. Unggah `foto-a.jpg` pada field Photo
9. Intercept request create dengan status 500
10. Klik `[Submit]`
11. Verifikasi muncul toast error: "Error, failed to register device SKU."
12. Verifikasi Popup Register SKU tetap terbuka
13. Verifikasi semua input dan foto dipertahankan
14. Verifikasi tombol `[Submit]` aktif kembali
15. Hapus intercept lalu klik `[Submit]` lagi
16. Verifikasi retry sukses: muncul toast sukses: "Success, device SKU has been registered."
17. Ketik Search `NEW-5XX`, tekan Enter
18. Verifikasi hanya satu SKU `NEW-5XX` terbentuk

### TC-AC-DS-176: Timeout jaringan saat Submit menampilkan pesan koneksi dan mempertahankan input

19. Klik tombol `[+ SKU]` pada toolbar
20. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
21. Klik field Device Name lalu pilih `Asset TAG`
22. Klik field Brand lalu pilih `Arcturus`
23. Ketik `T-TM` pada field Model/Type
24. Ketik `NEW-TMO` pada field SKU
25. Unggah `foto-a.jpg` pada field Photo
26. Tunda respons create sampai timeout dengan intercept
27. Klik `[Submit]`
28. Verifikasi muncul toast error: "Connection problem. Please try again."
29. Verifikasi Popup Register SKU tetap terbuka
30. Verifikasi input dan foto dipertahankan
31. Verifikasi tombol `[Submit]` aktif untuk retry manual
32. Hapus intercept request create dan tutup toast
33. Klik `[✕]` untuk menutup popup
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search `NEW-5XX` (menemukan baris target, R-16) dan penutupan toast (R-12); langkah 32 melepas intercept segera setelah pemicu dan langkah 33 menutup form dirty secara deterministik (S-08, dialog `Unsaved Changes` diverifikasi).
- Toast error 175 ditutup sebelum toast error 176 diasersi; toast sukses retry diverifikasi sebelum penutupan.
- Temuan untuk QA:
  - TC 175 Post Condition "Satu record SKU NEW-5XX setelah retry" diasersi lewat Search `NEW-5XX` (Expected butir c "hanya satu SKU"); jumlah baris yang diharapkan satu.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
