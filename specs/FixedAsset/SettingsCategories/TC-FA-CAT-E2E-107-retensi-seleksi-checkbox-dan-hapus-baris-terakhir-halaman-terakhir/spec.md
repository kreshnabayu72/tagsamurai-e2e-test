---
id: TC-FA-CAT-E2E-107-retensi-seleksi-checkbox-dan-hapus-baris-terakhir-halaman-terakhir
title: "Retensi Seleksi Checkbox saat Search atau Filter Berubah dan Hapus Baris Terakhir di Halaman Terakhir"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-386
  - TC-FA-CAT-366
coverage:
  web: automated
---

# Retensi Seleksi Checkbox saat Search atau Filter Berubah dan Hapus Baris Terakhir di Halaman Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Modified By bergantian `Jane Smith`, `Alex Brown`, `John Doe`, `System`).
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa), nama berakhiran `{runId}-107`: kategori L1 `Zulu Edit {runId}-107` dengan Modified By `Jane Smith` (menjadi baris ke-31 dan satu-satunya baris halaman 4 pada 10 baris per halaman; target Edit TC-386 dan target Delete TC-366, S-06). Dengan seed ini tabel memuat 31 kategori L1 sesuai precondition TC-366.
- Pelaku kedua: sesi API Principal Automation (Pre-setup #11, akun disediakan tim FE) yang hanya memicu pembuatan dan penghapusan `Zulu Filter {runId}-107`; mengikuti butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-386: Retensi seleksi checkbox dan mutasi real-time saat terfilter

1. Centang `Seed Cat 01`
2. Ketik Search `Seed Cat 2`, tekan Enter
3. Klik `✕` pada Search, tekan Enter
4. Verifikasi centang `Seed Cat 01` bertahan
5. Terapkan Filter Modified By `Jane S` lalu klik `[Apply]`
6. Verifikasi baris `Zulu Edit {runId}-107` tampil pada tabel terfilter
7. Sesi API Principal Automation membuat kategori `Zulu Filter {runId}-107` hingga pembuatan tersimpan
8. Klik `[Apply]` pada Filter untuk memuat ulang tabel terfilter
9. Verifikasi baris `Zulu Filter {runId}-107` tidak muncul di tabel terfilter
10. Klik elipsis (⋯) pada baris `Zulu Edit {runId}-107` > `Edit`
11. Isi Description `Edit {runId}-107`
12. Klik `[Save]`
13. Verifikasi toast `Success, category has been updated.` tampil
14. Verifikasi baris `Zulu Edit {runId}-107` hilang dari tabel terfilter
15. Sesi API Principal Automation menghapus `Zulu Filter {runId}-107` hingga penghapusan tersimpan
16. Klik `[Clear Field]` pada Filter lalu `[Apply]`
17. Hilangkan centang `Seed Cat 01`

### TC-FA-CAT-366: Hapus baris terakhir di halaman terakhir

18. Pindah ke halaman 4
19. Verifikasi halaman 4 hanya memuat satu baris `Zulu Edit {runId}-107`
20. Klik elipsis (⋯) pada baris `Zulu Edit {runId}-107` > `Delete`
21. Klik `[Delete]` pada dialog konfirmasi
22. Verifikasi toast `Success, category has been deleted.` tampil
23. Verifikasi tabel pindah ke halaman 3 (halaman terakhir yang masih ada)
24. Verifikasi tabel menampilkan sedikitnya satu baris (tidak ada halaman kosong)

## Notes

- Langkah penghubung (S-03): langkah 3 (mengosongkan Search), 8 (memuat ulang tabel terfilter), 15 sampai 17 (membersihkan data pelaku kedua, Filter, dan seleksi sebelum TC-366, S-09).
- Pelaku kedua memakai sesi API; tidak ada konteks UI kedua (tanpa butir `P-2`).
- Langkah 10 sampai 12 memakai kategori milik spec (`Zulu Edit {runId}-107`) sebagai pengganti `Seed Cat 05` pada TC-386 karena target tulis tidak boleh data Pre-setup (S-06); TC-366 menghapus kategori yang sama sebagai baris ke-31.
- Temuan untuk QA:
  - TC-386 menyebut Filter Modified By `Jane S` aktif sebelum membuat `Zulu Filter` "bernama user lain" tetapi tidak menyebut pemicu pemuatan ulang tabel; spec memakai `[Apply]` ulang (langkah 8).
  - TC-386 butir b dan c memakai `Seed Cat 05` sebagai target Edit yang harus tampil pada tabel terfilter Modified By `Jane S`; mapping Modified By ke nama seed tidak tertulis di Data Uji, sehingga spec memakai baris milik spec ber-Modified By `Jane Smith`.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
