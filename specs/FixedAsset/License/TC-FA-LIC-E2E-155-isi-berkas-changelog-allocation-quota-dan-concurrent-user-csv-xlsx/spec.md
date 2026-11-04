---
id: TC-FA-LIC-E2E-155-isi-berkas-changelog-allocation-quota-dan-concurrent-user-csv-xlsx
title: "Isi Berkas Download Modal Changelog: Allocation Quota (CSV dan XLSX) dan Concurrent User (CSV, Hasil Search)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-618
  - TC-FA-LIC-619
coverage:
  web: automated
---

# Isi Berkas Download Modal Changelog: Allocation Quota (CSV dan XLSX) dan Concurrent User (CSV, Hasil Search)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, Rudi Hartono, client PT Sejahtera plan Paid), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pembacaan berkas unduhan): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri, TC-FA-LIC-618; `Fixture.fixedAssetLicense.changelogAllocationQuota`) dan riwayat Changelog Concurrent User #31 (4 entri, TC-FA-LIC-619; `Fixture.fixedAssetLicense.changelogConcurrentUser`) pada client yang sama; fixture belum ada, disediakan tim FE. Tidak ada Search atau Filter aktif saat berkas TC-FA-LIC-618 diunduh. General Settings Pre-setup #1: tanggal `dd/MM/yy`, jam `HH:mm`, zona `Asia/Jakarta`.
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, encoding dan BOM, nama sheet, baris, sel, tipe sel); berkas tiap unduhan ditangkap ke direktori bersih; fixture BE pemulih riwayat Pre-setup #27 dan #31.
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: jumlah dan urutan baris data berkas Changelog diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.
- Spec ini hanya membaca data dan tidak mengubah state global atau konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-618: Isi berkas Download modal Changelog Allocation Quota

1. Klik Tab `Allocation Quota`
2. Klik ikon Changelog pada toolbar Section 2
3. Klik Download > `Download as CSV`
4. Buka isi berkas CSV yang terunduh
5. Verifikasi encoding berkas CSV UTF-8 dengan BOM
6. Verifikasi baris 1 berkas CSV adalah header `Date,Action,Group Name,Field,Old Value,New Value,Modified By`
7. Verifikasi baris 2 sampai 7 berkas CSV adalah enam baris data berurutan Date terbaru
8. Verifikasi baris 2 berkas CSV `30/09/26 11:15,Edit,-,Quota Alert Level,Normal,Low,System`
9. Verifikasi baris 3 berkas CSV `29/09/26 10:05,Edit,Divisi Logistik,Allocated Quota,500,600,Rudi Hartono`
10. Verifikasi baris 4 berkas CSV `28/09/26 15:30,Edit,Divisi IT,Allocated Quota,-,100,Dewi Lestari`
11. Verifikasi baris 5 berkas CSV `27/09/26 09:00,Remove Allocation,Gudang A,Allocated Quota,100,-,Rudi Hartono`
12. Verifikasi baris 6 berkas CSV `26/09/26 11:20,Edit,Divisi Keuangan,Allocated Quota,-,50,Dewi Lestari`
13. Verifikasi baris 7 berkas CSV `25/09/26 08:45,Remove Allocation,Divisi IT,Allocated Quota,100,-,Rudi Hartono`
14. Verifikasi sel `—` (Group Name entri Quota Alert Level, Old Value alokasi pertama, New Value Remove Allocation) ditulis `-` pada berkas CSV
15. Verifikasi tidak ada sel `—` pada berkas CSV
16. Verifikasi tanggal pada berkas CSV berformat General Settings (`dd/MM/yy HH:mm`)
17. Verifikasi Modified By pada berkas CSV ditulis nama lengkap
18. Verifikasi angka pada berkas CSV ditulis tanpa pemisah ribuan
19. Klik Download > `Download as XLSX`
20. Buka isi berkas XLSX yang terunduh
21. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`
22. Verifikasi isi `Sheet1` sama seperti berkas CSV (header langkah 6 dan enam baris data langkah 8 sampai 13)
23. Verifikasi sel angka pada `Sheet1` bertipe angka
24. Verifikasi sel `-` pada `Sheet1` bertipe teks

### TC-FA-LIC-619: Isi berkas Download modal Changelog Concurrent User

25. Tutup modal `Changelog: Allocation Quota` dengan `[×]`
26. Klik Tab `Concurrent User`
27. Klik ikon Changelog pada toolbar
28. Klik Download > `Download as CSV`
29. Buka isi berkas CSV yang terunduh
30. Verifikasi baris 1 berkas CSV adalah header `Date,Action,User Name,Field,Old Value,New Value,Modified By`
31. Verifikasi baris 2 sampai 5 berkas CSV adalah empat baris data berurutan Date terbaru
32. Verifikasi baris 2 berkas CSV `30/09/26 11:15,Force Logout,Budi Santoso,Session Status,Active,Force Logged Out,Rudi Hartono`
33. Verifikasi baris 3 berkas CSV `29/09/26 14:20,Force Logout,Siti Rahma,Session Status,Active,Force Logged Out,Dewi Lestari`
34. Verifikasi baris 4 berkas CSV `28/09/26 09:40,Force Logout,Andi Pratama,Session Status,Active,Force Logged Out,Rudi Hartono`
35. Verifikasi baris 5 berkas CSV `27/09/26 16:05,Force Logout,Siti Rahma,Session Status,Active,Force Logged Out,Dewi Lestari`
36. Verifikasi Modified By pada berkas CSV ditulis nama lengkap (bukan `[First Name] [Last Initial]`)
37. Verifikasi tanggal pada berkas CSV berformat General Settings (`dd/MM/yy HH:mm`)
38. Ketik Search `siti`, tekan Enter
39. Klik Download > `Download as CSV`
40. Buka isi berkas CSV yang terunduh
41. Verifikasi baris 1 berkas CSV langkah 40 adalah header yang sama dengan berkas langkah 29
42. Verifikasi berkas CSV langkah 40 hanya memuat dua baris data, yaitu baris 3 dan baris 5 pada berkas langkah 29
43. Verifikasi nilai sel kedua baris data berkas langkah 40 identik dengan baris 3 dan baris 5 berkas langkah 29
44. Klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Urutan TC dalam spec: 618, 619. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-LIC-618 bergantung pada TC-FA-LIC-360 dan TC-FA-LIC-619 pada TC-FA-LIC-582. TC-FA-LIC-360 (nama berkas `Changelog-Allocation-Quota.csv` dan `.xlsx`, tanpa toast sukses) ada di spec `TC-FA-LIC-E2E-095`; TC-FA-LIC-582 (nama berkas `Changelog-Concurrent-User.csv` dan `.xlsx`, tanpa toast sukses, header dan jumlah baris) ada di spec `TC-FA-LIC-E2E-106`. Langkah pembuka dan aksi Download kedua TC itu disalin utuh di sini sebagai langkah TC-FA-LIC-618 dan TC-FA-LIC-619 (langkah 1 sampai 4, 19 sampai 20, 26 sampai 29, 38 sampai 40); spec ini hanya mengasersi isi berkas.
- Spec ini di atas 35 langkah (44 langkah). Alasan: seluruh blok satu kelas harness (f, isi berkas CSV dan XLSX modal Changelog), memakai dataset Pre-setup yang hanya dibaca, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap `Verifikasi` sesuai satu klausa Expected TC (S-01), termasuk satu `Verifikasi` per baris data berkas.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 25 menutup modal Changelog Allocation Quota sebelum berpindah tab dan langkah 44 menutup Search dan modal (S-09). Langkah 4, 20, 29, dan 40 (membuka isi berkas) berasal dari langkah TC.
- Temuan untuk QA:
  - TC-FA-LIC-618 butir b menyebut sel `—` pada "Old Value alokasi pertama" tanpa menyebut barisnya; spec mengasersi sel `-` pada seluruh sel kosong baris data a (Group Name baris 2, Old Value baris 4 dan 6, New Value baris 5 dan 7) sesuai baris data TC.
  - TC-FA-LIC-618 butir b menyebut "tanggal berformat General Settings" tanpa menyebut formatnya; spec memakai `dd/MM/yy HH:mm` dari General Settings Pre-setup #1 dan baris data TC.
  - TC-FA-LIC-618 butir b menyebut "Modified By ditulis nama lengkap" sedangkan baris 2 bernilai `System` (entri sistem, bukan pengguna); spec mengikuti baris data TC.
  - TC-FA-LIC-618 dan 619 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
