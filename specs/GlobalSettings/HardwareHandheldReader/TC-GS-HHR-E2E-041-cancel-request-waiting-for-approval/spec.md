---
id: TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval
title: "Cancel Request Reader Waiting for Approval: Row Action Terkunci, Dialog, Go Back, Pembatalan Jalur A dan B, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-156
  - TC-GS-HHR-157
  - TC-GS-HHR-158
  - TC-GS-HHR-159
  - TC-GS-HHR-161
  - TC-GS-HHR-162
  - TC-GS-HHR-460
coverage:
  web: automated
---

# Cancel Request Reader Waiting for Approval: Row Action Terkunci, Dialog, Go Back, Pembatalan Jalur A dan B, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini menghapus reader Waiting for Approval dan memulihkan Seed Reader A (lihat butir pemulihan); aksi yang menghapus data berada di akhir spec.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman).
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-05 (`Chainway C72 - 1`, Jalur B, Long Range, Waiting for Approval) dan DD-10 (`Gudang Reader - 4`, Jalur A, Short Range, Waiting for Approval). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR).
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya sebelum TC-GS-HHR-460 (DD-05 dihapus lebih dulu oleh TC-GS-HHR-157) lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" yang disediakan tim FE/BE tanpa endpoint yang dikarang, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus dialog Cancel Request" (parameter langkah 10 sampai 20):

| TC | Reader | Device Name |
|---|---|---|
| TC-GS-HHR-156 | DD-05 | `Chainway C72 - 1` |
| TC-GS-HHR-158 | DD-10 | `Gudang Reader - 4` |

- Tabel "Kasus Cancel Request berhasil" (parameter langkah 21 sampai 26):

| TC | Reader | Device Name | Kartu kuota sesudah |
|---|---|---|---|
| TC-GS-HHR-157 | DD-05 | `Chainway C72 - 1` | `Long Range` `4 of 6`, `2 remaining` |
| TC-GS-HHR-159 | DD-10 | `Gudang Reader - 4` | `Short Range` `4 of 8`, `4 remaining` |

- Kemampuan teknis: klik ganda cepat pada `[Cancel Request]` (TC-GS-HHR-460); pembacaan Overlay row action, kartu kuota, Popup `Handheld Reader Detail`, dan Modal Changelog; pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-161 dan TC-GS-HHR-162: Reader Waiting for Approval hanya memiliki Detail dan Cancel Request

1. Buka Overlay row action baris DD-05 (`Chainway C72 - 1`, Waiting for Approval)
2. Verifikasi Overlay berisi tepat dua aksi berurutan: `Detail` (dark) lalu `Cancel Request` (danger)
3. Verifikasi Overlay tidak memuat `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Mark as Available`, dan `Delete`
4. Klik `Detail`
5. Verifikasi Popup `Handheld Reader Detail` terbuka untuk `Chainway C72 - 1`
6. Tutup Popup `Handheld Reader Detail` dengan `✕`
7. Buka Overlay row action baris DD-10 (`Gudang Reader - 4`, Waiting for Approval)
8. Verifikasi Overlay berisi tepat `Detail` dan `Cancel Request`
9. Tutup Overlay dengan klik di luar Overlay

### TC-GS-HHR-156 dan TC-GS-HHR-158: Screening dialog Cancel Request dan Go Back tidak membatalkan

Untuk setiap baris tabel "Kasus dialog Cancel Request" (langkah 10 sampai 20):

10. Buka Overlay row action baris {Reader}
11. Klik `Cancel Request`
12. Verifikasi Header dialog menampilkan Judul `Cancel Request`
13. Verifikasi Body dialog baris 1 menampilkan bullet `{Device Name}`
14. Verifikasi Body dialog baris 2 menampilkan teks `The device will be removed and its license quota returned.`
15. Verifikasi Body dialog baris 3 menampilkan teks `Are you sure you want to cancel this request?`
16. Verifikasi Footer dialog menampilkan `[Go Back]` dan `[Cancel Request]`
17. Klik `[Go Back]`
18. Verifikasi tidak ada toast
19. Verifikasi dialog tertutup
20. Verifikasi baris {Reader} tetap `Waiting for Approval`

### TC-GS-HHR-157 dan TC-GS-HHR-159: Cancel Request menghapus record dan mengembalikan kuota

Untuk setiap baris tabel "Kasus Cancel Request berhasil" (langkah 21 sampai 26):

21. Buka Overlay row action baris {Reader}
22. Klik `Cancel Request`
23. Klik `[Cancel Request]` pada dialog
24. Verifikasi muncul toast sukses: "Success, {Device Name} request has been canceled."
25. Verifikasi baris {Reader} hilang dari tabel
26. Verifikasi kartu kuota menampilkan {Kartu kuota sesudah}

### TC-GS-HHR-460: Klik ganda cepat pada konfirmasi Cancel Request hanya membatalkan satu kali

27. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
28. Buka ikon Changelog (Modal Changelog), catat jumlah entri sebagai baseline
29. Tutup Modal Changelog dengan `✕`
30. Buka Overlay row action baris DD-05
31. Klik `Cancel Request`
32. Tunggu toast lama hilang otomatis
33. Klik ganda cepat `[Cancel Request]` pada dialog
34. Verifikasi hanya satu toast sukses yang tampil: "Success, Chainway C72 - 1 request has been canceled."
35. Verifikasi tidak ada toast `This request is no longer available.`
36. Buka ikon Changelog
37. Verifikasi jumlah entri Changelog bertambah tepat 1 dibanding baseline langkah 28
38. Verifikasi entri baru: Action `Delete` untuk `Chainway C72 - 1`
39. Tutup Modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3f dan 3g).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 10 sampai 20 diulang dua kali dan langkah 21 sampai 26 diulang dua kali, sehingga ekspansi spec 9 + 22 + 12 + 13 = 56 langkah.
- Urutan TC di spec: 161 dan 162 (row action), 156 dan 158 (dialog dengan `[Go Back]`), 157 dan 159 (pembatalan), lalu 460 paling akhir karena memakai DD-05 yang sudah dihapus TC-GS-HHR-157 dan membutuhkan pemulihan Seed Reader A. Menyimpang dari urutan nomor TC sumber. Aksi yang menghapus data berada sesudah semua kasus yang membutuhkan baris tetap ada (prinsip 5). Kartu `Short Range` pada TC-GS-HHR-159 tidak terpengaruh pembatalan DD-05 (Long Range), sehingga nilai Expected TC tetap berlaku tanpa pemulihan antar-iterasi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (menutup Popup Detail), langkah 9 (menutup Overlay), langkah 27 (pemulihan dan muat ulang), langkah 28 dan 29 (baseline Changelog sebelum aksi pemicu; S-12), langkah 32 (menunggu toast lama hilang agar hitungan satu toast bermakna), dan langkah 39 (menutup Modal Changelog).
- Langkah 5 adalah klausa c Expected TC-GS-HHR-161 ("Klik `Detail` membuka Popup `Handheld Reader Detail` DD-05"); Popup ditutup pada langkah 6 sebelum screening berikutnya.
- Pada TC-GS-HHR-156, 158, dan 460 asersi tidak ada toast (langkah 18) diletakkan segera sesudah `[Go Back]` karena toast adalah state sementara; hitungan "satu toast" pada langkah 34 didahului muat ulang halaman pada langkah 27 dan langkah 32.
- Pengecualian alasan di atas sekitar 35 langkah (ekspansi 56): seluruh blok satu kelas (Cancel Request pada reader Waiting for Approval), tiap blok memakai reader sendiri dan tabel parameter, langkah diulang hanya per baris data, dan blok pembatalan berada di akhir sehingga kegagalan satu blok tidak menghilangkan makna blok screening.
- Pengecualian S-12 Population Seed Reader A HHR (A-5) berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Pencatatan log dan sinkronisasi Hardware Stock untuk Cancel Request dan approval collision di Admin Console tidak diasersi di spec ini (lihat Temuan untuk QA).
- Temuan untuk QA:
  - Post Condition TC-GS-HHR-157 dan 159 ("Approval collision terkait dibatalkan di Admin Console", "Status stok Admin Console tidak berubah", "Tiga surface log dengan Action `Delete` (Changelog, System Log) dan `Cancel Request` (Activity Log)") tidak punya langkah observasi di TC ini; tidak diasersi.
  - TC-GS-HHR-157 dan 159 Expected c menulis kartu kuota sesudah pembatalan tetapi tidak menyebut kartu lain; spec mengasersi hanya kartu yang disebut.
  - TC-GS-HHR-460 Expected b ("satu entri `Delete` untuk `Chainway C72 - 1`") tidak menyebut cara menemukan entri di Changelog kumulatif; spec memakai selisih jumlah entri terhadap baseline dan entri baru pada urutan default.
  - TC-GS-HHR-162 Expected a hanya menyebut `Detail` dan `Cancel Request` tanpa urutan severity dan tanpa daftar aksi yang tidak ada (berbeda dengan TC-GS-HHR-161); spec mengikuti TC masing-masing.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend hanya disebut "fixture backend" di Catatan TC dan tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
