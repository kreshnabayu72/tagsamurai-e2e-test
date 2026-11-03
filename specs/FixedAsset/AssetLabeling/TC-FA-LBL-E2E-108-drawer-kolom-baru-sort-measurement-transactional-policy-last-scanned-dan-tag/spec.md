---
id: TC-FA-LBL-E2E-108-drawer-kolom-baru-sort-measurement-transactional-policy-last-scanned-dan-tag
title: "Drawer Kolom Baru: Sort Measurement, Transactional Policy, Last Scanned, dan TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-540
  - TC-FA-LBL-574
coverage:
  web: automated
---

# Drawer Kolom Baru: Sort Measurement, Transactional Policy, Last Scanned, dan TAG

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Probe` (Pre-setup #37, pengguna `Total Control Probe`), `Fixture.assetLabeling.akun.totalControlProbe`, `Spectra.env.FA_TC_PROBE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Probe` (#37), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.probe` (nama label, aset, tag aktif, Symbol UoM, policy, dan Last Scanned sesuai Tabel Pre-setup TC): label `Column Probe` pada `Probe Asset - 41` (`Probe Item A`; tag aktif `RFID` Tag Code `RFID-41` dan `QR` Tag Code `QR-41`; UoM `Kilogram` Symbol `kg`; policy Borrow dan Assign On; Last Scanned 10 Oct 2026 08:00 dari Audit), `Probe Asset - 42` (`Probe Item B`; tanpa tag aktif; UoM `Piece` Symbol `pcs`; seluruh policy Off; belum pernah dipindai), `Probe Asset - 43` (`Probe Item C`; tag aktif `NFC` Tag Code `NFC-43`; `kg`; hanya Transfer On; Last Scanned 12 Oct 2026 09:00), dan `Probe Asset - 44` (`Probe Item D`; tag aktif `RFID` Tag Code `RFID-44`; `pcs`; Borrow, Self Service Borrow, dan Assign On; Last Scanned 08 Oct 2026 10:00). Label `Tie Probe` pada `Probe Asset - 45` (`Probe Item E`; tag aktif `QR`; policy Self Service Borrow dan Transfer On), `Probe Asset - 46` (`Probe Item F`; tag aktif `NFC`; policy Borrow dan Assign On), dan `Probe Asset - 47` (`Probe Item G`; tag aktif `RFID`; policy Assign dan Transfer On).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlProbe` (email akun Total Control `Company Probe`) dan `Fixture.assetLabeling.probe` (data Pre-setup #37).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_PROBE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-540: Sort Drawer kolom baru: Measurement, Transactional Policy, Last Scanned, dan TAG

1. Klik chip `Column Probe` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Measurement`, `Transactional Policy`, dan `Last Scanned`, lalu klik `[Save]`
3. Klik header kolom `Measurement` satu kali
4. Verifikasi urutan klik 1 (Ascending): `kg` (`Probe Asset - 41`, `Probe Asset - 43`) lalu `pcs` (`Probe Asset - 42`, `Probe Asset - 44`); baris bernilai sama mengikuti default Name
5. Klik header kolom `Measurement` kedua kali
6. Verifikasi urutan klik 2 (Descending): `pcs` lalu `kg`; baris bernilai sama mengikuti default Name
7. Klik header kolom `Measurement` ketiga kali
8. Verifikasi urutan klik 3 kembali ke default Name A-Z (`Measurement`)
9. Klik header kolom `Transactional Policy` satu kali
10. Verifikasi urutan klik 1 (Ascending): `Probe Asset - 41` (Assign, Borrow), `Probe Asset - 44` (Assign, Borrow, Self Service Borrow), `Probe Asset - 43` (Transfer), lalu `Probe Asset - 42` (`—`) di akhir
11. Klik header kolom `Transactional Policy` kedua kali
12. Verifikasi urutan klik 2 (Descending): `Probe Asset - 42` (`—`) di awal, lalu `Probe Asset - 43`, `Probe Asset - 44`, `Probe Asset - 41`
13. Klik header kolom `Transactional Policy` ketiga kali
14. Verifikasi urutan klik 3 kembali ke default Name A-Z (`Transactional Policy`)
15. Klik header kolom `Last Scanned` satu kali
16. Verifikasi urutan klik 1 (Ascending): Oldest First: `Probe Asset - 44` (08 Oct), `Probe Asset - 41` (10 Oct), `Probe Asset - 43` (12 Oct), lalu `Probe Asset - 42` (`—`) di akhir
17. Klik header kolom `Last Scanned` kedua kali
18. Verifikasi urutan klik 2 (Descending): Newest First: `Probe Asset - 42` (`—`) di awal, lalu `Probe Asset - 43`, `Probe Asset - 41`, `Probe Asset - 44`
19. Klik header kolom `Last Scanned` ketiga kali
20. Verifikasi urutan klik 3 kembali ke default Name A-Z (`Last Scanned`)
21. Klik header kolom `TAG` satu kali
22. Verifikasi urutan klik 1 (Ascending): `Probe Asset - 43` (NFC), `Probe Asset - 41` (QR, RFID), `Probe Asset - 44` (RFID), lalu `Probe Asset - 42` (`—`) di akhir
23. Klik header kolom `TAG` kedua kali
24. Verifikasi urutan klik 2 (Descending): `Probe Asset - 42` (`—`) di awal, lalu `Probe Asset - 44`, `Probe Asset - 41`, `Probe Asset - 43`
25. Klik header kolom `TAG` ketiga kali
26. Verifikasi urutan klik 3 kembali ke default Name A-Z (`TAG`)
27. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Measurement`, `Transactional Policy`, dan `Last Scanned`, lalu klik `[Save]`
28. Tutup Drawer Tagged Asset

### TC-FA-LBL-574: Sort Drawer: TAG dan Transactional Policy Descending alfabetis atas label ikon pada aset dengan jumlah ikon sama

29. Klik chip `Tie Probe` di kolom Label
30. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Transactional Policy`, lalu klik `[Save]`
31. Klik header kolom `TAG` dua kali
32. Verifikasi urutan TAG Descending (satu tag tiap aset): `Probe Asset - 47` (RFID), `Probe Asset - 45` (QR), `Probe Asset - 46` (NFC)
33. Klik header kolom `Transactional Policy` dua kali
34. Verifikasi urutan Transactional Policy Descending (dua ikon tiap aset): `Probe Asset - 45` (Self Service Borrow, Transfer), `Probe Asset - 47` (Assign, Transfer), `Probe Asset - 46` (Assign, Borrow)
35. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Transactional Policy`, lalu klik `[Save]`
36. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah Pemulihan kolom ke Hidden dan tutup Drawer sesudah TC-FA-LBL-540 dan TC-FA-LBL-574 memulihkan keadaan awal (S-09).
- Pembagian TC lintas spec: Sort kolom baru ada di spec ini; Filter kolom baru TC-FA-LBL-541 ada di spec 171 dan Filter sumber 0 baris TC-FA-LBL-542 serta Sort TAG awalan pendek TC-FA-LBL-588 di spec 109. Urutan TC-FA-LBL-540 lalu 574 mengikuti nomor TC.
- Ukuran spec (36 langkah, di atas smell 35 langkah): kedua TC satu kelas (fungsional, Sort Drawer kolom baru) pada akun dan data Pre-setup #37 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena empat kolom masing-masing tiga klik dengan satu `Verifikasi` per klik (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-540 Langkah Uji 3 sampai 6 menulis "klik 3 kembali ke default Name A-Z" tanpa menyebut baris yang diharapkan; spec memverifikasi urutan Name A-Z keempat aset `Column Probe`.
  - NC-15: urut dan pencocokan sel TAG multi-ikon belum dinyatakan; TC hanya meng-assert urutan relatif aset bertag tunggal dan sel multi-ikon `Probe Asset - 41` (QR, RFID) pada TC-FA-LBL-540 butir d; spec mengikuti TC.
