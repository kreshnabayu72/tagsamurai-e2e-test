---
id: TC-FA-RP-E2E-056-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-1
title: "Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-187
  - TC-FA-RP-188
  - TC-FA-RP-189
coverage:
  web: automated
---

# Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso, Budi Setiawan, Citra Lestari, Dimas Pranata, Endah Susanti; Citra Lestari memegang Global Role `Import data` Read saja, `Manage Open API` Read dan Update, `Manage accounting` CRUD penuh) dan #36 (Tab Total Control terisi).
- Waktu: jam server dan jam browser sinkron untuk asersi Last Updated (S-12); waktu dicatat sesudah `[Assign]` dan Last Updated dibandingkan dengan toleransi satu menit.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-187: Assign Total Control ke satu user Standard lewat popup

1. Klik `[+ Assign]` di Tab Total Control
2. Centang Ahmad Fauzi
3. Klik `[Assign]`
4. Catat waktu sesudah `[Assign]` untuk pembanding Last Updated
5. Verifikasi popup tertutup
6. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
7. Ketik Search `Ahmad Fauzi`, tekan Enter
8. Verifikasi baris Ahmad Fauzi (Asset Custodian, Logistics, Status `Active`) tampil di Tab Total Control
9. Verifikasi kolom Modified By baris Ahmad Fauzi berisi `Siti R`
10. Verifikasi kolom Last Updated baris Ahmad Fauzi berisi waktu Assign sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
11. Klik `(←)` pada kotak Search

### TC-FA-RP-188: Assign Total Control ke tiga user sekaligus menghasilkan satu toast tunggal

12. Tunggu toast lama hilang otomatis
13. Klik `[+ Assign]` di Tab Total Control
14. Centang Budi Santoso, Budi Setiawan, dan Dimas Pranata
15. Amati counter
16. Verifikasi counter sebelum Assign `3 Users selected`
17. Klik `[Assign]`
18. Verifikasi muncul satu toast sukses: `Success, Total Control has been assigned.` (bentuk tunggal tanpa angka)
19. Ketik Search `Budi`, tekan Enter
20. Verifikasi baris Budi Santoso dan Budi Setiawan tampil di Tab Total Control
21. Ganti isi kotak search dengan `Dimas Pranata`, tekan Enter
22. Verifikasi baris Dimas Pranata tampil di Tab Total Control
23. Klik `(←)` pada kotak Search

### TC-FA-RP-189: Assign Total Control menyelaraskan seluruh Global Role user dengan penugasan parsial

24. Klik `[+ Assign]` di Tab Total Control
25. Centang Citra Lestari lalu klik `[Assign]`
26. Tunggu aksi selesai: popup tertutup
27. Buka Tab System lalu Detail Role `Import data`
28. Verifikasi baris Citra Lestari: Create dan Read aktif
29. Verifikasi baris Citra Lestari: Update dan Delete menampilkan `—`
30. Buka Detail Role `Manage Open API`
31. Verifikasi baris Citra Lestari: Read dan Update aktif
32. Verifikasi baris Citra Lestari: Create dan Delete menampilkan `—`
33. Buka Detail Role `Manage asset transactional policy`
34. Verifikasi baris Citra Lestari (baru): Read dan Update aktif
35. Verifikasi baris Citra Lestari (baru): Create dan Delete menampilkan `—`
36. Buka Detail Role `Manage accounting`
37. Verifikasi baris Citra Lestari: Create, Read, Update, dan Delete aktif
38. Buka Detail Role Group Role `Manage files` lalu klik `All Groups`
39. Ketik Search `Citra Lestari`, tekan Enter
40. Verifikasi pada setiap group baris Citra Lestari tampil di Detail Role `Manage files` dengan Read dan Delete aktif (CRUD penuh sesuai kolom berlaku; Group Role ikut cascade pola tier, `FARP-LOGIC-17a`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 40 langkah.
- Langkah penghubung (S-03): langkah 4, 11–12, 23, 26, 38–39. Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 7, 19, 21.
- TC-FA-RP-187 Post Condition a sampai d, TC-FA-RP-189 Post Condition a dan b, dan Post Condition TC-FA-RP-188 tidak punya langkah observasi di TC sehingga tidak diasersi; entri log dan refleksi Tab Role Settings > User tidak diklaim teruji (S-01, S-15).
- Langkah Search pada Tab Total Control (langkah 7, 19, 21) menemukan baris yang baru ditambahkan karena tabel berisi lebih banyak baris daripada satu halaman (R-16).
- Temuan untuk QA:
  - TC-FA-RP-189 Expected e memuat klausa entri Changelog per Role × Group (`Assign (via Total Control)` dan `Edit`) tanpa langkah observasi di TC; klausa itu hanya dirujuk ke TC-FA-RP-860 yang diasersi dengan aksi nyata di spec `TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1` (S-05, S-15), sehingga langkah 40 hanya mengasersi baris Citra Lestari di Detail Role `Manage files`.
  - TC-FA-RP-189 Expected e menyebut "setiap group" tanpa daftar group; langkah 40 mengamati baris Citra Lestari pada hasil Search `All Groups` untuk seluruh group pohon Pre-setup #18.
  - Post Condition b TC-FA-RP-189 (kolom Users Tab System Global Role dan Group Role bertambah) tidak punya langkah observasi di TC; tidak diasersi.
- Ukuran spec (40 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan ketiga blok (TC-FA-RP-187, 188, 189) berurutan pada popup Assign Total Control di Tab Total Control dengan user dan Pre-setup yang sama, kondisi awalnya dibuat seeding di hook `before` dan Pre-setup dipulihkan di hook `after`, sehingga memecahnya hanya menggandakan login, hook, dan pembukaan popup yang sama tanpa membuat blok lebih mandiri; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
