---
id: TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403
title: "Log Absence: Request Langsung Create-Only, Update-Only, dan Delete-Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-598
  - TC-FA-FAAC-599
  - TC-FA-FAAC-600
  - TC-FA-FAAC-619
  - TC-FA-FAAC-620
sourceRules: ["E-FAAC-78", "§9.3#r3", "§9.3#r4", "§8#p1", "§8.4#r9", "§8.2#p1", "§8.3#p1", "§9.3#r2"]
smoke: []
dependsOn: []
trace:
  "E-FAAC-78": [3, 4, 5, 11, 12, 18, 19, 25, 31]
  "§9.3#r3": [3, 4, 19, 25, 31]
  "§9.3#r4": [5, 12]
  "§8#p1": [6, 13, 20, 26, 32]
  "§8.4#r9": [6, 7, 8, 13, 14, 15, 20, 21, 22, 26, 27, 28, 32, 33, 34]
  "§8.2#p1": [7, 14, 21, 27, 33]
  "§8.3#p1": [8, 15, 22, 28, 34]
  "§9.3#r2": [11, 18]
coverage:
  web: automated
---

# Log Absence: Request Langsung Create-Only, Update-Only, dan Delete-Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Create-Only. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Spec ini tidak punya langkah UI dan tidak ada langkah ganti akun UI: Update-Only dan Delete-Only memakai sesi API akunnya (sesi API aktor, lihat suite.md).
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_CO_PASSWORD` | TC-FA-FAAC-598, TC-FA-FAAC-619 |
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_UO_PASSWORD` | TC-FA-FAAC-599 |
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_DO_PASSWORD` | TC-FA-FAAC-600, TC-FA-FAAC-620 |

- Env var: `FA_AC_CO_PASSWORD`, `FA_AC_UO_PASSWORD`, `FA_AC_DO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create, Edit, Deactivate, Delete, Move, dan Unassign dengan sesi API akun role yang bersangkutan langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun pelaku permintaan, dan Activity Log FAMS. Ketiganya audit trail permanen: asersi memakai selisih terhadap baseline, bukan angka absolut (S-12).
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Penolakan UI dan state data diasersi di spec 034 dan spec 181.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua permintaan ditolak): Asset Class `B-ANCHOR` (Anchor Heavy Equipment, Active); Asset Name `Crane Rental Unit` ter-assign ke `Heavy Equipment` (`HEAVY-EQ`); Asset Class `Machinery` (`MACHINERY`) Active. Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (fixture BE menyetelnya sebelum TC-619 dan TC-620 dan memulihkan keadaan semula sesudahnya). Identitasnya dirujuk lewat `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- Jam server dan jam browser tidak digeser. State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-598: Create-Only tidak dapat Edit, Activate, Deactivate, atau Delete

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Create-Only, dan Activity Log FAMS
2. Kirim permintaan Edit, Deactivate, dan Delete Asset Class `B-ANCHOR` sebagai Create-Only langsung ke server tanpa melewati browser
3. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
4. Verifikasi respons server atas permintaan Deactivate ditolak dengan status 403
5. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
6. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
7. Verifikasi jumlah entri System Log akun Create-Only sama dengan baseline
8. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-599: Update-Only tidak dapat Create, Duplicate, atau Delete

9. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Update-Only, dan Activity Log FAMS
10. Kirim permintaan Create Asset Class dan permintaan Delete Asset Class `B-ANCHOR` sebagai Update-Only langsung ke server tanpa melewati browser
11. Verifikasi respons server atas permintaan Create ditolak dengan status 403
12. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
13. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
14. Verifikasi jumlah entri System Log akun Update-Only sama dengan baseline
15. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-600: Delete-Only tidak dapat Create atau Edit

16. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Delete-Only, dan Activity Log FAMS
17. Kirim permintaan Create Asset Class dan permintaan Edit Asset Class `B-ANCHOR` sebagai Delete-Only langsung ke server tanpa melewati browser
18. Verifikasi respons server atas permintaan Create ditolak dengan status 403
19. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
20. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
21. Verifikasi jumlah entri System Log akun Delete-Only sama dengan baseline
22. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-619: Permintaan langsung Move tanpa hak Update ditolak server dengan 403

23. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Create-Only, dan Activity Log FAMS
24. Kirim permintaan Move `Crane Rental Unit` ke `MACHINERY` sebagai Create-Only langsung ke server tanpa melewati browser
25. Verifikasi respons server atas permintaan Move `403 Forbidden`
26. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
27. Verifikasi jumlah entri System Log akun Create-Only sama dengan baseline
28. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-620: Permintaan langsung Unassign tanpa hak Update ditolak server dengan 403

29. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Delete-Only, dan Activity Log FAMS
30. Kirim permintaan Unassign `Crane Rental Unit` sebagai Delete-Only langsung ke server tanpa melewati browser
31. Verifikasi respons server atas permintaan Unassign `403 Forbidden`
32. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
33. Verifikasi jumlah entri System Log akun Delete-Only sama dengan baseline
34. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
2. Spec absence (kelas g) sekaligus Role Matrix negatif (bagian 3a): objek ujinya hanya klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log". Request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi UI Hidden atau Disabled dan tidak mengasersi state data. Tiap role ditulis per blok TC karena aksinya berbeda per role; Update-Only dan Delete-Only hanya memakai sesi API akunnya sehingga tidak ada langkah ganti akun UI.
3. Pembagian TC lintas spec (S-05): TC-598, TC-599, dan TC-600 ada di spec 034; TC-619 dan TC-620 ada di spec 181. Spec asal mengasersi UI, status respons 403, dan state data; spec ini mengasersi klausa "tidak ada entri log baru" dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri tiap TC.
4. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC (langkah 1, 9, 16, 23, dan 29) lewat kemampuan baca BE; asersi memakai selisih terhadap baseline TC itu, bukan angka absolut.
5. Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak tiap permintaan dengan 403 mendahului pembacaan jumlah entri, sebagai bukti permintaan sudah diproses server; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
6. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `B-ANCHOR`, `Crane Rental Unit`, dan `MACHINERY`; dipakai apa adanya tanpa suffix `{runId}`. Semua permintaan ditolak sehingga data tidak berubah.
7. Temuan untuk QA:
   - TC-619 dan TC-620 menyebut "tidak ada entri log baru" tanpa menyebut surface log; spec mengasersi Changelog Asset Class, System Log, dan Activity Log, mengikuti TC-598 sampai TC-600.
   - TC tidak menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan.
   - TC-619 dan TC-620 hanya menyebut `403 Forbidden` dan TC-598 sampai TC-600 hanya `403`; spec mengikuti TC. TC menulis "sebagai Create-Only" atau "sebagai Delete-Only" tanpa menyebut cara login; spec memakai sesi API. Endpoint dan bentuk permintaan langsung tidak disebut TC maupun PRD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
