---
id: TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2
title: "Sort Modal Changelog (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-305
  - TC-FA-LBL-306
  - TC-FA-LBL-307
  - TC-FA-LBL-308
  - TC-FA-LBL-309
coverage:
  web: automated
---

# Sort Modal Changelog (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14). Sort memakai tujuh baris seed dengan lebih dari dua nilai distinct pada tiap kolom yang diurutkan (S-11).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend.

## Test Steps

### Membuka Modal Changelog

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal
3. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`

### TC-FA-LBL-305: Sort Changelog kolom Date

4. Klik header kolom `Date` satu kali
5. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): Oldest First: dari `Delete Old Tag` (08 Sep) sampai `Edit High Priority` (15 Sep 14:25)
6. Klik header kolom `Date` untuk kedua kali
7. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): Newest First: dari `Edit High Priority` (15 Sep 14:25) sampai `Delete Old Tag`
8. Klik header kolom `Date` untuk ketiga kali
9. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-306: Sort Changelog kolom Label Name

10. Klik header kolom `Label Name` satu kali
11. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `Audit Ready`, `Executive Asset`, `Finance Department` (Edit 14 Sep 11:30 lalu Create 14 Sep 11:15), `High Priority` (Edit lalu Create), `Old Tag`
12. Klik header kolom `Label Name` untuk kedua kali
13. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): `Old Tag`, `High Priority` (Edit lalu Create), `Finance Department` (Edit lalu Create), `Executive Asset`, `Audit Ready`
14. Klik header kolom `Label Name` untuk ketiga kali
15. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-307: Sort Changelog kolom Action

16. Klik header kolom `Action` satu kali
17. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `Create` (empat baris, tie Date Newest), `Delete` (satu baris), `Edit` (dua baris)
18. Klik header kolom `Action` untuk kedua kali
19. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): `Edit` (dua baris), `Delete`, `Create`
20. Klik header kolom `Action` untuk ketiga kali
21. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-308: Sort Changelog kolom Field

22. Klik header kolom `Field` satu kali
23. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `Color` (satu baris `Edit High Priority`) lalu enam baris `Label Name`
24. Klik header kolom `Field` untuk kedua kali
25. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): enam baris `Label Name` lalu `Color`
26. Klik header kolom `Field` untuk ketiga kali
27. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-309: Sort Changelog kolom Old Value

28. Klik header kolom `Old Value` satu kali
29. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `#DC2626`, `Finance Dept`, `Old Tag`, lalu empat baris `—` di akhir
30. Klik header kolom `Old Value` untuk kedua kali
31. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): empat baris `—` di awal, lalu `Old Tag`, `Finance Dept`, `#DC2626`
32. Klik header kolom `Old Value` untuk ketiga kali
33. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### Menutup Modal Changelog

34. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Filter Date rentang seed di-Apply sekali di awal (langkah 2 dan 3, sama dengan langkah Filter tiap TC) dan tetap berlaku untuk kelima TC. Klik ketiga pada tiap kolom mengembalikan tabel ke default Date Newest First sehingga TC berikutnya dimulai dari state bersih (S-09).
- Pasangan TC sort bagian 2 (TC-FA-LBL-310, TC-FA-LBL-311, TC-FA-LBL-325) ada di spec 082; TC-FA-LBL-519 ada di spec 168.
- Spec ini tidak menulis log ke Company Changelog; urutan sort dinilai atas tepat tujuh baris seed hasil Filter Date, sedangkan entri TC lain bertanggal hari run berada di luar rentang (S-12, S-14).
- Temuan untuk QA:
  - TC-FA-LBL-309 menyebut empat baris `—` di akhir; urutan antar baris `—` mengikuti tie Date Newest dan tidak diasersi secara eksplisit oleh TC.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
