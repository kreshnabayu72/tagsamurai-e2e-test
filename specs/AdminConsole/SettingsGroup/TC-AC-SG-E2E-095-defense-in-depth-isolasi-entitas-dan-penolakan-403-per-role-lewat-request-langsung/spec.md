---
id: TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung
title: "Defense-in-Depth: Isolasi Entitas dan Penolakan 403 per Role lewat Request Langsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-355
  - TC-AC-SG-356
  - TC-AC-SG-357
  - TC-AC-SG-358
  - TC-AC-SG-359
  - TC-AC-SG-360
  - TC-AC-SG-361
  - TC-AC-SG-362
coverage:
  web: automated
---

# Defense-in-Depth: Isolasi Entitas dan Penolakan 403 per Role lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Pembanding, `totalControlPembanding_automated_{namaCompany}@qwertysystem.net` (Pre-setup #33), password `Spectra.env.AC_SG_PEMBANDING_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Seluruh langkah spec ini berupa request langsung ke server lewat klien HTTP dan tidak melewati browser.
- Akun yang diganti (ganti akun memakai sesi API aktor yang tidak dihitung sebagai sesi web, suite.md), semuanya entitas Principal:

  | Aktor | Email | Env password | Dipakai di |
  |---|---|---|---|
  | Read Only (Pre-setup #2) | `readOnlyGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_RO_PASSWORD` | langkah 8 sampai 17 |
  | Manage group tanpa capability mutasi (Pre-setup #10) | `manageGroupNone_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGNONE_PASSWORD` | langkah 18 sampai 23 |
  | Manage group Update saja (Pre-setup #5) | `manageGroupU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGU_PASSWORD` | langkah 24 sampai 25 |
  | Manage group Create saja (Pre-setup #4) | `manageGroupC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGC_PASSWORD` | langkah 26 sampai 27 |
  | Group Manager (Pre-setup #11) | `groupManagerGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_GM_PASSWORD` | langkah 30 sampai 31 |
  | Manage language (Pre-setup #12) | `manageLanguageGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_ML_PASSWORD` | langkah 32 sampai 33 |

- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Principal, dihapus hook `after`; Pohon Uji Utama Pre-setup #16 tidak diubah): `Region A {runId}-095`, `Region B {runId}-095`, dan `Region C {runId}-095` (level 1, tanpa entitas). ID ketiganya dibaca lewat Fixture BE.
- Kemampuan teknis: klien HTTP untuk request langsung ke endpoint Group (Pre-setup #36) dan Fixture BE untuk membaca state data (keberadaan group dan nama) tanpa melalui UI; keduanya disediakan tim FE/BE tanpa endpoint karangan di spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-355 dan TC-AC-SG-356: Request ke node milik entitas lain dari sesi Distributor Pembanding dijawab 404

1. Kirim request list langsung yang di-scope ke ID node `Region A {runId}-095` milik Principal dari sesi `Distributor Pembanding`
2. Verifikasi respons `404 Not Found`
3. Verifikasi respons tidak memuat data group milik Principal
4. Kirim request PATCH langsung ke ID group `Region A {runId}-095` milik Principal dari sesi `Distributor Pembanding`
5. Kirim request DELETE langsung ke ID group `Region A {runId}-095` milik Principal dari sesi `Distributor Pembanding`
6. Verifikasi kedua request dijawab `404 Not Found`
7. Verifikasi group Principal `Region A {runId}-095` tidak berubah (keberadaan dan nama, lewat Fixture BE)

### TC-AC-SG-357, TC-AC-SG-358, dan TC-AC-SG-359: Read Only mengirim Create, Edit, dan Delete langsung

8. Ganti akun: gunakan sesi API Read Only
9. Kirim request create group langsung sebagai Read Only
10. Verifikasi respons `403 Forbidden`
11. Verifikasi tidak ada group baru (lewat Fixture BE)
12. Kirim request update nama group `Region B {runId}-095` langsung sebagai Read Only
13. Verifikasi respons `403 Forbidden`
14. Verifikasi nama `Region B {runId}-095` tidak berubah
15. Kirim request delete group `Region C {runId}-095` langsung sebagai Read Only
16. Verifikasi respons `403 Forbidden`
17. Verifikasi `Region C {runId}-095` tetap ada

### TC-AC-SG-360: Manage group tanpa capability mutasi mengirim write langsung

18. Ganti akun: gunakan sesi API Manage group tanpa Create/Update/Delete
19. Kirim request create group langsung
20. Kirim request update group `Region B {runId}-095` langsung
21. Kirim request delete group `Region C {runId}-095` langsung
22. Verifikasi ketiga request ditolak `403 Forbidden`
23. Verifikasi data tidak berubah (tidak ada group baru, nama `Region B {runId}-095` tetap, `Region C {runId}-095` tetap ada)

### TC-AC-SG-361: Update-Only mengirim Delete dan Create-Only mengirim Update langsung

24. Ganti akun: gunakan sesi API Manage group Update saja
25. Kirim request delete group `Region C {runId}-095` langsung
26. Ganti akun: gunakan sesi API Manage group Create saja
27. Kirim request update nama `Region B {runId}-095` langsung
28. Verifikasi kedua request ditolak `403 Forbidden`
29. Verifikasi data tidak berubah (`Region C {runId}-095` tetap ada, nama `Region B {runId}-095` tetap)

### TC-AC-SG-362: Group Manager dan Role lain mengirim request baca langsung

30. Ganti akun: gunakan sesi API Group Manager
31. Kirim request daftar Group langsung
32. Ganti akun: gunakan sesi API Manage language
33. Kirim request daftar Group langsung
34. Verifikasi kedua request dijawab `403 Forbidden` (tanpa akses)
35. Verifikasi tidak ada data Group di kedua respons

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-group-backend.md`; BE mencatatnya pada tingkat endpoint. Asersi hanya status respons dan state data lewat Fixture BE (bagian 8b butir 1).
- Ganti akun pada langkah 8, 18, 24, 26, 30, dan 32 adalah ganti sesi API eksplisit (S-07). Sesi UI tetap akun Pembanding; hook `after` mengembalikan sesi ke akun default spec.
- Langkah 24 sampai 29 dan 30 sampai 35 menempatkan `Verifikasi` Expected sesudah kedua request terkirim karena Expected TC-AC-SG-361 dan TC-AC-SG-362 menyebut kedua request bersama.
- TC-AC-SG-355 sampai 362 menarget node Pre-setup `Region A`, `Region B`, dan `Region C`; request langsung yang diuji ditolak memakai data milik spec (S-06), jadi ketiga node di atas di-seed dengan suffix `{runId}-095`.
- Alasan di atas sekitar 35 langkah: spec berada pada batas 35 langkah dan seluruh blok satu kelas harness (defense-in-depth lewat request langsung) yang berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Tidak ada langkah UI sehingga tidak ada biaya navigasi.
- Temuan untuk QA:
  - TC-AC-SG-357 Expected menyebut "UI tidak menampilkan toast sukses" pada request langsung; klausa ini tidak disalin karena request langsung tidak melewati browser (bagian 8b butir 1).
  - TC-AC-SG-355 Expected menyebut "tidak ada data `Pohon Uji Utama` Principal pada respons"; spec mengasersi tidak ada data group milik Principal pada respons karena node yang diuji milik spec.
  - Pre-setup #5, #4, #10, #11, dan #12 menyebut capability role tetapi tidak menyebut password; nama env `AC_SG_*_PASSWORD` ditetapkan spec dan perlu didaftarkan pemilik repo (suite.md).
