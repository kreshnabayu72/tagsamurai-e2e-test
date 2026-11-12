---
id: TC-FA-FAAL-E2E-062-pencatatan-user-action-import-license-transaksi
title: "Pencatatan User Action: Import Group, License, Disposal, Damaged, dan Finish Audit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-242
  - TC-FA-FAAL-244
  - TC-FA-FAAL-245
  - TC-FA-FAAL-246
  - TC-FA-FAAL-247
  - TC-FA-FAAL-248
  - TC-FA-FAAL-249
coverage:
  web: automated
---

# Pencatatan User Action: Import Group, License, Disposal, Damaged, dan Finish Audit

## Prerequisites

- Mode: FE+BE.
- Akun aktor dan observer: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Pengecualian: tiap TC membuka modulnya (Import, License, Disposal, Damaged, Audit) untuk aksinya lalu Activity Log > User Action.
- Data uji, identitas dari `Fixture.activity-log.<kunci>` (fixture belum ada, disediakan tim FE):
  - File import Group berisi 3 baris valid (Pre-setup #27, TC-FA-FAAL-242).
  - Group `Gedung A` memiliki Allocated Quota 10 (Pre-setup #28, TC-FA-FAAL-244); hasil TC-FA-FAAL-244 (Allocated Quota 15) menjadi precondition TC-FA-FAAL-245.
  - Mike Tan memiliki sesi-produk Fixed Asset aktif (TC-FA-FAAL-246), dibuat langkah 14; password `Spectra.env.FA_MIKETAN_PASSWORD` (terdaftar di butir "Env var" `suite.md`, R-07).
  - Aset `Kendaraan Operasional (AST-2024-0088)` berstatus In Use (Pre-setup #24, TC-FA-FAAL-247).
  - Aset `Kamera DSLR (AST-2024-0141)` berstatus Borrowed (Pre-setup #24, TC-FA-FAAL-248).
  - Task `Task Audit Q3-Gedung A` berstatus In Audit (Pre-setup #25, TC-FA-FAAL-249).
- Kemampuan teknis disediakan tim FE/BE: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Mike Tan.
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada langkah 1; tiap Verifikasi baris baru juga memastikan total bertambah dari total terakhir yang dibaca.
- State yang diubah dan pemulihannya: tiga group hasil Import Group, Allocated Quota `Gedung A`, sesi-produk Mike Tan, status aset dan task dipulihkan oleh tim FE/BE di hook `after` lewat seed dan pemulihan API.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Penantian pencatatan: tiap Verifikasi baris baru memakai idiom polling (muat ulang Tab User Action tiap 5 detik, batas 2 menit) sebagai pengganti langkah tunggu tersendiri.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log > User Action dan catat total baris dari teks pagination (N0)

### TC-FA-FAAL-242: Commit Import Group tercatat sebagai satu ringkasan job

2. Jalankan Import Group dengan file import Group berisi 3 baris valid hingga commit selesai
3. Tunggu aksi selesai
4. Buka Activity Log > User Action
5. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): satu baris baru di Tab User Action, total baris bertambah: Action `Import Group`, Object `Import`, Name `Group`, Field `Import Summary`, Old Value `—`, New Value diawali `3 records imported`, Modified By `Admin A`

### TC-FA-FAAL-244: Edit kuota alokasi grup License tercatat dengan Object License

6. Ubah Allocated Quota Gedung A menjadi 15 di License > Allocation Quota
7. Tunggu aksi selesai
8. Buka Activity Log > User Action
9. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `License`, Name `Gedung A`, Field `Allocated Quota`, Old Value `10`, New Value `15`, Modified By `Admin A`

### TC-FA-FAAL-245: Remove alokasi grup License tercatat dengan New Value strip

10. Kosongkan Allocated Quota Gedung A di License > Allocation Quota dan simpan
11. Tunggu aksi selesai
12. Buka Activity Log > User Action
13. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Remove Allocation`, Object `License`, Name `Gedung A`, Field `Allocated Quota`, Old Value `15`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-246: Force Logout dari License tercatat dengan Name user target

14. Pelaku Mike Tan (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
15. Lakukan Force Logout sesi Mike Tan di License > Concurrent User
16. Tunggu aksi selesai
17. Buka Activity Log > User Action
18. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Force Logout`, Object `License`, Name `Mike Tan`, Modified By `Admin A`

### TC-FA-FAAL-247: Report Disposal tercatat sebagai perubahan status aset

19. Laporkan Disposal untuk aset `Kendaraan Operasional (AST-2024-0088)`
20. Tunggu aksi selesai
21. Buka Activity Log > User Action
22. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Report Disposal`, Object `Disposal`, Name `Kendaraan Operasional (AST-2024-0088)`, Field `Status`, Old Value `In Use`, New Value `Reported Disposal`, Modified By `Admin A`

### TC-FA-FAAL-248: Report Damaged tercatat sebagai perubahan status aset

23. Laporkan Damaged untuk aset `Kamera DSLR (AST-2024-0141)`
24. Tunggu aksi selesai
25. Buka Activity Log > User Action
26. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Report Damaged`, Object `Damaged`, Name `Kamera DSLR (AST-2024-0141)`, Field `Status`, Old Value `Borrowed`, New Value `Damaged`, Modified By `Admin A`

### TC-FA-FAAL-249: Finish Audit tercatat sebagai perubahan status task

27. Selesaikan task audit `Task Audit Q3-Gedung A` (Finish Audit)
28. Tunggu aksi selesai
29. Buka Activity Log > User Action
30. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Finish Audit`, Object `Audit`, Name `Task Audit Q3-Gedung A`, Field `Status`, Old Value `In Audit`, New Value `Waiting for Approval`, Modified By `Admin A`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 7, 11, 16, 20, 24, 28; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Langkah penghubung (S-03): langkah 1, 4, 8, 12, 17, 21, 25, 29 (membuka Tab User Action), langkah 14 (sesi-produk aktif Mike Tan sebagai precondition TC-FA-FAAL-246).
- Baseline S-12: langkah 1 mencatat N0. Tiap Verifikasi baris baru juga memeriksa total pagination lebih besar dari total pada Verifikasi sebelumnya; jumlah baris per aksi tidak dipakai sebagai angka absolut.
- Langkah 15 menjalankan Force Logout lewat UI License > Concurrent User sebagai objek log; sesi pelaku Mike Tan lewat sesi API aktor hanya membentuk sesi-produk aktif.
- R-14: Modified By diasersi `Admin A` (First Name dan Last Initial).
- Temuan untuk QA:
  - TC-FA-FAAL-246 Expected tidak menyebut Field, Old Value, dan New Value baris Force Logout; spec tidak menambah asersi itu.
  - TC-FA-FAAL-242 tidak menyebut data yang dibuat oleh Import Group (nama tiga group); pembersihan group hasil import disediakan tim FE/BE.
  - TC-FA-FAAL-244 dan 245 memakai Pre-setup #28 yang sama dengan nilai awal berbeda (10 dan 15); spec memakai hasil TC-FA-FAAL-244 sebagai precondition TC-FA-FAAL-245.
  - Email dan password Mike Tan tidak tertulis di Pre-setup TC; email disediakan tim FE dan env var password mengikuti `suite.md`.
  - Nama literal TC (`Kendaraan Operasional`, `Kamera DSLR`, `Task Audit Q3-Gedung A`) dipakai tanpa suffix per run; baris log immutable sehingga baris paling atas dijamin oleh baseline total.
