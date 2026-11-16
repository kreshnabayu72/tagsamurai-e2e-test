---
id: TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403
title: "Log Absence: Request Langsung Read Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-595
  - TC-FA-FAAC-596
  - TC-FA-FAAC-597
  - TC-FA-FAAC-618
  - TC-FA-FAAC-686
sourceRules: ["E-FAAC-78", "§9.3#r2", "§8#p1", "§8.4#r9", "§8.2#p1", "§8.3#p1", "§9.3#r3", "§9.3#r4", "E-FAAC-114", "F-FAAC-17.k1"]
smoke: []
dependsOn: []
trace:
  "E-FAAC-78": [3, 9, 10, 16, 22]
  "§9.3#r2": 3
  "§8#p1": [4, 11, 17, 23, 29]
  "§8.4#r9": [4, 5, 6, 11, 12, 13, 17, 18, 19, 23, 24, 25, 29, 30, 31]
  "§8.2#p1": [5, 12, 18, 24, 30]
  "§8.3#p1": [6, 13, 19, 25, 31]
  "§9.3#r3": [9, 10, 22]
  "§9.3#r4": 16
  "E-FAAC-114": 28
  "F-FAAC-17.k1": 28
coverage:
  web: automated
---

# Log Absence: Request Langsung Read Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Read Only `readOnly_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_AC_RO_PASSWORD`, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create, Edit, Deactivate, Delete, Assign, dan Cancel Scheduled Version dengan sesi API akun Read Only (sesi API aktor, lihat suite.md) langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun Read Only (pelaku permintaan), dan Activity Log FAMS. Ketiganya audit trail permanen: asersi memakai selisih terhadap baseline, bukan angka absolut (S-12).
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Penolakan UI dan state data diasersi di spec 035 dan spec 181.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua permintaan ditolak): Asset Class `B-ANCHOR` (Anchor Heavy Equipment, Active); `Heavy Equipment` (`HEAVY-EQ`) Active; Asset Name tanpa Asset Class `Hand Truck`; Asset Class `B-SCHED` dengan versi Scheduled sejak M+2 (bulan berjalan M mengikuti zona waktu General Settings client, NC-11). Identitasnya dirujuk lewat `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- Jam server dan jam browser tidak digeser. State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-595: Read Only tidak dapat Create Asset Class

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Read Only, dan Activity Log FAMS
2. Kirim permintaan Create Asset Class langsung ke server tanpa melewati browser
3. Verifikasi respons server atas permintaan Create ditolak dengan status 403
4. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
5. Verifikasi jumlah entri System Log akun Read Only sama dengan baseline
6. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-596: Read Only tidak dapat Save Edit, Activate, atau Deactivate

7. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Read Only, dan Activity Log FAMS
8. Kirim permintaan Edit dan permintaan Deactivate Asset Class `B-ANCHOR` langsung ke server tanpa melewati browser
9. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
10. Verifikasi respons server atas permintaan Deactivate ditolak dengan status 403
11. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
12. Verifikasi jumlah entri System Log akun Read Only sama dengan baseline
13. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-597: Read Only tidak dapat Delete

14. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Read Only, dan Activity Log FAMS
15. Kirim permintaan Delete Asset Class `B-ANCHOR` langsung ke server tanpa melewati browser
16. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
17. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
18. Verifikasi jumlah entri System Log akun Read Only sama dengan baseline
19. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-618: Permintaan langsung Assign tanpa hak Update ditolak server dengan 403

20. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Read Only, dan Activity Log FAMS
21. Kirim permintaan Assign `Hand Truck` ke `HEAVY-EQ` langsung ke server tanpa melewati browser
22. Verifikasi respons server atas permintaan Assign `403 Forbidden`
23. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
24. Verifikasi jumlah entri System Log akun Read Only sama dengan baseline
25. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-686: Read Only tidak dapat Cancel Scheduled Version lewat permintaan langsung

26. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Read Only, dan Activity Log FAMS
27. Kirim permintaan Cancel Scheduled Version atas `B-SCHED` langsung ke server tanpa melewati browser
28. Verifikasi respons server atas permintaan Cancel Scheduled Version `403`
29. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
30. Verifikasi jumlah entri System Log akun Read Only sama dengan baseline
31. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
2. Spec absence (kelas g): objek ujinya hanya klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log". Request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi UI Hidden atau Disabled dan tidak mengasersi state data.
3. Pembagian TC lintas spec (S-05): TC-595, TC-596, dan TC-597 ada di spec 035; TC-618 dan TC-686 ada di spec 181. Spec asal mengasersi UI, status respons 403, dan state data; spec ini mengasersi klausa "tidak ada entri log baru" dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri tiap TC.
4. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC (langkah 1, 7, 14, 20, dan 26) lewat kemampuan baca BE; asersi memakai selisih terhadap baseline TC itu, bukan angka absolut.
5. Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak tiap permintaan dengan 403 mendahului pembacaan jumlah entri, sebagai bukti permintaan sudah diproses server; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
6. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `B-ANCHOR`, `HEAVY-EQ`, `Hand Truck`, dan `B-SCHED`; dipakai apa adanya tanpa suffix `{runId}`. Semua permintaan ditolak sehingga data tidak berubah.
7. Temuan untuk QA:
   - TC-618 dan TC-686 menyebut "tidak ada entri log baru" atau "tidak ada log" tanpa menyebut surface log; spec mengasersi Changelog Asset Class, System Log, dan Activity Log, mengikuti TC-595 sampai TC-597.
   - TC tidak menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan (Read Only).
   - TC-618 hanya menyebut `403 Forbidden` dan TC-686 menyebut `403`; spec mengikuti TC. Endpoint dan bentuk permintaan langsung tidak disebut TC maupun PRD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
