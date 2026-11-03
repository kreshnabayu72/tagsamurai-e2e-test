---
id: TC-FA-CAID-E2E-044-multi-konteks-dua-admin-bersamaan
title: "Multi-Konteks: Dua Admin Registrasi dan Save Konfigurasi Bersamaan, Last-Write-Wins"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-324
  - TC-FA-CAID-326
  - TC-FA-CAID-327
coverage:
  web: automated
---

# Multi-Konteks: Dua Admin Registrasi dan Save Konfigurasi Bersamaan, Last-Write-Wins

## Prerequisites

- Mode: FE+BE.
- Akun aktor: sesi 1 Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`; sesi 2 Total Control sesi kedua `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 8), password `Spectra.env.FA_TC2_PASSWORD`. Keduanya login di hook `before` spec ini pada konteks browser terpisah (Company Alpha dua sesi, Pre-setup No 23); sesi 1 membuka halaman lewat hook `beforeEach` suite, sesi 2 ditutup di hook `after`.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11; A5 Deleted ber-Increment 5 sehingga Increment berikutnya 6), dipulihkan oleh hook `beforeEach` suite; form Quick Register berisi Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan aksi bersamaan pada dua sesi UI dengan selisih kurang dari satu detik (disediakan tim FE; TC berlabel Manual Only karena dua sesi paralel); kemampuan membaca jumlah entri Modal Changelog: Custom Asset ID sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: dua aset Draft baru terdaftar, konfigurasi dan Asset ID Company Alpha berubah. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-324: Dua aset diregistrasi bersamaan mendapat Increment berbeda

1. Di sesi 1 buka Fixed Asset > Assets > Registration, lalu isi form Quick Register: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`
2. Di sesi 2 buka Fixed Asset > Assets > Registration, lalu isi form Quick Register dengan nilai yang sama
3. Klik `[Save as Draft]` di sesi 1 dan sesi 2 pada detik yang sama
4. Tunggu aksi selesai di sesi 1 dan sesi 2
5. Buka Fixed Asset > Assets > All Assets di sesi 1
6. Verifikasi kedua aset tersimpan dengan Asset ID berbeda yang berakhiran Increment berurutan, yaitu `JKT/LAP/T490/0000/6` dan `JKT/LAP/T490/0000/7` dalam urutan mana pun
7. Verifikasi tidak ada dua aset ber-Increment sama

### TC-FA-CAID-326: Dua admin menyimpan konfigurasi nyaris bersamaan

8. Di sesi 1 dan sesi 2 buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Modal Changelog: Custom Asset ID
9. Di sesi 1 pilih Separator `- (Dash)`; di sesi 2 pilih Separator `. (Dot)`
10. Klik `[Save]` di sesi 1 lalu di sesi 2 dalam selisih kurang dari satu detik
11. Verifikasi tidak ada dialog konflik di sesi 1 dan sesi 2
12. Verifikasi kedua Save menampilkan toast sukses `Success, Custom Asset ID configuration has been updated.`
13. Muat ulang sesi 1 dan sesi 2
14. Buka Modal Changelog: Custom Asset ID di sesi 1
15. Verifikasi Modal Changelog bertambah dua entri Edit Separator (untuk kedua Save) dibanding baseline
16. Tutup Modal Changelog: Custom Asset ID
17. Verifikasi Separator konfigurasi akhir di sesi 1 dan sesi 2 sama dengan New Value entri Edit Separator terbaru, yaitu Save yang tiba terakhir
18. Buka Fixed Asset > Assets > All Assets di sesi 1
19. Verifikasi Asset ID seluruh aset berformat konfigurasi akhir itu, tanpa campuran dua separator

### TC-FA-CAID-327: Dua admin menggeser Master Switch ke arah berbeda nyaris bersamaan

20. Atur konfigurasi Company Alpha ke baseline B1 (seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1 dan sesi 2
21. Di sesi 1 geser Master Switch ke OFF dan klik `[Disable]`; di sesi 2 pada saat yang sama pilih Separator `- (Dash)` lalu klik `[Save]`
22. Verifikasi tidak ada dialog konflik di sesi 1 dan sesi 2
23. Muat ulang sesi 1 dan sesi 2
24. Verifikasi kondisi akhir konfigurasi (Master Switch dan Separator) konsisten dengan permintaan yang tiba terakhir, tanpa status campuran
25. Buka Fixed Asset > Assets > All Assets di sesi 1
26. Verifikasi seluruh Asset ID konsisten dengan permintaan yang tiba terakhir, tanpa status campuran (nomor polos `1`, `2`, `3` bila Master Switch OFF; format Dash bila Master Switch ON dengan Separator Dash)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 4 (tunggu aksi selesai karena langkah berikutnya berpindah surface), langkah 5, 8, 14, 18, 20, dan 25 (membuka halaman), langkah 13 dan 23 (muat ulang pada form pristine), langkah 16 (menutup modal), langkah 20 (pemulihan baseline lewat seed), dan baseline jumlah entri pada langkah 8 (S-12).
- Langkah 17 membaca Save yang tiba terakhir dari entri Edit Separator terbaru di Modal Changelog, sesuai Expected b TC-FA-CAID-326; langkah 15 (jumlah entri bertambah dua dibanding baseline) menjadi anchor positif untuk pembacaan itu.
- Pembagian TC lintas spec: TC-FA-CAID-328 dan TC-FA-CAID-329 ada di spec 048; TC-FA-CAID-330 dan TC-FA-CAID-331 di spec 045; TC-FA-CAID-310 dan TC-FA-CAID-311 di spec 043.
- Temuan untuk QA:
  - TC-FA-CAID-324, TC-FA-CAID-326, dan TC-FA-CAID-327 berlabel Manual Only (dua sesi paralel); spec tetap ditulis dengan kemampuan aksi bersamaan di Prerequisites.
  - TC-FA-CAID-327 Expected "konsisten dengan permintaan yang tiba terakhir" tidak menyebut cara menentukan permintaan terakhir (TC-FA-CAID-326 menyebutnya lewat entri Edit Separator terbaru, TC-FA-CAID-327 tidak); spec mengasersi dua keadaan konsisten yang dirinci TC (OFF dengan Asset ID polos, atau ON dengan Separator Dash dan Asset ID berformat Dash).
  - TC-FA-CAID-324 menyebut Increment `6` dan `7` yang bergantung pada A5 Deleted ber-Increment 5 (Pre-setup No 11); diasersi sesuai TC.
  - Post Condition TC-FA-CAID-324, TC-FA-CAID-326, dan TC-FA-CAID-327 tidak diasersi karena TC tidak memberi langkah observasinya.
