---
id: TC-FA-RP-E2E-346-assign-gm-menulis-baris-pola-group-role-tanpa-global-role
title: "Assign Group Manager menulis baris pola Group Role pada node penugasan dan descendant, tanpa baris Global Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1179
coverage:
  web: automated
---

# Assign Group Manager menulis baris pola Group Role pada node penugasan dan descendant, tanpa baris Global Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard; target Assign Group Manager), #18 (pohon Group: `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Dimas Pranata tanpa penugasan Group Role di `Data Center`, `Rack A1`, dan `Helpdesk`. Kondisi itu dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Tabel iterasi Group Role (urutan baris = urutan iterasi; kolom aktif pada baris Dimas Pranata mengikuti Expected b TC):

| No | Group Role | Kolom aktif |
|---|---|---|
| 1 | `Manage asset & TAG` | Create, Read, Update, Delete |
| 2 | `Manage files` | Read, Delete |
| 3 | `Manage group` | Create, Read, Update, Delete |
| 4 | `Manage purchase` | Create, Read, Update, Delete |
| 5 | `View asset value` | Read |

- State yang diubah dan pemulihannya: Assign Group Manager menulis penugasan Group Manager Dimas Pranata di `Data Center` dan baris pola Group Role di `Data Center` dan `Rack A1`. Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 (tanpa penugasan) lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1179: Assign Group Manager menulis baris pola Group Role pada node penugasan dan descendant, tanpa baris Global Role

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `Data Center` pada field Group
4. Centang Dimas Pranata
5. Klik `[Assign]`
6. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
7. Untuk setiap baris tabel iterasi Group Role (langkah 7 sampai 12): klik Tab `System`
8. Buka Detail Role Group Role pada baris tabel
9. Klik node `Data Center` di Sidebar Group Tree
10. Verifikasi baris Dimas Pranata tampil pada node `Data Center` dengan kolom aktif sesuai tabel iterasi (CRUD penuh sesuai kolom berlaku) dan Modified By `Siti R`
11. Klik node `Rack A1` di Sidebar Group Tree
12. Verifikasi baris Dimas Pranata tampil pada node `Rack A1` dengan kolom aktif sesuai tabel iterasi (CRUD penuh sesuai kolom berlaku) dan Modified By `Siti R`
13. Klik Tab `System`
14. Buka Detail Role Group Role `Manage user & role`
15. Klik node `Data Center` di Sidebar Group Tree
16. Verifikasi sedikitnya satu baris lain tampil pada node `Data Center`
17. Verifikasi tidak ada baris Dimas Pranata pada node `Data Center`
18. Klik node `Rack A1` di Sidebar Group Tree
19. Verifikasi sedikitnya satu baris lain tampil pada node `Rack A1`
20. Verifikasi tidak ada baris Dimas Pranata pada node `Rack A1`
21. Klik Tab `System`
22. Buka Detail Role Group Role `Manage files`
23. Klik node `Helpdesk` di Sidebar Group Tree
24. Verifikasi sedikitnya satu baris lain tampil pada node `Helpdesk`
25. Verifikasi tidak ada baris Dimas Pranata pada node `Helpdesk`
26. Klik Tab `System`
27. Buka Detail Role Global Role `Manage accounting`
28. Verifikasi sedikitnya satu baris lain tampil di Detail Role `Manage accounting`
29. Verifikasi tidak ada baris Global Role Dimas Pranata di Detail Role `Manage accounting`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 29 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (membuka Tab), 7, 13, 21, 26 (kembali ke daftar Detail Role lewat Tab `System`), 8, 14, 22, 27 (membuka Detail Role), 9, 11, 15, 18, 23 (memilih node). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah berulang (8b.7): langkah 7 sampai 12 diulang per baris tabel iterasi Group Role (lima iterasi, ekspansi 6 x 5 = 30 langkah; total ekspansi spec 53 langkah, nominal 29). Parameter tiap iterasi ada di `## Prerequisites` tanpa langkah bersyarat dan `Verifikasi` tetap satu per klausa. Alasan tetap satu spec: Expected b TC mensyaratkan kelima Group Role pada kedua node; TC tunggal, satu akun, satu dataset, dan satu pemicu Assign.
- Search tidak dipakai untuk menemukan baris Dimas Pranata pada Detail Role: tiap node memuat paling banyak enam baris, dalam satu halaman. Absence pada langkah 17, 20, 25, dan 29 didahului `Verifikasi` baris lain pada tabel yang sama (8b butir 2); anchor lain adalah toast sukses langkah 6 sebagai bukti respons server selesai.
- Pembagian TC lintas spec: TC-FA-RP-1180 (baris pola Role Transaksi pada Assign Group Manager yang sama) ada di spec 361; TC-FA-RP-1181 (log per baris pola) ada di spec 349.
- Post Condition TC-FA-RP-1179 ("baris pola ditulis dalam transaksi atomik yang sama dengan penugasan"; nilai kolom `Manage asset license` tidak di-assert) tidak punya langkah observasi; tidak diasersi. Kolom `Manage asset license` tidak diasersi sesuai Catatan TC.
- Temuan untuk QA:
  - TC-FA-RP-1179 tidak menyebut client; spec memakai client default (Company Alpha) dengan akun Siti Rahmawati, karena Expected b menyebut Modified By `Siti R`. Pre-setup #15 dan #18 milik client itu.
  - Pre-setup #38 mencantumkan Dimas Pranata sebagai Group Manager di `Rack A1` (Pending Activation) sebagai data tabel, sedangkan Precondition d TC-FA-RP-1179 menyatakan Dimas Pranata tanpa penugasan di `Rack A1`. Spec men-seed state Precondition d.
  - Expected b menulis "CRUD penuh sesuai kolom berlaku" lalu merinci kolom aktif per Group Role; spec memakai rincian itu sebagai tabel iterasi. TC tidak menyebut nilai kolom `Manage asset license`.
  - Expected c, d, dan e (tidak ada baris) tidak punya baris pembanding di TC; spec memakai `Verifikasi` sedikitnya satu baris lain pada tabel yang sama sebagai anchor positif (baris pembanding diasumsikan ada pada Detail Role `Manage user & role` node `Data Center` dan `Rack A1`, `Manage files` node `Helpdesk`, dan Global Role `Manage accounting`, mis. Total Control dan Citra Lestari pada Pre-setup #15).
  - Langkah 2 TC tidak menyebut cara membuka Detail Role (Tab `System`); spec memakai Tab `System` lalu baris Group Role.
  - Post Condition "Dimas Pranata dipulihkan ke state Pre-setup #15 oleh automation baseline" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
