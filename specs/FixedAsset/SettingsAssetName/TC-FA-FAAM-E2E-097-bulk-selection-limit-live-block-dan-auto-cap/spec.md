---
id: TC-FA-FAAM-E2E-097-bulk-selection-limit-live-block-dan-auto-cap
title: "Bulk: Selection Limit Live-Block dan Auto-Cap Select All"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-281
  - TC-FA-FAAM-282
coverage:
  web: automated
---

# Bulk: Selection Limit Live-Block dan Auto-Cap Select All

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`).
- State global yang diubah (Pre-setup #15c): Selection Limit diturunkan di System Limits sampai batas minimum yang diizinkan di hook `before`; nilai asal dipulihkan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial karena System Limits berlaku global.
- Data: katalog Asset Name client diisi lewat seed API di hook `before` sampai jumlahnya lebih besar dari Selection Limit yang diturunkan (disediakan tim BE/FE); seed dibersihkan di hook `after`. `[Limit]` pada langkah adalah nilai Selection Limit aktif sesudah diturunkan, dibaca lewat kemampuan baca System Limits; `[N]` adalah jumlah total Asset Name client pada akhir seeding (tanpa filter aktif), dicatat oleh seeding.
- Kemampuan teknis (disediakan tim BE/FE): mengubah dan membaca Selection Limit di System Limits; seed katalog di atas Selection Limit.
- Spec ini hanya memilih baris dan tidak pernah mengonfirmasi Delete; tidak ada record yang diubah.

## Test Steps

### TC-FA-FAAM-281: Selection Limit live-block, checkbox melewati batas disabled dengan tooltip

1. Centang baris satu per satu, berpindah ke halaman berikutnya sesuai kebutuhan, sampai jumlah terpilih sama dengan `[Limit]`
2. Coba centang baris berikutnya (arahkan pointer ke checkbox baris itu lalu klik)
3. Verifikasi checkbox baris berikutnya disabled
4. Verifikasi tooltip `You've reached the maximum selection of [Limit] rows.` tampil
5. Verifikasi baris yang sudah tercentang tetap tercentang
6. Verifikasi bar bulk tetap aktif dengan teks `[Limit] asset names selected`
7. Klik icon `×`

### TC-FA-FAAM-282: Selection Limit auto-cap pada Select All lintas halaman

8. Centang 1 baris
9. Klik `Select All ([N] records)`
10. Verifikasi toast error `Error, only the first [Limit] of [N] rows were selected. Narrow your filter to include the rest.` tampil
11. Tunggu 5 detik tanpa aksi
12. Verifikasi toast tersebut masih tampil
13. Verifikasi seleksi di-cap ke `[Limit]` baris pertama dengan teks `[Limit] asset names selected`
14. Klik `Bulk Action`
15. Verifikasi opsi `Delete` tersedia pada dropdown `Bulk Action`
16. Tekan Esc untuk menutup dropdown
17. Dismiss toast
18. Klik icon `×`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): membatalkan seleksi sebelum TC berikutnya (langkah 7, 18; S-09), mencentang satu baris agar bar bulk tampil (langkah 8), menutup dropdown dan toast (langkah 16, 17). Jeda 5 detik pada langkah 11 adalah pilihan spec untuk mengamati toast persisten (bagian 6, jeda pendek di bawah 30 detik); TC tidak menyebut durasi.
- Asersi pada langkah 4 (tooltip) ditulis tepat sesudah langkah 2 karena tooltip adalah state sementara (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAM-281 tidak menyebut nilai minimum Selection Limit yang diizinkan; jumlah halaman yang dilewati langkah 1 bergantung pada nilai itu.
  - TC-FA-FAAM-282 langkah 1 mengklik `Select All ([N] records)` tanpa menyebut baris yang dicentang lebih dulu agar bar bulk tampil; spec menambah langkah mencentang satu baris (langkah 8).
  - TC-FA-FAAM-282 Expected a menyebut toast "tetap sampai di-dismiss" tanpa cara dismiss; spec menunggu 5 detik, memastikan toast masih tampil, lalu men-dismiss lewat kontrol toast.
