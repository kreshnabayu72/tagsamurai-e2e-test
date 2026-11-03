---
id: TC-AC-CS-E2E-070-cancel-request-requester
title: "Cancel Request: Requester"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-270
  - TC-AC-CS-545
  - TC-AC-CS-272
  - TC-AC-CS-273
  - TC-AC-CS-275
coverage:
  web: automated
---

# Cancel Request: Requester

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Additional Approver Manage allocation Principal PT ABC, Maya Tanjung (Pre-setup #4), `approverSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_APPROVER_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup baca-saja/global: Toggle Require Approval for Allocation ON (#23); Main Pocket PT Maju Bersama (#20); tanggal acuan uji `19/08/26` (#28).
- Data seed milik aktor dan spec ini (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan PT Maju Bersama pada group `Jawa`, requester `Fajar N`, Plan Owner PT Maju Bersama; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed):
  1. TC-AC-CS-270, TC-AC-CS-545, dan TC-AC-CS-272 (545 dan 272 melanjutkan record 270): Client `Apotek Sehat Sentosa A+{runId}-070` dengan term FAMS Growth Waiting for Approval ber-Reserve, mode New tanpa predecessor (bentuk Pre-setup #49).
  2. TC-AC-CS-273: Client `Toko Serba Ada+{runId}-070` dengan predecessor FAMS Professional Active (Start Date `01/09/25`, End Date `31/08/26`) dan successor Renewal FAMS Enterprise Waiting for Approval (bentuk Pre-setup #67 dan #68).
  3. TC-AC-CS-275: Client `PT Bintang Timur+{runId}-070` dengan Trial FAMS Growth Waiting for Approval (bentuk Pre-setup #59).
- Data Dinamis: status Canceled, Reserve yang dilepas, dan entri audit trail hanya pada Client seed dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: jam server dan browser (hook `after`) dan saldo Reserved Wallet Main Pocket PT Maju Bersama yang berubah akibat Reserve seed (dikembalikan oleh fixture backend pemulihan state di hook `after`; Wallet bersama tidak dapat dimiliki spec).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`) supaya predecessor seed tetap Active; membaca saldo Reserved dan Captured Wallet Main Pocket; membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-270 dan TC-AC-CS-545: Screening dialog Cancel Request untuk requester original dan Go Back

1. Ketik Search `Apotek Sehat Sentosa A+{runId}-070`, tekan Enter, lalu catat jumlah entri Changelog Client `Apotek Sehat Sentosa A+{runId}-070` — FAMS dan saldo Reserved Main Pocket sebagai baseline
2. Klik ikon `⋯` pada baris Subscription ID seed Apotek Sehat Sentosa A lalu pilih `Cancel Request`
3. Verifikasi Header: Title "Cancel Request" (dialog danger)
4. Verifikasi Body: bullet "• Apotek Sehat Sentosa A+{runId}-070 — FAMS"
5. Verifikasi Body: "This will cancel this request." lalu "You can resubmit it later if needed." lalu "Are you sure you want to cancel it?"
6. Verifikasi Footer: tombol `[Go Back]` dan `[Cancel Request]` (danger)
7. Klik `[Go Back]`
8. Verifikasi dialog tertutup tanpa toast
9. Verifikasi baris tetap Waiting for Approval di tab `Current`
10. Verifikasi Reserve tidak dilepas (saldo Reserved sama dengan baseline)
11. Verifikasi jumlah entri Changelog sama dengan baseline

### TC-AC-CS-272: Cancel Request term Waiting for Approval: Canceled dan Reserve dilepas

12. Klik ikon `⋯` pada baris Subscription ID seed Apotek Sehat Sentosa A lalu pilih `Cancel Request`
13. Klik `[Cancel Request]`
14. Verifikasi toast sukses "Success, your request has been canceled."
15. Klik tab `History`, ganti isi kotak search dengan `Apotek Sehat Sentosa A+{runId}-070`, tekan Enter
16. Verifikasi baris berstatus Canceled di tab `History`
17. Verifikasi Reserve wallet dilepas (saldo Reserved berkurang dibanding baseline) dan tidak pernah di-Capture
18. Buka modal Changelog Client `Apotek Sehat Sentosa A+{runId}-070` — FAMS
19. Verifikasi jumlah entri Changelog bertambah satu dibanding baseline
20. Verifikasi entri baru Action `Cancel Request`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `Fajar N` (pelaku pembatalan aktor)

### TC-AC-CS-273: Cancel Request pada Renewal tidak menyentuh predecessor

21. Tutup modal Changelog, klik tab `Current`, ganti isi kotak search dengan `Toko Serba Ada+{runId}-070`, tekan Enter
22. Klik ikon `⋯` pada baris successor Renewal (Subscription ID seed Toko Serba Ada, Waiting for Approval) lalu pilih `Cancel Request`
23. Klik `[Cancel Request]`
24. Tunggu aksi selesai (dialog Cancel Request tertutup)
25. Klik tab `History`, ganti isi kotak search dengan `Toko Serba Ada+{runId}-070`, tekan Enter
26. Verifikasi successor Renewal berstatus Canceled
27. Klik tab `Current`, ganti isi kotak search dengan `Toko Serba Ada+{runId}-070`, tekan Enter
28. Verifikasi predecessor tetap Active
29. Klik ikon `⋯` pada baris predecessor
30. Verifikasi menu memuat Renew (Renew tersedia kembali)

### TC-AC-CS-275: Cancel Request pada baris Trial Waiting for Approval

31. Tutup menu, ganti isi kotak search dengan `PT Bintang Timur+{runId}-070`, tekan Enter, lalu catat jumlah entri Changelog Client `PT Bintang Timur+{runId}-070` — FAMS sebagai baseline
32. Klik ikon `⋯` pada baris Subscription ID seed PT Bintang Timur lalu pilih `Cancel Request`
33. Klik `[Cancel Request]`
34. Verifikasi toast sukses "Success, your request has been canceled."
35. Klik tab `History`, ganti isi kotak search dengan `PT Bintang Timur+{runId}-070`, tekan Enter
36. Verifikasi Trial berstatus Canceled
37. Buka modal Changelog Client `PT Bintang Timur+{runId}-070` — FAMS
38. Verifikasi jumlah entri Changelog bertambah satu dibanding baseline
39. Verifikasi entri baru Action `Cancel Request (Trial)`, Field `Status`, Old `Waiting for Approval`, New `Canceled`

### Notifikasi approver TC-AC-CS-272

40. Tutup modal Changelog. Ganti akun: Logout lalu login sebagai Additional Approver Manage allocation Principal (`Maya Tanjung`) dan buka notifikasi
41. Verifikasi notifikasi "Subscription request canceled" untuk Client `Apotek Sehat Sentosa A+{runId}-070` — FAMS diterima approver pool

## Notes

- TC-AC-CS-545 melanjutkan dialog TC-AC-CS-270 (aksi dan record sama) sehingga `[Go Back]` TC-AC-CS-545 ditulis di blok TC-AC-CS-270; keduanya tercatat di `sourceTc`.
- Urutan menyimpang dari urutan TC sumber (S-10): pemeriksaan notifikasi approver TC-AC-CS-272 butir e ditaruh di akhir supaya ganti akun hanya satu kali.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16), termasuk Search ulang sesudah pindah tab `History` dan `Current`; pindah tab `History` dan `Current` untuk baris Canceled; `Tunggu aksi selesai` sesudah `[Cancel Request]` yang hasilnya tidak diasersi dan diikuti pindah tab (8b.8); tutup menu dan modal Changelog; ganti akun eksplisit (S-07); baseline jumlah entri Changelog dicatat sebelum aksi supaya asersi "entri baru" memakai selisih (S-12); log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (Cancel Request oleh requester) pada record milik aktor, tanpa kelas harness lain.
- Temuan untuk QA: (1) TC-AC-CS-272 butir b ("pelaku pembatalan tercatat aktor") tidak menyebut layar; spec mengamatinya sebagai Modified By di Changelog. (2) TC-AC-CS-272 Post Condition a (Approvals Tab Active hilang dan Tab History Decision Canceled) tanpa langkah observasi sehingga tidak diasersi. (3) TC-AC-CS-275 butir b ("Client tidak disentuh") tanpa cara pengamatan sehingga tidak diasersi. (4) Email Additional Approver `Maya Tanjung` dirujuk lewat fixture yang disediakan tim FE.
