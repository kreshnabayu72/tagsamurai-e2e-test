---
id: TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog
title: "Baris pola Total Control dan Read Only tidak didaftar D-10, dan constraint tanpa Role Transaksi di luar constraint tidak menampilkan dialog"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1234
  - TC-FA-RP-1235
coverage:
  web: automated
---

# Baris pola Total Control dan Read Only tidak didaftar D-10, dan constraint tanpa Role Transaksi di luar constraint tidak menampilkan dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #12 (Maya Anggraeni, Read Only, baris pola Monitoring & Report pada setiap node), #15 (Ahmad Fauzi), #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group: `Helpdesk`, `Dock 1`, `Data Center`, `Rack A1`), dan #19 (baris Role Transaksi bersama; latar, tidak diasersi).
- Seeding precondition (hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan seeding disediakan tim FE/BE, tanpa endpoint karangan):
  - TC-FA-RP-1234: Ahmad Fauzi (Pre-setup #15, Standard) diberi tingkat akses Total Control tanpa Home Group, sehingga baris pola Asset Admin dan Approver terbentuk pada setiap node (sub-tab `Disposal`); Maya Anggraeni (Pre-setup #12) tanpa Home Group.
  - TC-FA-RP-1235: Gunawan Halim (Pre-setup #17) diatur tanpa Home Group, lalu ditugaskan Asset Admin pada `Data Center` dan Staff pada `Rack A1`, keduanya sub-tab `Disposal`.
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: Home Group Ahmad Fauzi, Maya Anggraeni, dan Gunawan Halim ditetapkan `Data Center` oleh langkah spec. Langkah 33 memulihkan lewat fixture BE (bukan lewat UI, supaya tidak menambah entri log): Home Group Ahmad Fauzi dan Maya Anggraeni dikosongkan, tingkat akses Total Control Ahmad Fauzi beserta baris polanya dilepas, Home Group Gunawan Halim dipulihkan ke `Data Center` (Pre-setup #17), dan penugasan seed Gunawan Halim dicabut. Hook `after` mengulang pemulihan itu sebagai cadangan (tidak berasumsi langkah spec berhasil penuh). Entri log bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1234: Baris pola Role Transaksi Total Control dan Read Only tidak didaftar di D-10 dan tidak dicabut saat constraint ditetapkan

1. Buka Settings > User lewat sidebar
2. Ketik Search `Ahmad Fauzi`, tekan Enter
3. Klik Name `Ahmad Fauzi`
4. Klik field Home Group, pilih `Data Center`, lalu klik `[Select]`
5. Verifikasi Home Group Ahmad Fauzi tersimpan `Data Center`
6. Verifikasi dialog D-10 tidak tampil
7. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, klik node `Helpdesk`, lalu klik sub-tab `Disposal`
8. Verifikasi Ahmad Fauzi tetap tampil di section Asset Admin `Helpdesk`
9. Verifikasi Ahmad Fauzi tetap tampil di section Approver `Helpdesk`
10. Klik node `Dock 1`
11. Verifikasi Ahmad Fauzi tetap tampil di section Asset Admin `Dock 1`
12. Verifikasi Ahmad Fauzi tetap tampil di section Approver `Dock 1`
13. Buka Settings > User lewat sidebar
14. Ketik Search `Maya Anggraeni`, tekan Enter
15. Klik Name `Maya Anggraeni`
16. Klik field Home Group, pilih `Data Center`, lalu klik `[Select]`
17. Verifikasi Home Group Maya Anggraeni tersimpan `Data Center`
18. Verifikasi dialog D-10 tidak tampil
19. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, klik node `Helpdesk`, lalu klik sub-tab `Disposal`
20. Verifikasi Maya Anggraeni tetap tampil di section Monitoring & Report `Helpdesk`
21. Klik node `Dock 1`
22. Verifikasi Maya Anggraeni tetap tampil di section Monitoring & Report `Dock 1`

### TC-FA-RP-1235: Penetapan constraint tanpa penugasan Role Transaksi di luar constraint tidak menampilkan dialog dan tidak mencabut apa pun

23. Buka Settings > User lewat sidebar
24. Ketik Search `Gunawan Halim`, tekan Enter
25. Klik Name `Gunawan Halim`
26. Klik field Home Group, pilih `Data Center`, klik `[Select]`
27. Verifikasi constraint Gunawan Halim tersimpan `Data Center`
28. Verifikasi dialog D-10 tidak tampil
29. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, klik node `Data Center`, lalu klik sub-tab `Disposal`
30. Verifikasi Gunawan Halim tetap tampil di section Asset Admin `Data Center`
31. Klik node `Rack A1`
32. Verifikasi Gunawan Halim tetap tampil di section Staff `Rack A1`
33. Pulihkan lewat fixture BE: kosongkan Home Group Ahmad Fauzi dan Maya Anggraeni, lepas tingkat akses Total Control Ahmad Fauzi beserta baris polanya, pulihkan Home Group Gunawan Halim ke `Data Center`, dan cabut penugasan seed Gunawan Halim (Asset Admin `Data Center`, Staff `Rack A1`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 sampai 3, 13 sampai 15, dan 23 sampai 25 (membuka Detail User; Search pada langkah 2, 14, dan 24 menemukan baris target, R-16 dan bagian 8b butir 13); langkah 7, 10, 19, 21, 29, 31 (navigasi ke Tab, node, dan sub-tab untuk mengamati hasil); langkah 33 (pemulihan, S-09).
- Asersi absence dialog D-10 (langkah 6, 18, 28): Home Group tersimpan diasersi lebih dulu (langkah 5, 17, 27) sebagai anchor positif bahwa Save selesai tanpa dialog (bagian 8b butir 2 dan 11).
- Pengulangan TC-FA-RP-1234 langkah 4 untuk Maya Anggraeni ditulis sebagai langkah 13 sampai 22 dengan section Monitoring & Report sebagaimana TC.
- Temuan untuk QA:
  - Precondition TC-FA-RP-1234 menyebut Ahmad Fauzi "berstatus Total Control", sedangkan Pre-setup #15 menyatakannya Standard tanpa tingkat akses; spec men-seed tingkat akses Total Control Ahmad Fauzi lewat kemampuan seeding yang disediakan tim FE/BE dan melepasnya di langkah 33. Pre-setup perlu menyebut seed status ini atau memakai pengguna Total Control lain.
  - Precondition TC-FA-RP-1234 mensyaratkan Ahmad Fauzi dan Maya Anggraeni tanpa Home Group; Pre-setup #12 dan #15 tidak menyebut Home Group, dan spec mengaturnya kosong di hook `before`.
  - TC-FA-RP-1234 Expected b dan c ("tetap tampil di section ... pada `Helpdesk` dan `Dock 1`") tidak menyebut sub-tab; spec memakai sub-tab `Disposal` sesuai langkah 2 TC.
  - Precondition TC-FA-RP-1235 menyebut Gunawan Halim "tanpa Home Group" sedangkan Pre-setup #17 menyatakan `Data Center`; spec mengaturnya lewat seeding dan memulihkannya di langkah 33. Pengaturan ini mengikuti gate Home Group yang masih menunggu PM (NC-20, PRD Open Item #9).
  - TC-FA-RP-1234 bergantung pada FARP-LOGIC-16g (pola Total Control dan Read Only dikecualikan dari D-10); bila PM mengubah arah gate (NC-20), asersi langkah 6 dan 18 perlu ditinjau.
  - Post Condition kedua TC kosong ("-").
