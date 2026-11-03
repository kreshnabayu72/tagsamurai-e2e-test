---
id: TC-AC-DS-E2E-153-log-absence-register-gagal-5xx
title: "Absence Log: Register Gagal 5xx Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-554
coverage:
  web: automated
---

# Absence Log: Register Gagal 5xx Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Riwayat Changelog Principal (#33).
- Data Dinamis: SKU `NEW-LOG5XX` (Data Dinamis #37) tidak boleh tersimpan; hook `before` menghapus sisa kode itu bila ada dan hook `after` memastikan tidak ada.
- Kemampuan baca (disediakan tim FE/BE): jumlah entri Changelog, System Log aktor, dan Activity Log tab User Action dicatat sebagai baseline sebelum aksi pemicu; audit trail permanen sehingga asersi memakai selisih terhadap baseline (S-12).
- Kemampuan teknis: `Spectra.intercept()` memaksa respons create 500 di atas backend nyata; intercept dilepas segera setelah pemicu selesai.
- Pemicu: kegagalan 5xx pada Register (kelas b, bukan objek uji; `P-5` butir a). Tidak ada state global yang diubah; suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-554: Register SKU yang gagal 5xx tidak menulis entri log

1. Klik ikon Changelog
2. Catat jumlah entri Changelog sebagai baseline N_CL, lalu tutup modal
3. Buka Settings > User, pilih user aktor `totalControlSku_automated_{namaCompany}@qwertysystem.net` (nama tampil `Jane Setiawan`), buka Detail lalu tab System Log
4. Catat jumlah entri System Log aktor sebagai baseline N_SL
5. Buka Activity Log lalu tab User Action
6. Catat jumlah entri Activity Log tab User Action sebagai baseline N_AL
7. Buka halaman `Settings > Device > Device SKU`
8. Klik tombol `[+ SKU]` pada toolbar
9. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
10. Klik field Device Name lalu pilih `Asset TAG`
11. Klik field Brand lalu pilih `Arcturus`
12. Ketik `T-L5` pada field Model/Type
13. Ketik `NEW-LOG5XX` pada field SKU
14. Unggah `foto-a.jpg` pada field Photo
15. Intercept request create dengan status 500
16. Klik `[Submit]`
17. Verifikasi muncul toast error: "Error, failed to register device SKU."
18. Verifikasi Popup Register SKU tetap terbuka setelah Submit gagal
19. Hapus intercept request create
20. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`
21. Klik ikon Changelog
22. Verifikasi jumlah entri Changelog sama dengan baseline N_CL (tidak bertambah)
23. Verifikasi tidak ada entri Create baru untuk `NEW-LOG5XX` pada Changelog
24. Buka Settings > User, pilih user aktor `totalControlSku_automated_{namaCompany}@qwertysystem.net` (nama tampil `Jane Setiawan`), buka Detail lalu tab System Log
25. Verifikasi jumlah entri System Log sama dengan baseline N_SL (tabel termuat)
26. Verifikasi System Log aktor tidak memuat entri Create untuk `NEW-LOG5XX`
27. Buka Activity Log lalu tab User Action
28. Verifikasi jumlah entri Activity Log tab User Action sama dengan baseline N_AL (tabel termuat)
29. Verifikasi Activity Log tidak memuat entri Create untuk `NEW-LOG5XX`

## Notes

- `P-5`: spec absence (kelas g); pemicu kegagalan 5xx (kelas b) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 sampai 7 (baseline tiga surface log dan membuka kembali halaman, S-12), langkah 19 (intercept dilepas segera setelah pemicu, S-09), dan langkah 20 (`[Clear Field]` lalu `[✕]`).
- Expected butir c dipecah menjadi jumlah entri Changelog sama dengan baseline dan tidak ada entri Create `NEW-LOG5XX` (angka absolut 35 pada TC diganti baseline, S-12); butir d dipecah per surface dengan anchor jumlah entri sama dengan baseline; anchor positif: toast error sudah diverifikasi.
- Temuan untuk QA:
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
