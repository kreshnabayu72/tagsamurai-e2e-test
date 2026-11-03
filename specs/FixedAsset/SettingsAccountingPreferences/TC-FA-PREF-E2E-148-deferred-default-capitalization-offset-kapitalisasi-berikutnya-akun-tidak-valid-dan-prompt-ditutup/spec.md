---
id: TC-FA-PREF-E2E-148-deferred-default-capitalization-offset-kapitalisasi-berikutnya-akun-tidak-valid-dan-prompt-ditutup
title: "[DEFERRED] Default Capitalization Offset: kapitalisasi berikutnya, akun tidak valid, dan prompt ditutup"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-476
  - TC-FA-PREF-477
  - TC-FA-PREF-478
  - TC-FA-PREF-479
  - TC-FA-PREF-480
coverage:
  web: automated
---

# [DEFERRED] Default Capitalization Offset: kapitalisasi berikutnya, akun tidak valid, dan prompt ditutup

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`1-2900 – Biaya Dikapitalisasi`, `6-9300 – Rugi Penghapusan Lama` Inactive); Asset Class IT Equipment; aset PC-16 'transfer - 31' dan 'transfer - 33' siap dikapitalisasi tanpa dokumen sumber, 'transfer - 32' dengan cost line sudah dicocokkan ke dokumen sumber. Data modul kapitalisasi dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Default Capitalization Offset per TC (dibentuk lewat seed): `1-2900 – Biaya Dikapitalisasi` untuk TC-FA-PREF-476; kosong untuk TC-FA-PREF-477, 478, 479, dan 480.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, aset, dan cost line; kapitalisasi lewat UI modul kapitalisasi (permintaan akun Capitalization Offset); kemampuan baca BE jumlah baris Changelog Preferences (baseline, bagian 8b butir 10); pembacaan status ditahan jurnal kapitalisasi pada Export Journal.
- State global yang diubah: Default Capitalization Offset company dan status kapitalisasi aset; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-476: Kapitalisasi berikutnya memakai akun default tanpa meminta ulang

1. Seed Default Capitalization Offset tersimpan "1-2900 – Biaya Dikapitalisasi" dan aset 'transfer - 31' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
2. Catat jumlah baris Changelog Preferences lewat kemampuan baca BE (baseline)
3. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
4. Verifikasi kapitalisasi memakai akun "1-2900 – Biaya Dikapitalisasi"
5. Verifikasi tidak ada permintaan akun Capitalization Offset
6. Buka Fixed Asset > Settings > Accounting > Preferences
7. Klik ikon View history
8. Verifikasi modal Changelog: Preferences memuat sedikitnya satu baris dan jumlah barisnya sama dengan baseline langkah 2 (tidak ada baris baru)
9. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-477: Kapitalisasi dengan cost line sudah dicocokkan ke dokumen sumber tidak memakai dan tidak meminta Offset

10. Seed Default Capitalization Offset tersimpan kosong dan cost line aset 'transfer - 32' sudah dicocokkan ke dokumen sumber hingga tersimpan
11. Lakukan kapitalisasi aset 'transfer - 32' di modul kapitalisasi
12. Verifikasi kapitalisasi selesai tanpa permintaan akun Capitalization Offset
13. Buka Fixed Asset > Settings > Accounting > Preferences
14. Verifikasi Select Default Capitalization Offset tetap kosong

### TC-FA-PREF-478: Akun Offset yang tidak valid ditolak dan Default Capitalization Offset tidak berubah

15. Seed Default Capitalization Offset tersimpan kosong, akun "6-9300 – Rugi Penghapusan Lama" berstatus Inactive, dan aset 'transfer - 31' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
16. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
17. Pilih akun "6-9300 – Rugi Penghapusan Lama" (Inactive) pada permintaan akun dan konfirmasi
18. Verifikasi pemilihan akun ditolak oleh evaluasi server
19. Buka Fixed Asset > Settings > Accounting > Preferences
20. Verifikasi Select Default Capitalization Offset tetap kosong

### TC-FA-PREF-479: Menutup prompt Offset tanpa memilih akun tetap menjalankan kapitalisasi dengan Offset kosong

21. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
22. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
23. Tutup permintaan akun Capitalization Offset tanpa memilih akun
24. Verifikasi kapitalisasi tetap berjalan
25. Buka Fixed Asset > Settings > Accounting > Preferences
26. Verifikasi Select Default Capitalization Offset tetap kosong
27. Buka Export Journal
28. Verifikasi jurnal kapitalisasi aset 'transfer - 31' ditahan saat Export Journal sampai akun diisi

### TC-FA-PREF-480: Prompt Offset muncul lagi pada kapitalisasi berikutnya selama Offset masih kosong

29. Seed Default Capitalization Offset tersimpan kosong setelah prompt kapitalisasi sebelumnya ditutup tanpa memilih akun dan aset 'transfer - 33' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
30. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 33' di modul kapitalisasi
31. Verifikasi permintaan akun Capitalization Offset tampil lagi
32. Pulihkan Default Capitalization Offset ke kosong dan status kapitalisasi aset ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 6, 13, 19, 25 (membuka layar Preferences), langkah 9 (menutup modal Changelog), langkah 27 (membuka Export Journal), langkah 32 (pemulihan state, S-09, R-08).
- Asersi "tidak ada baris baru" pada TC-FA-PREF-476 diasersi sebagai selisih jumlah terhadap baseline (asersi jumlah, S-12) dengan anchor sedikitnya satu baris pada modal yang sama (bagian 8b butir 2), bukan asersi log kelas g; spec absence tidak memuat aksi untuk TC ini.
- Langkah 28 membaca jurnal pada daftar Export Journal tanpa Search karena TC hanya menyebut "jurnal kapitalisasi ditahan"; jika daftar memuat lebih dari satu halaman, tim FE menyediakan cara menemukan baris (lihat Temuan untuk QA).
- Seed per TC (langkah 1, 10, 15, 21, 29) membentuk precondition tanpa bergantung hasil TC sebelumnya.
- Temuan untuk QA:
  - TC-FA-PREF-478 langkah TC menyebut "akun yang tidak memenuhi syarat (Inactive atau bukan function Capitalization Offset)"; spec memilih akun `6-9300 – Rugi Penghapusan Lama` (Inactive, PC-5) untuk menutup ambiguitas.
  - TC-FA-PREF-478 Expected a ("ditolak oleh evaluasi server") tidak menyebut pesan atau tampilan penolakan; spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-479 Expected c tidak menyebut cara menemukan jurnal kapitalisasi pada Export Journal; spec tidak menambah Search.
  - TC-FA-PREF-476 Expected a memuat dua klausa (memakai akun, tanpa permintaan akun) dan ditulis dua `Verifikasi` (S-01).
  - Post Condition TC-FA-PREF-476 sampai 480 adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
  - TC-FA-PREF-480 mensyaratkan keadaan setelah prompt ditutup pada TC-FA-PREF-479; spec men-seed keadaan itu sendiri tanpa bergantung TC lain.
  - TC-FA-PREF-471 sampai 475 ada di spec 147; TC-FA-PREF-481 sampai 483 dan 605 ada di spec 149.
