---
id: TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server
title: "Defense-in-Depth: Request Langsung ke Server yang Melanggar Guard Bisnis dan Validasi Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-207
  - TC-FA-FAAC-242
  - TC-FA-FAAC-601
  - TC-FA-FAAC-602
  - TC-FA-FAAC-603
  - TC-FA-FAAC-604
  - TC-FA-FAAC-605
  - TC-FA-FAAC-621
  - TC-FA-FAAC-648
  - TC-FA-FAAC-649
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung ke Server yang Melanggar Guard Bisnis dan Validasi Ditolak

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Move, Unassign, Deactivate, Delete, Edit, Create, dan Assign dengan sesi aktor ini langsung ke server tanpa melewati browser; pembacaan jumlah Asset Class serta state Asset Class dan Asset Name (status Active, keanggotaan, Class Code) lewat kemampuan baca BE.
- State global yang diubah spec: Master Data Count Limit (Admin Console > Plans & Licensing > Lifecycle Settings) diatur sama dengan jumlah Asset Class saat ini pada TC-604 oleh fixture BE "disediakan tim FE/BE"; nilai awal dicatat di hook `before` dan dipulihkan di hook `after`.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser. Effective From pada request Move TC-207 dan TC-605 adalah M+1.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibuat ulang bila berubah): Asset Name `Wheel Loader` (4 aset aktif) dan `Excavator PC200` (8 aset aktif) ter-assign ke `Heavy Equipment` (`HEAVY-EQ`); Asset Class `Machinery` (`MACHINERY`) Active; Asset Class `B-NAMES` (Active, dengan Asset Name ter-assign); `B-USED` dan `B-LOCK` dengan Last Posted Period `Mar 2026`; Asset Class `B-ASSETS` dengan satu Asset Name ber-aset aktif; Asset Class Inactive `B-INACT`; Asset Name tanpa Asset Class `Hand Truck`. Tidak ada Asset Class dengan Class Code `B-V18` dan `B-V21`.
- Data Uji request Create TC-648: Class Code `B-V18`; Class Name `V18 Test`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention kosong; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`. TC-649: Class Code `B-V21`; Class Name `V21 Test`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Start Rule kosong; field lain sama dengan TC-648.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-207: Permintaan langsung Move dengan Effective From setelah bulan berjalan ditolak

1. Kirim permintaan Move `Wheel Loader` ke `MACHINERY` dengan Effective From = bulan M+1 langsung ke server tanpa melewati browser
2. Verifikasi respons server menolak permintaan dengan pesan validasi `Effective from must not be later than [MMM YYYY]` dengan [MMM YYYY] = bulan berjalan (mis. `Oct 2026`)
3. Verifikasi `Wheel Loader` tetap di `Heavy Equipment`

### TC-FA-FAAC-605: Permintaan langsung dengan Effective From setelah bulan berjalan pada Move ditolak V-37

4. Kirim permintaan Move langsung ke server dengan Effective From = bulan M+1 untuk Asset Name ber-aset aktif yang ter-assign ke `B-ASSETS`
5. Verifikasi respons server menolak dengan caption `Effective from must not be later than [MMM YYYY]` ([MMM YYYY] = bulan berjalan)
6. Verifikasi Asset Name tetap ter-assign ke `B-ASSETS` (tidak ada data berubah)

### TC-FA-FAAC-242: Permintaan langsung Unassign Asset Name dengan aset aktif ditolak server

7. Kirim permintaan Unassign untuk `Excavator PC200` langsung ke server tanpa melewati browser
8. Verifikasi respons server menolak permintaan
9. Verifikasi `Excavator PC200` tetap ter-assign ke `Heavy Equipment`

### TC-FA-FAAC-621: Permintaan langsung Assign ke Asset Class Inactive ditolak server

10. Kirim permintaan Assign `Hand Truck` ke Asset Class Inactive `B-INACT` langsung ke server tanpa melewati browser
11. Verifikasi respons server menolak permintaan
12. Verifikasi `Hand Truck` tetap tanpa Asset Class

### TC-FA-FAAC-601: Permintaan langsung Deactivate atas Asset Class dengan Asset Name ditolak server

13. Kirim permintaan Deactivate langsung ke server untuk `B-NAMES`
14. Verifikasi respons server menolak permintaan
15. Muat ulang tabel Asset Class
16. Verifikasi `B-NAMES` tetap Active

### TC-FA-FAAC-602: Permintaan langsung Delete atas Asset Class yang pernah diposting ditolak server

17. Kirim permintaan Delete langsung ke server untuk `B-USED`
18. Verifikasi respons server menolak permintaan
19. Muat ulang tabel Asset Class
20. Verifikasi `B-USED` tetap ada

### TC-FA-FAAC-603: Permintaan langsung mengubah Class Code yang terkunci ditolak server

21. Catat baseline lewat kemampuan baca BE: Class Code `B-LOCK`
22. Kirim permintaan Edit langsung ke server untuk `B-LOCK` dengan Class Code baru
23. Verifikasi respons server menolak permintaan
24. Muat ulang Detail `B-LOCK`
25. Verifikasi Class Code `B-LOCK` tidak berubah

### TC-FA-FAAC-604: Permintaan langsung Create melampaui batas jumlah ditolak server

26. Atur lewat fixture BE Master Data Count Limit sama dengan jumlah Asset Class saat ini, lalu catat baseline: jumlah Asset Class
27. Kirim permintaan Create langsung ke server saat jumlah Asset Class sama dengan batas
28. Verifikasi respons server menolak permintaan
29. Verifikasi jumlah Asset Class sama dengan baseline (tanpa mutasi)
30. Pulihkan lewat fixture BE Master Data Count Limit ke nilai awal

### TC-FA-FAAC-648: Permintaan langsung Create dengan Depreciation Start Convention kosong ditolak

31. Kirim permintaan Create Asset Class langsung ke server dengan Data Uji TC-648 (Depreciation Start Convention kosong, field wajib lain valid) tanpa melewati browser
32. Verifikasi respons server menolak permintaan dengan caption validasi `Depreciation start convention must not be empty`
33. Verifikasi Asset Class `B-V18` tidak dibuat

### TC-FA-FAAC-649: Permintaan langsung Create dengan Tax Depreciation Start Rule kosong ditolak

34. Kirim permintaan Create Asset Class langsung ke server dengan Data Uji TC-649 (Tax Depreciation Start Rule kosong, field wajib lain valid) tanpa melewati browser
35. Verifikasi respons server menolak permintaan dengan caption validasi `Tax depreciation start rule must not be empty`
36. Verifikasi Asset Class `B-V21` tidak dibuat

## Notes

1. K-1: TC-207, TC-242, TC-601 sampai TC-605, TC-621, TC-648, dan TC-649 adalah TC defense-in-depth kelas a dengan Expected berupa respons API (status respons dan state data lewat fixture BE). Tetap masuk spec FE+BE walau tumpang tindih dengan tc-[modul]-backend.md, karena TC granular tetap sumber dan tiap TC tepat satu spec; BE mencatatnya pada tingkat endpoint.
2. Sesuai bagian 8b butir 1, langkah request langsung hanya mengasersi respons server dan state data lewat kemampuan baca BE; pengalihan halaman, toast, atau tampilan tidak diasersi di spec ini (perilaku FE untuk validasi yang sama diasersi di spec jalur form suite ini). Status respons tidak ditulis angka karena TC hanya menyebut "ditolak".
3. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor TC: request Move, Unassign, dan Assign (data Asset Name) lebih dulu, lalu request atas Asset Class, lalu Create (batas jumlah, validasi). TC-604 mengubah state global (Master Data Count Limit) sehingga diletakkan sesudah TC lain yang tidak boleh terpengaruh batas itu; pemulihan eksplisit di langkah 30.
4. Pembagian TC lintas spec (S-05): TC-207, TC-605, TC-242, dan TC-621 ada di spec ini (respons server dan state data) dan di spec 195; TC-601, TC-602, TC-603, dan TC-604 ada di spec ini dan di spec 196. Klausa "tidak ada log" (selisih jumlah entri Changelog Asset Class, System Log, dan Activity Log terhadap baseline, dengan permintaan yang sama sebagai pemicu) diasersi di spec 195 dan 196; spec ini tidak mengasersi log.
5. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 15, 19, dan 24 (memuat ulang tabel atau Detail sebelum membaca state, sesuai langkah TC); langkah 30 (memulihkan Master Data Count Limit).
6. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-NAMES`, `B-USED`, `B-LOCK`, `B-ASSETS`, `B-INACT`, `Wheel Loader`, `Excavator PC200`, `Hand Truck`, serta `B-V18` dan `B-V21`; nilai dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nilai itu. Semua request ditolak sehingga data tidak berubah; hook `after` memastikan `B-V18` dan `B-V21` tidak ada.
7. Alasan di atas sekitar 35 langkah: seluruh blok berkelas defense-in-depth tanpa harness eksternal (kelas a); konvensi bagian 3 prinsip 13 menetapkan kelas ringan cukup satu spec per kelas per modul, bukan per aksi. Tiap blok berdiri sendiri dan tidak mengubah data, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
8. Temuan untuk QA: TC-605 tidak menyebut kode Asset Name ber-aset aktif dan TC-601 sampai TC-605 tidak menyebut status respons; spec mengikuti TC. TC-621 menyebut "Asset Class Inactive (hasil TC anchor Deactivate)"; spec memakai seed `B-INACT`. TC-648 dan TC-649 tidak menyebut klausa "tidak ada log"; spec tidak mengasersinya.
