---
id: TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2
title: "Auto-Revert Group Manager dan pola subset baris eksplisit (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-399
  - TC-FA-RP-400
  - TC-FA-RP-401
  - TC-FA-RP-1042
coverage:
  web: automated
---

# Auto-Revert Group Manager dan pola subset baris eksplisit (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor kedua (langkah 18 dan 19, ganti akun eksplisit): Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Akun aktor ketiga (langkah 36 dan 37, ganti akun eksplisit): akun login Hesti Rahma (Pre-setup #17). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_HESTI_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #14 (Laila Nur, Group Manager di `Logistics Warehouse` dengan satu baris Group Role eksplisit `Manage purchase` Create, Read, Update, Delete aktif), #17 (Hesti Rahma), #18 (pohon group), #43 (seed Group Manager). Untuk TC-FA-RP-1042 Hesti Rahma disiapkan tanpa Home Group, ditugaskan Group Manager di `Data Center`, dan memiliki akun login (precondition TC, disiapkan lewat seeding API).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri Changelog Tab Group Manager sebagai baseline (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Home Group Hesti Rahma ditetapkan `Logistics Warehouse` dan penugasan Group Manager Hesti Rahma di `Data Center` dicabut oleh langkah 23. Hook `after` memulihkan Pre-setup #17 dan #43 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Buka Detail Role `Manage purchase` dari Tab `System`
2. Klik node `Logistics Warehouse` pada Sidebar Group Tree

### TC-FA-RP-399: Pola Group Manager pada subset baris eksplisit, edit yang membuat sel tidak penuh memicu D-05

3. Hapus centang Update pada baris Laila Nur
4. Verifikasi dialog D-05 varian edit tampil dengan Title `Remove Group Manager`, bullet `• Laila N`, dan `This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited.`
5. Klik `[Cancel]`

### TC-FA-RP-400: Pola Group Manager pada subset baris eksplisit, Remove satu baris memicu D-05 varian Remove baris

6. Klik `[⋯]` baris Laila Nur lalu `Remove`
7. Verifikasi dialog D-05 varian Remove baris tampil dengan `These users will lose Group Manager access:` lalu `• Laila N`
8. Klik `[Cancel]`

### TC-FA-RP-401: Pengguna Group Manager dengan subset baris eksplisit tetap Group Manager tanpa edit

9. Klik Tab `Group Manager`
10. Klik node `Logistics Warehouse` pada Sidebar Group Tree
11. Verifikasi baris Laila Nur di `Logistics Warehouse` tampil di Tab `Group Manager`
12. Klik Tab `System`
13. Buka Detail Role `Manage purchase`
14. Klik node `Logistics Warehouse` pada Sidebar Group Tree
15. Verifikasi baris eksplisit Laila Nur tampil di Detail Role
16. Verifikasi dialog tidak tampil
17. Verifikasi nilai Create, Read, Update, dan Delete baris Laila Nur tidak berubah (tetap aktif)

### TC-FA-RP-1042: Auto-Revert Group Manager akibat penetapan Home Group constraint, entri di semua surface dan notifikasi view-only

18. Logout dari akun Total Control
19. Login sebagai Manage global user & role dengan Update (Hendra Wijaya)
20. Buka Settings > User > Detail Hesti Rahma
21. Catat jumlah entri `Auto-Revert` Object `Group Manager` pada Changelog Tab Group Manager sebagai baseline lewat kemampuan baca
22. Atur Home Group Hesti Rahma ke group `Logistics Warehouse` lewat field Home Group dan `[Select]`
23. Klik `[Revoke]`
24. Buka menu Settings > Role & Permission dari sidebar
25. Klik Tab `Group Manager`
26. Klik ikon Changelog di toolbar Tab Group Manager
27. Verifikasi satu entri `Auto-Revert` Object `Group Manager`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`, dan Modified By `Hendra W` (aktor pengedit, bukan System) tampil
28. Verifikasi selisih jumlah entri `Auto-Revert` Object `Group Manager` terhadap baseline langkah 21 tepat satu
29. Tutup modal Changelog
30. Buka Settings > User > Detail Hesti Rahma > Changelog: User
31. Verifikasi entri `Auto-Revert` Object `Group Manager`, Field `Group Manager — Data Center`, Old Value `Assigned`, New Value `—`, Modified By `Hendra W` tampil
32. Buka Settings > User > Detail Hendra Wijaya > Tab System Log
33. Verifikasi System Log aktor memuat entri `Auto-Revert` Group Manager yang sama dengan pelaku aktor
34. Buka Activity Log FAMS aktor
35. Verifikasi Activity Log aktor memuat entri `Auto-Revert` Group Manager yang sama dengan pelaku aktor
36. Logout dari akun Hendra Wijaya
37. Login sebagai Hesti Rahma
38. Buka Overlay Notifikasi
39. Verifikasi satu notifikasi view-only (hanya `[Mark as Read]`) dengan Title `You are no longer Group Manager for Data Center` dan Body `Hendra Wijaya set your Home Group to Logistics Warehouse on [Date], so your Group Manager status for Data Center was removed.` dengan [Date] tanggal aksi dalam format General Settings

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5 dan 8 (menutup dialog D-05 dengan `[Cancel]` karena TC hanya mengasersi dialog), langkah 24 dan 25 (membuka Tab Group Manager untuk langkah TC 2), langkah 29 (menutup modal Changelog), langkah 21 (baseline log, S-12). Langkah 16 mengasersi tidak ada dialog setelah baris eksplisit tampil pada langkah 15 sebagai anchor.
- Klausa "Hanya satu entri" pada langkah 27 dan 28 diasersi sebagai selisih jumlah entri terhadap baseline, bukan asersi absence; pada System Log dan Activity Log (langkah 33 dan 35) entri dicari berdasarkan Object dan Field.
- Hesti Rahma pada TC-FA-RP-1042 adalah akun yang diasersi notifikasinya (objek asersi), bukan pemicu state; akun itu dipakai lewat ganti akun berurutan (langkah 36 dan 37), bukan konteks paralel. TC sumber menyebut `Manual Only (d) dua sesi paralel (aktor dan pengguna target)`.
- Alasan di atas sekitar 35 langkah (39 langkah): TC-FA-RP-1042 satu alur lintas surface (Changelog Group Manager, Changelog User, System Log, Activity Log, notifikasi) yang tidak dapat dipecah tanpa mengulang aksi Home Group; tiga TC lain satu topik pada Detail Role yang sama.
- Temuan untuk QA:
  - Email akun login Hesti Rahma tidak tertulis di Pre-setup #17; akun disediakan tim FE.
  - Pre-setup #17 menyatakan Hesti Rahma sudah ber-Home Group `Logistics Warehouse`, sedangkan TC-FA-RP-1042 (dan TC-FA-RP-410, TC-FA-RP-1041) menyatakan "tanpa Home Group" lalu menetapkannya ke `Logistics Warehouse`; spec menyiapkan Hesti tanpa Home Group lewat seeding.
  - TC-FA-RP-399 dan TC-FA-RP-400 tidak menyebut langkah sesudah dialog tampil; spec menutup dialog dengan `[Cancel]` (langkah 5 dan 8).
  - TC-FA-RP-1042 langkah 4 menyebut "Detail aktor > Tab System Log lalu Activity Log FAMS" tanpa menyebut lokasi Activity Log; spec memakai surface Activity Log aktor (langkah 34).
