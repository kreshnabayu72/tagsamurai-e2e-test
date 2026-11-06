---
id: TC-FA-RP-E2E-362-assign-gm-bersarang-satu-set-baris-pola-tanpa-duplikasi
title: "Assign Group Manager bersarang untuk user yang sama: satu set baris pola bersama tanpa duplikasi dan tanpa entri log ganda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1185
coverage:
  web: automated
---

# Assign Group Manager bersarang untuk user yang sama: satu set baris pola bersama tanpa duplikasi dan tanpa entri log ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard; target Assign Group Manager), #18 (pohon Group: `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Dimas Pranata tanpa penugasan Group Manager maupun baris Group Role di subtree `IT Infrastructure`. Kondisi itu dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Tabel iterasi node (urutan baris = urutan iterasi): `IT Infrastructure`, `Data Center`, `Rack A1`, `Helpdesk`.
- Kemampuan teknis: membaca jumlah entri `Assign (via Group Manager)` Dimas Pranata pada Changelog Detail Role `Manage files` lewat kemampuan baca yang disediakan tim FE/BE (langkah 13), sesuai langkah TC yang mencatat baseline. Asersi jumlah entri adalah selisih terhadap baseline, bukan total absolut (S-12).
- State yang diubah dan pemulihannya: dua Assign Group Manager (`IT Infrastructure` lalu `Data Center`) menulis dua penugasan Group Manager Dimas Pranata dan satu set baris pola pada subtree `IT Infrastructure`. Changelog bertambah entri (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 (tanpa penugasan) lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1185: Assign Group Manager bersarang untuk user yang sama (node induk lalu node anak)

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `IT Infrastructure` pada field Group
4. Ketik Search `Dimas Pranata`, tekan Enter pada popup Assign
5. Centang Dimas Pranata
6. Klik `[Assign]`
7. Tunggu aksi selesai: popup Assign tertutup
8. Klik Tab `System`
9. Buka Detail Role Group Role `Manage files`
10. Untuk setiap baris tabel iterasi node (langkah 10 dan 11): klik node pada baris tabel di Sidebar Group Tree
11. Verifikasi Dimas Pranata memiliki tepat satu baris pada `Manage files` di node itu
12. Klik ikon Changelog di toolbar Detail Role
13. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri `Assign (via Group Manager)` Dimas Pranata pada Changelog Detail Role `Manage files`
14. Tutup modal Changelog
15. Klik Tab `Group Manager`
16. Klik `[+ Assign]` di Tab Group Manager
17. Pilih group `Data Center` pada field Group
18. Ketik Search `Dimas Pranata`, tekan Enter pada popup Assign
19. Centang Dimas Pranata
20. Klik `[Assign]`
21. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
22. Klik Tab `System`
23. Buka Detail Role Group Role `Manage files`
24. Untuk setiap baris tabel iterasi node (langkah 24 dan 25): klik node pada baris tabel di Sidebar Group Tree
25. Verifikasi Dimas Pranata tetap memiliki tepat satu baris (tidak ganda) pada `Manage files` di node itu
26. Klik ikon Changelog di toolbar Detail Role
27. Verifikasi jumlah entri `Assign (via Group Manager)` Dimas Pranata sama dengan baseline langkah 13 (node `Data Center` dan `Rack A1` yang sudah tercakup tidak menulis entri baru)
28. Tutup modal Changelog
29. Klik Tab `Group Manager`
30. Ketik Search `Dimas Pranata`, tekan Enter
31. Verifikasi Tab Group Manager memuat dua baris Dimas Pranata (`IT Infrastructure` dan `Data Center`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 8, 15, 22, 29 (membuka Tab), 9, 23 (membuka Detail Role), 10, 24 (memilih node), 12, 14, 26, 28 (membuka dan menutup modal Changelog), 7 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), 13 (baseline, S-12), 4 dan 18 (Search kandidat di popup Assign supaya Dimas Pranata pasti tampil pada Table User Picker berpaginasi; R-22), 30 (Search baris target pada Tab Group Manager; R-16, 8b butir 13). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah berulang (8b.7): langkah 10 dan 11 serta langkah 24 dan 25 diulang per baris tabel iterasi node (empat iterasi); ekspansi spec 43 langkah, nominal 31. Parameter tiap iterasi ada di `## Prerequisites` tanpa langkah bersyarat. Spec tetap satu karena TC tunggal dan kedua blok Assign saling bergantung (Assign kedua bermakna hanya setelah Assign pertama).
- Search tidak dipakai pada Detail Role: tiap node memuat paling banyak enam baris, dalam satu halaman. Tidak ada asersi absence di spec ini; "tidak ganda" diasersi sebagai jumlah baris tepat satu dan selisih jumlah entri nol terhadap baseline (bukan kelas g).
- Pembagian TC lintas spec: TC-FA-RP-1180 (baris pola Role Transaksi) ada di spec 361 dan TC-FA-RP-1182 (menggantikan peran tangga) ada di spec 347.
- Post Condition TC-FA-RP-1185 ("Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline") tidak punya langkah observasi; tidak diasersi, dipulihkan di hook `after`.
- Temuan untuk QA:
  - Precondition d TC-FA-RP-1185 menyatakan Dimas Pranata tanpa penugasan Group Manager di subtree `IT Infrastructure`, sedangkan Pre-setup #38 mencantumkan Dimas Pranata sebagai Group Manager di `Rack A1` (Pending Activation). Spec men-seed Precondition d.
  - Langkah 2 TC mencatat baseline "jumlah entri `Assign (via Group Manager)` Dimas Pranata" tanpa menyebut filter node atau Object; spec membaca jumlah untuk seluruh entri Dimas Pranata pada Changelog Detail Role `Manage files`. Nama Action `Assign (via Group Manager)` menunggu konfirmasi PM (PRD 12 Open Item #7).
  - Expected c menyebut "tanpa entri log ganda" hanya untuk Changelog Detail Role `Manage files`; spec tidak memeriksa Changelog Transaction Role.
  - Expected a ("tepat satu baris") berlaku pada Group Role `Manage files`; TC tidak menyebut role lain, sehingga role lain tidak diasersi.
  - Langkah 3 TC ("Klik `[+ Assign]`, pilih group `Data Center`") tidak menyebut apakah Table User Picker menampilkan Dimas Pranata untuk node yang sudah tercakup penugasan `IT Infrastructure`; spec mengikuti TC dan mencarinya lewat Search.
