---
id: TC-AC-PP-E2E-055-konkurensi-dua-admin-publish
title: "Konkurensi Dua Admin Mem-publish Bersamaan pada Versi Active dan First-time Setup"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-187
  - TC-AC-PP-188
coverage:
  web: automated
---

# Konkurensi Dua Admin Mem-publish Bersamaan pada Versi Active dan First-time Setup

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks, race antar-sesi): dua konteks browser dengan dua admin berbeda yang menekan `[Publish]` pada waktu hampir bersamaan. Kolom Automation TC bernilai "Manual Only — (d) dua sesi paralel dalam satu skenario"; sesuai konvensi bagian 2, kebutuhan ini ditulis di Prerequisites sebagai sumber resmi bagi tim FE.

| Konteks | Peran | Nama tampil | Email | Env var password |
|---|---|---|---|---|
| A (akun default hook `before`) | Total Control (Pre-setup 1) | `Andi Wijaya` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| B (Pre-setup 6) | Total Control | `Rina Kusuma` | `secondAdminAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC2_PASSWORD` |

- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1) lalu login konteks A sebagai Total Control (aktor pertama). Login `Rina Kusuma` di konteks B adalah langkah eksplisit di `## Test Steps`.
- Dataset berganti di tengah spec lewat Fixture BE: Riwayat A untuk TC-AC-PP-187 lalu Riwayat C (0 versi) untuk TC-AC-PP-188.
- Hook `after` (tetap jalan walau spec gagal): logout konteks B, mengembalikan dataset ke Riwayat A lewat Fixture BE, dan mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Kemampuan teknis: dua konteks browser paralel dengan orkestrasi klik `[Publish]` pada kedua konteks dalam jendela waktu yang sangat berdekatan (barrier sinkronisasi antar konteks); Fixture BE (seeding Riwayat A dan C). Nama env `AC_TC2_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`, belum terdaftar (`AC_TC_PASSWORD` sudah terdaftar).
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish beberapa versi, sehingga suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Seluruh TC |

## Test Steps

### TC-AC-PP-187: Dua admin mem-publish hampir bersamaan dari versi Active yang sama, keduanya berhasil berurutan

1. Pada konteks A (`Andi Wijaya`), buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
2. Buka konteks B sebagai browser terpisah dan login sebagai `secondAdminAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Rina Kusuma`, `Spectra.env.AC_TC2_PASSWORD`), lalu buka Settings > Privacy Policy
3. Pada konteks A, klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
4. Pada konteks A, tambahkan " Edit A." di akhir konten editor
5. Pada konteks A, klik `[Publish New Version]` sehingga Dialog Publish Confirm terbuka
6. Pada konteks B, klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
7. Pada konteks B, tambahkan " Edit B." di akhir konten editor
8. Pada konteks B, klik `[Publish New Version]` sehingga Dialog Publish Confirm terbuka
9. Tekan `[Publish]` pada konteks A dan konteks B pada waktu hampir bersamaan
10. Verifikasi konteks A menerima toast sukses "Success, Privacy Policy has been published."
11. Verifikasi konteks B menerima toast sukses "Success, Privacy Policy has been published."
12. Muat ulang tabel Version History pada konteks A
13. Verifikasi tabel menampilkan `Version 5` (Active), `Version 4`, `Version 3`, `Version 2`, `Version 1` secara berurutan
14. Verifikasi tidak ada nomor versi ganda pada tabel
15. Verifikasi tidak ada dialog konflik pada kedua konteks
16. Verifikasi tidak ada toast error pada kedua konteks
17. Klik teks tautan `Version 4` pada konteks A
18. Verifikasi konten `Version 4` memuat tepat satu dari tambahan " Edit A." atau " Edit B." (konten admin yang diproses lebih dulu)
19. Tutup Modal View dengan `[✕]` lalu klik teks tautan `Version 5`
20. Verifikasi konten `Version 5` memuat tambahan lainnya dari pasangan " Edit A." dan " Edit B." (konten admin yang diproses kemudian)
21. Verifikasi Published At `Version 5` sama dengan atau lebih akhir daripada Published At `Version 4` pada kolom Published At tabel dan urutan baris default (Published At Newest First)

### TC-AC-PP-188: Dua admin mem-publish pertama kali bersamaan saat belum ada versi, satu menjadi Version 1 dan satu Version 2

22. Tutup Modal View dengan `[✕]` pada konteks A, lalu kembalikan dataset ke Riwayat C (0 versi) lewat Fixture BE dan muat ulang Settings > Privacy Policy pada konteks A dan konteks B
23. Pada konteks A, klik [Create Privacy Policy]
24. Pada konteks A, ketik "Policy A" pada editor
25. Pada konteks A, klik `[Publish New Version]` sehingga Dialog Publish Confirm terbuka
26. Pada konteks B, klik [Create Privacy Policy]
27. Pada konteks B, ketik "Policy B" pada editor
28. Pada konteks B, klik `[Publish New Version]` sehingga Dialog Publish Confirm terbuka
29. Tekan `[Publish]` pada konteks A dan konteks B pada waktu hampir bersamaan
30. Verifikasi konteks A menerima toast sukses "Success, Privacy Policy has been published."
31. Verifikasi konteks B menerima toast sukses "Success, Privacy Policy has been published."
32. Muat ulang tabel Version History pada konteks A
33. Verifikasi tabel menampilkan `Version 2` (Active) dan `Version 1`
34. Verifikasi tidak ada nomor versi ganda pada tabel
35. Verifikasi tidak ada error yang tampil ke user pada kedua konteks
36. Klik teks tautan `Version 1`
37. Verifikasi konten `Version 1` memuat salah satu dari "Policy A" atau "Policy B"
38. Tutup Modal View dengan `[✕]` lalu klik teks tautan `Version 2`
39. Verifikasi konten `Version 2` memuat teks lainnya dari pasangan "Policy A" dan "Policy B"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness c. Dua TC berbagi kelas dan topik (Publish bersamaan oleh dua admin) tetapi memakai dataset berbeda (Riwayat A lalu Riwayat C); dataset diganti lewat Fixture BE di langkah 22.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 2 (login `Rina Kusuma` di konteks B, ganti akun eksplisit), 19 dan 38 (tutup Modal View sebelum membuka versi berikutnya), dan 22 (tutup Modal View, ganti dataset ke Riwayat C lewat Fixture BE, muat ulang kedua konteks).
- Asersi atas TC: langkah 18, 20, 37, dan 39 menerjemahkan "konten sesuai konten yang diketik admin yang diproses pada urutannya" dan "sesuai teks Policy A dan Policy B" menjadi pasangan {A, B}, karena urutan pemrosesan tidak deterministik dalam race; ini penjabaran Expected d TC-AC-PP-187 dan Expected c TC-AC-PP-188, bukan asersi tambahan.
- Ukuran spec: 39 langkah (melewati sekitar 35) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01) dan dua konteks browser. Spec tidak dipecah: kedua blok TC mandiri (dataset di-reseed lewat Fixture BE di langkah 22), satu kelas harness (c), sehingga kegagalan TC-AC-PP-187 tidak membuat TC-AC-PP-188 kehilangan makna.
- Temuan untuk QA:
  - TC-AC-PP-187 Expected e meminta Published At `Version 5` "sama dengan atau lebih akhir" daripada `Version 4`, sementara Published At di UI hanya menampilkan tanggal tanpa jam (NC-11); perbandingan tingkat detik tidak dapat diamati di UI. Langkah 21 mengasersi tanggal dan urutan baris default; perbandingan waktu tepat membutuhkan pengamatan respons server (wilayah TC backend).
  - TC-AC-PP-187 dan TC-AC-PP-188 tidak menyatakan cara kedua klik `[Publish]` disinkronkan; TC hanya menulis "pada waktu hampir bersamaan". Cara orkestrasi (barrier antar konteks) dicatat sebagai kemampuan teknis di Prerequisites.
  - Post Condition kedua TC ("dua versi baru tersimpan berurutan dan dua record audit") tidak punya langkah observasi sendiri dan tidak diasersi di luar Expected.
