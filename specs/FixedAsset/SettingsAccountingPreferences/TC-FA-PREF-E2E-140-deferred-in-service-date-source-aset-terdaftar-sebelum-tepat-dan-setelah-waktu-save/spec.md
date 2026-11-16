---
id: TC-FA-PREF-E2E-140-deferred-in-service-date-source-aset-terdaftar-sebelum-tepat-dan-setelah-waktu-save
title: "[DEFERRED] Perubahan In-service Date Source terhadap aset terdaftar sebelum, tepat, dan setelah waktu Save"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-435
  - TC-FA-PREF-436
  - TC-FA-PREF-437
sourceRules: ["FAPREF-LOGIC-04f", "FAPREF-LOGIC-04d"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-04f": [9, 18, 27]
  "FAPREF-LOGIC-04d": 27
coverage:
  web: automated
---

# [DEFERRED] Perubahan In-service Date Source terhadap aset terdaftar sebelum, tepat, dan setelah waktu Save

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (In-service Date Source "Activation date"); Chart of Accounts PC-5; aset 'assignment - 13' dari PC-16 (data modul pemilik, disediakan tim FE setelah modul Asset tersedia). Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Waktu Save (T): TC tidak menyebut nilai T. Pilihan spec: jam server dan jam browser dibekukan bersama pada T = 28 Oktober 2026 pukul 10:00 (Time Zone entitas Asia/Jakarta) lewat kendali jam (kemampuan disediakan tim FE/BE, bagian 6 konvensi). Stempel waktu pendaftaran aset di-seed absolut relatif terhadap T (T - 1 menit, T, T + 1 menit), bukan dihitung dari waktu nyata; margin terhadap batas 1 menit (kurang dari 5 menit) sehingga T dibekukan sebelum Save (bagian 8b butir 3).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed aset dengan stempel waktu pendaftaran yang ditentukan; seed dan pemulihan Preferences; pembacaan sumber tanggal mulai penyusutan pada Detail aset (UI modul Asset).
- State global yang diubah: jam server dan jam browser (dibekukan pada T) dan In-service Date Source company; jam dipulihkan dan Preferences dikembalikan ke nilai awal PC-1 di hook `after` (tetap jalan bila spec gagal di tengah) dan oleh langkah pemulihan terakhir.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-435: Aset didaftarkan sebelum waktu Save memakai sumber in-service date lama

1. Seed In-service Date Source tersimpan "Activation date" dan aset 'assignment - 13' terdaftar pada satu menit sebelum T, lalu bekukan jam server dan jam browser pada T lewat kendali jam hingga tersimpan
2. Buka Fixed Asset > Settings > Accounting > Preferences
3. Pilih "Manual by Accounting" pada Select In-service Date Source
4. Klik [Save changes]
5. Tunggu aksi selesai
6. Buka daftar aset di modul Asset
7. Ketik Search "assignment - 13", tekan Enter
8. Klik Name "assignment - 13" untuk membuka Detail aset
9. Verifikasi Detail aset 'assignment - 13' menampilkan sumber tanggal mulai penyusutan "Activation date"

### TC-FA-PREF-436: Aset didaftarkan tepat pada waktu Save memakai sumber in-service date lama

10. Seed In-service Date Source tersimpan "Activation date" dan aset 'assignment - 13' terdaftar tepat pada T (stempel waktu sama dengan waktu Save), lalu bekukan jam server dan jam browser pada T lewat kendali jam hingga tersimpan
11. Buka Fixed Asset > Settings > Accounting > Preferences
12. Pilih "Manual by Accounting" pada Select In-service Date Source
13. Klik [Save changes]
14. Tunggu aksi selesai
15. Buka daftar aset di modul Asset
16. Ketik Search "assignment - 13", tekan Enter
17. Klik Name "assignment - 13" untuk membuka Detail aset
18. Verifikasi Detail aset 'assignment - 13' menampilkan sumber tanggal mulai penyusutan "Activation date"

### TC-FA-PREF-437: Aset didaftarkan setelah waktu Save memakai sumber in-service date baru

19. Seed In-service Date Source tersimpan "Activation date" dan aset 'assignment - 13' dengan stempel waktu pendaftaran satu menit setelah T, lalu bekukan jam server dan jam browser pada T lewat kendali jam hingga tersimpan
20. Buka Fixed Asset > Settings > Accounting > Preferences
21. Pilih "Manual by Accounting" pada Select In-service Date Source
22. Klik [Save changes]
23. Tunggu aksi selesai
24. Buka daftar aset di modul Asset
25. Ketik Search "assignment - 13", tekan Enter
26. Klik Name "assignment - 13" untuk membuka Detail aset
27. Verifikasi Detail aset 'assignment - 13' menampilkan sumber tanggal mulai penyusutan "Manual by Accounting"
28. Pulihkan In-service Date Source ke "Activation date" dan jam server serta jam browser ke waktu nyata lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 2, 11, dan 20 (membuka layar Preferences sesudah seed; layar dibuka hook `beforeEach` hanya sebelum `it()`), langkah 5, 14, dan 23 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 6, 15, dan 24 (membuka daftar aset), langkah 7, 16, dan 25 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 28 (pemulihan state global, S-09, R-08).
- Satu `it()` berisi tiga TC yang memakai aset bernama sama 'assignment - 13' (PC-16) dengan stempel waktu pendaftaran berbeda; seed ulang pada langkah 1, 10, dan 19 membentuk precondition tiap TC tanpa bergantung hasil TC sebelumnya.
- Temuan untuk QA:
  - TC-FA-PREF-437 precondition c menyebut aset 'assignment - 13' sudah "terdaftar pada satu menit setelah T" padahal Save terjadi pada T di langkah TC; spec mengikuti TC dengan men-seed stempel waktu pendaftaran T + 1 menit (bagian 8b butir 3). Urutan pendaftaran dan Save tidak dijelaskan di TC.
  - TC-FA-PREF-435, 436, dan 437 tidak menyebut nilai T, nama modul daftar aset, atau lokasi sumber tanggal mulai penyusutan pada Detail aset; spec memakai pilihan di Prerequisites dan teks Expected apa adanya.
  - Post Condition TC-FA-PREF-435, 436, dan 437 ("Aset yang sudah ada tidak berubah oleh Save") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-435 sampai 437 tidak menyebut hasil Save (toast atau dialog); spec tidak mengasersinya dan hanya menunggu aksi selesai.
  - TC-FA-PREF-438 dan 439 (perubahan In-service Date Source pada aset yang berpindah ke Active) ada di spec 173; TC-FA-PREF-440 ada di spec 139.
