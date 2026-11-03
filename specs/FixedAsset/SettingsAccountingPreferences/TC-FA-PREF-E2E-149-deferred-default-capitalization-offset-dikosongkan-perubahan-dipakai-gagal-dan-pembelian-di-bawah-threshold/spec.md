---
id: TC-FA-PREF-E2E-149-deferred-default-capitalization-offset-dikosongkan-perubahan-dipakai-gagal-dan-pembelian-di-bawah-threshold
title: "[DEFERRED] Default Capitalization Offset: dikosongkan kembali, perubahan dipakai, kapitalisasi gagal, dan pembelian di bawah threshold"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-481
  - TC-FA-PREF-482
  - TC-FA-PREF-483
  - TC-FA-PREF-605
coverage:
  web: automated
---

# [DEFERRED] Default Capitalization Offset: dikosongkan kembali, perubahan dipakai, kapitalisasi gagal, dan pembelian di bawah threshold

## Prerequisites

- Mode: FE+BE (kegagalan 5xx pada TC-FA-PREF-483 dipaksa lewat `Spectra.intercept()` di atas backend nyata; asersi memuat state backend).
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`1-2900 – Biaya Dikapitalisasi`, `1-2910 – Biaya Dikapitalisasi Proyek` Active, function Capitalization Offset, `1-2950 – Biaya Lama` Inactive); Asset Class PC-6 (Vehicles tanpa threshold sendiri; IT Equipment); aset PC-16 'transfer - 31', 'transfer - 33', 'transfer - 34' siap dikapitalisasi tanpa dokumen sumber dan aset 'assignment - 11' untuk pembelian. Data modul kapitalisasi dan transaksi aset disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Preferences per TC (dibentuk lewat seed): Default Capitalization Offset `1-2900 – Biaya Dikapitalisasi` untuk TC-FA-PREF-481 dan 482; kosong untuk TC-FA-PREF-483; Default Capitalization Threshold 5.000.000 untuk TC-FA-PREF-605.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan aset; kapitalisasi lewat UI modul kapitalisasi; pencatatan pembelian lewat UI modul transaksi aset; `Spectra.intercept()` untuk memaksa respons 5xx pada penyimpanan kapitalisasi (TC-FA-PREF-483), dilepas segera sesudah pemicu; kemampuan baca BE jumlah baris Changelog Preferences (baseline, bagian 8b butir 10).
- State global yang diubah: Default Capitalization Offset company dan status kapitalisasi aset; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-481: Prompt Offset muncul lagi setelah Default Capitalization Offset dikosongkan kembali

1. Seed Default Capitalization Offset tersimpan "1-2900 – Biaya Dikapitalisasi" dan aset 'transfer - 33' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
2. Buka Fixed Asset > Settings > Accounting > Preferences
3. Kosongkan Select Default Capitalization Offset
4. Klik [Save changes]
5. Verifikasi toast "Success, accounting preferences have been saved." tampil
6. Verifikasi tidak ada dialog Save Changes yang tampil
7. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 33' di modul kapitalisasi
8. Verifikasi permintaan akun Capitalization Offset tampil pada kapitalisasi itu

### TC-FA-PREF-482: Perubahan Default Capitalization Offset dipakai kapitalisasi tanpa dokumen sumber berikutnya

9. Seed Default Capitalization Offset tersimpan "1-2900 – Biaya Dikapitalisasi", akun "1-2910 – Biaya Dikapitalisasi Proyek" Active, dan aset 'transfer - 34' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
10. Buka Fixed Asset > Settings > Accounting > Preferences
11. Buka Select Default Capitalization Offset
12. Verifikasi daftar opsi Select Default Capitalization Offset hanya memuat akun Active ber-function Capitalization Offset: "1-2900 – Biaya Dikapitalisasi" dan "1-2910 – Biaya Dikapitalisasi Proyek"
13. Pilih "1-2910 – Biaya Dikapitalisasi Proyek"
14. Klik [Save changes]
15. Verifikasi toast "Success, accounting preferences have been saved." tampil
16. Verifikasi tidak ada dialog Save Changes yang tampil
17. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 34' di modul kapitalisasi
18. Verifikasi kapitalisasi memakai akun "1-2910 – Biaya Dikapitalisasi Proyek"
19. Verifikasi tidak ada permintaan akun Capitalization Offset

### TC-FA-PREF-483: Kapitalisasi yang gagal tidak mengubah Default Capitalization Offset

20. Seed Default Capitalization Offset tersimpan kosong dan aset 'transfer - 31' siap dikapitalisasi tanpa dokumen sumber hingga tersimpan
21. Catat jumlah baris Changelog Preferences lewat kemampuan baca BE (baseline)
22. Pasang intercept respons 5xx pada penyimpanan kapitalisasi
23. Lakukan kapitalisasi tanpa dokumen sumber pada aset 'transfer - 31' di modul kapitalisasi
24. Pilih akun "1-2900 – Biaya Dikapitalisasi" pada permintaan akun Capitalization Offset dan konfirmasi
25. Verifikasi kapitalisasi gagal
26. Lepas intercept respons 5xx
27. Buka Fixed Asset > Settings > Accounting > Preferences
28. Verifikasi Select Default Capitalization Offset tetap kosong
29. Klik ikon View history
30. Verifikasi modal Changelog: Preferences memuat sedikitnya satu baris dan jumlah barisnya sama dengan baseline langkah 21 (tidak ada baris L-03 baru)
31. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-605: Pembelian di bawah Default Capitalization Threshold tetap dapat dicatat sebagai aset

32. Seed Default Capitalization Threshold tersimpan 5.000.000 dan Asset Class Vehicles tanpa threshold sendiri hingga tersimpan
33. Catat pembelian senilai "800000" pada Asset Class Vehicles sebagai aset 'assignment - 11' di modul transaksi aset
34. Verifikasi pembelian tetap dapat dicatat sebagai aset
35. Verifikasi aset 'assignment - 11' tercatat
36. Pulihkan Preferences ke nilai awal PC-1 dan status kapitalisasi aset ke nilai awal lewat seed hingga tersimpan

## Notes

- P-5: TC-FA-PREF-483 adalah objek-uji ringan kelas b (satu kegagalan 5xx pada penyimpanan kapitalisasi) tanpa harness eksternal dan tanpa state berat sendiri; ia berada di spec fungsional dengan permukaan Default Capitalization Offset yang sama, dan hanya satu TC kelas b dalam spec ini.
- Langkah penghubung (S-03): langkah 2, 10, 27 (membuka layar Preferences), langkah 26 (melepas intercept segera sesudah pemicu, S-09), langkah 31 (menutup modal Changelog), langkah 36 (pemulihan state, S-09, R-08).
- Asersi "tidak ada baris L-03 baru" pada TC-FA-PREF-483 diasersi sebagai selisih jumlah terhadap baseline (asersi jumlah, S-12) dengan anchor sedikitnya satu baris pada modal yang sama (bagian 8b butir 2); spec absence tidak memuat aksi untuk TC ini.
- Seed per TC (langkah 1, 9, 20, 32) membentuk precondition tanpa bergantung hasil TC sebelumnya.
- Spec 36 langkah, di atas 35 langkah. Alasan: tiap blok TC berdiri sendiri dengan seed dan precondition sendiri (langkah 1, 9, 20, 32) tanpa bergantung hasil blok lain, dan semuanya satu permukaan Default Capitalization Offset; langkah pemulihan terakhir (langkah 36) dan hook `after` mengembalikan state. Jumlah langkah terutama dari Expected yang dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-PREF-481 dan 482 Expected "Toast ... tampil tanpa dialog Save Changes" memuat dua klausa dan ditulis dua `Verifikasi` (S-01).
  - TC-FA-PREF-483 precondition c tidak menyebut endpoint yang di-intercept; spec menyebut "penyimpanan kapitalisasi" tanpa endpoint karangan (S-13), nama endpoint disediakan tim FE.
  - TC-FA-PREF-483 Expected a ("Kapitalisasi gagal") tidak menyebut tanda tampilan kegagalan; spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-605 menyebut HINT volume (e) pada indeks tetapi hanya satu pembelian; diperlakukan fungsional.
  - TC-FA-PREF-605 Expected a memuat klausa tambahan ("threshold hanya berupa saran agar dibebankan dan tidak memblokir pencatatan") yang tidak punya tanda teramati terpisah; langkah 34 mengasersi klausa utama (pembelian tetap dapat dicatat).
  - Post Condition TC-FA-PREF-481, 482, 483, dan 605 adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
  - TC-FA-PREF-476 sampai 480 ada di spec 148.
