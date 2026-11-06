---
id: TC-FA-FAAC-E2E-069-assign-klik-ganda-dan-spinner
title: "Tombol Assign: Spinner Saat Permintaan Berjalan dan Klik Ganda Hanya Memproses Satu Permintaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-625
  - TC-FA-FAAC-627
coverage:
  web: automated
---

# Tombol Assign: Spinner Saat Permintaan Berjalan dan Klik Ganda Hanya Memproses Satu Permintaan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API, dihapus di hook `after`; kode literal, lihat Notes): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-069`, Class Name `Anchor Class {runId}-069` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke tanpa Asset Class oleh fixture BE di langkah penghubung dan di hook `before` dan `after`): Asset Name "Hand Truck". Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; `Spectra.intercept` untuk menahan respons permintaan Assign di atas backend nyata (dilepas segera di langkah 7); kemampuan baca BE untuk jumlah entri Changelog (audit trail permanen, S-12).
- State global: keanggotaan Hand Truck; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-627: Tombol Assign menampilkan spinner dan non-interaktif saat permintaan dikirim

1. Klik link Class Code `ANCHOR-069`, lalu klik tab "Asset Names"
2. Klik tombol "+ Assign Asset Names"
3. Centang "Hand Truck"
4. Tunda respons permintaan Assign, lalu klik [Assign]
5. Verifikasi tombol [Assign] menampilkan spinner selama permintaan berjalan
6. Verifikasi tombol [Assign] tidak dapat diklik selama permintaan berjalan
7. Lepas tahanan respons permintaan Assign
8. Verifikasi dialog menutup
9. Verifikasi toast sukses "Success, asset name has been assigned." tampil
10. Pulihkan "Hand Truck" menjadi tanpa Asset Class lewat fixture BE

### TC-FA-FAAC-625: Klik ganda tombol Assign hanya memproses satu permintaan

11. Baca jumlah entri Changelog sebagai baseline
12. Klik tombol "+ Assign Asset Names"
13. Centang "Hand Truck"
14. Tunggu toast lama hilang otomatis
15. Klik [Assign] dua kali dengan cepat
16. Verifikasi hanya satu toast sukses "Success, asset name has been assigned."
17. Verifikasi "Hand Truck" tampil tepat satu kali di tabel tab Asset Names
18. Klik breadcrumb "Asset Class"
19. Klik ikon Changelog
20. Verifikasi selisih jumlah entri Changelog terhadap baseline langkah 11 adalah 1, yaitu satu entri L-06 untuk "Hand Truck"

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 627 lalu 625 (keduanya memakai "Hand Truck"; langkah 10 memulihkan state di antaranya).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): "Hand Truck" adalah seed Pre-setup literal.
- Class Code `ANCHOR-069` ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 047 dan 048); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh).
- Langkah penghubung (S-03): langkah 10 (pemulihan), 11 (baseline S-12), 14 (menunggu toast lama, R-12), 18 dan 19 (membuka Changelog).
- Intercept pada langkah 4 hanya menahan respons untuk mengamati state UI (bukan kelas b) dan dilepas pada langkah 7.
- Temuan untuk QA: TC-625 tidak menyebut cara menghitung entri L-06; spec memakai selisih jumlah entri terhadap baseline.
