---
id: TC-AC-ACTS-E2E-098-approvals-duplicate-approve-register-duplicate-activation-collision-dan-unit-tidak-tampil
title: "Approvals Duplicate: Approve Register Duplicate dan Activation Collision, Unit Rejected Tidak Masuk Stok, dan Total Registered Tidak Berubah saat Pending"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-277
  - TC-AC-ACTS-278
  - TC-AC-ACTS-298
  - TC-AC-ACTS-879
coverage:
  web: automated
---

# Approvals Duplicate: Approve Register Duplicate dan Activation Collision, Unit Rejected Tidak Masuk Stok, dan Total Registered Tidak Berubah saat Pending

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject disiapkan seeding fixture BE (disediakan tim FE/BE): SKU `RFID-ASSET-CORE-R5` dengan Total Registered 10 sebelum Submit; Subject Register Duplicate pending dari requester Distributor (satu untuk TC-AC-ACTS-879 yang tetap pending, satu untuk TC-AC-ACTS-277 yang di-Approve); Subject Activation Collision dengan SKU yang di-Approve (TC-AC-ACTS-278); Subject Register Duplicate yang sudah Rejected (TC-AC-ACTS-298). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca saldo Stock Ledger (Device Allocation > Stock Balance Summary Panel), jam server dan jam browser sinkron untuk TC-AC-ACTS-278 (Activated At = waktu keputusan Approve, toleransi satu menit).
- Unit hasil Approve (TAG Code baru) dan perubahan saldo dipulihkan lewat fixture BE di hook `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-879: Register Duplicate, Total Registered tidak berubah dan unit tidak tampil di Tab Available; Subject tampil di Tab Active

1. Buka TAG > Stock dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
2. Verifikasi Total Registered tetap `10`
3. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available dan hitung baris
4. Verifikasi Tab Available memuat sedikitnya satu baris (anchor unit Available seeding)
5. Verifikasi Tab Available tidak memuat baris baru untuk unit itu
6. Buka Approvals > TAG Stock > Tab Active
7. Verifikasi Tab Active memuat Subject Register Duplicate itu

### TC-AC-ACTS-298: Unit Rejected tidak tampil di Tab Available dan tidak menambah Total Registered

8. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
9. Verifikasi Tab Available memuat sedikitnya satu baris
10. Verifikasi unit Rejected tidak muncul di Tab Available
11. Buka TAG > Stock dan baca Total Registered SKU itu
12. Verifikasi Total Registered tidak bertambah (tetap `10`)

### TC-AC-ACTS-277: Approve Register Duplicate menerbitkan TAG Code baru dan menambah stok

13. Buka Approvals > TAG Stock > Tab Active
14. Klik `Review` pada Subject Register Duplicate pending
15. Pilih Approve
16. Klik `[Submit]` tanpa Approval Note
17. Verifikasi toast "Success, duplicate TAG has been approved and registered as [TAG Code]."
18. Verifikasi dialog tertutup
19. Verifikasi Subject hilang dari Tab Active
20. Buka Approvals > Tab History
21. Verifikasi Subject masuk Tab History dengan Approval `Approved`
22. Buka TAG > Stock dan baca Total Registered SKU itu
23. Verifikasi unit berstatus Available dengan TAG Code baru dan Total Registered `11`
24. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas requester
25. Verifikasi saldo Stock Ledger entitas requester bertambah 1

### TC-AC-ACTS-278: Approve Activation Collision membuat unit langsung In Use tanpa Stock Ledger

26. Catat baseline kolom In Use SKU dan saldo Stock Ledger
27. Buka Approvals > TAG Stock > Tab Active
28. Klik `Review` pada Subject Activation Collision dengan SKU
29. Pilih Approve
30. Klik `[Submit]`
31. Catat waktu keputusan Approve
32. Verifikasi toast "Success, request has been approved."
33. Buka Detail SKU > Tab In Use dan baca Activated At
34. Verifikasi unit berstatus In Use dengan TAG Code baru
35. Verifikasi Activated At sama dengan waktu keputusan Approve ini (toleransi satu menit), bukan waktu percobaan aktivasi Client
36. Buka TAG > Stock dan baca kolom In Use SKU itu
37. Verifikasi In Use SKU bertambah 1 terhadap baseline
38. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo
39. Verifikasi saldo Stock Ledger tidak berubah

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu dataset Subject pending dan satu SKU, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sebagian besar langkah adalah pembacaan layar lain (Stock List, Tab History, Device Allocation) yang dituntut Expected TC.
- Approve di akhir spec: TC-AC-ACTS-879 dan TC-AC-ACTS-298 membaca keadaan sebelum keputusan, lalu TC-AC-ACTS-277 dan TC-AC-ACTS-278 memutuskan Subject (aksi yang mengubah data di akhir; S-10).
- Langkah penghubung tanpa Verifikasi (S-03): membaca Total Registered dan saldo sebagai baseline, mencatat waktu keputusan Approve (S-12), dan membuka layar baca.
- Nilai absolut Expected TC (`10` dan `11`) diperlakukan sebagai Total Registered seeding (10) dan selisih +1; Total Registered seeding `10` ditetapkan seeding (S-12, 8b butir 10).
- Temuan untuk QA:
  - TC-AC-ACTS-277 menyebut "Isi Approval Note opsional" dan Data "Approve tanpa catatan"; spec menjalankan Approve tanpa catatan.
  - TC-AC-ACTS-298 menyebut Total Registered "tidak bertambah" tanpa nilai awal; spec memakai nilai seeding `10`.
