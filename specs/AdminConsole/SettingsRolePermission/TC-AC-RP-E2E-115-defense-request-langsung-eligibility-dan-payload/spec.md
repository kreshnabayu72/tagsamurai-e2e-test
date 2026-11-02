---
id: TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload
title: "Defense-in-depth: Request Langsung atas Target Total Control, Kandidat Pending, Payload CRUD, Bulk Remove, dan Group Manager"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-384
  - TC-AC-RP-385
  - TC-AC-RP-386
  - TC-AC-RP-387
  - TC-AC-RP-388
  - TC-AC-RP-389
  - TC-AC-RP-390
coverage:
  web: automated
---

# Defense-in-depth: Request Langsung atas Target Total Control, Kandidat Pending, Payload CRUD, Bulk Remove, dan Group Manager

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP, tanpa browser)
- Akun aktor (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat langkah Ganti akun):

| Urutan | Aktor | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | `Siti Nurhaliza` (Total Control Principal, Pre-setup #1) | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` | TC-AC-RP-384, 385, 386, 387, 388, 389 |
| 2 | `Fajar Nugroho` (Group Manager, Pre-setup #6) | `groupManagerRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_GM_PASSWORD` | TC-AC-RP-390 |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal; `Region A`), #12 (user Standard: `Teguh Santoso` Inactive, `Maya Putri` Pending Activation, `Alex Tan`, `Jane Smith`), #13 (pemegang Total Control `John Doe`, `Bambang Hartono`), #15 (peran individual: `Manage hardware stock` `Alex Tan` C/R; `Manage device master data` `Jane Smith` R, `Bambang Hartono`; `Manage language` `Rudi Hartono` R), #17 (approver `Manage TAG stock`: `Sarah Kimura`), dan #25 (klien HTTP). Target aksi adalah data Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-115` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung (Pre-setup #25); sesi API aktor (dinyatakan di `suite.md`) untuk kedua akun; kemampuan membaca state data lewat fixture BE (penugasan Group Manager `John Doe`, tingkat akses `John Doe`, pemegang `Manage language`, daftar approver `Manage TAG stock`, nilai C/R/U/D `Alex Tan` pada `Manage hardware stock`, pemegang `Manage device master data`).
- Pemulihan baseline: TC-AC-RP-386, 388, dan 389 mengubah data Pre-setup (penugasan `Manage language` `Teguh Santoso`, nilai Delete `Alex Tan` pada `Manage hardware stock`, baris `Jane Smith` pada `Manage device master data`); dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama), dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" sesudah tiap TC yang mengubah data. Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_GM_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Catat lewat fixture BE sebagai baseline: penugasan Group Manager `John Doe`, tingkat akses `John Doe`, pemegang `Manage language`, daftar approver `Manage TAG stock`, nilai C/R/U/D `Alex Tan` pada `Manage hardware stock`, dan pemegang `Manage device master data`

### TC-AC-RP-384: Assign GM ke target Total Control langsung

2. Sesi API `Siti Nurhaliza`: kirim request Assign GM `John Doe` di `Region A`
3. Verifikasi respons request ditolak dengan status 422 (`V-09`)
4. Verifikasi lewat fixture BE bahwa penugasan Group Manager `John Doe` sama dengan baseline langkah 1 (`John Doe` tidak menjadi GM)

### TC-AC-RP-385: Assign Read Only ke target Total Control langsung

5. Sesi API `Siti Nurhaliza`: kirim request Assign Read Only `John Doe`
6. Verifikasi respons request ditolak dengan status 422 (`V-09`)
7. Verifikasi lewat fixture BE bahwa tingkat akses `John Doe` tetap Total Control

### TC-AC-RP-387: Assign Approver kandidat Pending Activation langsung

8. Sesi API `Siti Nurhaliza`: kirim request Assign Approver `Maya Putri` ke `Manage TAG stock`
9. Verifikasi respons request ditolak dengan status 422 (`V-09`)
10. Verifikasi lewat fixture BE bahwa daftar approver `Manage TAG stock` sama dengan baseline langkah 1 (approver tidak ditambahkan)

### TC-AC-RP-386: Assign User to Role target Inactive langsung diterima

11. Sesi API `Siti Nurhaliza`: kirim request Assign `Teguh Santoso` (Inactive) ke `Manage language`
12. Verifikasi respons request diterima dengan status sukses
13. Verifikasi lewat fixture BE bahwa `Teguh Santoso` memegang `Manage language`
14. Pulihkan baseline: `Teguh Santoso` kembali tidak memegang `Manage language` lewat kemampuan reset FE/BE

### TC-AC-RP-388: Edit CRUD mengirim nilai Read dan kolom tidak berlaku

15. Sesi API `Siti Nurhaliza`: kirim request Edit CRUD `Alex Tan` pada `Manage hardware stock` dengan Read=false, Update=true, Delete=true
16. Verifikasi respons request sukses tanpa error
17. Verifikasi lewat fixture BE bahwa Read `Alex Tan` pada `Manage hardware stock` tetap aktif
18. Verifikasi lewat fixture BE bahwa Update `Alex Tan` pada `Manage hardware stock` tetap tidak berlaku (`—`)
19. Verifikasi lewat fixture BE bahwa Delete `Alex Tan` pada `Manage hardware stock` tersimpan aktif
20. Pulihkan baseline: nilai C/R/U/D `Alex Tan` pada `Manage hardware stock` kembali ke baseline langkah 1 lewat kemampuan reset FE/BE

### TC-AC-RP-389: Bulk Remove langsung memuat baris Default User

21. Sesi API `Siti Nurhaliza`: kirim request bulk Remove `Manage device master data` untuk `Jane Smith` dan `Bambang Hartono`
22. Verifikasi baris `Jane Smith` terhapus dari `Manage device master data`
23. Verifikasi baris `Bambang Hartono` ditolak per baris
24. Verifikasi baris `Bambang Hartono` dihitung gagal (partial success)
25. Pulihkan baseline: `Jane Smith` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE

26. Ganti akun: login sesi API sebagai `Fajar Nugroho` (`Spectra.env.AC_RP_GM_PASSWORD`)

### TC-AC-RP-390: Group Manager membuka endpoint modul langsung

27. Sesi API `Fajar Nugroho`: kirim request list Tab Total Control
28. Verifikasi respons request ditolak dengan status 403
29. Verifikasi pesan respons "You don't have permission to do this."
30. Verifikasi respons tidak mengembalikan data

## Notes

- K-1: TC-AC-RP-384 sampai TC-AC-RP-390 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap berada di spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec, walau isinya tumpang tindih dengan `tc-settings-role-permission-backend.md`; BE mencatatnya pada tingkat endpoint.
- Asersi hanya status respons, pesan respons, dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (S-03, S-07, S-09): langkah 1 (baseline state), langkah 14, 20, 25 (pemulihan baseline), langkah 26 (Ganti akun sesi API). TC-AC-RP-386, 388, dan 389 (request yang mengubah data) diletakkan sesudah TC yang ditolak tanpa mengubah data, dan TC-AC-RP-387 diletakkan sebelum TC-AC-RP-386 agar baseline langkah 1 dan state Pre-setup tidak dipengaruhi; TC-AC-RP-390 (aktor Group Manager) di akhir agar ganti akun hanya sekali (S-10).
- TC-AC-RP-418 (prioritas pesan 403 dengan tiga sesi) ada di spec 136.
- Temuan untuk QA:
  - TC-AC-RP-384 dan 385: Expected hanya menyebut `422` (`V-09`) tanpa pesan; spec mengasersi status dan state data saja (S-02). Mohon QA menambah teks pesan bila ada.
  - TC-AC-RP-386: Expected "Request diterima" tidak menyebut status respons; spec mengasersi status sukses tanpa nilai angka (S-13).
  - TC-AC-RP-387: Expected "approver tidak ditambahkan" tidak menyebut keadaan awal daftar approver; spec membandingkan dengan baseline langkah 1.
  - TC-AC-RP-388: Expected tidak menyebut nilai Create `Alex Tan`; spec tidak mengasersi Create dan mengikuti Expected untuk Read, Update, dan Delete.
  - TC-AC-RP-389: Expected tidak menyebut status respons keseluruhan; spec mengasersi hasil per baris saja (S-02).
  - TC-AC-RP-390: Expected "tidak ada data dikembalikan" tidak menyebut bentuk respons (body kosong atau tanpa daftar); spec mengasersi respons tidak memuat data.
  - TC-AC-RP-384 sampai 390 tidak menyebut endpoint, method, atau body request; spec menulis aksi seperti di TC tanpa mengarang endpoint (S-13).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
