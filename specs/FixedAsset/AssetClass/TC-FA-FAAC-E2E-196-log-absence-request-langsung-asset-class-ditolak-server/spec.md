---
id: TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server
title: "Log Absence: Request Langsung Deactivate, Delete, Edit Class Code, dan Create Melampaui Batas yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-601
  - TC-FA-FAAC-602
  - TC-FA-FAAC-603
  - TC-FA-FAAC-604
coverage:
  web: automated
---

# Log Absence: Request Langsung Deactivate, Delete, Edit Class Code, dan Create Melampaui Batas yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Deactivate, Delete, Edit, dan Create dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun Total Control (pelaku permintaan), dan Activity Log FAMS. Ketiganya audit trail permanen: asersi memakai selisih terhadap baseline, bukan angka absolut (S-12).
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Respons server dan state data diasersi di spec 180.
- State global yang diubah spec: Master Data Count Limit (Admin Console > Plans & Licensing > Lifecycle Settings) diatur sama dengan jumlah Asset Class saat ini pada TC-604 oleh fixture BE "disediakan tim FE/BE"; nilai awal dicatat di hook `before` dan dipulihkan di hook `after`. Jam server dan jam browser tidak digeser.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua permintaan ditolak): Asset Class `B-NAMES` (Active, dengan Asset Name ter-assign); `B-USED` dan `B-LOCK` dengan Last Posted Period `Mar 2026`. Identitasnya dirujuk lewat `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-601: Permintaan langsung Deactivate atas Asset Class dengan Asset Name ditolak server

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
2. Kirim permintaan Deactivate langsung ke server untuk `B-NAMES`
3. Verifikasi respons server menolak permintaan
4. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
5. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
6. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-602: Permintaan langsung Delete atas Asset Class yang pernah diposting ditolak server

7. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
8. Kirim permintaan Delete langsung ke server untuk `B-USED`
9. Verifikasi respons server menolak permintaan
10. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
11. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
12. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-603: Permintaan langsung mengubah Class Code yang terkunci ditolak server

13. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
14. Kirim permintaan Edit langsung ke server untuk `B-LOCK` dengan Class Code baru
15. Verifikasi respons server menolak permintaan
16. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
17. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
18. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-604: Permintaan langsung Create melampaui batas jumlah ditolak server

19. Atur lewat fixture BE Master Data Count Limit sama dengan jumlah Asset Class saat ini
20. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
21. Kirim permintaan Create langsung ke server saat jumlah Asset Class sama dengan batas
22. Verifikasi respons server menolak permintaan
23. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
24. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
25. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline
26. Pulihkan lewat fixture BE Master Data Count Limit ke nilai awal

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
2. Spec absence (kelas g): objek ujinya hanya klausa "tidak ada log" (Changelog Asset Class, System Log, dan Activity Log). Request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi state data Asset Class.
3. Pembagian TC lintas spec (S-05): TC-601, TC-602, TC-603, dan TC-604 ada di spec 180 (respons server dan state data). Spec ini mengasersi klausa "tidak ada log" dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri tiap TC.
4. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC (langkah 1, 7, 13, dan 20) lewat kemampuan baca BE; asersi memakai selisih terhadap baseline TC itu, bukan angka absolut.
5. Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak tiap permintaan mendahului pembacaan jumlah entri, sebagai bukti permintaan sudah diproses server; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 19 (mengatur Master Data Count Limit sebagai prasyarat TC-604) dan langkah 26 (memulihkannya).
7. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-NAMES`, `B-USED`, dan `B-LOCK`; dipakai apa adanya tanpa suffix `{runId}`. Semua permintaan ditolak sehingga data tidak berubah.
8. Temuan untuk QA:
   - TC-601 sampai TC-604 menyebut "tidak ada log" tanpa menyebut surface log; spec mengasersi Changelog Asset Class, System Log, dan Activity Log.
   - TC tidak menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan.
   - TC-601 sampai TC-604 tidak menyebut status respons; spec mengikuti TC.
