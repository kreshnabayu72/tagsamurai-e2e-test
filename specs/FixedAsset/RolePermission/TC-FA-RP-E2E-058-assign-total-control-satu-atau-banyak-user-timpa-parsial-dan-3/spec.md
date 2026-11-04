---
id: TC-FA-RP-E2E-058-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-3
title: "Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (3/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1085
  - TC-FA-RP-1139
coverage:
  web: automated
---

# Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Budi Santoso memegang Global Role `Manage accounting` inactive-retained dengan Create dan Update aktif, Delete tidak aktif; Citra Lestari dan lainnya), #12 (Maya Anggraeni Read Only: seluruh Global Role hanya Read; baris pola Group Role Read saja pada setiap group, termasuk `Manage files` di `Data Center`), #24 (Company Changelog), #18 (pohon group).
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Detail Role `Manage accounting` dan daftar penugasan Group Role Maya Anggraeni dicatat sebagai baseline sebelum aksi.
- Urutan default Changelog: entri terbaru di atas (asumsi, tidak disebut TC; lihat Temuan untuk QA). Asersi isi Changelog hanya atas entri terbaru karena audit trail permanen tumbuh (S-14).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1085: Assign Total Control pada user dengan Global Role inactive-retained parsial menyelaraskan CRUD penuh dan mencatat Edit hanya kolom yang berubah

1. Klik Tab `System`
2. Buka Detail Role `Manage accounting`
3. Klik ikon Changelog di toolbar Detail Role
4. Catat jumlah entri Changelog sebagai baseline
5. Tutup modal
6. Klik Tab `Total Control`
7. Klik `[+ Assign]` di Tab Total Control
8. Centang Budi Santoso lalu klik `[Assign]`
9. Tunggu aksi selesai: popup tertutup
10. Buka Tab System lalu Detail Role `Manage accounting`
11. Verifikasi baris Budi Santoso tampil kembali dengan Create, Read, Update, dan Delete aktif (CRUD penuh sesuai kolom yang berlaku)
12. Klik ikon Changelog di toolbar Detail Role
13. Verifikasi Changelog memuat entri `Assign (via Total Control)` Field `Access` `—` ke `Assigned` untuk Budi Santoso
14. Verifikasi Changelog memuat satu entri `Edit` Field `Delete` `Inactive` ke `Active` untuk Budi Santoso
15. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline, sehingga tidak ada entri `Edit` untuk Create dan Update karena nilai tersimpannya sudah sama
16. Tutup modal

### TC-FA-RP-1139: Assign Total Control ke user Read Only menyelaraskan seluruh Global Role dan seluruh baris pola Group Role ke CRUD penuh

17. Klik Tab `Total Control`
18. Klik `[+ Assign]` di Tab Total Control
19. Centang Maya Anggraeni lalu klik `[Assign]`
20. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
21. Ketik Search `Maya Anggraeni`, tekan Enter
22. Verifikasi Maya Anggraeni tampil di Tab Total Control
23. Klik `(←)` pada kotak Search
24. Klik Tab `Read Only`
25. Ketik Search `Maya Anggraeni`, tekan Enter
26. Verifikasi Maya Anggraeni tidak lagi ada di Tab Read Only (empty state hasil Search)
27. Klik `(←)` pada kotak Search
28. Buka Tab System lalu Detail Role `Import data`
29. Verifikasi baris Maya Anggraeni: Create dan Read aktif
30. Buka Detail Role `Manage Open API`
31. Verifikasi baris Maya Anggraeni: Read dan Update aktif
32. Buka Detail Role Group Role `Manage files`, klik node `Data Center`, lalu cari Maya Anggraeni
33. Verifikasi baris Maya Anggraeni pada `Manage files` di `Data Center` kini Read dan Delete aktif (CRUD penuh sesuai kolom yang berlaku)
34. Verifikasi daftar penugasan Group Role Maya Anggraeni (lewat fixture BE): jumlah baris sama dengan baseline (baris pola sudah ada, tidak bertambah dan tidak hilang) dan setiap baris kini CRUD penuh sesuai kolom yang berlaku

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 34 langkah.
- Langkah penghubung (S-03): langkah 1, 3–6, 9, 16–17, 23, 25, 27. Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 21.
- Pembagian asersi TC-FA-RP-1085: kalimat "tidak ada entri `Edit` untuk Create dan Update" diasersi sebagai selisih jumlah entri tepat 2 terhadap baseline (asersi jumlah, bukan absence kelas g; konvensi bagian 3 prinsip 13g), bukan sebagai pernyataan tidak ada entri.
- Langkah Search pada Tab (R-16) menemukan baris yang baru ditambahkan; langkah "cari Maya Anggraeni" pada Detail Role mengikuti TC (langkah 5 TC-FA-RP-1139).
- Temuan untuk QA:
  - TC-FA-RP-1085: baseline jumlah entri Changelog Detail Role `Manage accounting` tidak dinyatakan TC; spec mencatat baseline sebelum Assign (S-12) dan mengandalkan urutan default terbaru di atas untuk entri yang diasersi (tidak disebut TC).
  - TC-FA-RP-1139 precondition merujuk Pre-setup #12 dan #18 dan menyebut baris `Manage files` Maya Anggraeni di `Data Center`; kesetaraan CRUD penuh pada seluruh baris pola Group Role hanya teramati sebagian lewat UI (`Manage files` di `Data Center`); spec membandingkan seluruh Group Role Maya Anggraeni lewat fixture BE (kemampuan disediakan tim FE/BE).
