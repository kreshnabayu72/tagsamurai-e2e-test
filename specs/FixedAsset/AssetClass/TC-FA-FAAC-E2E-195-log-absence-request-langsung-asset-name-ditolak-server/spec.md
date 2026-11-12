---
id: TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server
title: "Log Absence: Request Langsung Move, Unassign, dan Assign Asset Name yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-207
  - TC-FA-FAAC-605
  - TC-FA-FAAC-242
  - TC-FA-FAAC-621
coverage:
  web: automated
---

# Log Absence: Request Langsung Move, Unassign, dan Assign Asset Name yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Move, Unassign, dan Assign dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun Total Control (pelaku permintaan), dan Activity Log FAMS. Ketiganya audit trail permanen: asersi memakai selisih terhadap baseline, bukan angka absolut (S-12).
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Respons server dan state data diasersi di spec 180.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser. Effective From pada request Move TC-207 dan TC-605 adalah M+1.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua permintaan ditolak): Asset Name `Wheel Loader` (4 aset aktif) dan `Excavator PC200` (8 aset aktif) ter-assign ke `Heavy Equipment` (`HEAVY-EQ`); Asset Class `Machinery` (`MACHINERY`) Active; Asset Class `B-ASSETS` dengan satu Asset Name ber-aset aktif; Asset Class Inactive `B-INACT`; Asset Name tanpa Asset Class `Hand Truck`. Identitasnya dirujuk lewat `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-207: Permintaan langsung Move dengan Effective From setelah bulan berjalan ditolak

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
2. Kirim permintaan Move `Wheel Loader` ke `MACHINERY` dengan Effective From = bulan M+1 langsung ke server tanpa melewati browser
3. Verifikasi respons server menolak permintaan dengan pesan validasi `Effective from must not be later than [MMM YYYY]` dengan [MMM YYYY] = bulan berjalan (mis. `Oct 2026`)
4. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
5. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
6. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-605: Permintaan langsung dengan Effective From setelah bulan berjalan pada Move ditolak V-37

7. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
8. Kirim permintaan Move langsung ke server dengan Effective From = bulan M+1 untuk Asset Name ber-aset aktif yang ter-assign ke `B-ASSETS`
9. Verifikasi respons server menolak dengan caption `Effective from must not be later than [MMM YYYY]` ([MMM YYYY] = bulan berjalan)
10. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
11. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
12. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-242: Permintaan langsung Unassign Asset Name dengan aset aktif ditolak server

13. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
14. Kirim permintaan Unassign untuk `Excavator PC200` langsung ke server tanpa melewati browser
15. Verifikasi respons server menolak permintaan
16. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
17. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
18. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

### TC-FA-FAAC-621: Permintaan langsung Assign ke Asset Class Inactive ditolak server

19. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
20. Kirim permintaan Assign `Hand Truck` ke Asset Class Inactive `B-INACT` langsung ke server tanpa melewati browser
21. Verifikasi respons server menolak permintaan
22. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
23. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
24. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
2. Spec absence (kelas g): objek ujinya hanya klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log". Request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi state data Asset Name.
3. Pembagian TC lintas spec (S-05): TC-207, TC-605, TC-242, dan TC-621 ada di spec 180 (respons server dan state data). Spec ini mengasersi klausa "tidak ada log" dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri tiap TC.
4. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC (langkah 1, 7, 13, dan 19) lewat kemampuan baca BE; asersi memakai selisih terhadap baseline TC itu, bukan angka absolut.
5. Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak tiap permintaan mendahului pembacaan jumlah entri, sebagai bukti permintaan sudah diproses server; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
6. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `Wheel Loader`, `Excavator PC200`, `MACHINERY`, `B-ASSETS`, `B-INACT`, dan `Hand Truck`; dipakai apa adanya tanpa suffix `{runId}`. Semua permintaan ditolak sehingga data tidak berubah.
7. Temuan untuk QA:
   - TC-207, TC-242, TC-605, dan TC-621 menyebut "tidak ada log" atau "tidak ada entri log baru" tanpa menyebut surface log; spec mengasersi Changelog Asset Class, System Log, dan Activity Log.
   - TC tidak menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan.
   - TC-605 tidak menyebut kode Asset Name ber-aset aktif dan TC-242, TC-605, TC-621 tidak menyebut status respons; spec mengikuti TC. TC-621 menyebut "Asset Class Inactive (hasil TC anchor Deactivate)"; spec memakai seed `B-INACT`.
