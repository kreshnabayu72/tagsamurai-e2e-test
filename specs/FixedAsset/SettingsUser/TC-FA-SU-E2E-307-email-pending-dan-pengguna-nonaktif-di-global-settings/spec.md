---
id: TC-FA-SU-E2E-307-email-pending-dan-pengguna-nonaktif-di-global-settings
title: "Email Pending dan Pengguna Nonaktif di Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-946
  - TC-FA-SU-947
  - TC-FA-SU-948
coverage:
  web: automated
---

# Email Pending dan Pengguna Nonaktif di Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), layanan (#37), dan Global Settings (#38). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Indra Wijaya {runId}-307`, email `indra.wijaya+{runId}-307@qwertysystem.net`: Pending Email Confirmation dengan alamat email baru pending `indra.wijaya.baru+{runId}-307@qwertysystem.net`.
  - `Rudi Hartono {runId}-307`, email `rudi.hartono+{runId}-307@qwertysystem.net`: sakelar FAMS ON dan nonaktif di Global Settings (Inactive efektif).
- Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-947: Email pending di Detail: teks Pending email change tanpa tombol aksi

1. Ketik Search `Indra Wijaya {runId}-307`, tekan Enter, lalu klik nama Indra Wijaya {runId}-307 untuk membuka Detail
2. Verifikasi field Email Indra Wijaya {runId}-307 menampilkan alamat saat ini dan teks `Pending email change to indra.wijaya.baru+{runId}-307@qwertysystem.net` di sampingnya
3. Verifikasi tidak ada tombol konfirmasi atau pembatalan perubahan email di FAMS

### TC-FA-SU-946: Email Confirmed atau Cancel di Global Settings: status Pending Email Confirmation hilang dan Resend lenyap

4. Catat jumlah entri Tab Changelog Indra Wijaya {runId}-307 sebagai baseline
5. Principal Automation mengonfirmasi perubahan email Indra Wijaya {runId}-307 di Global Settings hingga konfirmasi tersimpan
6. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Indra Wijaya {runId}-307`, tekan Enter
7. Verifikasi baris Indra Wijaya {runId}-307 tampil pada User List
8. Verifikasi badge `Pending Email Confirmation` baris Indra Wijaya {runId}-307 hilang
9. Klik ⋯ pada baris Indra Wijaya {runId}-307
10. Verifikasi menu row action terbuka dan memuat sedikitnya satu item aksi lain (pembanding)
11. Verifikasi menu row action tidak memuat `Resend Confirmation Email`
12. Tutup menu, lalu klik nama Indra Wijaya {runId}-307 untuk membuka Detail
13. Verifikasi field Email menampilkan alamat baru `indra.wijaya.baru+{runId}-307@qwertysystem.net`
14. Verifikasi field Email tidak memuat teks `Pending email change to`
15. Buka Tab Changelog
16. Verifikasi header kolom Tab Changelog tampil
17. Verifikasi jumlah entri Tab Changelog Indra Wijaya {runId}-307 sama dengan baseline (modul ini tidak menulis log)

### TC-FA-SU-948: Pengguna nonaktif di Global Settings: status Inactive efektif, sakelar terkunci posisi terakhir dipertahankan, dan kembali interaktif

18. Catat jumlah entri Tab Changelog Rudi Hartono {runId}-307 sebagai baseline
19. Ketik Search `Rudi Hartono {runId}-307`, tekan Enter, lalu klik nama Rudi Hartono {runId}-307 untuk membuka Detail
20. Verifikasi badge status Detail Rudi Hartono {runId}-307 `Inactive`
21. Verifikasi sakelar FAMS Rudi Hartono {runId}-307 menampilkan posisi ON terakhir
22. Principal Automation mengaktifkan Rudi Hartono {runId}-307 di Global Settings hingga perubahan tersimpan
23. Tunggu aksi selesai, lalu muat ulang Detail Rudi Hartono {runId}-307
24. Verifikasi sakelar Rudi Hartono {runId}-307 interaktif dengan posisi ON yang sama
25. Buka Tab Changelog
26. Verifikasi header kolom Tab Changelog tampil
27. Verifikasi jumlah entri Tab Changelog Rudi Hartono {runId}-307 sama dengan baseline (modul ini tidak menulis log untuk peristiwa Global Settings)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-947 (membaca keadaan pending) dikerjakan sebelum TC-FA-SU-946 yang mengonfirmasi email (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 6, 9, 12, 15, 19, 23, 25; langkah baseline jumlah entri (S-12): 4, 18. Langkah 7 dan 10 adalah anchor positif untuk asersi absence berikutnya (8b.2). Langkah 1 juga Search untuk menemukan baris target (R-16).
- Klausa "tidak menulis log" ditulis sebagai asersi jumlah dengan baseline dan anchor header kolom (S-12), bukan asersi absence kelas g.
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-307` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-946 menyebut "Email Confirmed atau Cancel" tetapi Langkah Uji hanya memuat konfirmasi; jalur Cancel tidak diasersi. Post Condition TC-FA-SU-946 butir b (tidak ada entri log) sama dengan butir b Expected.
  - TC-FA-SU-948 tidak menyebut apakah sakelar tampil Disabled saat nonaktif di Global Settings (itu dicakup TC-FA-SU-13); spec mengasersi hanya posisi ON dan keadaan interaktif sesudah aktif kembali.
