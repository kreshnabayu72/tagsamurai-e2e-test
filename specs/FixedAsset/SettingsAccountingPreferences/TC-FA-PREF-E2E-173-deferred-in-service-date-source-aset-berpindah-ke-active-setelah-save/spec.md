---
id: TC-FA-PREF-E2E-173-deferred-in-service-date-source-aset-berpindah-ke-active-setelah-save
title: "[DEFERRED] In-service Date Source: aset yang berpindah ke Active setelah Save memakai sumber menurut waktu pendaftaran"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-438
  - TC-FA-PREF-439
coverage:
  web: automated
---

# [DEFERRED] In-service Date Source: aset yang berpindah ke Active setelah Save memakai sumber menurut waktu pendaftaran

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5; aset 'assignment - 14' dan 'assignment - 15' dari PC-16 (data modul pemilik, disediakan tim FE setelah modul Asset tersedia). Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Waktu Save (T): TC tidak menyebut nilai T. Pilihan spec: jam server dan jam browser dibekukan bersama pada T = 28 Oktober 2026 pukul 10:00 (Time Zone entitas Asia/Jakarta) lewat kendali jam (kemampuan disediakan tim FE/BE, bagian 6 konvensi). Stempel waktu pendaftaran aset di-seed absolut relatif terhadap T (T - 1 menit untuk 'assignment - 15', T + 1 menit untuk 'assignment - 14'), bukan dihitung dari waktu nyata; margin 1 menit (kurang dari 5 menit) sehingga T dibekukan sebelum Save (bagian 8b butir 3).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed aset dengan stempel waktu pendaftaran yang ditentukan; seed dan pemulihan Preferences; pemindahan status aset ke Active untuk pertama kali (UI modul Asset); pembacaan tanggal mulai penyusutan pada Detail aset.
- State global yang diubah: jam server dan jam browser (dibekukan pada T) dan In-service Date Source company; jam dipulihkan dan Preferences dikembalikan ke nilai awal PC-1 di hook `after` (tetap jalan bila spec gagal di tengah) dan oleh langkah pemulihan terakhir.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-438: Aset didaftarkan setelah Save memakai Activation date saat perubahan dari Manual by Accounting

1. Seed In-service Date Source tersimpan "Manual by Accounting" dan aset 'assignment - 14' terdaftar satu menit setelah T, lalu bekukan jam server dan jam browser pada T lewat kendali jam hingga tersimpan
2. Buka Fixed Asset > Settings > Accounting > Preferences
3. Pilih "Activation date" pada Select In-service Date Source
4. Klik [Save changes]
5. Tunggu aksi selesai
6. Buka daftar aset di modul Asset
7. Ketik Search "assignment - 14", tekan Enter
8. Pindahkan aset 'assignment - 14' ke status Active untuk pertama kali pada 7 Mei 2026
9. Klik Name "assignment - 14" untuk membuka Detail aset
10. Verifikasi Detail aset 'assignment - 14' memakai Activation date sebagai sumber tanggal mulai penyusutan
11. Verifikasi tanggal mulai penyusutan aset 'assignment - 14' adalah 7 Mei 2026

### TC-FA-PREF-439: Aset terdaftar sebelum Save yang belum berstatus operasional tetap memakai sumber lama

12. Seed In-service Date Source tersimpan "Activation date" dan aset 'assignment - 15' terdaftar sebelum T serta belum pernah berstatus operasional, lalu bekukan jam server dan jam browser pada T lewat kendali jam hingga tersimpan
13. Buka Fixed Asset > Settings > Accounting > Preferences
14. Pilih "Manual by Accounting" pada Select In-service Date Source
15. Klik [Save changes]
16. Tunggu aksi selesai
17. Buka daftar aset di modul Asset
18. Ketik Search "assignment - 15", tekan Enter
19. Pindahkan aset 'assignment - 15' ke status Active untuk pertama kali setelah T
20. Klik Name "assignment - 15" untuk membuka Detail aset
21. Verifikasi Detail aset 'assignment - 15' tetap memakai Activation date sebagai sumber tanggal mulai penyusutan
22. Verifikasi tanggal mulai penyusutan aset 'assignment - 15' terisi otomatis dari tanggal aset berpindah ke Active
23. Pulihkan In-service Date Source ke "Activation date" dan jam server serta jam browser ke waktu nyata lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 2 dan 13 (membuka layar Preferences sesudah seed), langkah 5 dan 16 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 6 dan 17 (membuka daftar aset), langkah 7 dan 18 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 23 (pemulihan state global, S-09, R-08).
- Langkah 8 dan 19 memindahkan aset dari baris hasil Search sebelum Detail dibuka; Search tetap berisi nilainya sampai langkah Detail.
- TC-FA-PREF-438 dan 439 memakai nama aset berbeda ('assignment - 14' dan 'assignment - 15', PC-16); seed pada langkah 1 dan 12 membentuk precondition tiap TC tanpa bergantung hasil TC sebelumnya.
- TC-FA-PREF-435 sampai 437 (aset terdaftar sebelum, tepat, dan setelah waktu Save) ada di spec 140.
- Temuan untuk QA:
  - TC-FA-PREF-438 precondition c menyebut aset 'assignment - 14' "terdaftar satu menit setelah waktu Save T" padahal Save terjadi pada langkah TC; spec mengikuti TC dengan men-seed stempel waktu pendaftaran T + 1 menit. Urutan pendaftaran dan Save tidak dijelaskan di TC.
  - TC-FA-PREF-438 Expected memuat dua klausa (memakai Activation date, tanggal mulai penyusutan = 7 Mei 2026) dan ditulis sebagai dua `Verifikasi` (S-01); TC-FA-PREF-439 Expected ditulis dua `Verifikasi` dengan cara yang sama.
  - TC-FA-PREF-439 langkah TC "Pindahkan ... setelah T" (langkah 19) tidak menyebut tanggal pemindahan ke Active; spec tidak menetapkan tanggal dan hanya mengasersi bahwa tanggal mulai penyusutan terisi otomatis dari tanggal pemindahan.
  - TC-FA-PREF-438 dan 439 tidak menyebut nilai T, modul daftar aset, atau hasil Save (toast atau dialog); spec tidak mengasersinya.
  - Post Condition TC-FA-PREF-438 ("Aset sebelum Save tidak berubah") dan TC-FA-PREF-439 ("Sumber aset ditentukan oleh waktu pendaftaran, bukan waktu berpindah status") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
