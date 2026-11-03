---
id: TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit
title: "Defense-in-Depth: Root All Groups, Parent, Duplikat, Depth Limit, Guard Delete, dan Selection Limit lewat Request Langsung"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-363
  - TC-AC-SG-364
  - TC-AC-SG-365
  - TC-AC-SG-366
  - TC-AC-SG-367
  - TC-AC-SG-368
  - TC-AC-SG-401
  - TC-AC-SG-402
coverage:
  web: automated
---

# Defense-in-Depth: Root All Groups, Parent, Duplikat, Depth Limit, Guard Delete, dan Selection Limit lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #16 dan #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Seluruh langkah spec ini berupa request langsung ke server lewat klien HTTP dan tidak melewati browser.
- Akun yang diganti (ganti akun memakai sesi API aktor yang tidak dihitung sebagai sesi web, suite.md):

  | Aktor | Email | Env password | Dipakai di |
  |---|---|---|---|
  | Total Control Distributor Hapus Utama (Pre-setup #21) | `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_HAPUS_PASSWORD` | langkah 19 sampai 22 |
  | Total Control Distributor Satu Group (Pre-setup #22) | `totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_SATU_PASSWORD` | langkah 23 sampai 26 |
  | Total Control Distributor Seleksi Besar (Pre-setup #35) | `totalControlSeleksi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_SELEKSI_PASSWORD` | langkah 27 sampai 30 |

- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus hook `after`; setiap nama bersuffix `{runId}-096`):
  - Entitas Principal: `Region A {runId}-096` dengan anak `Branch 1 {runId}-096` dan `Branch 2 {runId}-096`; `Region B {runId}-096` dengan anak `Branch 3 {runId}-096`; dan satu node pada depth sama dengan Hierarchy Depth Limit (50, Pre-setup #34) bernama `Kedalaman 50 {runId}-096` yang dibangun Fixture BE (rantai kedalaman). Pohon Uji Utama (Pre-setup #16) tidak diubah.
  - Entitas Distributor Hapus Utama: `Hapus Member A {runId}-096` dengan satu Client Active `Client Mawar {runId}-096`.
  - Entitas Distributor Satu Group dan Seleksi Besar: tidak ada data tambahan; `Default Group` (Pre-setup #22) dan `Seleksi 001` sampai `Seleksi 105` (Pre-setup #35) hanya menjadi sasaran request yang ditolak dan tidak diubah.
- Kemampuan teknis: klien HTTP untuk request langsung ke endpoint Group (Pre-setup #36) dan Fixture BE untuk membaca state data (keberadaan, nama, parent group, dan ID root `All Groups`) tanpa melalui UI; keduanya disediakan tim FE/BE tanpa endpoint karangan di spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-363: Rename atau delete root All Groups lewat request langsung ditolak

1. Kirim request update langsung untuk node root `All Groups`
2. Kirim request delete langsung untuk node root `All Groups`
3. Verifikasi kedua request ditolak `403 Forbidden`
4. Verifikasi root `All Groups` tidak di-rename dan tidak terhapus (lewat Fixture BE)

### TC-AC-SG-364: Nama All Groups lewat request langsung ditolak validasi server

5. Kirim request create group dengan nama `all groups` langsung
6. Kirim request update `Region B {runId}-096` dengan nama `ALL GROUPS` langsung
7. Verifikasi kedua request ditolak `422 Unprocessable Entity` dengan body `{ "message": "Invalid request body", "error": [{ "field": "name", "message": "'All Groups' is a reserved name and cannot be used" }] }`
8. Verifikasi tidak ada group baru dan tidak ada nama group yang berubah (lewat Fixture BE)

### TC-AC-SG-365: Perubahan parent lewat request update langsung dijawab 422

9. Kirim request update `Branch 3 {runId}-096` dengan menyertakan parent baru `Region A {runId}-096` langsung
10. Verifikasi respons `422` dengan body `{ "message": "Invalid request body", "error": [{ "field": "parentId", "message": "Parent cannot be changed" }] }`
11. Verifikasi parent `Branch 3 {runId}-096` tetap `Region B {runId}-096` dan group tidak berpindah (lewat Fixture BE)

### TC-AC-SG-401: Nama duplikat per parent lewat request langsung ditolak 409

12. Kirim request create subgroup bernama `branch 1 {runId}-096` di bawah `Region A {runId}-096` langsung
13. Kirim request update `Branch 2 {runId}-096` dengan nama `BRANCH 1 {runId}-096` langsung
14. Verifikasi kedua request ditolak `409 Conflict` dengan body `{ "message": "Group name already exists in this level" }`
15. Verifikasi tidak ada group baru dan nama `Branch 2 {runId}-096` tidak berubah (lewat Fixture BE)

### TC-AC-SG-402: Hierarchy Depth Limit terlampaui lewat request create langsung ditolak 409

16. Kirim request create subgroup langsung di bawah `Kedalaman 50 {runId}-096` (depth sama dengan Hierarchy Depth Limit)
17. Verifikasi respons `409 Conflict` dengan body `{ "message": "You've reached the platform limit of 50 levels. Contact support if you need a higher limit." }`
18. Verifikasi tidak ada group baru (lewat Fixture BE)

### TC-AC-SG-366: Delete group dengan entitas menempel lewat request langsung ditolak

19. Ganti akun: gunakan sesi API Total Control Distributor Hapus Utama
20. Kirim request delete `Hapus Member A {runId}-096` langsung
21. Verifikasi respons `409 Conflict` dengan `data.code` `HAS_MEMBERS`
22. Verifikasi `Hapus Member A {runId}-096` tetap ada (lewat Fixture BE)

### TC-AC-SG-367: Delete yang menyisakan 0 group lewat request langsung ditolak

23. Ganti akun: gunakan sesi API Total Control Distributor Satu Group
24. Kirim request delete `Default Group` langsung
25. Verifikasi respons `409 Conflict` dengan `data.code` `LAST_GROUP`
26. Verifikasi `Default Group` tetap ada (lewat Fixture BE)

### TC-AC-SG-368: Bypass Selection Limit lewat request bulk delete 101 ID ditolak

27. Ganti akun: gunakan sesi API Total Control Distributor Seleksi Besar
28. Kirim request bulk delete langsung berisi 101 ID group dengan Selection Limit 100
29. Verifikasi respons `422 Unprocessable Entity` (jumlah ID melebihi Selection Limit)
30. Verifikasi tidak ada group yang terhapus (lewat Fixture BE)

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-group-backend.md`; BE mencatatnya pada tingkat endpoint. Asersi hanya status respons, body, dan state data lewat Fixture BE (bagian 8b butir 1).
- Ganti akun pada langkah 19, 23, dan 27 adalah ganti sesi API eksplisit (S-07). Sesi UI tetap akun Total Control Principal; hook `after` mengembalikan sesi ke akun default spec.
- Urutan TC mengikuti entitas (Principal lebih dulu, lalu tiga entitas lain) agar ganti akun seminimal mungkin (S-10); nomor TC tidak berurutan karena TC-AC-SG-401 dan TC-AC-SG-402 disisipkan di bagian 8 TC.
- TC-AC-SG-363 sampai 365, 401, dan 402 menarget node Pre-setup `All Groups`, `Region B`, `Branch 3`, `Region A`, dan `Branch 2`; request langsung yang diuji ditolak memakai data milik spec (S-06) kecuali root `All Groups` (milik entitas, bukan data yang dapat dimiliki spec) yang hanya menjadi sasaran request yang ditolak dan tidak diubah.
- Temuan untuk QA:
  - TC-AC-SG-368 Expected menyebut "Dialog Blok `[OK]` pada UI berisi 'You have selected 101 rows, which exceeds the maximum of 100 rows per bulk action...'" pada request langsung; klausa ini tidak disalin karena request langsung tidak melewati browser (bagian 8b butir 1). Dialog Blok pada UI diuji di spec Selection Limit.
  - TC-AC-SG-402 memakai teks "50 levels" dengan Fixture Hierarchy Depth Limit (Pre-setup #34) tanpa menyatakan cara fixture membangun node pada depth 50 di Principal; pembentukan rantai kedalaman disediakan tim FE/BE.
  - TC-AC-SG-363 tidak menyebut cara memperoleh ID root `All Groups`; ID dibaca lewat Fixture BE.
  - TC-AC-SG-367 dan TC-AC-SG-368 menarget `Default Group` Pre-setup #22 dan `Seleksi 001`-`105` Pre-setup #35 yang hanya dibaca dan ditolak; entitasnya tidak dapat dibentuk ulang oleh spec.
