---
id: TC-FA-FAAC-E2E-156-tab-asset-names-sembunyikan-dan-tampilkan-tiap-kolom
title: "Tab Asset Names: Menyembunyikan dan Menampilkan Tiap Kolom Satu per Satu"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-464
coverage:
  web: automated
---

# Tab Asset Names: Menyembunyikan dan Menampilkan Tiap Kolom Satu per Satu

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) dengan tiga Asset Name ter-assign (Excavator PC200, Wheel Loader, Crane Rental Unit).
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-464; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `Reset to Default`.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-464)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`

### TC-FA-FAAC-464: Menyembunyikan dan menampilkan tiap kolom tab Asset Names satu per satu

5. Klik ikon `⋯` pada header kolom Actions
6. Hilangkan centang `Asset Name`
7. Verifikasi kolom `Asset Name` hilang dari tabel dan kelima kolom lain tetap tampil
8. Centang kembali `Asset Name`
9. Verifikasi kolom `Asset Name` tampil lagi pada posisi semula
10. Hilangkan centang `Category`
11. Verifikasi kolom `Category` hilang dari tabel dan kelima kolom lain tetap tampil
12. Centang kembali `Category`
13. Verifikasi kolom `Category` tampil lagi pada posisi semula
14. Hilangkan centang `Label`
15. Verifikasi kolom `Label` hilang dari tabel dan kelima kolom lain tetap tampil
16. Centang kembali `Label`
17. Verifikasi kolom `Label` tampil lagi pada posisi semula
18. Hilangkan centang `Assets`
19. Verifikasi kolom `Assets` hilang dari tabel dan kelima kolom lain tetap tampil
20. Centang kembali `Assets`
21. Verifikasi kolom `Assets` tampil lagi pada posisi semula
22. Hilangkan centang `Assigned At`
23. Verifikasi kolom `Assigned At` hilang dari tabel dan kelima kolom lain tetap tampil
24. Centang kembali `Assigned At`
25. Verifikasi kolom `Assigned At` tampil lagi pada posisi semula
26. Hilangkan centang `Assigned By`
27. Verifikasi kolom `Assigned By` hilang dari tabel dan kelima kolom lain tetap tampil
28. Centang kembali `Assigned By`
29. Verifikasi kolom `Assigned By` tampil lagi pada posisi semula

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Urutan kolom sesuai TC-464: `Asset Name`, `Category`, `Label`, `Assets`, `Assigned At`, `Assigned By`; tiap kolom ditulis eksplisit (empat langkah per kolom). Spec ini hanya memuat TC-464 karena enam iterasi sudah mendekati batas langkah.
3. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, termasuk Search untuk menemukan baris target (R-16).
4. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-464; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
