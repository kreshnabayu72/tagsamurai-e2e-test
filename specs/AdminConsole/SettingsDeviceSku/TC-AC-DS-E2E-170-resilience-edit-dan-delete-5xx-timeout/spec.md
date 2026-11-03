---
id: TC-AC-DS-E2E-170-resilience-edit-dan-delete-5xx-timeout
title: "Resilience Edit dan Delete: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input dan Dialog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-252
  - TC-AC-DS-253
  - TC-AC-DS-268
  - TC-AC-DS-269
coverage:
  web: automated
---

# Resilience Edit dan Delete: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input dan Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Target Edit `HHR-ARC-200` dan target Delete `TAG-ARC-OBJ` (Pre-setup #29).
- Data Dinamis: tidak ada. Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata (bukan `Mode: mock`) untuk memaksa respons 500 atau menunda respons sampai timeout; intercept dilepas segera setelah pemicu selesai (S-09). Plan: backend nyata dipertahankan agar tidak membutuhkan daftar endpoint mock (R-15).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-252: Kegagalan server 5xx saat Save mempertahankan input dan tombol aktif

1. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
2. Ubah Model/Type menjadi `H-5X`
3. Intercept request update dengan status 500
4. Klik `[Save]`
5. Verifikasi muncul toast error: "Error, failed to update device SKU."
6. Verifikasi Popup Edit tetap terbuka dengan input dipertahankan
7. Verifikasi tombol `[Save]` aktif kembali
8. Hapus intercept lalu klik `[Save]` lagi
9. Verifikasi retry sukses: muncul toast sukses: "Success, device SKU has been updated."
10. Tutup toast; pulihkan `HHR-ARC-200` ke keadaan awal Pre-setup lewat fixture BE

### TC-AC-DS-253: Timeout jaringan saat Save menampilkan pesan koneksi dan mempertahankan input

11. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
12. Ubah Model/Type menjadi `H-TM`
13. Tunda respons update sampai timeout dengan intercept
14. Klik `[Save]`
15. Verifikasi muncul toast error: "Connection problem. Please try again."
16. Verifikasi Popup Edit tetap terbuka dengan input dipertahankan
17. Verifikasi tombol `[Save]` aktif untuk retry manual
18. Hapus intercept request update dan tutup toast
19. Kembalikan Model/Type ke nilai tersimpan `H200` lalu tutup popup dengan `[✕]`

### TC-AC-DS-268: Kegagalan server 5xx saat Confirm Delete menampilkan toast gagal dan dialog tetap terbuka

20. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter, klik ⋯ pada baris `TAG-ARC-OBJ` lalu pilih `Delete`
21. Intercept request delete dengan status 500
22. Klik `[Delete]`
23. Verifikasi muncul toast error: "Error, failed to delete device SKU."
24. Verifikasi dialog konfirmasi tetap terbuka
25. Verifikasi SKU tidak terhapus
26. Verifikasi tombol `[Delete]` aktif kembali untuk retry
27. Hapus intercept request delete, tutup toast, lalu klik `[Cancel]`

### TC-AC-DS-269: Timeout jaringan saat Confirm Delete menampilkan pesan koneksi dan dialog tetap terbuka

28. Klik ⋯ pada baris `TAG-ARC-OBJ` lalu pilih `Delete`
29. Tunda respons delete sampai timeout dengan intercept
30. Klik `[Delete]`
31. Verifikasi muncul toast error: "Connection problem. Please try again."
32. Verifikasi dialog tetap terbuka
33. Verifikasi SKU tidak terhapus
34. Hapus intercept request delete, tutup toast, klik `[Cancel]`, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search untuk menemukan baris target (R-16, langkah 1), penutupan toast agar toast error berikutnya tidak tertukar (R-12), langkah 10 (pemulihan data Pre-setup, S-09), langkah 18 dan 19 (pelepasan intercept dan pengembalian field dirty ke nilai tersimpan sebelum menutup popup), serta langkah 27 dan 34 (pelepasan intercept dan penutupan dialog).
- Spec berada di atas sekitar 35 langkah (34 langkah); alasan: semua blok satu kelas harness (b) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC 252 ("Model/Type H-5X tersimpan setelah retry", "Entri log tercatat ...") tidak punya langkah observasi di TC dan tidak diasersi.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
