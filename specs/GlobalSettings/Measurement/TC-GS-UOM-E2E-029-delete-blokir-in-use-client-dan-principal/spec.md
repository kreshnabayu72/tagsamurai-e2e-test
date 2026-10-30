---
id: TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal
title: "Delete Unit Diblokir karena In-Use: FAMS, SAMS, Admin Console Principal dan Distributor, dan Breakdown"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-97
  - TC-GS-UOM-98
  - TC-GS-UOM-99
  - TC-GS-UOM-100
  - TC-GS-UOM-101
  - TC-GS-UOM-395
coverage:
  web: automated
---

# Delete Unit Diblokir karena In-Use: FAMS, SAMS, Admin Console Principal dan Distributor, dan Breakdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (seedSession). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`; relevan karena spec berakhir di akun Distributor).
- Akun aktor 2: Total Control Principal (Hendra Wijaya) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, instance Principal. Login lewat langkah ganti akun eksplisit di tengah spec.
- Akun aktor 3: Total Control Distributor (Bayu Pratama) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`, instance Distributor. Login lewat langkah ganti akun eksplisit di tengah spec.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite), untuk ketiga akun aktor.
- Data pre-setup Client A (data baca, in-use, tidak pernah dihapus atau diubah; pengecualian S-06 untuk aksi hapus yang selalu diblokir guard): `Box` / `box` (FAMS: 4 asset names) dan `Kilogram` / `kg` (Supply: 1 item name).
- Data pre-setup Principal (data baca, in-use): `Watt` / `W` (Device Name `BLE Gateway` dan `Handheld Reader`, Admin Console: 2 device names) dan `Ampere` / `A` (FAMS: 1 asset name `Power Meter`; Supply: 1 item name `Battery Pack`; Admin Console: 1 device name `Fixed Reader`).
- Data pre-setup Distributor: `Hertz` / `Hz` (bebas relasi pada Pre-setup). Untuk TC-GS-UOM-395 hook `before` menyiapkan satu Device Name `Frequency Meter {runId}-029` di Admin Console Distributor yang memakai `Hertz`, lewat fixture backend yang disediakan tim FE (tanpa endpoint karangan, S-13). Hook `after` menghapus Device Name itu sehingga Used By (Items) `Hertz` kembali `0`.
- Fixture belum ada; tim FE menyiapkan `fixtures/measurement.json` dengan kunci `preSetupClientA`, `preSetupPrincipal`, dan `preSetupDistributor`.
- Data dinamis: hanya Device Name `Frequency Meter {runId}-029` di atas. Tidak ada unit yang dihapus, sehingga tidak ada cleanup unit.
- Kemampuan teknis: login ke tiga instance (Client A, Principal, lalu Distributor) dalam satu spec dengan logout atau konteks browser bersih di antaranya; fixture backend untuk Device Name Distributor (S-11).
- State global yang diubah: tidak ada (Device Name fixture dibersihkan di hook `after`).

## Test Steps

### TC-GS-UOM-97 dan TC-GS-UOM-101: Delete unit yang dipakai Asset Name FAMS diblokir, OK menutup dialog

1. Klik `⋯` baris `Box` > Delete
2. Verifikasi dialog `Cannot Delete Data` (warning) tampil langsung tanpa dialog konfirmasi
3. Verifikasi dialog `Cannot Delete Data`: bullet `Box` dengan sub-bullet `FAMS (4 asset names)`
4. Verifikasi teks `Remove the references before deleting.`
5. Verifikasi dialog hanya memuat tombol `[OK]`
6. Verifikasi tidak ada toast
7. Klik [OK]
8. Verifikasi dialog tertutup
9. Verifikasi baris `Box` tetap ada di tabel

### TC-GS-UOM-98: Delete unit yang dipakai Item Name Supply diblokir

10. Klik `⋯` baris `Kilogram` > Delete
11. Verifikasi dialog `Cannot Delete Data` tampil
12. Verifikasi sub-bullet `SAMS (1 item name)`
13. Verifikasi dialog tidak memuat baris FAMS
14. Verifikasi dialog tidak memuat baris Admin Console
15. Klik [OK]

### Ganti akun ke Principal

16. Logout dari akun Total Control Client A
17. Login sebagai Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) pada instance Principal
18. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-99: Delete unit yang dipakai Device Name Admin Console diblokir pada instance Principal

19. Klik `⋯` baris `Watt` > Delete
20. Verifikasi dialog `Cannot Delete Data` tampil
21. Verifikasi sub-bullet `Admin Console (2 device names)`
22. Klik [OK]

### TC-GS-UOM-100: Breakdown dialog blokir terpisah per modul dengan urutan FAMS, SAMS, Admin Console

23. Klik `⋯` baris `Ampere` > Delete
24. Verifikasi sub-bullet berurutan: `FAMS (1 asset name)`, `SAMS (1 item name)`, `Admin Console (1 device name)`
25. Verifikasi breakdown tidak tampil sebagai jumlah gabungan
26. Klik [OK]

### Ganti akun ke Distributor

27. Logout dari akun Total Control Principal
28. Login sebagai Total Control Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`) pada instance Distributor
29. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-395: Delete unit yang dipakai Device Name Admin Console diblokir pada instance Distributor

30. Klik `⋯` baris `Hertz` > Delete
31. Verifikasi dialog `Cannot Delete Data` tampil langsung tanpa dialog konfirmasi
32. Verifikasi sub-bullet `Admin Console (1 device name)`
33. Klik [OK]
34. Verifikasi baris `Hertz` tetap ada di tabel
35. Verifikasi Used By (Items) `Hertz` bernilai `1`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 35.
- Urutan TC dalam spec: 97/101, 98, 99, 100, 395 (urutan sumber 97, 98, 99, 100, 101, 395). TC-GS-UOM-101 (klik `[OK]`) digabung ke TC-GS-UOM-97 karena memakai dialog `Box` yang sama (langkah "Delete Box" TC-101 sama dengan langkah 1; klik `[OK]` adalah langkah 7). Kasus dikelompokkan per akun (Client A, Principal, Distributor) supaya ganti akun hanya dua kali.
- Spec memakai tiga akun dengan langkah ganti akun eksplisit (subjudul "Ganti akun ke ..."), sesuai pengecualian bagian 3 "Tidak boleh" (b): bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung: langkah 15, 22, dan 26 (klik `[OK]` untuk menutup dialog blokir; TC sumber tidak menyebutnya untuk TC-98, 99, dan 100). Langkah 18 dan 29 (buka halaman Measurement sesudah login).
- Asersi dialog `Cannot Delete Data` pada TC-98 butir b ("tanpa baris FAMS dan Admin Console (count 0 tidak ditampilkan)") dipecah menjadi langkah 13 dan 14 (S-01).
- Langkah 6: Expected TC-97 butir d ("Tidak ada toast") diasersi segera setelah dialog tampil, sebelum `[OK]`.
- Hertz pada TC-395: TC sumber menulis Device Name `Frequency Meter` disiapkan fixture backend; spec memakai nama bersuffix `Frequency Meter {runId}-029` (S-12). Kolom Dependensi TC-395 (TC-366, TC-370) dipenuhi oleh seeding spec sendiri (S-04, S-06); asersi Used By (Items) Hertz `1` pada langkah 35 tetap sesuai Expected TC-395 butir c.
- Temuan untuk QA: TC-GS-UOM-395 tidak menyebut cara menyiapkan Device Name Distributor selain "lewat fixture backend sebelum TC ini"; mekanisme seeding dan endpoint-nya tidak disebut TC, PRD, atau LLD yang dibaca, sehingga ditulis "disediakan tim FE" (S-13).
